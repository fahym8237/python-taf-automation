from dataclasses import dataclass
from typing import Optional

@dataclass(frozen=True)
class UserCredentials:
    email: str
    password: str

@dataclass(frozen=True)
class RegistrationDraft:
    firstname: str
    lastname: str
    email: str
    password: str
    newsletter: bool = False
    agree_privacy: bool = True

@dataclass(frozen=True)
class RegistrationResult:
    # field -> error message (or True/False flags; we keep messages optional)
    firstname_error: Optional[str] = None
    lastname_error: Optional[str] = None
    email_error: Optional[str] = None
    password_error: Optional[str] = None

    def has_errors(self) -> bool:
        return any([self.firstname_error, self.lastname_error, self.email_error, self.password_error])
