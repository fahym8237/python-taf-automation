import os
from behave import given, when, then

from tas.core import DomainAssert
from tas.structure.ui.pages.openCartBasePage import PageContext
from tas.structure.ui.pages.openCartRegisterPage import OpenCartRegisterPage
from tas.domain.flows.openCartRegisterPageFlows import OpenCartRegisterPageFlows
from tas.domain.ports.openCartRegisterPagePort import OpenCartRegisterPageState
from tas.data.registry import resolve_dataset, load_dataset
from tas.data.validators import require_columns
from tas.data.transforms import parse_bool, with_unique_email

class OpenCartRegisterPageAdapter:

    def __init__(self, page: OpenCartRegisterPage):
        self._page = page
    def open_register_page(self) -> None:
        self._page.open_register_page()
    def read_register_page_state(self) -> OpenCartRegisterPageState:
        return OpenCartRegisterPageState(**self._page.read_state())
    def fill_registration_form_with_generated_user(self) -> None:
        self._page.fill_registration_form_with_generated_user()
    def enter_invalid_email(self) -> None:
        self._page.enter_invalid_email()
    def agree_to_privacy_policy(self) -> None:
        self._page.agree_to_privacy_policy()
    def submit_registration_form(self) -> None:
        self._page.submit_form()
    def submit_registration_form_without_fields(self) -> None:
        self._page.submit_without_fields()
    def is_success_message_visible(self, message: str) -> bool:
        return self._page.is_success_message_visible(message)
    def are_all_mandatory_errors_displayed(self) -> bool:
        return self._page.are_all_mandatory_errors_displayed()
    def is_privacy_policy_warning_displayed(self) -> bool:
        return self._page.is_privacy_policy_warning_displayed()
    def is_email_validation_error_displayed(self) -> bool:
        return self._page.is_email_validation_error_displayed()
    def is_password_field_masked(self) -> bool:
        return self._page.is_password_field_masked() 
    def refresh_register_page(self) -> None:
        self._page.refresh_register_page()
    def is_register_form_usable(self) -> bool:
        return self._page.is_register_form_usable()
    def is_firstname_field_empty(self) -> bool:
        return self._page.is_firstname_field_empty()
    def is_lastname_field_empty(self) -> bool:
        return self._page.is_lastname_field_empty()
    def is_email_field_empty(self) -> bool:
        return self._page.is_email_field_empty()
    def is_password_field_empty(self) -> bool:
        return self._page.is_password_field_empty()
    def click_login_link(self) -> None:
        self._page.click_login_link()
    def is_login_page_loaded(self) -> bool:
        return self._page.is_login_page_loaded()
    def navigate_back_in_browser_to_register_page(self) -> None:
        self._page.navigate_back_in_browser_to_register_page()
    def open_register_page_again(self) -> None:
        self._page.open_register_page_again() 
    def set_desktop_viewport(self) -> None:
        self._page.set_desktop_viewport()
    def set_tablet_viewport(self) -> None:
        self._page.set_tablet_viewport()
    def set_mobile_viewport(self) -> None:
        self._page.set_mobile_viewport()
    def are_register_primary_elements_visible(self) -> bool:
        return self._page.are_register_primary_elements_visible()
    def register_page_uses_https(self) -> bool:
        return self._page.register_page_uses_https()
    def enter_malicious_firstname_input(self) -> None:
        self._page.enter_malicious_firstname_input()
    def enter_malicious_lastname_input(self) -> None:
        self._page.enter_malicious_lastname_input()
    def enter_malicious_email_input(self) -> None:
        self._page.enter_malicious_email_input()
    def enter_malicious_password_input(self) -> None:
        self._page.enter_malicious_password_input()
    def enter_very_long_firstname(self) -> None:
        self._page.enter_very_long_firstname()
    def enter_very_long_lastname(self) -> None:
        self._page.enter_very_long_lastname()
    def enter_very_long_email(self) -> None:
        self._page.enter_very_long_email()
    def enter_very_long_password(self) -> None:
        self._page.enter_very_long_password()
    def is_register_page_stable(self) -> bool:
        return self._page.is_register_page_stable()
    def breadcrumb_contains(self, text: str) -> bool:
        return self._page.breadcrumb_contains(text)
    def click_side_menu_login_link(self) -> None:
        self._page.click_side_menu_login_link()
    def click_side_menu_register_link(self) -> None:
        self._page.click_side_menu_register_link()
    def click_side_menu_forgotten_password_link(self) -> None:
        self._page.click_side_menu_forgotten_password_link()
    def is_forgotten_password_page_loaded(self) -> bool:
        return self._page.is_forgotten_password_page_loaded()
    def click_privacy_policy_link(self) -> None:
        self._page.click_privacy_policy_link()
    def is_privacy_policy_opened(self) -> bool:
        return self._page.is_privacy_policy_opened()
    def execute_registration_dataset(self, dataset_name: str) -> None:
        ref = resolve_dataset(dataset_name)
        rows = load_dataset(ref)

        require_columns(
            rows,
            required=[
                "firstname",
                "lastname",
                "email",
                "password",
                "expect_firstname_error",
                "expect_lastname_error",
                "expect_email_error",
                "expect_password_error",
            ],
            dataset_name=ref.name,
        )

        results = []

        for index, row in enumerate(rows, start=1):
            safe_row = with_unique_email(row)

            self._page.open_register_page()

            self._page.submit_registration_data(
                firstname=safe_row.get("firstname", ""),
                lastname=safe_row.get("lastname", ""),
                email=safe_row.get("email", ""),
                password=safe_row.get("password", ""),
                agree_privacy=True,
            )

            actual = self._page.read_validation_errors()

            expected = {
                "firstname_error": parse_bool(safe_row["expect_firstname_error"]),
                "lastname_error": parse_bool(safe_row["expect_lastname_error"]),
                "email_error": parse_bool(safe_row["expect_email_error"]),
                "password_error": parse_bool(safe_row["expect_password_error"]),
            }

            results.append({
                "row": index,
                "input": safe_row,
                "expected": expected,
                "actual": actual,
                "passed": expected == actual,
            })

        self._dataset_results = results
    def all_registration_dataset_rows_passed(self) -> bool:
        failed = [
            result for result in getattr(self, "_dataset_results", [])
            if not result["passed"]
        ]

        if failed:
            print("Registration dataset failures:")
            for failure in failed:
                print(failure)

        return not failed

