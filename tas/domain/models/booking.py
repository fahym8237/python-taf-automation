from dataclasses import dataclass
from typing import Optional

@dataclass(frozen=True)
class BookingDraft:
    firstname: str
    lastname: str
    total_price: int
    deposit_paid: bool
    checkin: str   
    checkout: str
    additional_needs: Optional[str] = None

@dataclass(frozen=True)
class BookingRef:
    booking_id: int

@dataclass(frozen=True)
class Booking:
    booking_id: int
    firstname: str
    lastname: str
    total_price: int
    deposit_paid: bool
    checkin: str
    checkout: str
    additional_needs: Optional[str] = None
