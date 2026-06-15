@ui @change_password_page @opencart
Feature: OpenCart Account - Change Password
  As an authenticated user
  I want to change my account password
  So that I can secure my account

  Background:
  Given the user is logged in
  And the user navigates to the change password page
    

  @PY-CP-001 @smoke @trace=REQ-CP-001
  Scenario: Change password page is displayed correctly
    Then the OpenCart change password page should be loaded
    And the password field should be displayed on change password page
    And the password confirm field should be displayed on change password page
    And the continue button should be displayed on change password page
    And the back button should be displayed on change password page

  @PY-CP-002 @smoke @trace=REQ-CP-002
  Scenario: User changes password with valid matching values
    When the user enters a valid new password on change password page
    And the user enters the same confirm password on change password page
    And the user submits the change password form
    Then the password should be changed successfully

  @PY-CP-003 @negative @trace=REQ-CP-003
  Scenario: Change password with both fields empty
    When the user submits the change password form without entering passwords
    Then a password validation error should be displayed on change password page

  @PY-CP-004 @negative @trace=REQ-CP-004
  Scenario: Change password with password only
    When the user enters a valid new password on change password page
    And the user submits the change password form
    Then a confirm password validation error should be displayed on change password page

  @PY-CP-005 @negative @trace=REQ-CP-005
  Scenario: Change password with mismatched values
    When the user enters a valid new password on change password page
    And the user enters a different confirm password on change password page
    And the user submits the change password form
    Then a password mismatch validation error should be displayed on change password page

  @PY-CP-006 @validation @trace=REQ-CP-006
  Scenario: Password field masks entered value on change password page
    When the user enters a valid new password on change password page
    Then the password field should mask the entered value on change password page

  @PY-CP-007 @validation @trace=REQ-CP-007
  Scenario: Confirm password field masks entered value on change password page
    When the user enters the same confirm password on change password page
    Then the confirm password field should mask the entered value on change password page

  @PY-CP-008 @navigation @trace=REQ-CP-008
  Scenario: User navigates back to my account page from change password page
    When the user clicks the back button on change password page
    Then the my account page should be loaded from change password flow