#temporary, can delete later
#We verify that:
    #imports work
    #flows can execute using fake ports
    #the domain is tool-agnostic (no Playwright imports)

from dataclasses import replace
from tas.domain.flows.auth_flows import AuthFlows
from tas.domain.ports.auth_port import AuthPort, LoginPageState, ForgotPasswordPageState

class FakeAuthPort(AuthPort):
    def open_login_page(self) -> None: pass
    def open_forgot_password_page(self) -> None: pass
    def click_forgotten_password_link(self) -> None: pass
    def login(self, creds) -> None: pass

    def read_login_page_state(self) -> LoginPageState:
        return LoginPageState(True, True, True, True, True, True)

    def read_forgot_password_page_state(self) -> ForgotPasswordPageState:
        return ForgotPasswordPageState(True, True, True, True, True, True, True, True)

if __name__ == "__main__":
    flows = AuthFlows(FakeAuthPort())
    flows.open_login()
    state = flows.login_page_should_render()
    assert state.login_form_visible
    print("Layer 3 domain smoke OK")
