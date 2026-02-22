from tas.domain.flows.auth_flows import AuthFlows

class AuthJourneys:
    def __init__(self, auth: AuthFlows):
        self._auth = auth

    def login_page_smoke(self):
        self._auth.open_login()
        return self._auth.login_page_should_render()
