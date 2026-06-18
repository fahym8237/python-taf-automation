@ui @login_page @opencart
Feature: OpenCart Authentication - Login Page
  As a visitor or registered customer
  I want to use the login page correctly
  So that I can access my account or navigate to related authentication pages

  Background:
    Given the user opens the OpenCart login page

  @PAS-69 @PY-LP-001 @smoke @trace=REQ-LP-001
  Scenario: Login page is displayed correctly
    Then the OpenCart login page should be loaded
    And the returning customer section should be displayed
    And the email field should be displayed
    And the password field should be displayed
    And the login button should be displayed
    And the forgotten password link should be displayed

  @PAS-71 @PY-LP-002 @navigation @trace=REQ-LP-002
  Scenario: User navigates to the forgotten password page
    When the user navigates to the forgotten password page
    Then the forgotten password page should be loaded

  @PAS-65 @PY-LP-003 @navigation @trace=REQ-LP-003
  Scenario: User navigates to the register account page
    When the user navigates to the register account page
    Then the register account page should be loaded

  @PAS-70 @PY-LP-004 @negative @trace=REQ-LP-004
  Scenario: Login with empty email and empty password
    When the user submits the login form without credentials
    Then a login warning message should be displayed

  @PAS-68 @PY-LP-005 @negative @trace=REQ-LP-005
  Scenario: Login with valid email and empty password
    When the user enters a valid login email
    And the user submits the login form without password
    Then a login warning message should be displayed

  @PAS-72 @PY-LP-006 @negative @trace=REQ-LP-006
  Scenario: Login with empty email and valid password
    When the user enters a valid login password
    And the user submits the login form without email
    Then a login warning message should be displayed

  @PAS-63 @PY-LP-007 @negative @trace=REQ-LP-007
  Scenario: Login with invalid credentials
    When the user enters an invalid login email
    And the user enters an invalid login password
    And the user submits the login form
    Then a login warning message should be displayed

  @PAS-64 @PY-LP-008 @negative @trace=REQ-LP-008
  Scenario: Login with unregistered email
    When the user enters an unregistered login email
    And the user enters a valid login password
    And the user submits the login form
    Then a login warning message should be displayed

  @PAS-67 @PY-LP-009 @positive @trace=REQ-LP-009
  Scenario: Login with valid credentials
    When the user enters a valid login email
    And the user enters a valid login password
    And the user submits the login form
    Then the user should be logged in successfully

  @PAS-66 @PY-LP-010 @validation @trace=REQ-LP-010
  Scenario: Password field masks typed value
    When the user enters a valid login password
    Then the login password field should mask the entered value