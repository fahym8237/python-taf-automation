import os
from pydoc import text
from behave import given, when, then

from tas.core import DomainAssert
from tas.structure.ui.pages.openCartBasePage import PageContext
from tas.structure.ui.pages.openCartLoginPage import OpenCartLoginPage
from tas.domain.flows.openCartLoginPageFlows import OpenCartLoginPageFlows
from tas.domain.ports.openCartLoginPagePort import (
    OpenCartLoginPageState,
    LoginResultState,
)
from tas.core.util.runtimeCredentials import RuntimeCredentials


class OpenCartLoginPageAdapter:

    def __init__(self, page: OpenCartLoginPage):
        self._page = page
    def open_login_page(self) -> None:
        self._page.open_login_page()
    def read_login_page_state(self) -> OpenCartLoginPageState:
        return OpenCartLoginPageState(**self._page.read_state())
    def navigate_to_forgotten_password_page(self) -> None:
        self._page.click_forgotten_password_link()
    def navigate_to_register_account_page(self) -> None:
        self._page.click_register_continue_button()
    def is_forgotten_password_page_loaded(self) -> bool:
        return self._page.is_forgotten_password_page_loaded()
    def is_register_account_page_loaded(self) -> bool:
        return self._page.is_register_account_page_loaded()
    def enter_email(self, email: str) -> None:
        self._page.enter_email(email)
    def enter_password(self, password: str) -> None:
        self._page.enter_password(password)
    def submit_login(self) -> None:
        self._page.submit_login()
    def read_login_result_state(self) -> LoginResultState:
        return LoginResultState(**self._page.read_login_result())
    def is_password_masked(self) -> bool:
        return self._page.is_password_masked()
    def breadcrumb_contains(self, text: str) -> bool:
        return self._page.breadcrumb_contains(text)
    def click_side_menu_register_link(self) -> None:
        self._page.click_side_menu_register_link()
    def click_side_menu_forgotten_password_link(self) -> None:
        self._page.click_side_menu_forgotten_password_link()
    def click_side_menu_login_link(self) -> None:
        self._page.click_side_menu_login_link()
    def open_my_account_page_directly(self) -> None:
        self._page.open_my_account_page_directly()
    def open_edit_account_page_directly(self) -> None:
        self._page.open_edit_account_page_directly()
    def open_change_password_page_directly(self) -> None:
        self._page.open_change_password_page_directly()
    def is_redirected_to_login_page(self) -> bool:
        return self._page.is_redirected_to_login_page()
    def is_my_account_page_loaded(self) -> bool:
        return self._page.is_my_account_page_loaded()
    def logout_from_account_area(self) -> None:
        self._page.logout_from_account_area()
    def is_logged_out_successfully(self) -> bool:
        return self._page.is_logged_out_successfully()
    def open_login_page_again(self) -> None:
        self._page.open_login_page_again()
    def is_authenticated_login_access_handled(self) -> bool:
        return self._page.is_authenticated_login_access_handled()
    def set_desktop_viewport(self) -> None:
        self._page.set_desktop_viewport()
    def set_tablet_viewport(self) -> None:
        self._page.set_tablet_viewport()
    def set_mobile_viewport(self) -> None:
        self._page.set_mobile_viewport()
    def is_login_form_usable(self) -> bool:
        return self._page.is_login_form_usable()
    def are_primary_elements_visible(self) -> bool:
        return self._page.are_primary_elements_visible()
    def login_page_uses_https(self) -> bool:
        return self._page.login_page_uses_https()
    def enter_malicious_email_input(self) -> None:
        if hasattr(self._page, "start_javascript_alert_monitoring"):
            self._page.start_javascript_alert_monitoring()
        self._page.enter_malicious_email_input()
    def enter_malicious_password_input(self) -> None:
        self._page.enter_malicious_password_input()
    def is_browser_native_validation_displayed(self) -> bool:
        return self._page.is_browser_native_validation_displayed()
    def is_javascript_alert_displayed(self) -> bool:
        return self._page.is_javascript_alert_displayed()
    def submit_invalid_credentials_multiple_times(self) -> None:
        self._page.submit_invalid_credentials_multiple_times()
    def is_login_page_stable(self) -> bool:
        return self._page.is_login_page_stable()





def _ui(context):
    ui = context.scenario_ctx.get_service("ui")
    if not ui:
        raise RuntimeError("UI session not started. Ensure scenario has @ui tag.")
    return ui
def _login_url(context) -> str:
    cfg = context.run_ctx.services.get("config")

    if cfg and hasattr(cfg, "ui_pilot"):
        return cfg.ui_pilot.login_url

    url = os.getenv("OPENCART_LOGIN_URL")
    if not url:
        raise RuntimeError("Missing OpenCart login URL. Set OPENCART_LOGIN_URL or config.ui_pilot.login_url.")

    return url
