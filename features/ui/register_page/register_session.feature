@ui @register_page @session @opencart
Feature: OpenCart Authentication - Register Page Session Management
  As a visitor
  I want registration flow state and navigation to remain stable
  So that I can create an account reliably

  Background:
    Given the user opens the OpenCart register page

  @PAS-120 @PY-RPSE-001 @session @stability @trace=REQ-RPSE-001
  Scenario: Refresh register page
    When the user refreshes the register page
    Then the OpenCart register page should be loaded
    And the register form should remain usable
    And the first name field should be empty on register page
    And the last name field should be empty on register page
    And the email field should be empty on register page
    And the password field should be empty on register page

  @PAS-121 @PY-RPSE-002 @session @navigation @trace=REQ-RPSE-002
  Scenario: Browser back and forward keeps register page stable
    When the user clicks the login link on register page
    Then the OpenCart login page should be loaded from register flow
    When the user navigates back in the browser from login to register page
    Then the OpenCart register page should be loaded

  @PAS-119 @PY-RPSE-003 @session @stability @trace=REQ-RPSE-003
  Scenario: Reopen register page after leaving it
    When the user clicks the login link on register page
    Then the OpenCart login page should be loaded from register flow
    When the user opens the OpenCart register page again
    Then the OpenCart register page should be loaded
    And the register form should remain usable

  @PAS-118 @PY-RPSE-004 @session @positive @trace=REQ-RPSE-004
  Scenario: Successful registration reaches the account creation success flow
    When the user fills the registration form with a generated valid user
    And the user agrees to the privacy policy
    And the user submits the registration form
    Then the success message "Your Account Has Been Created!" should be visible