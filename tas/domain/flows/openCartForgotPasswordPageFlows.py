from tas.domain.ports.openCartForgotPasswordPagePort import (
    OpenCartForgotPasswordPagePort,
    OpenCartForgotPasswordPageState,
)


class OpenCartForgotPasswordPageFlows:

    def __init__(self, port: OpenCartForgotPasswordPagePort):
        self._port = port
    def open_forgotten_password_page(self) -> None:
        self._port.open_forgotten_password_page()
    def forgotten_password_page_should_be_displayed(self) -> OpenCartForgotPasswordPageState:
        return self._port.read_forgotten_password_page_state()
    def enter_registered_email(self) -> None:
        self._port.enter_registered_email()
    def enter_unregistered_email(self) -> None:
        self._port.enter_unregistered_email()
    def enter_invalid_email(self) -> None:
        self._port.enter_invalid_email()
    def submit_forgotten_password_form(self) -> None:
        self._port.submit_forgotten_password_form()
    def submit_forgotten_password_form_without_email(self) -> None:
        self._port.submit_forgotten_password_form_without_email()
    def forgotten_password_request_should_be_accepted(self) -> bool:
        return self._port.is_forgotten_password_request_accepted()
    def email_validation_error_should_be_displayed(self) -> bool:
        return self._port.is_email_validation_error_displayed()
    def navigate_back_to_login_page(self) -> None:
        self._port.click_back_button()
    def login_page_should_be_loaded(self) -> bool:
        return self._port.is_login_page_loaded()
    def forgotten_password_page_breadcrumb_should_display(self, text: str) -> bool:
        return self._port.breadcrumb_contains(text)
    def navigate_to_login_from_side_menu(self) -> None:
        self._port.click_side_menu_login_link()
    def navigate_to_register_from_side_menu(self) -> None:
        self._port.click_side_menu_register_link()
    def navigate_to_forgotten_password_from_side_menu(self) -> None:
        self._port.click_side_menu_forgotten_password_link()
    def register_account_page_should_be_loaded(self) -> bool:
        return self._port.is_register_account_page_loaded()
    def set_desktop_viewport(self) -> None:
        self._port.set_desktop_viewport()
    def set_tablet_viewport(self) -> None:
        self._port.set_tablet_viewport()
    def set_mobile_viewport(self) -> None:
        self._port.set_mobile_viewport()
    def forgotten_password_form_should_remain_usable(self) -> bool:
        return self._port.is_forgotten_password_form_usable()
    def forgotten_password_primary_elements_should_be_visible(self) -> bool:
        return self._port.are_forgotten_password_primary_elements_visible()
    def forgotten_password_page_should_use_https(self) -> bool:
        return self._port.forgotten_password_page_uses_https()
    def enter_malicious_email_input(self) -> None:
        self._port.enter_malicious_email_input()
    def enter_very_long_email(self) -> None:
        self._port.enter_very_long_email()
    def forgotten_password_page_should_remain_stable(self) -> bool:
        return self._port.is_forgotten_password_page_stable()
    def no_javascript_alert_should_be_displayed(self) -> bool:
        return not self._port.is_javascript_alert_displayed()
    def submit_form_multiple_times_with_unregistered_email(self) -> None:
        self._port.submit_form_multiple_times_with_unregistered_email()
    def refresh_forgotten_password_page(self) -> None:
        self._port.refresh_forgotten_password_page()
    def email_field_should_be_empty(self) -> bool:
        return self._port.is_email_field_empty()
    def navigate_back_in_browser_to_forgotten_password_page(self) -> None:
        self._port.navigate_back_in_browser_to_forgotten_password_page()
    def open_forgotten_password_page_again(self) -> None:
        self._port.open_forgotten_password_page_again()



