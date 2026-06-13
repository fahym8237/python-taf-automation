import os
from behave import given, when, then

from features.steps.openCartLoginPageSteps import OpenCartLoginPageAdapter, _login_url
from tas.core import DomainAssert
from tas.structure.ui.pages.openCartBasePage import PageContext
from tas.structure.ui.pages.openCartChangePasswordPage import OpenCartChangePasswordPage
from tas.domain.flows.openCartChangePasswordPageFlows import OpenCartChangePasswordPageFlows
from tas.domain.ports.openCartChangePasswordPagePort import OpenCartChangePasswordPageState
from tas.core.util.runtimeCredentials import RuntimeCredentials
from tas.domain.flows.openCartLoginPageFlows import (
    OpenCartLoginPageFlows
)

from tas.structure.ui.pages.openCartLoginPage import (
    OpenCartLoginPage
)



class OpenCartChangePasswordPageAdapter:

    def __init__(self, page: OpenCartChangePasswordPage):
        self._page = page
    def open_change_password_page(self) -> None:
        self._page.open_change_password_page()
    def read_change_password_page_state(self) -> OpenCartChangePasswordPageState:
        return OpenCartChangePasswordPageState(**self._page.read_state())
    def enter_valid_new_password(self) -> None:
        self._page.enter_valid_new_password()
    def enter_same_confirm_password(self) -> None:
        self._page.enter_same_confirm_password()
    def enter_different_confirm_password(self) -> None:
        self._page.enter_different_confirm_password()
    def submit_change_password_form(self) -> None:
        self._page.submit_form()
    def submit_change_password_form_without_passwords(self) -> None:
        self._page.submit_without_passwords()
    def is_password_changed_successfully(self) -> bool:
        return self._page.is_password_changed_successfully()
    def is_password_validation_error_displayed(self) -> bool:
        return self._page.is_password_validation_error_displayed()
    def is_confirm_password_validation_error_displayed(self) -> bool:
        return self._page.is_confirm_password_validation_error_displayed()
    def is_password_mismatch_validation_error_displayed(self) -> bool:
        return self._page.is_password_mismatch_validation_error_displayed()
    def is_password_field_masked(self) -> bool:
        return self._page.is_password_field_masked()
    def is_confirm_password_field_masked(self) -> bool:
        return self._page.is_confirm_password_field_masked()
    def click_back_button(self) -> None:
        self._page.click_back_button()
    def is_my_account_page_loaded(self) -> bool:
        return self._page.is_my_account_page_loaded()
    def latest_new_password(self) -> str | None:
        return self._page.latest_new_password()
    def breadcrumb_contains(self, text: str) -> bool:
        return self._page.breadcrumb_contains(text)
    def click_side_menu_my_account_link(self) -> None:
        self._page.click_side_menu_my_account_link()
    def click_side_menu_edit_account_link(self) -> None:
        self._page.click_side_menu_edit_account_link()
    def click_side_menu_password_link(self) -> None:
        self._page.click_side_menu_password_link()
    def click_side_menu_logout_link(self) -> None:
        self._page.click_side_menu_logout_link()
    def is_edit_account_page_loaded(self) -> bool:
        return self._page.is_edit_account_page_loaded()
    def is_logged_out_successfully(self) -> bool:
        return self._page.is_logged_out_successfully()
    def set_desktop_viewport(self) -> None:
        self._page.set_desktop_viewport()
    def set_tablet_viewport(self) -> None:
        self._page.set_tablet_viewport()
    def set_mobile_viewport(self) -> None:
        self._page.set_mobile_viewport()
    def is_change_password_form_usable(self) -> bool:
        return self._page.is_change_password_form_usable()
    def are_change_password_primary_elements_visible(self) -> bool:
        return self._page.are_change_password_primary_elements_visible()
    def change_password_page_uses_https(self) -> bool:
     return self._page.change_password_page_uses_https()
    def enter_malicious_password_input(self) -> None:
        self._page.enter_malicious_password_input()
    def enter_malicious_confirm_input(self) -> None:
        self._page.enter_malicious_confirm_input()
    def is_change_password_page_stable(self) -> bool:
        return self._page.is_change_password_page_stable()
    def is_javascript_alert_displayed(self) -> bool:
        return self._page.is_javascript_alert_displayed()
    def clear_authenticated_session(self) -> None:
        self._page.clear_authenticated_session()
    def open_change_password_page_directly(self) -> None:
        self._page.open_change_password_page_directly()
    def is_redirected_to_login_page(self) -> bool:
        return self._page.is_redirected_to_login_page()
    def logout_after_password_change(self) -> None:
        self._page.logout_after_password_change()
    def login_with_newly_changed_password(self) -> None:
        self._page.login_with_newly_changed_password()
    def login_with_old_password_after_password_change(self) -> None:
        self._page.login_with_old_password_after_password_change()
    def is_logged_in_after_password_change(self) -> bool:
        return self._page.is_logged_in_after_password_change()
    def is_login_warning_displayed_after_password_change(self) -> bool:
        return self._page.is_login_warning_displayed_after_password_change()
    def refresh_change_password_page(self) -> None:
        self._page.refresh_change_password_page()
    def is_password_field_empty(self) -> bool:
        return self._page.is_password_field_empty()
    def is_confirm_password_field_empty(self) -> bool:
        return self._page.is_confirm_password_field_empty()
                

