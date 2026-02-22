from tas.domain.ports.auth_port import AuthPort, LoginPageState, ForgotPasswordPageState

class AuthFlows:
    def __init__(self, port: AuthPort):
        self._port = port

    def open_login(self) -> None:
        self._port.open_login_page()

    def login_page_should_render(self) -> LoginPageState:
        state = self._port.read_login_page_state()
        # Business-level expectation: all required elements must be visible
        # We don't assert here yet (assertions in Layer 5); return state for step assertions later
        return state

    def navigate_to_forgot_password_from_login(self) -> None:
        self._port.open_login_page()
        self._port.click_forgotten_password_link()

    def forgot_password_page_should_render(self) -> ForgotPasswordPageState:
        return self._port.read_forgot_password_page_state()
