from tas.structure.ui.pages.openCartBasePage import OpenCartBasePage


class OpenCartLoginPage(OpenCartBasePage):

    ACCOUNT_LOGIN_CONTAINER = "#account-login"
    LOGIN_FORM = "#form-login"
    RETURNING_CUSTOMER_HEADER = "xpath=//form[@id='form-login']//h2[normalize-space()='Returning Customer']"
    EMAIL_INPUT = "#input-email"
    PASSWORD_INPUT = "#input-password"
    LOGIN_BUTTON = "xpath=//form[@id='form-login']//button[normalize-space()='Login']"
    FORGOTTEN_PASSWORD_LINK = "xpath=//form[@id='form-login']//a[normalize-space()='Forgotten Password']"
    REGISTER_CONTINUE_BUTTON = "xpath=//h2[normalize-space()='New Customer']/ancestor::div[contains(@class,'border')]//a[normalize-space()='Continue']"
    WARNING_ALERT = "#alert .alert-danger, .alert-danger"
    BREADCRUMB = "#account-login .breadcrumb"
    SIDE_MENU_LOGIN_LINK = "aside#column-right a[href*='route=account/login']"
    SIDE_MENU_REGISTER_LINK = "aside#column-right a[href*='route=account/register']"
    SIDE_MENU_FORGOTTEN_PASSWORD_LINK = "aside#column-right a[href*='route=account/forgotten']"
    MY_ACCOUNT_PATH = "index.php?route=account/account&language=en-gb"
    EDIT_ACCOUNT_PATH = "index.php?route=account/edit&language=en-gb"
    CHANGE_PASSWORD_PATH = "index.php?route=account/password&language=en-gb"
    LOGOUT_PATH = "index.php?route=account/logout&language=en-gb"
    ACCOUNT_CONTENT = "#account-account, #account-login, #account-logout"
    LOGOUT_LINK = "a[href*='route=account/logout']"
    CONTINUE_BUTTON = "a.btn.btn-primary"
    MALICIOUS_EMAIL_INPUT = "<script>alert('PYT')</script>"
    MALICIOUS_PASSWORD_INPUT = "' OR '1'='1"
    REPEATED_ATTEMPTS_COUNT = 3

    def __init__(self, ctx, login_url: str):
        super().__init__(ctx)
        self._login_url = login_url
    def open_login_page(self) -> None:
        self.goto(self._login_url)
    def read_state(self) -> dict:
        return {
            "page_loaded": self.is_visible(self.ACCOUNT_LOGIN_CONTAINER),
            "returning_customer_section_visible": self.is_visible(self.RETURNING_CUSTOMER_HEADER),
            "email_field_visible": self.is_visible(self.EMAIL_INPUT),
            "password_field_visible": self.is_visible(self.PASSWORD_INPUT),
            "login_button_visible": self.is_visible(self.LOGIN_BUTTON),
            "forgotten_password_link_visible": self.is_visible(self.FORGOTTEN_PASSWORD_LINK),
        }
    def click_forgotten_password_link(self) -> None:
        self.click(self.FORGOTTEN_PASSWORD_LINK)
    def click_register_continue_button(self) -> None:
        self.click(self.REGISTER_CONTINUE_BUTTON)
    def enter_email(self, email: str) -> None:
        self.fill(self.EMAIL_INPUT, email)
    def enter_password(self, password: str) -> None:
        self.fill(self.PASSWORD_INPUT, password)
    def submit_login(self) -> None:
        self.click(self.LOGIN_BUTTON)
    def is_forgotten_password_page_loaded(self) -> bool:
        return "route=account/forgotten" in self.current_url()
    def is_register_account_page_loaded(self) -> bool:
        return "route=account/register" in self.current_url()
    def read_login_result(self) -> dict:
        current_url = self.current_url()

        return {
            "warning_visible": self.is_visible(self.WARNING_ALERT),
            "warning_text": self.text_content(self.WARNING_ALERT),
            "logged_in": "route=account/account" in current_url,
        }
    def is_password_masked(self) -> bool:
        return self.get_attribute(self.PASSWORD_INPUT, "type") == "password"  
    def breadcrumb_contains(self, text: str) -> bool:
        breadcrumb_text = self.text_content(self.BREADCRUMB)
        return breadcrumb_text is not None and text in breadcrumb_text
    def click_side_menu_register_link(self) -> None:
        self.click(self.SIDE_MENU_REGISTER_LINK)
    def click_side_menu_forgotten_password_link(self) -> None:
        self.click(self.SIDE_MENU_FORGOTTEN_PASSWORD_LINK)
    def click_side_menu_login_link(self) -> None:
        self.click(self.SIDE_MENU_LOGIN_LINK)
    def _absolute_url(self, path: str) -> str:
        if self._login_url.endswith("/"):
            base = self._login_url.split("index.php")[0]
        else:
            base = self._login_url.split("index.php")[0]

        return base + path
    def open_my_account_page_directly(self) -> None:
        self.goto(self._absolute_url(self.MY_ACCOUNT_PATH))
    def open_edit_account_page_directly(self) -> None:
        self.goto(self._absolute_url(self.EDIT_ACCOUNT_PATH))
    def open_change_password_page_directly(self) -> None:
        self.goto(self._absolute_url(self.CHANGE_PASSWORD_PATH))
    def is_redirected_to_login_page(self) -> bool:
        return "route=account/login" in self.current_url() and self.is_visible(self.LOGIN_FORM)
    def is_my_account_page_loaded(self) -> bool:
        return "route=account/account" in self.current_url()
    def logout_from_account_area(self) -> None:
        if self.is_visible(self.LOGOUT_LINK):
            self.click(self.LOGOUT_LINK)
        else:
            self.goto(self._absolute_url(self.LOGOUT_PATH))
    def is_logged_out_successfully(self) -> bool:
        return "route=account/logout" in self.current_url()
    def open_login_page_again(self) -> None:
        self.open_login_page()
    def is_authenticated_login_access_handled(self) -> bool:
        current_url = self.current_url()

        return (
            "route=account/login" in current_url
            or "route=account/account" in current_url
        )
    def set_desktop_viewport(self) -> None:
     self.set_viewport(1440, 900)
    def set_tablet_viewport(self) -> None:
        self.set_viewport(768, 1024)
    def set_mobile_viewport(self) -> None:
        self.set_viewport(390, 844)
    def is_login_form_usable(self) -> bool:
        return (
            self.is_visible(self.LOGIN_FORM)
            and self.is_visible(self.EMAIL_INPUT)
            and self.is_visible(self.PASSWORD_INPUT)
            and self.is_visible(self.LOGIN_BUTTON)
        )
    def are_primary_elements_visible(self) -> bool:
        return (
            self.is_visible(self.ACCOUNT_LOGIN_CONTAINER)
            and self.is_visible(self.RETURNING_CUSTOMER_HEADER)
            and self.is_visible(self.EMAIL_INPUT)
            and self.is_visible(self.PASSWORD_INPUT)
            and self.is_visible(self.LOGIN_BUTTON)
            and self.is_visible(self.FORGOTTEN_PASSWORD_LINK)
        )
    def login_page_uses_https(self) -> bool:
        return self.current_url().startswith("https://")
    def enter_malicious_email_input(self) -> None:
        self.fill(self.EMAIL_INPUT, self.MALICIOUS_EMAIL_INPUT)
    def enter_malicious_password_input(self) -> None:
        self.fill(self.PASSWORD_INPUT, self.MALICIOUS_PASSWORD_INPUT)
    def is_browser_native_validation_displayed(self) -> bool:
        return self.page.locator(self.EMAIL_INPUT).evaluate(
            "element => !element.validity.valid"
        )
    def is_javascript_alert_displayed(self) -> bool:
        dialog_opened = {"value": False}

        def handle_dialog(dialog):
            dialog_opened["value"] = True
            dialog.dismiss()

        self.page.once("dialog", handle_dialog)

        return dialog_opened["value"]
    def submit_invalid_credentials_multiple_times(self) -> None:
        for index in range(self.REPEATED_ATTEMPTS_COUNT):
            self.enter_email(f"invalid{index}@example.invalid")
            self.enter_password("WrongPassword123!")
            self.submit_login()

            try:
                self.page.wait_for_load_state("networkidle", timeout=3000)
            except Exception:
                pass
    def is_login_page_stable(self) -> bool:
        return (
            self.is_visible(self.ACCOUNT_LOGIN_CONTAINER)
            and self.is_visible(self.LOGIN_FORM)
            and self.is_visible(self.EMAIL_INPUT)
            and self.is_visible(self.PASSWORD_INPUT)
            
        )
    def start_javascript_alert_monitoring(self) -> None:
        self._javascript_alert_displayed = False

        def handle_dialog(dialog):
            self._javascript_alert_displayed = True
            dialog.dismiss()

        self.page.on("dialog", handle_dialog)
    def is_javascript_alert_displayed(self) -> bool:
        return getattr(self, "_javascript_alert_displayed", False)



