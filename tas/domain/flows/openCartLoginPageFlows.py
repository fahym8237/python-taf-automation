from email.mime import text

from tas.domain.ports.openCartLoginPagePort import (
    OpenCartLoginPagePort,
    OpenCartLoginPageState,
    LoginResultState,
)


class OpenCartLoginPageFlows:

    def __init__(self, port: OpenCartLoginPagePort):
        self._port = port
    def open_login_page(self) -> None:
        self._port.open_login_page()
    def login_page_should_be_displayed(self) -> OpenCartLoginPageState:
        return self._port.read_login_page_state()
    def navigate_to_forgotten_password_page(self) -> None:
        self._port.navigate_to_forgotten_password_page()
    def navigate_to_register_account_page(self) -> None:
        self._port.navigate_to_register_account_page()
    def forgotten_password_page_should_be_loaded(self) -> bool:
        return self._port.is_forgotten_password_page_loaded()
    def register_account_page_should_be_loaded(self) -> bool:
        return self._port.is_register_account_page_loaded()
    def enter_login_email(self, email: str) -> None:
        self._port.enter_email(email)
    def enter_login_password(self, password: str) -> None:
        self._port.enter_password(password)
    def submit_login_form(self) -> None:
        self._port.submit_login()
    def login_result_should_be_available(self) -> LoginResultState:
        return self._port.read_login_result_state()
    def password_field_should_mask_value(self) -> bool:
        return self._port.is_password_masked()   
    def login_page_breadcrumb_should_display(self, text: str) -> bool:
        return self._port.breadcrumb_contains(text)
    def navigate_to_register_from_side_menu(self) -> None:
        self._port.click_side_menu_register_link()
    def navigate_to_forgotten_password_from_side_menu(self) -> None:
        self._port.click_side_menu_forgotten_password_link()
    def navigate_to_login_from_side_menu(self) -> None:
        self._port.click_side_menu_login_link()   
    def open_my_account_page_directly(self) -> None:
        self._port.open_my_account_page_directly()
    def open_edit_account_page_directly(self) -> None:
        self._port.open_edit_account_page_directly()
    def open_change_password_page_directly(self) -> None:
        self._port.open_change_password_page_directly()
    def user_should_be_redirected_to_login_page(self) -> bool:
        return self._port.is_redirected_to_login_page()
    def my_account_page_should_be_loaded(self) -> bool:
        return self._port.is_my_account_page_loaded()
    def logout_from_account_area(self) -> None:
        self._port.logout_from_account_area()
    def user_should_be_logged_out_successfully(self) -> bool:
        return self._port.is_logged_out_successfully()
    def open_login_page_again(self) -> None:
        self._port.open_login_page_again()
    def authenticated_login_access_should_be_handled(self) -> bool:
        return self._port.is_authenticated_login_access_handled()
    def set_desktop_viewport(self) -> None:
        self._port.set_desktop_viewport()
    def set_tablet_viewport(self) -> None:
        self._port.set_tablet_viewport()
    def set_mobile_viewport(self) -> None:
        self._port.set_mobile_viewport()
    def login_form_should_remain_usable(self) -> bool:
        return self._port.is_login_form_usable()
    def login_page_primary_elements_should_be_visible(self) -> bool:
        return self._port.are_primary_elements_visible()
    def login_page_should_use_https(self) -> bool:
        return self._port.login_page_uses_https()
    def enter_malicious_login_email_input(self) -> None:
        self._port.enter_malicious_email_input()
    def enter_malicious_login_password_input(self) -> None:
        self._port.enter_malicious_password_input()
    def login_browser_native_message_should_be_displayed(self) -> bool:
        return self._port.is_browser_native_validation_displayed()
    def no_javascript_alert_should_be_displayed(self) -> bool:
        return not self._port.is_javascript_alert_displayed()
    def submit_invalid_login_credentials_multiple_times(self) -> None:
        self._port.submit_invalid_credentials_multiple_times()
    def login_page_should_remain_stable(self) -> bool:
        return self._port.is_login_page_stable()










        