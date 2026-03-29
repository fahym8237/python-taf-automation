from tas.domain.models.user import UserCredentials
from tas.domain.ports.auth_port import AuthPort, LoginPageState, ForgotPasswordPageState
from tas.structure.ui.pages.login_page import LoginPage
from tas.structure.ui.pages.forgot_password_page import ForgotPasswordPage

class AuthUiAdapter(AuthPort):
    def __init__(self, login_page: LoginPage, forgot_page: ForgotPasswordPage, login_file_url: str, forgot_file_url: str):
        self._login = login_page
        self._forgot = forgot_page
        self._login_url = login_file_url
        self._forgot_url = forgot_file_url

    def open_login_page(self) -> None:
        self._login.open_file(self._login_url)

    def open_forgot_password_page(self) -> None:
        self._forgot.open_file(self._forgot_url)

    def click_forgotten_password_link(self) -> None:
        self._login.click_forgotten_password()

    def read_login_page_state(self) -> LoginPageState:
        s = self._login.read_state()
        return LoginPageState(**s)

    def read_forgot_password_page_state(self) -> ForgotPasswordPageState:
        s = self._forgot.read_state()
        return ForgotPasswordPageState(**s)

    def login(self, creds: UserCredentials) -> None:
        # Pilot HTML has no backend; keep as no-op for now
        # Later if button triggers JS validation, we can fill inputs + click
        self._login.page.locator("#input-email").fill(creds.email)
        self._login.page.locator("#input-password").fill(creds.password)
        self._login.page.locator("xpath=//button[normalize-space()='Login']").click()
