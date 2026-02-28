from tas.structure.ui.pages.base_page import BasePage
from tas.structure.ui.locators import login_locators as L

class LoginPage(BasePage):
    def open_file(self, file_url: str) -> None:
        self.goto(file_url)

    def click_forgotten_password(self) -> None:
        self.page.locator(L.FORGOTTEN_PASSWORD_LINK).click()

    def read_state(self) -> dict:
        return {
            "login_form_visible": self.is_visible(L.LOGIN_FORM),
            "returning_customer_header_visible": self.is_visible(L.RETURNING_CUSTOMER_HEADER),
            "email_input_visible": self.is_visible(L.EMAIL_INPUT),
            "password_input_visible": self.is_visible(L.PASSWORD_INPUT),
            "login_button_visible": self.is_visible(L.LOGIN_BUTTON),
            "forgotten_password_link_visible": self.is_visible(L.FORGOTTEN_PASSWORD_LINK),
        }
