from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Dict, Optional

from tas.structure.api.clients.booking_client import BookingClient
from tas.interaction.api.api_response import ApiResponse


@dataclass(frozen=True)
class CreateBookingResult:
    booking_id: Optional[int]
    booking: Optional[Dict[str, Any]]
    status: int


class BookingApiAdapter:
    def __init__(self, client: BookingClient):
        self._client = client
        self._token: Optional[str] = None

    def ensure_token(self, username: str = "admin", password: str = "password123") -> str:
        if self._token:
            return self._token
        r = self._client.create_token(username, password)
        token = None
        if isinstance(r.json, dict):
            token = r.json.get("token")
        if not token:
            raise RuntimeError(f"Failed to obtain token. status={r.status} body={r.body_text}")
        self._token = token
        return token

    def create_booking(self, payload: Dict[str, Any]) -> CreateBookingResult:
        r = self._client.create_booking(payload)
        booking_id = None
        booking = None
        if isinstance(r.json, dict):
            booking_id = r.json.get("bookingid")
            booking = r.json.get("booking")
        return CreateBookingResult(booking_id=booking_id, booking=booking, status=r.status)

    def get_booking(self, booking_id: int) -> ApiResponse:
        return self._client.get_booking(booking_id)

    def update_put(self, booking_id: int, payload: Dict[str, Any]) -> ApiResponse:
        token = self.ensure_token()
        return self._client.update_booking_put(booking_id, payload, token=token)

    def update_patch(self, booking_id: int, payload: Dict[str, Any]) -> ApiResponse:
        token = self.ensure_token()
        return self._client.update_booking_patch(booking_id, payload, token=token)

    def delete(self, booking_id: int) -> ApiResponse:
        token = self.ensure_token()
        return self._client.delete_booking(booking_id, token=token)
