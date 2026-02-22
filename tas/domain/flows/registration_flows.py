from tas.domain.models.user import RegistrationDraft, RegistrationResult
from tas.domain.ports.registration_port import RegistrationPort, RegisterPageState

class RegistrationFlows:
    def __init__(self, port: RegistrationPort):
        self._port = port

    def open_register(self) -> None:
        self._port.open_register_page()

    def register_page_should_render(self) -> RegisterPageState:
        return self._port.read_register_page_state()

    def submit_registration(self, draft: RegistrationDraft) -> RegistrationResult:
        self._port.submit_registration(draft)
        return self._port.read_registration_errors()
