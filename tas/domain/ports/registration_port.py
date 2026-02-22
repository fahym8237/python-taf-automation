from __future__ import annotations
from dataclasses import dataclass
from typing import Protocol

from tas.domain.models.user import RegistrationDraft, RegistrationResult

@dataclass(frozen=True)
class RegisterPageState:
    content_container_visible: bool
    header_visible: bool
    form_visible: bool
    personal_details_legend_visible: bool
    firstname_input_visible: bool
    lastname_input_visible: bool
    email_input_visible: bool
    password_legend_visible: bool
    password_input_visible: bool
    newsletter_legend_visible: bool
    newsletter_checkbox_visible: bool
    privacy_checkbox_visible: bool
    privacy_link_visible: bool
    continue_button_visible: bool
    login_page_link_visible: bool

class RegistrationPort(Protocol):
    def open_register_page(self) -> None: ...
    def read_register_page_state(self) -> RegisterPageState: ...

    def submit_registration(self, draft: RegistrationDraft) -> None: ...
    def read_registration_errors(self) -> RegistrationResult: ...