def _valid_email() -> str:
    return RuntimeCredentials.get_login_email()
def _valid_password() -> str:
    return RuntimeCredentials.get_login_password()
def _invalid_email() -> str:
    return "invalid.user@example.invalid"
def _invalid_password() -> str:
    return "WrongPassword123!"
def _unregistered_email() -> str:
    return "unregistered.user@example.com"
def _flows(context) -> OpenCartLoginPageFlows:
    flows = context.scenario_ctx.get_service("opencart_login_flows")
    if flows:
        return flows

    ui = _ui(context)
    page_ctx = PageContext(page=ui.page, base_url="")
    login_page = OpenCartLoginPage(page_ctx, _login_url(context))
    adapter = OpenCartLoginPageAdapter(login_page)
    flows = OpenCartLoginPageFlows(adapter)

    context.scenario_ctx.set_service("opencart_login_flows", flows)
    return flows


@given("the user opens the OpenCart login page")
def step_open_opencart_login_page(context):
    _flows(context).open_login_page()

@then("the OpenCart login page should be loaded")
def step_login_page_loaded(context):
    state = _flows(context).login_page_should_be_displayed()
    DomainAssert.that(state.page_loaded, "opencart_login_page_loaded").is_true()

@then("the returning customer section should be displayed")
def step_returning_customer_section_displayed(context):
    state = _flows(context).login_page_should_be_displayed()
    DomainAssert.that(
        state.returning_customer_section_visible,
        "returning_customer_section_visible"
    ).is_true()

@then("the email field should be displayed")
def step_email_field_displayed(context):
    state = _flows(context).login_page_should_be_displayed()
    DomainAssert.that(state.email_field_visible, "email_field_visible").is_true()

@then("the password field should be displayed")
def step_password_field_displayed(context):
    state = _flows(context).login_page_should_be_displayed()
    DomainAssert.that(state.password_field_visible, "password_field_visible").is_true()

@then("the login button should be displayed")
def step_login_button_displayed(context):
    state = _flows(context).login_page_should_be_displayed()
    DomainAssert.that(state.login_button_visible, "login_button_visible").is_true()

@then("the forgotten password link should be displayed")
def step_forgotten_password_link_displayed(context):
    state = _flows(context).login_page_should_be_displayed()
    DomainAssert.that(
        state.forgotten_password_link_visible,
        "forgotten_password_link_visible"
    ).is_true()

@when("the user navigates to the forgotten password page")
def step_navigate_to_forgotten_password_page(context):
    _flows(context).navigate_to_forgotten_password_page()

@then("the forgotten password page should be loaded")
def step_forgotten_password_page_loaded(context):
    loaded = _flows(context).forgotten_password_page_should_be_loaded()
    DomainAssert.that(loaded, "forgotten_password_page_loaded").is_true()

@when("the user navigates to the register account page")
def step_navigate_to_register_account_page(context):
    _flows(context).navigate_to_register_account_page()

@then("the register account page should be loaded")
def step_register_account_page_loaded(context):
    loaded = _flows(context).register_account_page_should_be_loaded()
    DomainAssert.that(loaded, "register_account_page_loaded").is_true()


@when("the user submits the login form without credentials")
def step_submit_login_without_credentials(context):
    _flows(context).submit_login_form()

@when("the user enters a valid login email")
def step_enter_valid_login_email(context):
    _flows(context).enter_login_email(_valid_email())

@when("the user submits the login form without password")
def step_submit_login_without_password(context):
    _flows(context).submit_login_form()

@when("the user enters a valid login password")
def step_enter_valid_login_password(context):
    _flows(context).enter_login_password(_valid_password())

@when("the user submits the login form without email")
def step_submit_login_without_email(context):
    _flows(context).submit_login_form()

@when("the user enters an invalid login email")
def step_enter_invalid_login_email(context):
    _flows(context).enter_login_email(_invalid_email())

@when("the user enters an invalid login password")
def step_enter_invalid_login_password(context):
    _flows(context).enter_login_password(_invalid_password())

@when("the user submits the login form")
def step_submit_login_form(context):
    _flows(context).submit_login_form()

@when("the user enters an unregistered login email")
def step_enter_unregistered_login_email(context):
    _flows(context).enter_login_email(_unregistered_email())

@then("a login warning message should be displayed")
def step_login_warning_message_displayed(context):
    result = _flows(context).login_result_should_be_available()
    DomainAssert.that(result.warning_visible, "login_warning_visible").is_true()

@then("the user should be logged in successfully")
def step_user_logged_in_successfully(context):
    result = _flows(context).login_result_should_be_available()
    DomainAssert.that(result.logged_in, "user_logged_in_successfully").is_true()

