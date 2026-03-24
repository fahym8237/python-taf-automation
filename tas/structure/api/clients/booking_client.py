from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Dict, Optional

from tas.interaction.api.api_session import ApiSession
from tas.interaction.api.api_response import ApiResponse


class BookingClient:
    def __init__(self, api: ApiSession):
        self._api = api

    def create_booking(self, payload: Dict[str, Any]) -> ApiResponse:
        return self._api.post("/booking", json=payload)

    def get_booking(self, booking_id: int) -> ApiResponse:
        return self._api.get(f"/booking/{booking_id}")

    def update_booking_put(self, booking_id: int, payload: Dict[str, Any], token: Optional[str] = None) -> ApiResponse:
        headers = {"Content-Type": "application/json"}
        if token:
            headers["Cookie"] = f"token={token}"
        return self._api.put(f"/booking/{booking_id}", json=payload, headers=headers)

    def update_booking_patch(self, booking_id: int, payload: Dict[str, Any], token: Optional[str] = None) -> ApiResponse:
        headers = {"Content-Type": "application/json"}
        if token:
            headers["Cookie"] = f"token={token}"
        return self._api.patch(f"/booking/{booking_id}", json=payload, headers=headers)

    def delete_booking(self, booking_id: int, token: Optional[str] = None) -> ApiResponse:
        headers = {}
        if token:
            headers["Cookie"] = f"token={token}"
        return self._api.delete(f"/booking/{booking_id}", headers=headers)

    def create_token(self, username: str, password: str) -> ApiResponse:
        return self._api.post("/auth", json={"username": username, "password": password})
