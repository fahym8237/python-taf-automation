from __future__ import annotations
from dataclasses import dataclass
from typing import Protocol

from tas.domain.models.user import UserCredentials

@dataclass(frozen=True)
class LoginPageState:
    login_form_visible: bool
    returning_customer_header_visible: bool
    email_input_visible: bool
    password_input_visible: bool
    login_button_visible: bool
    forgotten_password_link_visible: bool

@dataclass(frozen=True)
class ForgotPasswordPageState:
    content_container_visible: bool
    header_visible: bool
    instruction_visible: bool
    form_visible: bool
    email_legend_visible: bool
    email_input_visible: bool
    continue_button_visible: bool
    back_button_visible: bool

class AuthPort(Protocol):
    # Navigation
    def open_login_page(self) -> None: ...
    def open_forgot_password_page(self) -> None: ...
    def click_forgotten_password_link(self) -> None: ...

    # State reads (structural)
    def read_login_page_state(self) -> LoginPageState: ...
    def read_forgot_password_page_state(self) -> ForgotPasswordPageState: ...

    # Actions
    def login(self, creds: UserCredentials) -> None: ...