def _ui(context):
    ui = context.scenario_ctx.get_service("ui")
    if not ui:
        raise RuntimeError("UI session not started. Ensure scenario has @ui tag.")
    return ui
def _register_url(context) -> str:
    cfg = context.run_ctx.services.get("config")

    if cfg and hasattr(cfg, "ui_pilot") and hasattr(cfg.ui_pilot, "register_url"):
        return cfg.ui_pilot.register_url

    url = os.getenv("OPENCART_REGISTER_URL")
    if not url:
        raise RuntimeError(
            "Missing register URL. Set OPENCART_REGISTER_URL or config.ui_pilot.register_url."
        )

    return url
def _flows(context) -> OpenCartRegisterPageFlows:
    flows = context.scenario_ctx.get_service("opencart_register_flows")
    if flows:
        return flows

    ui = _ui(context)
    page_ctx = PageContext(page=ui.page, base_url="")
    page = OpenCartRegisterPage(page_ctx, _register_url(context))
    adapter = OpenCartRegisterPageAdapter(page)
    flows = OpenCartRegisterPageFlows(adapter)

    context.scenario_ctx.set_service("opencart_register_flows", flows)
    return flows

@given("the user opens the OpenCart register page")
def step_open_register_page(context):
    _flows(context).open_register_page()
@then("the OpenCart register page should be loaded")
def step_register_page_loaded(context):
    state = _flows(context).register_page_should_be_displayed()
    DomainAssert.that(state.page_loaded, "register_page_loaded").is_true()
@then("the first name field should be displayed on register page")
def step_firstname_field_displayed(context):
    state = _flows(context).register_page_should_be_displayed()
    DomainAssert.that(state.firstname_field_visible, "register_firstname_visible").is_true()
@then("the last name field should be displayed on register page")
def step_lastname_field_displayed(context):
    state = _flows(context).register_page_should_be_displayed()
    DomainAssert.that(state.lastname_field_visible, "register_lastname_visible").is_true()
@then("the email field should be displayed on register page")
def step_email_field_displayed(context):
    state = _flows(context).register_page_should_be_displayed()
    DomainAssert.that(state.email_field_visible, "register_email_visible").is_true()
@then("the password field should be displayed on register page")
def step_password_field_displayed(context):
    state = _flows(context).register_page_should_be_displayed()
    DomainAssert.that(state.password_field_visible, "register_password_visible").is_true()
