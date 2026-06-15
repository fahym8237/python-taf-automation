import os
from behave import given, when, then
from tas.core import DomainAssert
from tas.structure.ui.pages.openCartBasePage import PageContext
from tas.structure.ui.pages.openCartForgotPasswordPage import OpenCartForgotPasswordPage
from tas.domain.flows.openCartForgotPasswordPageFlows import OpenCartForgotPasswordPageFlows
from tas.domain.ports.openCartForgotPasswordPagePort import OpenCartForgotPasswordPageState


class OpenCartForgotPasswordPageAdapter:

    def __init__(self, page: OpenCartForgotPasswordPage):
        self._page = page
    def open_forgotten_password_page(self) -> None:
        self._page.open_forgotten_password_page()
    def read_forgotten_password_page_state(self) -> OpenCartForgotPasswordPageState:
        return OpenCartForgotPasswordPageState(**self._page.read_state())
    def enter_registered_email(self) -> None:
        self._page.enter_email(os.getenv("LOGIN_EMAIL"))
    def enter_unregistered_email(self) -> None:
        self._page.enter_email("unregistered.user@example.com")
    def enter_invalid_email(self) -> None:
        self._page.enter_email("invalid-email-format")
    def submit_forgotten_password_form(self) -> None:
        self._page.submit_form()
    def submit_forgotten_password_form_without_email(self) -> None:
        self._page.submit_without_email()
    def is_forgotten_password_request_accepted(self) -> bool:
        return self._page.is_request_accepted()
    def is_email_validation_error_displayed(self) -> bool:
        return self._page.is_email_validation_error_displayed()
    def click_back_button(self) -> None:
        self._page.click_back_button()
    def is_login_page_loaded(self) -> bool:
        return self._page.is_login_page_loaded()
    def breadcrumb_contains(self, text: str) -> bool:
        return self._page.breadcrumb_contains(text)
    def click_side_menu_login_link(self) -> None:
        self._page.click_side_menu_login_link()
    def click_side_menu_register_link(self) -> None:
        self._page.click_side_menu_register_link()
    def click_side_menu_forgotten_password_link(self) -> None:
        self._page.click_side_menu_forgotten_password_link()
    def is_register_account_page_loaded(self) -> bool:
        return self._page.is_register_account_page_loaded()
    def set_desktop_viewport(self) -> None:
        self._page.set_desktop_viewport()
    def set_tablet_viewport(self) -> None:
        self._page.set_tablet_viewport()
    def set_mobile_viewport(self) -> None:
        self._page.set_mobile_viewport()
    def is_forgotten_password_form_usable(self) -> bool:
        return self._page.is_forgotten_password_form_usable()
    def are_forgotten_password_primary_elements_visible(self) -> bool:
        return self._page.are_forgotten_password_primary_elements_visible()
    def forgotten_password_page_uses_https(self) -> bool:
        return self._page.forgotten_password_page_uses_https()
    def enter_malicious_email_input(self) -> None:
        self._page.enter_malicious_email_input()
    def enter_very_long_email(self) -> None:
        self._page.enter_very_long_email()
    def is_forgotten_password_page_stable(self) -> bool:
        return self._page.is_forgotten_password_page_stable()
    def is_javascript_alert_displayed(self) -> bool:
        return self._page.is_javascript_alert_displayed()
    def submit_form_multiple_times_with_unregistered_email(self) -> None:
        self._page.submit_form_multiple_times_with_unregistered_email()
    def refresh_forgotten_password_page(self) -> None:
        self._page.refresh_forgotten_password_page()
    def is_email_field_empty(self) -> bool:
        return self._page.is_email_field_empty()
    def navigate_back_in_browser_to_forgotten_password_page(self) -> None:
        self._page.navigate_back_in_browser_to_forgotten_password_page()
    def open_forgotten_password_page_again(self) -> None:
        self._page.open_forgotten_password_page_again()


def _ui(context):
    ui = context.scenario_ctx.get_service("ui")
    if not ui:
        raise RuntimeError("UI session not started. Ensure scenario has @ui tag.")
    return ui
