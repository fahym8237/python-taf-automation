from tas.domain.ports.openCartRegisterPagePort import (
    OpenCartRegisterPagePort,
    OpenCartRegisterPageState,
)


class OpenCartRegisterPageFlows:

    def __init__(self, port: OpenCartRegisterPagePort):
        self._port = port

    def open_register_page(self) -> None:
        self._port.open_register_page()

    def register_page_should_be_displayed(self) -> OpenCartRegisterPageState:
        return self._port.read_register_page_state()

    def fill_registration_form_with_generated_user(self) -> None:
        self._port.fill_registration_form_with_generated_user()

    def enter_invalid_email(self) -> None:
        self._port.enter_invalid_email()

    def agree_to_privacy_policy(self) -> None:
        self._port.agree_to_privacy_policy()

    def submit_registration_form(self) -> None:
        self._port.submit_registration_form()

    def submit_registration_form_without_fields(self) -> None:
        self._port.submit_registration_form_without_fields()

    def success_message_should_be_visible(self, message: str) -> bool:
        return self._port.is_success_message_visible(message)

    def all_mandatory_errors_should_be_displayed(self) -> bool:
        return self._port.are_all_mandatory_errors_displayed()

    def privacy_policy_warning_should_be_displayed(self) -> bool:
        return self._port.is_privacy_policy_warning_displayed()

    def email_validation_error_should_be_displayed(self) -> bool:
        return self._port.is_email_validation_error_displayed()

    def password_field_should_mask_value(self) -> bool:
        return self._port.is_password_field_masked()
    
    def refresh_register_page(self) -> None:
        self._port.refresh_register_page()


    def register_form_should_remain_usable(self) -> bool:
        return self._port.is_register_form_usable()


    def firstname_field_should_be_empty(self) -> bool:
        return self._port.is_firstname_field_empty()


    def lastname_field_should_be_empty(self) -> bool:
        return self._port.is_lastname_field_empty()


    def email_field_should_be_empty(self) -> bool:
        return self._port.is_email_field_empty()


    def password_field_should_be_empty(self) -> bool:
        return self._port.is_password_field_empty()


    def navigate_to_login_from_register_page(self) -> None:
        self._port.click_login_link()


    def login_page_should_be_loaded(self) -> bool:
        return self._port.is_login_page_loaded()


    def navigate_back_in_browser_to_register_page(self) -> None:
        self._port.navigate_back_in_browser_to_register_page()


    def open_register_page_again(self) -> None:
        self._port.open_register_page_again()
    
    def set_desktop_viewport(self) -> None:
        self._port.set_desktop_viewport()


    def set_tablet_viewport(self) -> None:
        self._port.set_tablet_viewport()


    def set_mobile_viewport(self) -> None:
        self._port.set_mobile_viewport()


    def register_primary_elements_should_be_visible(self) -> bool:
        return self._port.are_register_primary_elements_visible()


    def register_page_should_use_https(self) -> bool:
        return self._port.register_page_uses_https()


    def enter_malicious_firstname_input(self) -> None:
        self._port.enter_malicious_firstname_input()


    def enter_malicious_lastname_input(self) -> None:
        self._port.enter_malicious_lastname_input()


    def enter_malicious_email_input(self) -> None:
        self._port.enter_malicious_email_input()


    def enter_malicious_password_input(self) -> None:
        self._port.enter_malicious_password_input()


    def enter_very_long_firstname(self) -> None:
        self._port.enter_very_long_firstname()


    def enter_very_long_lastname(self) -> None:
        self._port.enter_very_long_lastname()


    def enter_very_long_email(self) -> None:
        self._port.enter_very_long_email()
    def enter_very_long_password(self) -> None:
        self._port.enter_very_long_password()
    def register_page_should_remain_stable(self) -> bool:
        return self._port.is_register_page_stable()
    def register_page_breadcrumb_should_display(self, text: str) -> bool:
        return self._port.breadcrumb_contains(text)
    def navigate_to_login_from_side_menu(self) -> None:
        self._port.click_side_menu_login_link()
    def navigate_to_register_from_side_menu(self) -> None:
        self._port.click_side_menu_register_link()
    def navigate_to_forgotten_password_from_side_menu(self) -> None:
        self._port.click_side_menu_forgotten_password_link()
    def forgotten_password_page_should_be_loaded(self) -> bool:
        return self._port.is_forgotten_password_page_loaded()
    def open_privacy_policy_from_register_page(self) -> None:
        self._port.click_privacy_policy_link()
    def privacy_policy_should_be_opened(self) -> bool:
        return self._port.is_privacy_policy_opened()
    def execute_registration_dataset(self, dataset_name: str) -> None:
        self._port.execute_registration_dataset(dataset_name)
    def all_registration_dataset_rows_should_pass(self) -> bool:
        return self._port.all_registration_dataset_rows_passed()