@then("the continue button should be displayed on register page")
def step_continue_button_displayed(context):
    state = _flows(context).register_page_should_be_displayed()
    DomainAssert.that(state.continue_button_visible, "register_continue_visible").is_true()
@then("the privacy policy link should be displayed on register page")
def step_privacy_policy_link_displayed(context):
    state = _flows(context).register_page_should_be_displayed()
    DomainAssert.that(state.privacy_policy_link_visible, "register_privacy_policy_link_visible").is_true()
@then("the login link should be displayed on register page")
def step_login_link_displayed(context):
    state = _flows(context).register_page_should_be_displayed()
    DomainAssert.that(state.login_link_visible, "register_login_link_visible").is_true()
@when("the user fills the registration form with a generated valid user")
def step_fill_registration_form_with_generated_valid_user(context):
    _flows(context).fill_registration_form_with_generated_user()
@when("the user agrees to the privacy policy")
def step_user_agrees_to_privacy_policy(context):
    _flows(context).agree_to_privacy_policy()
@when("the user submits the registration form")
def step_submit_registration_form(context):
    _flows(context).submit_registration_form()
@then('the success message "{message}" should be visible')
def step_success_message_should_be_visible(context, message):
    visible = _flows(context).success_message_should_be_visible(message)
    DomainAssert.that(visible, f"success_message_visible_{message}").is_true()
@when("the user submits the registration form without filling any fields")
def step_submit_registration_form_without_fields(context):
    _flows(context).submit_registration_form_without_fields()
@then("all mandatory field validation errors should be displayed")
def step_all_mandatory_errors_displayed(context):
    displayed = _flows(context).all_mandatory_errors_should_be_displayed()
    DomainAssert.that(displayed, "register_all_mandatory_errors_displayed").is_true()
@then("a privacy policy warning should be displayed")
def step_privacy_policy_warning_displayed(context):
    displayed = _flows(context).privacy_policy_warning_should_be_displayed()
    DomainAssert.that(displayed, "register_privacy_policy_warning_displayed").is_true()
@when("the user enters an invalid email on register page")
def step_enter_invalid_email_on_register_page(context):
    _flows(context).enter_invalid_email()
@then("the email validation error should be displayed on register page")
def step_email_validation_error_displayed_on_register_page(context):
    displayed = _flows(context).email_validation_error_should_be_displayed()
    DomainAssert.that(displayed, "register_email_validation_error_displayed").is_true()
@then("the password field should mask the entered value on register page")
def step_password_field_masks_value_on_register_page(context):
    masked = _flows(context).password_field_should_mask_value()
    DomainAssert.that(masked, "register_password_field_masked").is_true()
@when("the user refreshes the register page")
def step_user_refreshes_register_page(context):
    _flows(context).refresh_register_page()
@then("the register form should remain usable")
def step_register_form_should_remain_usable(context):
    usable = _flows(context).register_form_should_remain_usable()
    DomainAssert.that(
        usable,
        "register_form_usable"
    ).is_true()
@then("the first name field should be empty on register page")
def step_firstname_field_should_be_empty_on_register_page(context):
    empty = _flows(context).firstname_field_should_be_empty()
    DomainAssert.that(
        empty,
        "register_firstname_field_empty"
    ).is_true()
@then("the last name field should be empty on register page")
def step_lastname_field_should_be_empty_on_register_page(context):
    empty = _flows(context).lastname_field_should_be_empty()
    DomainAssert.that(
        empty,
        "register_lastname_field_empty"
    ).is_true()
@then("the email field should be empty on register page")
def step_email_field_should_be_empty_on_register_page(context):
    empty = _flows(context).email_field_should_be_empty()
    DomainAssert.that(
        empty,
        "register_email_field_empty"
    ).is_true()
@then("the password field should be empty on register page")
def step_password_field_should_be_empty_on_register_page(context):
    empty = _flows(context).password_field_should_be_empty()
    DomainAssert.that(
        empty,
        "register_password_field_empty"
    ).is_true()
@when("the user clicks the login link on register page")
def step_user_clicks_login_link_on_register_page(context):
    _flows(context).navigate_to_login_from_register_page()
@then("the OpenCart login page should be loaded from register flow")
def step_login_page_should_be_loaded_from_register_flow(context):
    loaded = _flows(context).login_page_should_be_loaded()
    DomainAssert.that(
        loaded,
        "login_page_loaded_from_register_flow"
    ).is_true()
