from tas.domain.models.user import RegistrationDraft, RegistrationResult
from tas.domain.ports.registration_port import RegistrationPort, RegisterPageState
from tas.structure.ui.pages.register_page import RegisterPage

class RegistrationUiAdapter(RegistrationPort):
    def __init__(self, register_page: RegisterPage, register_file_url: str):
        self._register = register_page
        self._url = register_file_url

    def open_register_page(self) -> None:
        self._register.open_file(self._url)

    def read_register_page_state(self) -> RegisterPageState:
        s = self._register.read_state()
        return RegisterPageState(**s)

    def submit_registration(self, draft: RegistrationDraft) -> None:
        self._register.submit_registration(
            firstname=draft.firstname,
            lastname=draft.lastname,
            email=draft.email,
            password=draft.password,
            newsletter=draft.newsletter,
            agree_privacy=draft.agree_privacy,
        )

    def read_registration_errors(self) -> RegistrationResult:
        e = self._register.read_errors()
        return RegistrationResult(
            firstname_error=e.get("firstname_error_text"),
            lastname_error=e.get("lastname_error_text"),
            email_error=e.get("email_error_text"),
            password_error=e.get("password_error_text"),
        )
