@ui @login_page @security @opencart
Feature: OpenCart Authentication - Login Page Security
  As a visitor
  I want login security controls to behave correctly
  So that authentication is safe and robust

  Background:
    Given the user opens the OpenCart login page

  @PY-LPS-001 @security @trace=REQ-LPS-001
  Scenario: Password field masks typed value
    When the user enters a valid login password
    Then the login password field should mask the entered value

  @PY-LPS-002 @security @trace=REQ-LPS-002
  Scenario: Login page is served over HTTPS
    Then the login page URL should use HTTPS

  @PY-LPS-003 @security @negative @trace=REQ-LPS-003
  Scenario: Login with malicious input values
    When the user enters malicious login email input
    And the user enters malicious login password input
    And the user submits the login form
    Then a login browser Native message should be displayed
    And no PYaScript alert should be displayed

  @PY-LPS-004 @security @negative @trace=REQ-LPS-004
  Scenario: Repeated invalid login attempts are handled safely
    When the user submits invalid login credentials multiple times
    Then the login page should remain stable
    And a login warning message should be displayed