@ui @change_password_page @security @opencart
Feature: OpenCart Account - Change Password Security
  As a user
  I want password change security controls to behave correctly
  So that my account remains protected

  Background:
    Given the user is logged in
    And the user navigates to the change password page

  @PY-CPS-001 @security @trace=REQ-CPS-001
  Scenario: Password field masks entered value
    When the user enters a valid new password on change password page
    Then the password field should mask the entered value on change password page

  @PY-CPS-002 @security @trace=REQ-CPS-002
  Scenario: Confirm password field masks entered value
    When the user enters the same confirm password on change password page
    Then the confirm password field should mask the entered value on change password page

  @PY-CPS-003 @security @trace=REQ-CPS-003
  Scenario: Change password page is served over HTTPS
    Then the change password page URL should use HTTPS

  @PY-CPS-004 @security @negative @trace=REQ-CPS-004
  Scenario: Password change form safely handles malicious input
    When the user enters malicious password input on change password page
    And the user enters malicious confirm input on change password page
    And the user submits the change password form
    Then the change password page should remain stable
    And no PYaScript alert should be displayed on change password page

  @PY-CPS-005 @security @access_control @trace=REQ-CPS-005
  Scenario: Unauthenticated user cannot access change password page directly
    Given the user is not authenticated
    When the user tries to open the OpenCart change password page directly
    Then the user should be redirected to the login page from change password flow