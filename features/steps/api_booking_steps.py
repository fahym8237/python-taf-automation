from behave import given, when, then

from tas.core import DomainAssert
from tas.structure.api.clients.booking_client import BookingClient
from tas.structure.api.adapters.booking_api_adapter import BookingApiAdapter
from tas.domain.flows.booking_flows import BookingFlows


def _api(context):
    api = context.scenario_ctx.get_service("api")
    if not api:
        raise RuntimeError("API session not started. Ensure scenario has @api tag and api_base_url is set.")
    return api


def _booking_flows(context) -> BookingFlows:
    flows = context.scenario_ctx.get_service("booking_flows")
    if flows:
        return flows
    client = BookingClient(_api(context))
    adapter = BookingApiAdapter(client)
    flows = BookingFlows(adapter)
    context.scenario_ctx.set_service("booking_flows", flows)
    return flows


@when("I create a booking via API with valid data")
def step_create_booking(context):
    st = _booking_flows(context).create_booking_valid()
    context.scenario_ctx.get_service("data")["booking_id"] = st.booking_id


@then("the booking should be created successfully")
def step_created_ok(context):
    booking_id = context.scenario_ctx.get_service("data").get("booking_id")
    DomainAssert.that(booking_id, "booking_id").is_not_none()
    DomainAssert.that(isinstance(booking_id, int), "booking_id_is_int").is_true()


@then("I can retrieve the booking by id")
def step_get_booking(context):
    booking_id = context.scenario_ctx.get_service("data")["booking_id"]
    obj = _booking_flows(context).get_should_succeed(booking_id)
    DomainAssert.that(obj.get("firstname"), "firstname").is_not_none()


@given("I have an existing booking via API")
def step_have_booking(context):
    st = _booking_flows(context).create_booking_valid()
    context.scenario_ctx.get_service("data")["booking_id"] = st.booking_id


@when("I update the booking using PUT")
def step_put(context):
    booking_id = context.scenario_ctx.get_service("data")["booking_id"]
    obj = _booking_flows(context).put_update(booking_id)
    context.scenario_ctx.get_service("data")["put_obj"] = obj


@then("the booking data should be updated")
def step_put_assert(context):
    obj = context.scenario_ctx.get_service("data")["put_obj"]
    DomainAssert.that(obj.get("firstname"), "firstname").is_equal_to("James")


@when("I update the booking using PATCH")
def step_patch(context):
    booking_id = context.scenario_ctx.get_service("data")["booking_id"]
    obj = _booking_flows(context).patch_update(booking_id)
    context.scenario_ctx.get_service("data")["patch_obj"] = obj


@then("the booking data should be partially updated")
def step_patch_assert(context):
    obj = context.scenario_ctx.get_service("data")["patch_obj"]
    DomainAssert.that(obj.get("firstname"), "firstname").is_equal_to("Jimmy")


@when("I delete the booking")
def step_delete(context):
    booking_id = context.scenario_ctx.get_service("data")["booking_id"]
    _booking_flows(context).delete_then_get_should_404(booking_id)


@then("the booking should not be retrievable")
def step_not_retrievable(context):
    # already asserted in flow; keep step for readability
    DomainAssert.that(True, "delete_verified").is_true()