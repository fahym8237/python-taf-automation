import os
import time

from tas.core.util.runtimeCredentials import RuntimeCredentials
from tas.structure.ui.pages.openCartBasePage import OpenCartBasePage


class OpenCartChangePasswordPage(OpenCartBasePage):

    CHANGE_PASSWORD_CONTAINER = "#account-password"
    FORM = "#form-password"
    PASSWORD_INPUT = "#input-password"
    CONFIRM_INPUT = "#input-confirm"
    PASSWORD_ERROR = "#error-password"
    CONFIRM_ERROR = "#error-confirm"
    CONTINUE_BUTTON = "xpath=//form[@id='form-password']//button[normalize-space()='Continue']"
    BACK_BUTTON = "xpath=//form[@id='form-password']//a[normalize-space()='Back']"
    SUCCESS_ALERT = "xpath=//div[@class='alert alert-success alert-dismissible']"
    MY_ACCOUNT_ROUTE = "route=account/account"
    CHANGE_PASSWORD_ROUTE = "route=account/password"
    CHANGE_PASSWORD_LINK = "xpath=//a[normalize-space()='Password']"
    BREADCRUMB = "#account-password .breadcrumb"
    SIDE_MENU_MY_ACCOUNT_LINK = "aside#column-right a[href*='route=account/account']"
    SIDE_MENU_EDIT_ACCOUNT_LINK = "aside#column-right a[href*='route=account/edit']"
    SIDE_MENU_PASSWORD_LINK = "aside#column-right a[href*='route=account/password']"
    SIDE_MENU_LOGOUT_LINK = "aside#column-right a[href*='route=account/logout']"
    EDIT_ACCOUNT_ROUTE = "route=account/edit"
    LOGOUT_ROUTE = "route=account/logout"
    MALICIOUS_PASSWORD_INPUT = "<script>alert('PYT')</script>"
    MALICIOUS_CONFIRM_INPUT = "' OR '1'='1"
    DIRECT_CHANGE_PASSWORD_ROUTE = "https://opencart.liveblog365.com/index.php?route=account/password&language=en-gb"
    LOGIN_ROUTE = "route=account/login"
    LOGIN_EMAIL_INPUT = "#input-email"
    LOGIN_PASSWORD_INPUT = "#input-password"
    LOGIN_BUTTON = "xpath=//button[normalize-space()='Login']"
    LOGIN_WARNING = "#alert .alert-danger, .alert-danger"
    LOGOUT_LINK = "a[href*='route=account/logout']"
    LOGIN_ROUTE = "route=account/login"
    ACCOUNT_ROUTE = "route=account/account"

    def __init__(self, ctx):
        super().__init__(ctx)
        self._latest_new_password = None
    def open_change_password_page(self) -> None:
        self.click(self.CHANGE_PASSWORD_LINK)
    def read_state(self) -> dict:
        return {
            "page_loaded": self.is_visible(self.CHANGE_PASSWORD_CONTAINER),
            "password_field_visible": self.is_visible(self.PASSWORD_INPUT),
            "confirm_field_visible": self.is_visible(self.CONFIRM_INPUT),
            "continue_button_visible": self.is_visible(self.CONTINUE_BUTTON),
            "back_button_visible": self.is_visible(self.BACK_BUTTON),
        }
    def generate_valid_new_password(self) -> str:
        old_password = os.getenv("LOGIN_PASSWORD")
        new_password = f"Pwd{int(time.time())}!"

        if new_password == old_password:
            new_password = f"Pwd{int(time.time())}X!"

        self._latest_new_password = new_password
        return new_password
    def enter_valid_new_password(self) -> None:
        password = self.generate_valid_new_password()
        self.clear_and_fill(self.PASSWORD_INPUT, password)
    def enter_same_confirm_password(self) -> None:
        if not self._latest_new_password:
            self._latest_new_password = os.getenv("LOGIN_PASSWORD")
        self.clear_and_fill(self.CONFIRM_INPUT, self._latest_new_password)
    def enter_different_confirm_password(self) -> None:
        self.clear_and_fill(self.CONFIRM_INPUT, "DifferentPassword123!")
    def submit_form(self) -> None:
        self.click(self.CONTINUE_BUTTON)
    def submit_without_passwords(self) -> None:
        self.submit_form()
    def is_password_changed_successfully(self) -> bool:
        success = (
            self.is_visible_changePassword(self.SUCCESS_ALERT)
            or self.url_contains(self.MY_ACCOUNT_ROUTE)
        )
        

        if success:
            if not self._latest_new_password:
                raise RuntimeError("Password changed but _latest_new_password is empty.")

            print(f"Password changed successfully. Latest new password: {self._latest_new_password}")
            RuntimeCredentials.set_login_password(self._latest_new_password)

        return success
    def latest_new_password(self) -> str | None:
        return self._latest_new_password
    def is_password_validation_error_displayed(self) -> bool:
        return self.is_visible(self.PASSWORD_ERROR) or bool(self.text_content(self.PASSWORD_ERROR))
    def is_confirm_password_validation_error_displayed(self) -> bool:
        return self.is_visible(self.CONFIRM_ERROR) or bool(self.text_content(self.CONFIRM_ERROR))
    def is_password_mismatch_validation_error_displayed(self) -> bool:
        text = self.text_content(self.CONFIRM_ERROR)
        return self.is_confirm_password_validation_error_displayed() and (
            text is None or "match" in text.lower() or "confirmation" in text.lower()
        )
    def is_password_field_masked(self) -> bool:
        return self.get_attribute(self.PASSWORD_INPUT, "type") == "password"
    def is_confirm_password_field_masked(self) -> bool:
        return self.get_attribute(self.CONFIRM_INPUT, "type") == "password"
    def click_back_button(self) -> None:
        self.click(self.BACK_BUTTON)
    def is_my_account_page_loaded(self) -> bool:
        return self.url_contains(self.MY_ACCOUNT_ROUTE)
    def breadcrumb_contains(self, text: str) -> bool:
        breadcrumb_text = self.text_content(self.BREADCRUMB)
        return breadcrumb_text is not None and text in breadcrumb_text
    def click_side_menu_my_account_link(self) -> None:
        self.click(self.SIDE_MENU_MY_ACCOUNT_LINK)
    def click_side_menu_edit_account_link(self) -> None:
        self.click(self.SIDE_MENU_EDIT_ACCOUNT_LINK)
    def click_side_menu_password_link(self) -> None:
        self.click(self.SIDE_MENU_PASSWORD_LINK)
    def click_side_menu_logout_link(self) -> None:
        self.click(self.SIDE_MENU_LOGOUT_LINK)
    def is_edit_account_page_loaded(self) -> bool:
        return self.url_contains(self.EDIT_ACCOUNT_ROUTE)
    def is_logged_out_successfully(self) -> bool:
        return self.url_contains(self.LOGOUT_ROUTE)
    def set_desktop_viewport(self) -> None:
        self.set_viewport(1440, 900)
    def set_tablet_viewport(self) -> None:
        self.set_viewport(768, 1024)
    def set_mobile_viewport(self) -> None:
        self.set_viewport(390, 844)
    def is_change_password_form_usable(self) -> bool:
        return (
            self.is_visible(self.FORM)
            and self.is_visible(self.PASSWORD_INPUT)
            and self.is_visible(self.CONFIRM_INPUT)
            and self.is_visible(self.CONTINUE_BUTTON)
        )
    def are_change_password_primary_elements_visible(self) -> bool:
        return (
            self.is_visible(self.CHANGE_PASSWORD_CONTAINER)
            and self.is_visible(self.FORM)
            and self.is_visible(self.PASSWORD_INPUT)
            and self.is_visible(self.CONFIRM_INPUT)
            and self.is_visible(self.CONTINUE_BUTTON)
            and self.is_visible(self.BACK_BUTTON)
        )
    def change_password_page_uses_https(self) -> bool:
        return self.current_url().startswith("https://")
    def start_javascript_alert_monitoring(self) -> None:
        self._javascript_alert_displayed = False

        def handle_dialog(dialog):
            self._javascript_alert_displayed = True
            dialog.dismiss()

        self.page.on("dialog", handle_dialog)
    def is_javascript_alert_displayed(self) -> bool:
        return getattr(self, "_javascript_alert_displayed", False)
    def enter_malicious_password_input(self) -> None:
        self.start_javascript_alert_monitoring()
        self.clear_and_fill(self.PASSWORD_INPUT, self.MALICIOUS_PASSWORD_INPUT)
    def enter_malicious_confirm_input(self) -> None:
        self.clear_and_fill(self.CONFIRM_INPUT, self.MALICIOUS_CONFIRM_INPUT)
    def is_change_password_page_stable(self) -> bool:
        return (
            self.is_visible(self.CHANGE_PASSWORD_CONTAINER)
            and self.is_visible(self.FORM)
            and self.is_visible(self.PASSWORD_INPUT)
            and self.is_visible(self.CONFIRM_INPUT)
            and self.is_visible(self.CONTINUE_BUTTON)
        )
    def clear_authenticated_session(self) -> None:
        self.clear_cookies()
    def open_change_password_page_directly(self) -> None:
        self.goto(self.DIRECT_CHANGE_PASSWORD_ROUTE)
    def is_redirected_to_login_page(self) -> bool:
        return self.url_contains(self.LOGIN_ROUTE)
    def store_old_password_before_change(self) -> None:
        self._old_password = os.getenv("LOGIN_PASSWORD")
    def enter_valid_new_password(self) -> None:
        self.store_old_password_before_change()
        password = self.generate_valid_new_password()
        self.clear_and_fill(self.PASSWORD_INPUT, password)
    def logout_after_password_change(self) -> None:
        if self.is_visible(self.LOGOUT_LINK):
            self.click(self.LOGOUT_LINK)
        else:
            self.goto("https://opencart.liveblog365.com/index.php?route=account/logout&language=en-gb")
    def login_with_newly_changed_password(self) -> None:
        login_email = RuntimeCredentials.get_login_email()
        login_password = RuntimeCredentials.get_login_password()

        self.goto("https://opencart.liveblog365.com/index.php?route=account/login&language=en-gb")
        self.clear_and_fill(self.LOGIN_EMAIL_INPUT, login_email)
        self.clear_and_fill(self.LOGIN_PASSWORD_INPUT, login_password)
        self.click(self.LOGIN_BUTTON)
    def login_with_old_password_after_password_change(self) -> None:
        login_email = os.getenv("LOGIN_EMAIL")
        old_password = getattr(self, "_old_password", None)

        if not old_password:
            raise RuntimeError("Old password was not stored before password change.")

        self.goto("https://opencart.liveblog365.com/index.php?route=account/login&language=en-gb")
        self.clear_and_fill(self.LOGIN_EMAIL_INPUT, login_email)
        self.clear_and_fill(self.LOGIN_PASSWORD_INPUT, old_password)
        self.click(self.LOGIN_BUTTON)
    def is_logged_in_after_password_change(self) -> bool:
        return self.url_contains(self.ACCOUNT_ROUTE)
    def is_login_warning_displayed_after_password_change(self) -> bool:
        return self.is_visible(self.LOGIN_WARNING)
    def refresh_change_password_page(self) -> None:
        self.refresh_page()
    def is_password_field_empty(self) -> bool:
        return self.input_value(self.PASSWORD_INPUT) == ""
    def is_confirm_password_field_empty(self) -> bool:
        return self.input_value(self.CONFIRM_INPUT) == ""