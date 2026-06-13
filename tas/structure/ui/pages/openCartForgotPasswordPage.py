import os
from tas.structure.ui.pages.openCartBasePage import OpenCartBasePage


class OpenCartForgotPasswordPage(OpenCartBasePage):

    FORGOT_PASSWORD_CONTAINER = "#account-forgotten"
    HEADER = "xpath=//h1[contains(normalize-space(), 'Forgot Your Password')]"
    INSTRUCTION_TEXT = "xpath=//p[contains(text(), 'Enter the e-mail address')]"
    FORM = "#form-forgotten"
    EMAIL_INPUT = "#input-email"
    CONTINUE_BUTTON = "xpath=//button[normalize-space()='Continue']"
    BACK_BUTTON = "xpath=//a[normalize-space()='Back']"
    ALERT_SUCCESS = "#alert .alert-success, .alert-success"
    ALERT_DANGER = "#alert .alert-danger, .alert-danger"
    BREADCRUMB = "#account-forgotten .breadcrumb"
    SIDE_MENU_LOGIN_LINK = "aside#column-right a[href*='route=account/login']"
    SIDE_MENU_REGISTER_LINK = "aside#column-right a[href*='route=account/register']"
    SIDE_MENU_FORGOTTEN_PASSWORD_LINK = "aside#column-right a[href*='route=account/forgotten']"
    MALICIOUS_EMAIL_INPUT = "<script>alert('PYT')</script>"
    VERY_LONG_EMAIL = "a" * 250 + "@example.com"
    REPEATED_SUBMISSIONS_COUNT = 3

    def __init__(self, ctx, forgotten_password_url: str):
        super().__init__(ctx)
        self._forgotten_password_url = forgotten_password_url
    def open_forgotten_password_page(self) -> None:
        self.goto(self._forgotten_password_url)
    def read_state(self) -> dict:
        return {
            "page_loaded": self.is_visible(self.FORGOT_PASSWORD_CONTAINER),
            "instruction_text_visible": self.is_visible(self.INSTRUCTION_TEXT),
            "email_field_visible": self.is_visible(self.EMAIL_INPUT),
            "continue_button_visible": self.is_visible(self.CONTINUE_BUTTON),
            "back_button_visible": self.is_visible(self.BACK_BUTTON),
        }
    def enter_email(self, email: str) -> None:
        self.clear_and_fill(self.EMAIL_INPUT, email)
    def submit_form(self) -> None:
        self.click(self.CONTINUE_BUTTON)
    def submit_without_email(self) -> None:
        self.submit_form()
    def click_back_button(self) -> None:
        self.click(self.BACK_BUTTON)
    def is_request_accepted(self) -> bool:
        return self.is_visible(self.ALERT_SUCCESS)
    def is_email_validation_error_displayed(self) -> bool:
        browser_validation_failed = not self.is_input_valid(self.EMAIL_INPUT)
        server_warning_visible = self.is_visible(self.ALERT_DANGER)
        validation_message = self.get_input_validation_message(self.EMAIL_INPUT)

        return (
            browser_validation_failed
            or server_warning_visible
            or bool(validation_message)
        )
    def is_login_page_loaded(self) -> bool:
        return self.url_contains("route=account/login")
    def breadcrumb_contains(self, text: str) -> bool:
        breadcrumb_text = self.text_content(self.BREADCRUMB)
        return breadcrumb_text is not None and text in breadcrumb_text
    def click_side_menu_login_link(self) -> None:
        self.click(self.SIDE_MENU_LOGIN_LINK)
    def click_side_menu_register_link(self) -> None:
        self.click(self.SIDE_MENU_REGISTER_LINK)
    def click_side_menu_forgotten_password_link(self) -> None:
        self.click(self.SIDE_MENU_FORGOTTEN_PASSWORD_LINK)
    def is_register_account_page_loaded(self) -> bool:
        return self.url_contains("route=account/register")
    def set_desktop_viewport(self) -> None:
        self.set_viewport(1440, 900)
    def set_tablet_viewport(self) -> None:
        self.set_viewport(768, 1024)
    def set_mobile_viewport(self) -> None:
        self.set_viewport(390, 844)
    def is_forgotten_password_form_usable(self) -> bool:
        return (
            self.is_visible(self.FORM)
            and self.is_visible(self.EMAIL_INPUT)
            and self.is_visible(self.CONTINUE_BUTTON)
        )
    def are_forgotten_password_primary_elements_visible(self) -> bool:
        return (
            self.is_visible(self.FORGOT_PASSWORD_CONTAINER)
            and self.is_visible(self.INSTRUCTION_TEXT)
            and self.is_visible(self.EMAIL_INPUT)
            and self.is_visible(self.CONTINUE_BUTTON)
            and self.is_visible(self.BACK_BUTTON)
        )
    def forgotten_password_page_uses_https(self) -> bool:
        return self.current_url().startswith("https://")
    def start_javascript_alert_monitoring(self) -> None:
        self._javascript_alert_displayed = False

        def handle_dialog(dialog):
            self._javascript_alert_displayed = True
            dialog.dismiss()

        self.page.on("dialog", handle_dialog)
    def is_javascript_alert_displayed(self) -> bool:
        return getattr(self, "_javascript_alert_displayed", False)
    def enter_malicious_email_input(self) -> None:
        self.start_javascript_alert_monitoring()
        self.enter_email(self.MALICIOUS_EMAIL_INPUT)
    def enter_very_long_email(self) -> None:
        self.enter_email(self.VERY_LONG_EMAIL)
    def is_forgotten_password_page_stable(self) -> bool:
        return (
            self.is_visible(self.FORGOT_PASSWORD_CONTAINER)
            and self.is_visible(self.FORM)
            and self.is_visible(self.EMAIL_INPUT)
            and self.is_visible(self.CONTINUE_BUTTON)
        )
    def submit_form_multiple_times_with_unregistered_email(self) -> None:
        for index in range(self.REPEATED_SUBMISSIONS_COUNT):
            self.enter_email(f"unregistered{index}@example.invalid")
            self.submit_form()

            try:
                self.page.wait_for_load_state("networkidle", timeout=3000)
            except Exception:
                pass
    def refresh_forgotten_password_page(self) -> None:
        self.refresh_page()
    def is_email_field_empty(self) -> bool:
        return self.input_value(self.EMAIL_INPUT) == ""
    def navigate_back_in_browser_to_forgotten_password_page(self) -> None:
        self.browser_back()
    def open_forgotten_password_page_again(self) -> None:
        self.open_forgotten_password_page()