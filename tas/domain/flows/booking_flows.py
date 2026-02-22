from tas.domain.models.booking import BookingDraft, BookingRef, Booking
from tas.domain.ports.booking_port import BookingPort

class BookingFlows:
    def __init__(self, port: BookingPort):
        self._port = port

    def create_booking(self, draft: BookingDraft) -> BookingRef:
        return self._port.create(draft)

    def read_booking(self, ref: BookingRef) -> Booking:
        return self._port.read(ref)

    def update_booking_put(self, ref: BookingRef, draft: BookingDraft) -> Booking:
        return self._port.update_put(ref, draft)

    def update_booking_patch(self, ref: BookingRef, patch: dict) -> Booking:
        return self._port.update_patch(ref, patch)

    def delete_booking(self, ref: BookingRef) -> None:
        self._port.delete(ref)
