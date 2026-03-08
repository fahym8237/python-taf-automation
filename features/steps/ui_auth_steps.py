# features/steps/ui_auth_steps.py  Full version 

from pathlib import Path
from behave import given, when, then
import os
from tas.core import DomainAssert
from tas.structure.ui.pages.base_page import PageContext
from tas.structure.ui.pages.login_page import LoginPage
from tas.structure.ui.pages.forgot_password_page import ForgotPasswordPage
from tas.structure.ui.pages.register_page import RegisterPage

from tas.structure.adapters.auth_ui_adapter import AuthUiAdapter
from tas.structure.adapters.registration_ui_adapter import RegistrationUiAdapter

from tas.domain.flows.auth_flows import AuthFlows
from tas.domain.flows.registration_flows import RegistrationFlows
from tas.domain.models.user import RegistrationDraft


# ----------------------------
# Helpers
# ----------------------------
def _ui(context):
    ui = context.scenario_ctx.get_service("ui")
    if not ui:
        raise RuntimeError("UI session not started. Ensure scenario has @ui tag.")
    return ui


def _cfg(context):
    # Layer 7: config snapshot is stored by LifecycleManager.before_all
    cfg = context.run_ctx.services.get("config")
    if not cfg:
        raise RuntimeError("Config not loaded. Check LifecycleManager.before_all stores run_ctx.services['config'].")
    return cfg


def _login_url(context) -> str:
    return _cfg(context).ui_pilot.login_url


def _forgot_url(context) -> str:
    return _cfg(context).ui_pilot.forgot_url


def _register_url(context) -> str:
    return _cfg(context).ui_pilot.register_url


def _page_ctx(context) -> PageContext:
    ui = _ui(context)
    return PageContext(page=ui.page, base_url="")


def _auth_adapter(context) -> AuthUiAdapter:
    adapter = context.scenario_ctx.get_service("auth_adapter")
    if adapter:
        return adapter

    ctx = _page_ctx(context)
    login = LoginPage(ctx)
    forgot = ForgotPasswordPage(ctx)
    adapter = AuthUiAdapter(
        login_page=login,
        forgot_page=forgot,
        login_file_url=_login_url(context),
        forgot_file_url=_forgot_url(context),
    )
    context.scenario_ctx.set_service("auth_adapter", adapter)
    return adapter


def _reg_adapter(context) -> RegistrationUiAdapter:
    adapter = context.scenario_ctx.get_service("reg_adapter")
    if adapter:
        return adapter

    ctx = _page_ctx(context)
    reg_page = RegisterPage(ctx)
    adapter = RegistrationUiAdapter(reg_page, _register_url(context))
    context.scenario_ctx.set_service("reg_adapter", adapter)
    return adapter


# ----------------------------
# LOGIN
# ----------------------------
@given("I open the login page")
def step_open_login(context):
    adapter = _auth_adapter(context)
    AuthFlows(adapter).open_login()


@then("the login form should be visible")
def step_login_form(context):
    adapter = _auth_adapter(context)
    state = AuthFlows(adapter).login_page_should_render()
    DomainAssert.that(state.login_form_visible, "login_form_visible").is_true()


@then("the returning customer header should be visible")
def step_returning_customer_header(context):
    adapter = _auth_adapter(context)
    state = AuthFlows(adapter).login_page_should_render()
    DomainAssert.that(state.returning_customer_header_visible, "returning_customer_header_visible").is_true()


@then("the email input should be visible")
def step_email_input_visible(context):
    """
    This step phrase is used across login/forgot/register features.
    We resolve it safely based on which adapter is present in the scenario.
    """
    # Register context
    reg_adapter = context.scenario_ctx.get_service("reg_adapter")
    if reg_adapter:
        st = reg_adapter.read_register_page_state()
        DomainAssert.that(st.email_input_visible, "register_email_input_visible").is_true()
        return

    # Auth context (login or forgot)
    auth_adapter = context.scenario_ctx.get_service("auth_adapter")
    if auth_adapter:
        # If forgot page is opened, use forgot state
        try:
            st_f = auth_adapter.read_forgot_password_page_state()
            # Content container visible is a safe indicator of the forgot page
            if st_f.content_container_visible:
                DomainAssert.that(st_f.email_input_visible, "forgot_email_input_visible").is_true()
                return
        except Exception:
            pass

        # Default to login state
        st_l = AuthFlows(auth_adapter).login_page_should_render()
        DomainAssert.that(st_l.email_input_visible, "login_email_input_visible").is_true()
        return

    raise RuntimeError("No UI adapter found in scenario context (auth_adapter/reg_adapter).")


@then("the password input should be visible")
def step_password_input(context):
    adapter = _auth_adapter(context)
    state = AuthFlows(adapter).login_page_should_render()
    DomainAssert.that(state.password_input_visible, "password_input_visible").is_true()


@then("the login button should be visible")
def step_login_button(context):
    adapter = _auth_adapter(context)
    state = AuthFlows(adapter).login_page_should_render()
    DomainAssert.that(state.login_button_visible, "login_button_visible").is_true()


@then("the forgotten password link should be visible")
def step_forgotten_password_link(context):
    adapter = _auth_adapter(context)
    state = AuthFlows(adapter).login_page_should_render()
    DomainAssert.that(state.forgotten_password_link_visible, "forgotten_password_link_visible").is_true()


@when("I click the forgotten password link")
def step_click_forgot(context):
    adapter = _auth_adapter(context)
    AuthFlows(adapter).navigate_to_forgot_password_from_login()


