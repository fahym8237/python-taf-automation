from tas.domain.ports.openCartChangePasswordPagePort import (
    OpenCartChangePasswordPagePort,
    OpenCartChangePasswordPageState,
)


class OpenCartChangePasswordPageFlows:

    def __init__(self, port: OpenCartChangePasswordPagePort):
        self._port = port
    def open_change_password_page(self) -> None:
        self._port.open_change_password_page()
    def change_password_page_should_be_displayed(self) -> OpenCartChangePasswordPageState:
        return self._port.read_change_password_page_state()
    def enter_valid_new_password(self) -> None:
        self._port.enter_valid_new_password()
    def enter_same_confirm_password(self) -> None:
        self._port.enter_same_confirm_password()
    def enter_different_confirm_password(self) -> None:
        self._port.enter_different_confirm_password()
    def submit_change_password_form(self) -> None:
        self._port.submit_change_password_form()
    def submit_change_password_form_without_passwords(self) -> None:
        self._port.submit_change_password_form_without_passwords()
    def password_should_be_changed_successfully(self) -> bool:
        return self._port.is_password_changed_successfully()
    def password_validation_error_should_be_displayed(self) -> bool:
        return self._port.is_password_validation_error_displayed()
    def confirm_password_validation_error_should_be_displayed(self) -> bool:
        return self._port.is_confirm_password_validation_error_displayed()
    def password_mismatch_validation_error_should_be_displayed(self) -> bool:
        return self._port.is_password_mismatch_validation_error_displayed()
    def password_field_should_mask_value(self) -> bool:
        return self._port.is_password_field_masked()
    def confirm_password_field_should_mask_value(self) -> bool:
        return self._port.is_confirm_password_field_masked()
    def navigate_back_to_my_account_page(self) -> None:
        self._port.click_back_button()
    def my_account_page_should_be_loaded(self) -> bool:
        return self._port.is_my_account_page_loaded()
    def latest_new_password(self) -> str | None:
        return self._port.latest_new_password()
    def change_password_page_breadcrumb_should_display(self, text: str) -> bool:
        return self._port.breadcrumb_contains(text)
    def navigate_to_my_account_from_side_menu(self) -> None:
        self._port.click_side_menu_my_account_link()
    def navigate_to_edit_account_from_side_menu(self) -> None:
        self._port.click_side_menu_edit_account_link()
    def navigate_to_password_from_side_menu(self) -> None:
        self._port.click_side_menu_password_link()
    def logout_from_side_menu(self) -> None:
        self._port.click_side_menu_logout_link()
    def edit_account_page_should_be_loaded(self) -> bool:
        return self._port.is_edit_account_page_loaded()
    def user_should_be_logged_out_successfully(self) -> bool:
        return self._port.is_logged_out_successfully()
    def set_desktop_viewport(self) -> None:
        self._port.set_desktop_viewport()
    def set_tablet_viewport(self) -> None:
        self._port.set_tablet_viewport()
    def set_mobile_viewport(self) -> None:
        self._port.set_mobile_viewport()
    def change_password_form_should_remain_usable(self) -> bool:
        return self._port.is_change_password_form_usable()
    def change_password_primary_elements_should_be_visible(self) -> bool:
        return self._port.are_change_password_primary_elements_visible()
    def change_password_page_should_use_https(self) -> bool:
        return self._port.change_password_page_uses_https()
    def enter_malicious_password_input(self) -> None:
        self._port.enter_malicious_password_input()
    def enter_malicious_confirm_input(self) -> None:
        self._port.enter_malicious_confirm_input()
    def change_password_page_should_remain_stable(self) -> bool:
        return self._port.is_change_password_page_stable()
    def no_javascript_alert_should_be_displayed(self) -> bool:
        return not self._port.is_javascript_alert_displayed()
    def user_should_not_be_authenticated(self) -> None:
        self._port.clear_authenticated_session()
    def open_change_password_page_directly(self) -> None:
        self._port.open_change_password_page_directly()
    def user_should_be_redirected_to_login_page(self) -> bool:
        return self._port.is_redirected_to_login_page() 
    def logout_after_password_change(self) -> None:
        self._port.logout_after_password_change()
    def login_with_newly_changed_password(self) -> None:
        self._port.login_with_newly_changed_password()
    def login_with_old_password_after_password_change(self) -> None:
        self._port.login_with_old_password_after_password_change()
    def user_should_be_logged_in_after_password_change(self) -> bool:
        return self._port.is_logged_in_after_password_change()
    def login_warning_should_be_displayed_after_password_change(self) -> bool:
        return self._port.is_login_warning_displayed_after_password_change()
    def refresh_change_password_page(self) -> None:
        self._port.refresh_change_password_page()
    def password_field_should_be_empty(self) -> bool:
        return self._port.is_password_field_empty()
    def confirm_password_field_should_be_empty(self) -> bool:
        return self._port.is_confirm_password_field_empty()