def _ui(context):
    ui = context.scenario_ctx.get_service("ui")
    if not ui:
        raise RuntimeError("UI session not started. Ensure scenario has @ui tag.")
    return ui
def _flows(context) -> OpenCartChangePasswordPageFlows:
    flows = context.scenario_ctx.get_service("opencart_change_password_flows")
    if flows:
        return flows

    ui = _ui(context)
    page_ctx = PageContext(page=ui.page, base_url="")
    page = OpenCartChangePasswordPage(page_ctx)
    adapter = OpenCartChangePasswordPageAdapter(page)
    flows = OpenCartChangePasswordPageFlows(adapter)

    context.scenario_ctx.set_service("opencart_change_password_flows", flows)
    return flows
def _login_flows(context) -> OpenCartLoginPageFlows:

    flows = context.scenario_ctx.get_service(
        "opencart_login_flows"
    )

    if flows:
        return flows

    ui = _ui(context)

    page_ctx = PageContext(
        page=ui.page,
        base_url=""
    )

    login_page = OpenCartLoginPage(
        page_ctx,
        _login_url(context)
    )

    adapter = OpenCartLoginPageAdapter(
        login_page
    )

    flows = OpenCartLoginPageFlows(
        adapter
    )

    context.scenario_ctx.set_service(
        "opencart_login_flows",
        flows
    )

    return flows



@given("the user is logged in")
def step_user_is_logged_in(context):

    login_email = RuntimeCredentials.get_login_email()
    login_password = RuntimeCredentials.get_login_password()

    login_flows = _login_flows(context)

    login_flows.open_login_page()
    login_flows.enter_login_email(login_email)
    login_flows.enter_login_password(login_password)
    login_flows.submit_login_form()

    result = login_flows.login_result_should_be_available()
    
    DomainAssert.that(
        result.logged_in,
        "user_logged_in"
    ).is_true()
@given("the user navigates to the change password page")
def step_user_navigates_to_change_password_page(context):
    _flows(context).open_change_password_page()
@then("the OpenCart change password page should be loaded")
def step_change_password_page_loaded(context):
    state = _flows(context).change_password_page_should_be_displayed()
    DomainAssert.that(state.page_loaded, "change_password_page_loaded").is_true()
@then("the password field should be displayed on change password page")
def step_password_field_displayed_on_change_password_page(context):
    state = _flows(context).change_password_page_should_be_displayed()
    DomainAssert.that(state.password_field_visible, "change_password_password_field_visible").is_true()
@then("the password confirm field should be displayed on change password page")
def step_password_confirm_field_displayed_on_change_password_page(context):
    state = _flows(context).change_password_page_should_be_displayed()
    DomainAssert.that(state.confirm_field_visible, "change_password_confirm_field_visible").is_true()
@then("the continue button should be displayed on change password page")
def step_continue_button_displayed_on_change_password_page(context):
    state = _flows(context).change_password_page_should_be_displayed()
    DomainAssert.that(state.continue_button_visible, "change_password_continue_button_visible").is_true()
@then("the back button should be displayed on change password page")
def step_back_button_displayed_on_change_password_page(context):
    state = _flows(context).change_password_page_should_be_displayed()
    DomainAssert.that(state.back_button_visible, "change_password_back_button_visible").is_true()
