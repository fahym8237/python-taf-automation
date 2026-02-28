from tas.structure.ui.pages.base_page import BasePage
from tas.structure.ui.locators import register_locators as L

class RegisterPage(BasePage):
    def open_file(self, file_url: str) -> None:
        self.goto(file_url)

    def submit_registration(self, firstname: str, lastname: str, email: str, password: str,
                            newsletter: bool, agree_privacy: bool) -> None:
        self.page.locator(L.FIRSTNAME_INPUT).fill(firstname)
        self.page.locator(L.LASTNAME_INPUT).fill(lastname)
        self.page.locator(L.EMAIL_INPUT).fill(email)
        self.page.locator(L.PASSWORD_INPUT).fill(password)

        if newsletter:
            self.page.locator(L.NEWSLETTER_CHECKBOX).check()
        else:
            self.page.locator(L.NEWSLETTER_CHECKBOX).uncheck()

        if agree_privacy:
            self.page.locator(L.PRIVACY_POLICY_CHECKBOX).check()
        else:
            self.page.locator(L.PRIVACY_POLICY_CHECKBOX).uncheck()

        self.page.locator(L.CONTINUE_BUTTON).click()

    def read_state(self) -> dict:
        return {
            "content_container_visible": self.is_visible(L.CONTENT_CONTAINER),
            "header_visible": self.is_visible(L.REGISTER_HEADER),
            "form_visible": self.is_visible(L.REGISTER_FORM),
            "personal_details_legend_visible": self.is_visible(L.PERSONAL_DETAILS_LEGEND),
            "firstname_input_visible": self.is_visible(L.FIRSTNAME_INPUT),
            "lastname_input_visible": self.is_visible(L.LASTNAME_INPUT),
            "email_input_visible": self.is_visible(L.EMAIL_INPUT),
            "password_legend_visible": self.is_visible(L.PASSWORD_LEGEND),
            "password_input_visible": self.is_visible(L.PASSWORD_INPUT),
            "newsletter_legend_visible": self.is_visible(L.NEWSLETTER_LEGEND),
            "newsletter_checkbox_visible": self.is_visible(L.NEWSLETTER_CHECKBOX),
            "privacy_checkbox_visible": self.is_visible(L.PRIVACY_POLICY_CHECKBOX),
            "privacy_link_visible": self.is_visible(L.PRIVACY_POLICY_LINK),
            "continue_button_visible": self.is_visible(L.CONTINUE_BUTTON),
            "login_page_link_visible": self.is_visible(L.LOGIN_PAGE_LINK),
        }

    def read_errors(self) -> dict:
        # If errors are absent, Playwright locator.is_visible() may be false.
        return {
            "firstname_error_visible": self.page.locator(L.FIRSTNAME_ERROR).is_visible(),
            "lastname_error_visible": self.page.locator(L.LASTNAME_ERROR).is_visible(),
            "email_error_visible": self.page.locator(L.EMAIL_ERROR).is_visible(),
            "password_error_visible": self.page.locator(L.PASSWORD_ERROR).is_visible(),
            "firstname_error_text": self.page.locator(L.FIRSTNAME_ERROR).text_content() if self.page.locator(L.FIRSTNAME_ERROR).is_visible() else None,
            "lastname_error_text": self.page.locator(L.LASTNAME_ERROR).text_content() if self.page.locator(L.LASTNAME_ERROR).is_visible() else None,
            "email_error_text": self.page.locator(L.EMAIL_ERROR).text_content() if self.page.locator(L.EMAIL_ERROR).is_visible() else None,
            "password_error_text": self.page.locator(L.PASSWORD_ERROR).text_content() if self.page.locator(L.PASSWORD_ERROR).is_visible() else None,
        }
