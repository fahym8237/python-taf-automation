from tas.structure.ui.pages.base_page import BasePage
from tas.structure.ui.locators import forgot_password_locators as L

class ForgotPasswordPage(BasePage):
    def open_file(self, file_url: str) -> None:
        self.goto(file_url)

    def read_state(self) -> dict:
        return {
            "content_container_visible": self.is_visible(L.CONTENT_CONTAINER),
            "header_visible": self.is_visible(L.FORGOTTEN_PASSWORD_HEADER),
            "instruction_visible": self.is_visible(L.INSTRUCTION_TEXT),
            "form_visible": self.is_visible(L.FORGOTTEN_FORM),
            "email_legend_visible": self.is_visible(L.EMAIL_LEGEND),
            "email_input_visible": self.is_visible(L.EMAIL_INPUT),
            "continue_button_visible": self.is_visible(L.CONTINUE_BUTTON),
            "back_button_visible": self.is_visible(L.BACK_BUTTON),
        }