@when("the user enters a valid new password on change password page")
def step_enter_valid_new_password_on_change_password_page(context):
    _flows(context).enter_valid_new_password()
@when("the user enters the same confirm password on change password page")
def step_enter_same_confirm_password_on_change_password_page(context):
    _flows(context).enter_same_confirm_password()
@when("the user enters a different confirm password on change password page")
def step_enter_different_confirm_password_on_change_password_page(context):
    _flows(context).enter_different_confirm_password()
@when("the user submits the change password form")
def step_submit_change_password_form(context):
    _flows(context).submit_change_password_form()
@when("the user submits the change password form without entering passwords")
def step_submit_change_password_form_without_passwords(context):
    _flows(context).submit_change_password_form_without_passwords()
@then("the password should be changed successfully")
def step_password_should_be_changed_successfully(context):

    changed = _flows(context).password_should_be_changed_successfully()

    DomainAssert.that(changed, "password_changed_successfully").is_true()
@then("a password validation error should be displayed on change password page")
def step_password_validation_error_displayed(context):
    displayed = _flows(context).password_validation_error_should_be_displayed()
    DomainAssert.that(displayed, "change_password_password_validation_error_displayed").is_true()
@then("a confirm password validation error should be displayed on change password page")
def step_confirm_password_validation_error_displayed(context):
    displayed = _flows(context).confirm_password_validation_error_should_be_displayed()
    DomainAssert.that(displayed, "change_password_confirm_validation_error_displayed").is_true()
@then("a password mismatch validation error should be displayed on change password page")
def step_password_mismatch_validation_error_displayed(context):
    displayed = _flows(context).password_mismatch_validation_error_should_be_displayed()
    DomainAssert.that(displayed, "change_password_mismatch_validation_error_displayed").is_true()
@then("the password field should mask the entered value on change password page")
def step_password_field_masks_value_on_change_password_page(context):
    masked = _flows(context).password_field_should_mask_value()
    DomainAssert.that(masked, "change_password_field_masked").is_true()
@then("the confirm password field should mask the entered value on change password page")
def step_confirm_password_field_masks_value_on_change_password_page(context):
    masked = _flows(context).confirm_password_field_should_mask_value()
    DomainAssert.that(masked, "change_password_confirm_field_masked").is_true()
@when("the user clicks the back button on change password page")
def step_user_clicks_back_button_on_change_password_page(context):
    _flows(context).navigate_back_to_my_account_page()
@then("the my account page should be loaded from change password flow")
def step_my_account_page_loaded_from_change_password_flow(context):
    loaded = _flows(context).my_account_page_should_be_loaded()
    DomainAssert.that(loaded, "my_account_page_loaded_from_change_password_flow").is_true()
@then('the change password page breadcrumb should display "{text}"')
def step_change_password_breadcrumb_should_display(context, text):
    displayed = _flows(context).change_password_page_breadcrumb_should_display(text)
    DomainAssert.that(
        displayed,
        f"change_password_breadcrumb_should_display_{text}"
    ).is_true()
@when("the user clicks the side menu my account link on change password page")
def step_click_side_menu_my_account_link_on_change_password_page(context):
    _flows(context).navigate_to_my_account_from_side_menu()
@when("the user clicks the side menu edit account link on change password page")
def step_click_side_menu_edit_account_link_on_change_password_page(context):
    _flows(context).navigate_to_edit_account_from_side_menu()
@then("the edit account page should be loaded from change password flow")
def step_edit_account_page_loaded_from_change_password_flow(context):
    loaded = _flows(context).edit_account_page_should_be_loaded()
    DomainAssert.that(
        loaded,
        "edit_account_page_loaded_from_change_password_flow"
    ).is_true()
@when("the user clicks the side menu password link on change password page")
def step_click_side_menu_password_link_on_change_password_page(context):
    _flows(context).navigate_to_password_from_side_menu()
@when("the user clicks the side menu logout link on change password page")
def step_click_side_menu_logout_link_on_change_password_page(context):
    _flows(context).logout_from_side_menu()
@then("the user should be logged out successfully from change password flow")
def step_user_logged_out_successfully_from_change_password_flow(context):
    logged_out = _flows(context).user_should_be_logged_out_successfully()
    DomainAssert.that(
        logged_out,
        "user_logged_out_successfully_from_change_password_flow"
    ).is_true()
@when("the user sets the browser viewport to desktop size on change password page")
def step_set_desktop_viewport_on_change_password_page(context):
    _flows(context).set_desktop_viewport()
