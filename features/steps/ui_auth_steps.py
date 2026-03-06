import os
from behave import given, when, then

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


def _file_url(env_name: str) -> str:
    url = os.getenv(env_name)
    if not url:
        raise RuntimeError(
            f"Missing env var {env_name}. "
            f"Set it to your file URL, e.g. file:///C:/Users/.../login.html"
        )
    return url


def _ui(context):
    ui = context.scenario_ctx.get_service("ui")
    if not ui:
        raise RuntimeError("UI session not started. Ensure scenario has @ui tag.")
    return ui


@given("I open the login page")
def step_open_login(context):
    ui = _ui(context)
    ctx = PageContext(page=ui.page, base_url="")
    login = LoginPage(ctx)
    forgot = ForgotPasswordPage(ctx)

    adapter = AuthUiAdapter(
        login_page=login,
        forgot_page=forgot,
        login_file_url=_file_url("LOGIN_URL"),
        forgot_file_url=_file_url("FORGOT_URL"),
    )
    context.scenario_ctx.set_service("auth_adapter", adapter)
    AuthFlows(adapter).open_login()


@then("the login form should be visible")
def step_login_form(context):
    adapter = context.scenario_ctx.get_service("auth_adapter")
    state = AuthFlows(adapter).login_page_should_render()
    DomainAssert.that(state.login_form_visible, "login_form_visible").is_true()


@then("the returning customer header should be visible")
def step_header(context):
    adapter = context.scenario_ctx.get_service("auth_adapter")
    state = AuthFlows(adapter).login_page_should_render()
    DomainAssert.that(state.returning_customer_header_visible, "returning_customer_header_visible").is_true()


@then("the email input should be visible")
def step_email(context):
    adapter = context.scenario_ctx.get_service("auth_adapter")
    state = AuthFlows(adapter).login_page_should_render()
    DomainAssert.that(state.email_input_visible, "email_input_visible").is_true()


@then("the password input should be visible")
def step_pass(context):
    adapter = context.scenario_ctx.get_service("auth_adapter")
    state = AuthFlows(adapter).login_page_should_render()
    DomainAssert.that(state.password_input_visible, "password_input_visible").is_true()


@then("the login button should be visible")
def step_btn(context):
    adapter = context.scenario_ctx.get_service("auth_adapter")
    state = AuthFlows(adapter).login_page_should_render()
    DomainAssert.that(state.login_button_visible, "login_button_visible").is_true()


@then("the forgotten password link should be visible")
def step_link(context):
    adapter = context.scenario_ctx.get_service("auth_adapter")
    state = AuthFlows(adapter).login_page_should_render()
    DomainAssert.that(state.forgotten_password_link_visible, "forgotten_password_link_visible").is_true()


@when("I click the forgotten password link")
def step_click_forgot(context):
    adapter = context.scenario_ctx.get_service("auth_adapter")
    AuthFlows(adapter).navigate_to_forgot_password_from_login()


@then("the forgot password page header should be visible")
def step_forgot_header(context):
    ui = _ui(context)
    ctx = PageContext(page=ui.page, base_url="")
    login = LoginPage(ctx)
    forgot = ForgotPasswordPage(ctx)
    adapter = AuthUiAdapter(login, forgot, _file_url("LOGIN_URL"), _file_url("FORGOT_URL"))
    st = adapter.read_forgot_password_page_state()
    DomainAssert.that(st.header_visible, "forgot_header_visible").is_true()


@given("I open the forgot password page")
def step_open_forgot(context):
    ui = _ui(context)
    ctx = PageContext(page=ui.page, base_url="")
    login = LoginPage(ctx)
    forgot = ForgotPasswordPage(ctx)
    adapter = AuthUiAdapter(login, forgot, _file_url("LOGIN_URL"), _file_url("FORGOT_URL"))
    context.scenario_ctx.set_service("auth_adapter", adapter)
    adapter.open_forgot_password_page()


