from typing import Any, Dict, Optional

class BookingClient:
    """
    Structure-level endpoint wrapper.
    Implementation will be wired to Interaction.ApiSession in Layer 6.
    """

    def __init__(self, api_session: Any):
        self._api = api_session

    def create(self, payload: Dict[str, Any]):
        return self._api.post("/booking", json=payload)

    def read(self, booking_id: int):
        return self._api.get(f"/booking/{booking_id}")

    def update_put(self, booking_id: int, payload: Dict[str, Any]):
        return self._api.put(f"/booking/{booking_id}", json=payload)

    def update_patch(self, booking_id: int, patch: Dict[str, Any]):
        return self._api.patch(f"/booking/{booking_id}", json=patch)

    def delete(self, booking_id: int):
        return self._api.delete(f"/booking/{booking_id}")