@then("the forgot password page header should be visible")
def step_forgot_password_page_header(context):
    adapter = _auth_adapter(context)
    st = adapter.read_forgot_password_page_state()
    DomainAssert.that(st.header_visible, "forgot_password_page_header_visible").is_true()




# ----------------------------
# FORGOT PASSWORD PAGE
# ----------------------------
@given("I open the forgot password page")
def step_open_forgot(context):
    adapter = _auth_adapter(context)
    adapter.open_forgot_password_page()


@then("the forgot password content container should be visible")
def step_forgot_container(context):
    adapter = _auth_adapter(context)
    st = adapter.read_forgot_password_page_state()
    DomainAssert.that(st.content_container_visible, "content_container_visible").is_true()


@then("the forgot password header should be visible")
def step_forgot_header_visible(context):
    adapter = _auth_adapter(context)
    st = adapter.read_forgot_password_page_state()
    DomainAssert.that(st.header_visible, "forgot_password_header_visible").is_true()


@then("the instruction paragraph should be visible")
def step_instruction_visible(context):
    adapter = _auth_adapter(context)
    st = adapter.read_forgot_password_page_state()
    DomainAssert.that(st.instruction_visible, "instruction_visible").is_true()


@then("the forgotten form should be visible")
def step_forgot_form_visible(context):
    adapter = _auth_adapter(context)
    st = adapter.read_forgot_password_page_state()
    DomainAssert.that(st.form_visible, "form_visible").is_true()


@then("the email legend should be visible")
def step_email_legend_visible(context):
    adapter = _auth_adapter(context)
    st = adapter.read_forgot_password_page_state()
    DomainAssert.that(st.email_legend_visible, "email_legend_visible").is_true()


@then("the continue button should be visible")
def step_continue_button_visible(context):
    adapter = _auth_adapter(context)
    st = adapter.read_forgot_password_page_state()
    DomainAssert.that(st.continue_button_visible, "continue_button_visible").is_true()


@then("the back button should be visible")
def step_back_button_visible(context):
    adapter = _auth_adapter(context)
    st = adapter.read_forgot_password_page_state()
    DomainAssert.that(st.back_button_visible, "back_button_visible").is_true()



# ----------------------------
# REGISTER PAGE
# ----------------------------
@given("I open the register page")
def step_open_register(context):
    adapter = _reg_adapter(context)
    RegistrationFlows(adapter).open_register()


@then("the register content container should be visible")
def step_register_container(context):
    adapter = _reg_adapter(context)
    st = adapter.read_register_page_state()
    DomainAssert.that(st.content_container_visible, "register_content_container_visible").is_true()


@then("the register header should be visible")
def step_register_header(context):
    adapter = _reg_adapter(context)
    st = adapter.read_register_page_state()
    DomainAssert.that(st.header_visible, "register_header_visible").is_true()


@then("the register form should be visible")
def step_register_form(context):
    adapter = _reg_adapter(context)
    st = adapter.read_register_page_state()
    DomainAssert.that(st.form_visible, "register_form_visible").is_true()


@then("the personal details legend should be visible")
def step_personal_details_legend(context):
    adapter = _reg_adapter(context)
    st = adapter.read_register_page_state()
    DomainAssert.that(st.personal_details_legend_visible, "personal_details_legend_visible").is_true()


@then("the first name input should be visible")
def step_first_name_input(context):
    adapter = _reg_adapter(context)
    st = adapter.read_register_page_state()
    DomainAssert.that(st.firstname_input_visible, "firstname_input_visible").is_true()


@then("the last name input should be visible")
def step_last_name_input(context):
    adapter = _reg_adapter(context)
    st = adapter.read_register_page_state()
    DomainAssert.that(st.lastname_input_visible, "lastname_input_visible").is_true()


@then("the password legend should be visible")
def step_password_legend(context):
    adapter = _reg_adapter(context)
    st = adapter.read_register_page_state()
    DomainAssert.that(st.password_legend_visible, "password_legend_visible").is_true()



@then("the newsletter legend should be visible")
def step_newsletter_legend(context):
    adapter = _reg_adapter(context)
    st = adapter.read_register_page_state()
    DomainAssert.that(st.newsletter_legend_visible, "newsletter_legend_visible").is_true()


@then("the newsletter checkbox should be visible")
def step_newsletter_checkbox(context):
    adapter = _reg_adapter(context)
    st = adapter.read_register_page_state()
    DomainAssert.that(st.newsletter_checkbox_visible, "newsletter_checkbox_visible").is_true()


@then("the privacy policy checkbox should be visible")
def step_privacy_checkbox(context):
    adapter = _reg_adapter(context)
    st = adapter.read_register_page_state()
    DomainAssert.that(st.privacy_checkbox_visible, "privacy_checkbox_visible").is_true()


@then("the privacy policy link should be visible")
def step_privacy_link(context):
    adapter = _reg_adapter(context)
    st = adapter.read_register_page_state()
    DomainAssert.that(st.privacy_link_visible, "privacy_link_visible").is_true()


@then("the register continue button should be visible")
def step_register_continue_button(context):
    adapter = _reg_adapter(context)
    st = adapter.read_register_page_state()
    DomainAssert.that(st.continue_button_visible, "register_continue_button_visible").is_true()


@then("the login page link should be visible")
def step_register_login_page_link(context):
    adapter = _reg_adapter(context)
    st = adapter.read_register_page_state()
    DomainAssert.that(st.login_page_link_visible, "register_login_page_link_visible").is_true()


# ----------------------------
# DATASET SCENARIO (temporary; Layer 8 will replace this loader)
# ----------------------------
