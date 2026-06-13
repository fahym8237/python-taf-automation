import time
from dataclasses import dataclass

from tas.structure.ui.pages.openCartBasePage import OpenCartBasePage


@dataclass
class RegisterUserDraft:
    firstname: str
    lastname: str
    email: str
    password: str


class OpenCartRegisterPage(OpenCartBasePage):

    REGISTER_CONTAINER = "#account-register"
    FORM = "#form-register"
    FIRSTNAME_INPUT = "#input-firstname"
    LASTNAME_INPUT = "#input-lastname"
    EMAIL_INPUT = "#input-email"
    PASSWORD_INPUT = "#input-password"
    CONTINUE_BUTTON = "xpath=//form[@id='form-register']//button[normalize-space()='Continue']"
    PRIVACY_CHECKBOX = "input[name='agree']"
    PRIVACY_POLICY_LINK = "xpath=//form[@id='form-register']//a[contains(normalize-space(), 'Privacy Policy')]"
    LOGIN_LINK = "xpath=//div[@id='content']//a[contains(@href, 'route=account/login')]"
    FIRSTNAME_ERROR = "#error-firstname"
    LASTNAME_ERROR = "#error-lastname"
    EMAIL_ERROR = "#error-email"
    PASSWORD_ERROR = "#error-password"
    SUCCESS_HEADER = "xpath=//h1[normalize-space()='Your Account Has Been Created!']"
    ALERT_DANGER = "#alert .alert-danger, .alert-danger"
    BREADCRUMB = "#account-register .breadcrumb"
    SIDE_MENU_LOGIN_LINK = "aside#column-right a[href*='route=account/login']"
    SIDE_MENU_REGISTER_LINK = "aside#column-right a[href*='route=account/register']"
    SIDE_MENU_FORGOTTEN_PASSWORD_LINK = "aside#column-right a[href*='route=account/forgotten']"
    MALICIOUS_FIRSTNAME = "<script>alert('PYT')</script>"
    MALICIOUS_LASTNAME = "' OR '1'='1"
    MALICIOUS_EMAIL = "<script>alert('PYT')</script>"
    MALICIOUS_PASSWORD = "' OR '1'='1"
    VERY_LONG_FIRSTNAME = "A" * 255
    VERY_LONG_LASTNAME = "B" * 255
    VERY_LONG_EMAIL = ("a" * 240) + "@example.com"
    VERY_LONG_PASSWORD = "P" * 255

    def __init__(self, ctx, register_url: str):
        super().__init__(ctx)
        self._register_url = register_url
        self._latest_user = None
    def open_register_page(self) -> None:
        self.goto(self._register_url)
    def read_state(self) -> dict:
        return {
            "page_loaded": self.is_visible(self.REGISTER_CONTAINER),
            "firstname_field_visible": self.is_visible(self.FIRSTNAME_INPUT),
            "lastname_field_visible": self.is_visible(self.LASTNAME_INPUT),
            "email_field_visible": self.is_visible(self.EMAIL_INPUT),
            "password_field_visible": self.is_visible(self.PASSWORD_INPUT),
            "continue_button_visible": self.is_visible(self.CONTINUE_BUTTON),
            "privacy_policy_link_visible": self.is_visible(self.PRIVACY_POLICY_LINK),
            "login_link_visible": self.is_visible(self.LOGIN_LINK),
        }
    def generate_valid_user(self) -> RegisterUserDraft:
        suffix = int(time.time())
        user = RegisterUserDraft(
            firstname="John",
            lastname="Smith",
            email=f"john.smith.{suffix}@example.com",
            password="Pass123!"
        )
        self._latest_user = user
        return user
    def fill_registration_form_with_generated_user(self) -> None:
        user = self.generate_valid_user()
        self.fill_registration_form(user)
    def fill_registration_form(self, user: RegisterUserDraft) -> None:
        self.clear_and_fill(self.FIRSTNAME_INPUT, user.firstname)
        self.clear_and_fill(self.LASTNAME_INPUT, user.lastname)
        self.clear_and_fill(self.EMAIL_INPUT, user.email)
        self.clear_and_fill(self.PASSWORD_INPUT, user.password)
    def enter_invalid_email(self) -> None:
        self.clear_and_fill(self.EMAIL_INPUT, "invalid-email-format")
    def agree_to_privacy_policy(self) -> None:
        checkbox = self.page.locator(self.PRIVACY_CHECKBOX).first
        if not checkbox.is_checked():
            checkbox.check()
    def submit_form(self) -> None:
        self.click(self.CONTINUE_BUTTON)
    def submit_without_fields(self) -> None:
        self.submit_form()
    def is_success_message_visible(self, message: str) -> bool:
        return self.is_visible(self.SUCCESS_HEADER) and message in self.text_content(self.SUCCESS_HEADER)
    def are_all_mandatory_errors_displayed(self) -> bool:
        return (
            self.is_visible(self.FIRSTNAME_ERROR)
            and self.is_visible(self.LASTNAME_ERROR)
            and self.is_visible(self.EMAIL_ERROR)
            and self.is_visible(self.PASSWORD_ERROR)
        )
    def is_privacy_policy_warning_displayed(self) -> bool:
        text = self.text_content(self.ALERT_DANGER)
        return text is not None and "privacy" in text.lower()
    def is_email_validation_error_displayed(self) -> bool:
        browser_validation_failed = not self.is_input_valid(self.EMAIL_INPUT)
        server_error_visible = self.is_visible(self.EMAIL_ERROR)
        return browser_validation_failed or server_error_visible
    def is_password_field_masked(self) -> bool:
        return self.get_attribute(self.PASSWORD_INPUT, "type") == "password" 
    def refresh_register_page(self) -> None:
        self.refresh_page()
    def is_register_form_usable(self) -> bool:
        return (
            self.is_visible(self.FORM)
            and self.is_visible(self.FIRSTNAME_INPUT)
            and self.is_visible(self.LASTNAME_INPUT)
            and self.is_visible(self.EMAIL_INPUT)
            and self.is_visible(self.PASSWORD_INPUT)
            and self.is_visible(self.CONTINUE_BUTTON)
        )
    def is_firstname_field_empty(self) -> bool:
        return self.input_value(self.FIRSTNAME_INPUT) == ""
    def is_lastname_field_empty(self) -> bool:
        return self.input_value(self.LASTNAME_INPUT) == ""
    def is_email_field_empty(self) -> bool:
        return self.input_value(self.EMAIL_INPUT) == ""
    def is_password_field_empty(self) -> bool:
        return self.input_value(self.PASSWORD_INPUT) == ""
    def click_login_link(self) -> None:
        self.click(self.LOGIN_LINK)
    def is_login_page_loaded(self) -> bool:
        return self.url_contains("route=account/login")
    def navigate_back_in_browser_to_register_page(self) -> None:
        self.browser_back()
    def open_register_page_again(self) -> None:
        self.open_register_page()
    def set_desktop_viewport(self) -> None:
        self.set_viewport(1440, 900)
    def set_tablet_viewport(self) -> None:
        self.set_viewport(768, 1024)
    def set_mobile_viewport(self) -> None:
        self.set_viewport(390, 844)
    def are_register_primary_elements_visible(self) -> bool:
        return (
            self.is_visible(self.REGISTER_CONTAINER)
            and self.is_visible(self.FORM)
            and self.is_visible(self.FIRSTNAME_INPUT)
            and self.is_visible(self.LASTNAME_INPUT)
            and self.is_visible(self.EMAIL_INPUT)
            and self.is_visible(self.PASSWORD_INPUT)
            and self.is_visible(self.CONTINUE_BUTTON)
            and self.is_visible(self.PRIVACY_POLICY_LINK)
        )
    def register_page_uses_https(self) -> bool:
        return self.current_url().startswith("https://")
    def enter_malicious_firstname_input(self) -> None:
        self.clear_and_fill(self.FIRSTNAME_INPUT, self.MALICIOUS_FIRSTNAME)
    def enter_malicious_lastname_input(self) -> None:
        self.clear_and_fill(self.LASTNAME_INPUT, self.MALICIOUS_LASTNAME)
    def enter_malicious_email_input(self) -> None:
        self.clear_and_fill(self.EMAIL_INPUT, self.MALICIOUS_EMAIL)
    def enter_malicious_password_input(self) -> None:
        self.clear_and_fill(self.PASSWORD_INPUT, self.MALICIOUS_PASSWORD)
    def enter_very_long_firstname(self) -> None:
        self.clear_and_fill(self.FIRSTNAME_INPUT, self.VERY_LONG_FIRSTNAME)
    def enter_very_long_lastname(self) -> None:
        self.clear_and_fill(self.LASTNAME_INPUT, self.VERY_LONG_LASTNAME)
    def enter_very_long_email(self) -> None:
        self.clear_and_fill(self.EMAIL_INPUT, self.VERY_LONG_EMAIL)
    def enter_very_long_password(self) -> None:
        self.clear_and_fill(self.PASSWORD_INPUT, self.VERY_LONG_PASSWORD)
    def is_register_page_stable(self) -> bool:
        return (
            self.is_visible(self.REGISTER_CONTAINER)
            and self.is_visible(self.FORM)
            and self.is_visible(self.FIRSTNAME_INPUT)
            and self.is_visible(self.LASTNAME_INPUT)
            and self.is_visible(self.EMAIL_INPUT)
            and self.is_visible(self.PASSWORD_INPUT)
            and self.is_visible(self.CONTINUE_BUTTON)
        )
    def breadcrumb_contains(self, text: str) -> bool:
        breadcrumb_text = self.text_content(self.BREADCRUMB)
        return breadcrumb_text is not None and text in breadcrumb_text
    def click_side_menu_login_link(self) -> None:
        self.click(self.SIDE_MENU_LOGIN_LINK)
    def click_side_menu_register_link(self) -> None:
        self.click(self.SIDE_MENU_REGISTER_LINK)
    def click_side_menu_forgotten_password_link(self) -> None:
        self.click(self.SIDE_MENU_FORGOTTEN_PASSWORD_LINK)
    def is_forgotten_password_page_loaded(self) -> bool:
        return self.url_contains("route=account/forgotten")
    def click_privacy_policy_link(self) -> None:
        self.click(self.PRIVACY_POLICY_LINK)
    def is_privacy_policy_opened(self) -> bool:
        return (
            self.url_contains("route=information/information")
            or self.page.locator(".modal.show, .modal-dialog").count() > 0
        )
    def submit_registration_data(
    self,
    firstname: str,
    lastname: str,
    email: str,
    password: str,
    agree_privacy: bool = True,
    ) -> None:
        self.clear_and_fill(self.FIRSTNAME_INPUT, firstname)
        self.clear_and_fill(self.LASTNAME_INPUT, lastname)
        self.clear_and_fill(self.EMAIL_INPUT, email)
        self.clear_and_fill(self.PASSWORD_INPUT, password)

        checkbox = self.page.locator(self.PRIVACY_CHECKBOX).first
        if agree_privacy and not checkbox.is_checked():
            checkbox.check()
        elif not agree_privacy and checkbox.is_checked():
            checkbox.uncheck()

        self.submit_form()
    def read_validation_errors(self) -> dict:
        return {
            "firstname_error": self.is_visible(self.FIRSTNAME_ERROR),
            "lastname_error": self.is_visible(self.LASTNAME_ERROR),
            "email_error": self.is_visible(self.EMAIL_ERROR) or not self.is_input_valid(self.EMAIL_INPUT),
            "password_error": self.is_visible(self.PASSWORD_ERROR),
        }