def _forgotten_password_url(context) -> str:
    cfg = context.run_ctx.services.get("config")

    if cfg and hasattr(cfg, "ui_pilot") and hasattr(cfg.ui_pilot, "forgot_url"):
        return cfg.ui_pilot.forgot_url

    url = os.getenv("OPENCART_FORGOT_PASSWORD_URL")
    if not url:
        raise RuntimeError(
            "Missing forgotten password URL. Set OPENCART_FORGOT_PASSWORD_URL or config.ui_pilot.forgot_url."
        )

    return url
def _flows(context) -> OpenCartForgotPasswordPageFlows:
    flows = context.scenario_ctx.get_service("opencart_forgot_password_flows")
    if flows:
        return flows
    ui = _ui(context)
    page_ctx = PageContext(page=ui.page, base_url="")
    page = OpenCartForgotPasswordPage(page_ctx, _forgotten_password_url(context))
    adapter = OpenCartForgotPasswordPageAdapter(page)
    flows = OpenCartForgotPasswordPageFlows(adapter)
    context.scenario_ctx.set_service("opencart_forgot_password_flows", flows)
    return flows



@given("the user opens the OpenCart forgotten password page")
def step_open_forgotten_password_page(context):
    _flows(context).open_forgotten_password_page()
@then("the OpenCart forgotten password page should be loaded")
def step_forgotten_password_page_loaded(context):
    state = _flows(context).forgotten_password_page_should_be_displayed()
    DomainAssert.that(state.page_loaded, "forgotten_password_page_loaded").is_true()
@then("the forgotten password instruction text should be displayed")
def step_instruction_text_displayed(context):
    state = _flows(context).forgotten_password_page_should_be_displayed()
    DomainAssert.that(
        state.instruction_text_visible,
        "forgotten_password_instruction_text_visible"
    ).is_true()
@then("the email field should be displayed on forgotten password page")
def step_email_field_displayed_on_forgotten_password_page(context):
    state = _flows(context).forgotten_password_page_should_be_displayed()
    DomainAssert.that(
        state.email_field_visible,
        "forgotten_password_email_field_visible"
    ).is_true()
@then("the continue button should be displayed on forgotten password page")
def step_continue_button_displayed_on_forgotten_password_page(context):
    state = _flows(context).forgotten_password_page_should_be_displayed()
    DomainAssert.that(
        state.continue_button_visible,
        "forgotten_password_continue_button_visible"
    ).is_true()
@then("the back button should be displayed on forgotten password page")
def step_back_button_displayed_on_forgotten_password_page(context):
    state = _flows(context).forgotten_password_page_should_be_displayed()
    DomainAssert.that(
        state.back_button_visible,
        "forgotten_password_back_button_visible"
    ).is_true()
@when("the user enters a registered email on forgotten password page")
def step_enter_registered_email_on_forgotten_password_page(context):
    _flows(context).enter_registered_email()
@when("the user enters an unregistered email on forgotten password page")
def step_enter_unregistered_email_on_forgotten_password_page(context):
    _flows(context).enter_unregistered_email()
@when("the user enters an invalid email on forgotten password page")
def step_enter_invalid_email_on_forgotten_password_page(context):
    _flows(context).enter_invalid_email()
@when("the user submits the forgotten password form")
def step_submit_forgotten_password_form(context):
    _flows(context).submit_forgotten_password_form()
@when("the user submits the forgotten password form without email")
def step_submit_forgotten_password_form_without_email(context):
    _flows(context).submit_forgotten_password_form_without_email()
@then("the forgotten password request should be accepted")
def step_forgotten_password_request_should_be_accepted(context):
    accepted = _flows(context).forgotten_password_request_should_be_accepted()
    DomainAssert.that(
        accepted,
        "forgotten_password_request_accepted"
    ).is_true()
@then("the email validation error should be displayed on forgotten password page")
def step_email_validation_error_displayed_on_forgotten_password_page(context):
    displayed = _flows(context).email_validation_error_should_be_displayed()
    DomainAssert.that(
        displayed,
        "forgotten_password_email_validation_error_displayed"
    ).is_true()
@when("the user clicks the back button on forgotten password page")
def step_click_back_button_on_forgotten_password_page(context):
    _flows(context).navigate_back_to_login_page()
@then('the forgotten password page breadcrumb should display "{text}"')
def step_forgotten_password_breadcrumb_should_display(context, text):
    displayed = _flows(context).forgotten_password_page_breadcrumb_should_display(text)
    DomainAssert.that(
        displayed,
        f"forgotten_password_breadcrumb_should_display_{text}"
    ).is_true()
