from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Dict, Optional

from tas.core import DomainAssert
from tas.structure.api.adapters.booking_api_adapter import BookingApiAdapter


@dataclass
class BookingCrudState:
    booking_id: Optional[int] = None
    created_payload: Optional[Dict[str, Any]] = None


class BookingFlows:
    def __init__(self, adapter: BookingApiAdapter):
        self._a = adapter

    def create_booking_valid(self) -> BookingCrudState:
        payload = {
            "firstname": "Jim",
            "lastname": "Brown",
            "totalprice": 111,
            "depositpaid": True,
            "bookingdates": {"checkin": "2018-01-01", "checkout": "2019-01-01"},
            "additionalneeds": "Breakfast",
        }
        res = self._a.create_booking(payload)
        DomainAssert.that(res.status, "create_status").is_equal_to(200)
        DomainAssert.that(res.booking_id, "booking_id").is_not_none()
        DomainAssert.that(isinstance(res.booking_id, int), "booking_id_is_int").is_true()
        return BookingCrudState(booking_id=res.booking_id, created_payload=payload)

    def get_should_succeed(self, booking_id: int) -> Dict[str, Any]:
        r = self._a.get_booking(booking_id)
        DomainAssert.that(r.status, "get_status").is_equal_to(200)
        DomainAssert.that(isinstance(r.json, dict), "get_json_is_dict").is_true()
        return r.json  # type: ignore

    def put_update(self, booking_id: int) -> Dict[str, Any]:
        payload = {
            "firstname": "James",
            "lastname": "Brown",
            "totalprice": 222,
            "depositpaid": False,
            "bookingdates": {"checkin": "2018-02-01", "checkout": "2019-02-01"},
            "additionalneeds": "Lunch",
        }
        r = self._a.update_put(booking_id, payload)
        DomainAssert.that(r.status, "put_status").is_equal_to(200)
        DomainAssert.that(isinstance(r.json, dict), "put_json_is_dict").is_true()
        return r.json  # type: ignore

    def patch_update(self, booking_id: int) -> Dict[str, Any]:
        payload = {"firstname": "Jimmy"}
        r = self._a.update_patch(booking_id, payload)
        DomainAssert.that(r.status, "patch_status").is_equal_to(200)
        DomainAssert.that(isinstance(r.json, dict), "patch_json_is_dict").is_true()
        return r.json  # type: ignore

    def delete_then_get_should_404(self, booking_id: int) -> None:
        d = self._a.delete(booking_id)
        DomainAssert.that(d.status, "delete_status").matches(lambda s: s in (201, 200), "Expected delete success")
        g = self._a.get_booking(booking_id)
        DomainAssert.that(g.status, "get_after_delete_status").matches(lambda s: s in (404, 410))
