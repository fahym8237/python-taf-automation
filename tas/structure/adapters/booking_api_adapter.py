from tas.domain.models.booking import BookingDraft, BookingRef, Booking
from tas.domain.ports.booking_port import BookingPort
from tas.structure.api.clients.booking_client import BookingClient

class BookingApiAdapter(BookingPort):
    def __init__(self, client: BookingClient):
        self._client = client

    def create(self, draft: BookingDraft) -> BookingRef:
        payload = {
            "firstname": draft.firstname,
            "lastname": draft.lastname,
            "totalprice": draft.total_price,
            "depositpaid": draft.deposit_paid,
            "bookingdates": {"checkin": draft.checkin, "checkout": draft.checkout},
            "additionalneeds": draft.additional_needs,
        }
        resp = self._client.create(payload)
        booking_id = int(resp.json.get("bookingid"))
        return BookingRef(booking_id=booking_id)

    def read(self, ref: BookingRef) -> Booking:
        resp = self._client.read(ref.booking_id)
        j = resp.json
        return Booking(
            booking_id=ref.booking_id,
            firstname=j["firstname"],
            lastname=j["lastname"],
            total_price=j["totalprice"],
            deposit_paid=j["depositpaid"],
            checkin=j["bookingdates"]["checkin"],
            checkout=j["bookingdates"]["checkout"],
            additional_needs=j.get("additionalneeds"),
        )

    def update_put(self, ref: BookingRef, draft: BookingDraft) -> Booking:
        payload = {
            "firstname": draft.firstname,
            "lastname": draft.lastname,
            "totalprice": draft.total_price,
            "depositpaid": draft.deposit_paid,
            "bookingdates": {"checkin": draft.checkin, "checkout": draft.checkout},
            "additionalneeds": draft.additional_needs,
        }
        resp = self._client.update_put(ref.booking_id, payload)
        j = resp.json
        return Booking(
            booking_id=ref.booking_id,
            firstname=j["firstname"],
            lastname=j["lastname"],
            total_price=j["totalprice"],
            deposit_paid=j["depositpaid"],
            checkin=j["bookingdates"]["checkin"],
            checkout=j["bookingdates"]["checkout"],
            additional_needs=j.get("additionalneeds"),
        )

    def update_patch(self, ref: BookingRef, patch: dict) -> Booking:
        resp = self._client.update_patch(ref.booking_id, patch)
        j = resp.json
        return Booking(
            booking_id=ref.booking_id,
            firstname=j["firstname"],
            lastname=j["lastname"],
            total_price=j["totalprice"],
            deposit_paid=j["depositpaid"],
            checkin=j["bookingdates"]["checkin"],
            checkout=j["bookingdates"]["checkout"],
            additional_needs=j.get("additionalneeds"),
        )

    def delete(self, ref: BookingRef) -> None:
        self._client.delete(ref.booking_id)
