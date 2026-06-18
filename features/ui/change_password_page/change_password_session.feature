@ui @change_password_page @session @opencart
Feature: OpenCart Account - Change Password Session Management
  As an authenticated user
  I want password changes to persist correctly across my session
  So that only the new password grants access after update

  Background:
    Given the user is logged in
    And the user navigates to the change password page

  @PAS-32 @PY-CPSE-001 @session @positive @trace=REQ-CPSE-001
  Scenario: User can login with the new password after changing it
    When the user enters a valid new password on change password page
    And the user enters the same confirm password on change password page
    And the user submits the change password form
    Then the password should be changed successfully
    When the user logs out from the account area after password change
    And the user logs in with the newly changed password
    Then the user should be logged in successfully after password change

  @PAS-31 @PY-CPSE-002 @session @security @trace=REQ-CPSE-002
  Scenario: User cannot login with the old password after changing it
    When the user enters a valid new password on change password page
    And the user enters the same confirm password on change password page
    And the user submits the change password form
    Then the password should be changed successfully
    When the user logs out from the account area after password change
    And the user logs in with the old password after password change
    Then a login warning message should be displayed after password change

  @PAS-33 @PY-CPSE-003 @session @stability @trace=REQ-CPSE-003
  Scenario: Refresh change password page
    When the user refreshes the change password page
    Then the OpenCart change password page should be loaded
    And the password field should be empty on change password page
    And the confirm password field should be empty on change password page

  @PAS-34 @PY-CPSE-004 @session @navigation @trace=REQ-CPSE-004
  Scenario: Browser back and forward keeps navigation stable
    When the user clicks the back button on change password page
    Then the my account page should be loaded from change password flow
    