@when("the user sets the browser viewport to tablet size on change password page")
def step_set_tablet_viewport_on_change_password_page(context):
    _flows(context).set_tablet_viewport()
@when("the user sets the browser viewport to mobile size on change password page")
def step_set_mobile_viewport_on_change_password_page(context):
    _flows(context).set_mobile_viewport()
@then("the change password form should remain usable")
def step_change_password_form_should_remain_usable(context):
    usable = _flows(context).change_password_form_should_remain_usable()
    DomainAssert.that(
        usable,
        "change_password_form_usable"
    ).is_true()
@then("the change password page primary elements should be visible")
def step_change_password_primary_elements_should_be_visible(context):
    visible = _flows(context).change_password_primary_elements_should_be_visible()
    DomainAssert.that(
        visible,
        "change_password_primary_elements_visible"
    ).is_true()
@then("the change password page URL should use HTTPS")
def step_change_password_page_url_should_use_https(context):
    uses_https = _flows(context).change_password_page_should_use_https()
    DomainAssert.that(
        uses_https,
        "change_password_page_uses_https"
    ).is_true()
@when("the user enters malicious password input on change password page")
def step_user_enters_malicious_password_input_on_change_password_page(context):
    _flows(context).enter_malicious_password_input()
@when("the user enters malicious confirm input on change password page")
def step_user_enters_malicious_confirm_input_on_change_password_page(context):
    _flows(context).enter_malicious_confirm_input()
@then("the change password page should remain stable")
def step_change_password_page_should_remain_stable(context):
    stable = _flows(context).change_password_page_should_remain_stable()
    DomainAssert.that(
        stable,
        "change_password_page_stable"
    ).is_true()
@then("no PYaScript alert should be displayed on change password page")
def step_no_pyascript_alert_should_be_displayed_on_change_password_page(context):
    safe = _flows(context).no_javascript_alert_should_be_displayed()
    DomainAssert.that(
        safe,
        "no_javascript_alert_on_change_password_page"
    ).is_true()
@given("the user is not authenticated")
def step_user_is_not_authenticated(context):
    _flows(context).user_should_not_be_authenticated()
@when("the user tries to open the OpenCart change password page directly")
def step_user_tries_to_open_change_password_page_directly(context):
    _flows(context).open_change_password_page_directly()
@then("the user should be redirected to the login page from change password flow")
def step_user_redirected_to_login_page_from_change_password_flow(context):
    redirected = _flows(context).user_should_be_redirected_to_login_page()
    DomainAssert.that(
        redirected,
        "redirected_to_login_page_from_change_password_flow"
    ).is_true()
@when("the user logs out from the account area after password change")
def step_user_logs_out_after_password_change(context):
    _flows(context).logout_after_password_change()
@when("the user logs in with the newly changed password")
def step_user_logs_in_with_newly_changed_password(context):
    _flows(context).login_with_newly_changed_password()
@then("the user should be logged in successfully after password change")
def step_user_logged_in_successfully_after_password_change(context):
    logged_in = _flows(context).user_should_be_logged_in_after_password_change()
    DomainAssert.that(
        logged_in,
        "user_logged_in_successfully_after_password_change"
    ).is_true()
@when("the user logs in with the old password after password change")
def step_user_logs_in_with_old_password_after_password_change(context):
    _flows(context).login_with_old_password_after_password_change()
@then("a login warning message should be displayed after password change")
def step_login_warning_displayed_after_password_change(context):
    warning = _flows(context).login_warning_should_be_displayed_after_password_change()
    DomainAssert.that(
        warning,
        "login_warning_displayed_after_password_change"
    ).is_true()
@when("the user refreshes the change password page")
def step_user_refreshes_change_password_page(context):
    _flows(context).refresh_change_password_page()
@then("the password field should be empty on change password page")
def step_password_field_should_be_empty_on_change_password_page(context):
    empty = _flows(context).password_field_should_be_empty()
    DomainAssert.that(
        empty,
        "change_password_password_field_empty"
    ).is_true()
@then("the confirm password field should be empty on change password page")
def step_confirm_password_field_should_be_empty_on_change_password_page(context):
    empty = _flows(context).confirm_password_field_should_be_empty()
    DomainAssert.that(
        empty,
        "change_password_confirm_password_field_empty"
    ).is_true()