@then("the login password field should mask the entered value")
def step_password_field_masks_value(context):
    masked = _flows(context).password_field_should_mask_value()
    DomainAssert.that(masked, "login_password_field_masked").is_true()

@then('the login page breadcrumb should display "{text}"')
def step_login_page_breadcrumb_should_display(context, text):
    displayed = _flows(context).login_page_breadcrumb_should_display(text)
    DomainAssert.that(displayed, f"breadcrumb_should_display_{text}").is_true()

@when("the user clicks the side menu register link on login page")
def step_click_side_menu_register_link(context):
    _flows(context).navigate_to_register_from_side_menu()

@when("the user clicks the side menu forgotten password link on login page")
def step_click_side_menu_forgotten_password_link(context):
    _flows(context).navigate_to_forgotten_password_from_side_menu()

@when("the user clicks the side menu login link on login page")
def step_click_side_menu_login_link(context):
    _flows(context).navigate_to_login_from_side_menu()

@then("the my account page should be loaded")
def step_my_account_page_should_be_loaded(context):
    loaded = _flows(context).my_account_page_should_be_loaded()
    DomainAssert.that(loaded, "my_account_page_loaded").is_true()

@when("the user opens the OpenCart my account page directly")
def step_open_my_account_page_directly(context):
    _flows(context).open_my_account_page_directly()

@when("the user opens the OpenCart edit account page directly")
def step_open_edit_account_page_directly(context):
    _flows(context).open_edit_account_page_directly()

@when("the user opens the OpenCart change password page directly")
def step_open_change_password_page_directly(context):
    _flows(context).open_change_password_page_directly()


@then("the user should be redirected to the login page")
def step_user_should_be_redirected_to_login_page(context):
    redirected = _flows(context).user_should_be_redirected_to_login_page()
    DomainAssert.that(redirected, "redirected_to_login_page").is_true()

@when("the user logs out from the account area")
def step_user_logs_out_from_account_area(context):
    _flows(context).logout_from_account_area()

@then("the user should be logged out successfully")
def step_user_should_be_logged_out_successfully(context):
    logged_out = _flows(context).user_should_be_logged_out_successfully()
    DomainAssert.that(logged_out, "user_logged_out_successfully").is_true()

@when("the user opens the OpenCart login page again")
def step_user_opens_login_page_again(context):
    _flows(context).open_login_page_again()

@then("the application should handle the authenticated login-page access correctly")
def step_authenticated_login_page_access_handled(context):
    handled = _flows(context).authenticated_login_access_should_be_handled()
    DomainAssert.that(handled, "authenticated_login_page_access_handled").is_true()

@when("the user sets the browser viewport to desktop size")
def step_set_desktop_viewport(context):
    _flows(context).set_desktop_viewport()

@when("the user sets the browser viewport to tablet size")
def step_set_tablet_viewport(context):
    _flows(context).set_tablet_viewport()

@when("the user sets the browser viewport to mobile size")
def step_set_mobile_viewport(context):
    _flows(context).set_mobile_viewport()

@then("the login page form should remain usable")
def step_login_form_should_remain_usable(context):
    usable = _flows(context).login_form_should_remain_usable()
    DomainAssert.that(usable, "login_form_usable").is_true()

@then("the login page primary elements should be visible")
def step_login_page_primary_elements_visible(context):
    visible = _flows(context).login_page_primary_elements_should_be_visible()
    DomainAssert.that(visible, "login_page_primary_elements_visible").is_true()
@then("the login page URL should use HTTPS")
def step_login_page_url_should_use_https(context):
    uses_https = _flows(context).login_page_should_use_https()
    DomainAssert.that(uses_https, "login_page_uses_https").is_true()

@when("the user enters malicious login email input")
def step_user_enters_malicious_login_email_input(context):
    _flows(context).enter_malicious_login_email_input()

@when("the user enters malicious login password input")
def step_user_enters_malicious_login_password_input(context):
    _flows(context).enter_malicious_login_password_input()

@then("a login browser Native message should be displayed")
def step_login_browser_native_message_should_be_displayed(context):
    displayed = _flows(context).login_browser_native_message_should_be_displayed()
    DomainAssert.that(displayed, "login_browser_native_validation_displayed").is_true()

@then("no PYaScript alert should be displayed")
def step_no_pyascript_alert_should_be_displayed(context):
    safe = _flows(context).no_javascript_alert_should_be_displayed()
    DomainAssert.that(safe, "no_javascript_alert_displayed").is_true()

@when("the user submits invalid login credentials multiple times")
def step_submit_invalid_login_credentials_multiple_times(context):
    _flows(context).submit_invalid_login_credentials_multiple_times()

@then("the login page should remain stable")
def step_login_page_should_remain_stable(context):
    stable = _flows(context).login_page_should_remain_stable()
    DomainAssert.that(stable, "login_page_stable_after_repeated_invalid_attempts").is_true()