@then("the forgot password content container should be visible")
def step_forgot_container(context):
    adapter = context.scenario_ctx.get_service("auth_adapter")
    st = adapter.read_forgot_password_page_state()
    DomainAssert.that(st.content_container_visible, "content_container_visible").is_true()


@then("the forgot password header should be visible")
def step_forgot_h1(context):
    adapter = context.scenario_ctx.get_service("auth_adapter")
    st = adapter.read_forgot_password_page_state()
    DomainAssert.that(st.header_visible, "header_visible").is_true()


@then("the instruction paragraph should be visible")
def step_instr(context):
    adapter = context.scenario_ctx.get_service("auth_adapter")
    st = adapter.read_forgot_password_page_state()
    DomainAssert.that(st.instruction_visible, "instruction_visible").is_true()


@then("the forgotten form should be visible")
def step_form(context):
    adapter = context.scenario_ctx.get_service("auth_adapter")
    st = adapter.read_forgot_password_page_state()
    DomainAssert.that(st.form_visible, "form_visible").is_true()


@then("the email legend should be visible")
def step_legend(context):
    adapter = context.scenario_ctx.get_service("auth_adapter")
    st = adapter.read_forgot_password_page_state()
    DomainAssert.that(st.email_legend_visible, "email_legend_visible").is_true()


@then("the continue button should be visible")
def step_continue_btn(context):
    adapter = context.scenario_ctx.get_service("auth_adapter")
    st = adapter.read_forgot_password_page_state()
    DomainAssert.that(st.continue_button_visible, "continue_button_visible").is_true()


@then("the back button should be visible")
def step_back_btn(context):
    adapter = context.scenario_ctx.get_service("auth_adapter")
    st = adapter.read_forgot_password_page_state()
    DomainAssert.that(st.back_button_visible, "back_button_visible").is_true()


@given("I open the register page")
def step_open_register(context):
    ui = _ui(context)
    ctx = PageContext(page=ui.page, base_url="")
    reg_page = RegisterPage(ctx)
    adapter = RegistrationUiAdapter(reg_page, _file_url("REGISTER_URL"))
    context.scenario_ctx.set_service("reg_adapter", adapter)
    RegistrationFlows(adapter).open_register()


@then("the register header should be visible")
def step_reg_header(context):
    adapter = context.scenario_ctx.get_service("reg_adapter")
    st = adapter.read_register_page_state()
    DomainAssert.that(st.header_visible, "register_header_visible").is_true()


@when('I submit registration from dataset "{csv_name}"')
def step_submit_dataset(context, csv_name):
    # Minimal CSV read (Layer 8 loader will replace later)
    import csv
    adapter = context.scenario_ctx.get_service("reg_adapter")
    path = os.path.join("features", "data", csv_name)
    with open(path, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    results = []
    for row in rows:
        draft = RegistrationDraft(
            firstname=row["firstname"],
            lastname=row["lastname"],
            email=row["email"],
            password=row["password"],
            newsletter=False,
            agree_privacy=True,
        )
        adapter.open_register_page()
        adapter.submit_registration(draft)
        res = adapter.read_registration_errors()
        results.append((row, res))
    context.scenario_ctx.state["reg_dataset_results"] = results


@then("I should see the expected validation errors")
def step_validate_errors(context):
    results = context.scenario_ctx.state["reg_dataset_results"]
    for row, res in results:
        exp_first = row["expect_firstname_error"].lower() == "true"
        exp_last = row["expect_lastname_error"].lower() == "true"
        exp_email = row["expect_email_error"].lower() == "true"
        exp_pass = row["expect_password_error"].lower() == "true"

        DomainAssert.that((res.firstname_error is not None), "firstname_error_present").is_equal_to(exp_first)
        DomainAssert.that((res.lastname_error is not None), "lastname_error_present").is_equal_to(exp_last)
        DomainAssert.that((res.email_error is not None), "email_error_present").is_equal_to(exp_email)
        DomainAssert.that((res.password_error is not None), "password_error_present").is_equal_to(exp_pass)