@when("the user clicks the side menu login link on forgotten password page")
def step_click_side_menu_login_link_on_forgotten_password_page(context):
    _flows(context).navigate_to_login_from_side_menu()
@when("the user clicks the side menu register link on forgotten password page")
def step_click_side_menu_register_link_on_forgotten_password_page(context):
    _flows(context).navigate_to_register_from_side_menu()
@when("the user clicks the side menu forgotten password link on forgotten password page")
def step_click_side_menu_forgotten_password_link_on_forgotten_password_page(context):
    _flows(context).navigate_to_forgotten_password_from_side_menu()
@then("the register account page should be loaded from forgotten password flow")
def step_register_account_page_loaded_from_forgotten_password_flow(context):
    loaded = _flows(context).register_account_page_should_be_loaded()
    DomainAssert.that(
        loaded,
        "register_account_page_loaded_from_forgotten_password_flow"
    ).is_true()
@when("the user sets the browser viewport to desktop size on forgotten password page")
def step_set_desktop_viewport_on_forgotten_password_page(context):
    _flows(context).set_desktop_viewport()
@when("the user sets the browser viewport to tablet size on forgotten password page")
def step_set_tablet_viewport_on_forgotten_password_page(context):
    _flows(context).set_tablet_viewport()
@when("the user sets the browser viewport to mobile size on forgotten password page")
def step_set_mobile_viewport_on_forgotten_password_page(context):
    _flows(context).set_mobile_viewport()
@then("the forgotten password form should remain usable")
def step_forgotten_password_form_should_remain_usable(context):
    usable = _flows(context).forgotten_password_form_should_remain_usable()
    DomainAssert.that(
        usable,
        "forgotten_password_form_usable"
    ).is_true()
@then("the forgotten password page primary elements should be visible")
def step_forgotten_password_primary_elements_should_be_visible(context):
    visible = _flows(context).forgotten_password_primary_elements_should_be_visible()
    DomainAssert.that(
        visible,
        "forgotten_password_primary_elements_visible"
    ).is_true()
@then("the forgotten password page URL should use HTTPS")
def step_forgotten_password_page_url_should_use_https(context):
    uses_https = _flows(context).forgotten_password_page_should_use_https()
    DomainAssert.that(
        uses_https,
        "forgotten_password_page_uses_https"
    ).is_true()
@when("the user enters malicious email input on forgotten password page")
def step_enter_malicious_email_input_on_forgotten_password_page(context):
    _flows(context).enter_malicious_email_input()
@then("the forgotten password page should remain stable")
def step_forgotten_password_page_should_remain_stable(context):
    stable = _flows(context).forgotten_password_page_should_remain_stable()
    DomainAssert.that(
        stable,
        "forgotten_password_page_stable"
    ).is_true()
@then("no PYaScript alert should be displayed on forgotten password page")
def step_no_pyascript_alert_should_be_displayed_on_forgotten_password_page(context):
    safe = _flows(context).no_javascript_alert_should_be_displayed()
    DomainAssert.that(
        safe,
        "no_javascript_alert_on_forgotten_password_page"
    ).is_true()
@when("the user enters a very long email on forgotten password page")
def step_enter_very_long_email_on_forgotten_password_page(context):
    _flows(context).enter_very_long_email()
@when("the user submits the forgotten password form multiple times with unregistered email")
def step_submit_forgotten_password_form_multiple_times_with_unregistered_email(context):
    _flows(context).submit_form_multiple_times_with_unregistered_email()
@when("the user refreshes the forgotten password page")
def step_user_refreshes_forgotten_password_page(context):
    _flows(context).refresh_forgotten_password_page()
@then("the email field should be empty on forgotten password page")
def step_email_field_should_be_empty_on_forgotten_password_page(context):
    empty = _flows(context).email_field_should_be_empty()
    DomainAssert.that(
        empty,
        "forgotten_password_email_field_empty"
    ).is_true()
@when("the user navigates back in the browser from login to forgotten password page")
def step_user_navigates_back_from_login_to_forgotten_password_page(context):
    _flows(context).navigate_back_in_browser_to_forgotten_password_page()
@when("the user opens the OpenCart forgotten password page again")
def step_user_opens_forgotten_password_page_again(context):
    _flows(context).open_forgotten_password_page_again()