@when("the user navigates back in the browser from login to register page")
def step_user_navigates_back_from_login_to_register_page(context):
    _flows(context).navigate_back_in_browser_to_register_page()
@when("the user opens the OpenCart register page again")
def step_user_opens_register_page_again(context):
    _flows(context).open_register_page_again()
@when("the user sets the browser viewport to desktop size on register page")
def step_set_desktop_viewport_on_register_page(context):
    _flows(context).set_desktop_viewport()
@when("the user sets the browser viewport to tablet size on register page")
def step_set_tablet_viewport_on_register_page(context):
    _flows(context).set_tablet_viewport()
@when("the user sets the browser viewport to mobile size on register page")
def step_set_mobile_viewport_on_register_page(context):
    _flows(context).set_mobile_viewport()
@then("the register page primary elements should be visible")
def step_register_primary_elements_visible(context):
    visible = _flows(context).register_primary_elements_should_be_visible()
    DomainAssert.that(visible, "register_primary_elements_visible").is_true()
@then("the register page URL should use HTTPS")
def step_register_page_url_should_use_https(context):
    uses_https = _flows(context).register_page_should_use_https()
    DomainAssert.that(uses_https, "register_page_uses_https").is_true()
@when("the user enters malicious first name input on register page")
def step_malicious_firstname_on_register_page(context):
    _flows(context).enter_malicious_firstname_input()
@when("the user enters malicious last name input on register page")
def step_malicious_lastname_on_register_page(context):
    _flows(context).enter_malicious_lastname_input()
@when("the user enters malicious email input on register page")
def step_malicious_email_on_register_page(context):
    _flows(context).enter_malicious_email_input()
@when("the user enters malicious password input on register page")
def step_malicious_password_on_register_page(context):
    _flows(context).enter_malicious_password_input()
@when("the user enters a very long first name on register page")
def step_very_long_firstname_on_register_page(context):
    _flows(context).enter_very_long_firstname()
@when("the user enters a very long last name on register page")
def step_very_long_lastname_on_register_page(context):
    _flows(context).enter_very_long_lastname()
@when("the user enters a very long email on register page")
def step_very_long_email_on_register_page(context):
    _flows(context).enter_very_long_email()
@when("the user enters a very long password on register page")
def step_very_long_password_on_register_page(context):
    _flows(context).enter_very_long_password()
@then("the register page should remain stable")
def step_register_page_should_remain_stable(context):
    stable = _flows(context).register_page_should_remain_stable()
    DomainAssert.that(stable, "register_page_stable").is_true()
@then('the register page breadcrumb should display "{text}"')
def step_register_breadcrumb_should_display(context, text):
    displayed = _flows(context).register_page_breadcrumb_should_display(text)
    DomainAssert.that(displayed, f"register_breadcrumb_should_display_{text}").is_true()
@when("the user clicks the side menu login link on register page")
def step_click_side_menu_login_link_on_register_page(context):
    _flows(context).navigate_to_login_from_side_menu()
@when("the user clicks the side menu register link on register page")
def step_click_side_menu_register_link_on_register_page(context):
    _flows(context).navigate_to_register_from_side_menu()
@when("the user clicks the side menu forgotten password link on register page")
def step_click_side_menu_forgotten_password_link_on_register_page(context):
    _flows(context).navigate_to_forgotten_password_from_side_menu()
@then("the OpenCart forgotten password page should be loaded from register flow")
def step_forgotten_password_page_loaded_from_register_flow(context):
    loaded = _flows(context).forgotten_password_page_should_be_loaded()
    DomainAssert.that(loaded, "forgotten_password_page_loaded_from_register_flow").is_true()
@when("the user clicks the privacy policy link on register page")
def step_click_privacy_policy_link_on_register_page(context):
    _flows(context).open_privacy_policy_from_register_page()
@then("the privacy policy should be opened from register page")
def step_privacy_policy_opened_from_register_page(context):
    opened = _flows(context).privacy_policy_should_be_opened()
    DomainAssert.that(opened, "privacy_policy_opened_from_register_page").is_true()
@when('the user executes the registration dataset "{dataset_name}"')
def step_execute_registration_dataset(context, dataset_name):
    _flows(context).execute_registration_dataset(dataset_name)
@then("all registration dataset rows should pass")
def step_all_registration_dataset_rows_should_pass(context):
    passed = _flows(context).all_registration_dataset_rows_should_pass()
    DomainAssert.that(
        passed,
        "all_registration_dataset_rows_passed"
    ).is_true()