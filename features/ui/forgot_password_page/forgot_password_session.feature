@ui @forgot_password_page @session @opencart
Feature: OpenCart Authentication - Forgotten Password Session Management
  As a visitor
  I want forgotten password page state and navigation to remain stable
  So that I can recover my account reliably

  Background:
    Given the user opens the OpenCart forgotten password page

  @PY-FPSE-001 @session @stability @trace=REQ-FPSE-001
  Scenario: Refresh forgotten password page
    When the user refreshes the forgotten password page
    Then the OpenCart forgotten password page should be loaded
    And the forgotten password form should remain usable
    And the email field should be empty on forgotten password page

  @PY-FPSE-002 @session @navigation @trace=REQ-FPSE-002
  Scenario: Browser back and forward keeps forgotten password page stable
    When the user clicks the back button on forgotten password page
    Then the OpenCart login page should be loaded
    When the user navigates back in the browser from login to forgotten password page
    Then the OpenCart forgotten password page should be loaded

  @PY-FPSE-003 @session @stability @trace=REQ-FPSE-003
  Scenario: Reopen forgotten password page after leaving it
    When the user clicks the back button on forgotten password page
    Then the OpenCart login page should be loaded
    When the user opens the OpenCart forgotten password page again
    Then the OpenCart forgotten password page should be loaded
    And the forgotten password form should remain usable

  @PY-FPSE-004 @session @public_access @trace=REQ-FPSE-004
  Scenario: Direct access to forgotten password page remains available
    When the user opens the OpenCart forgotten password page again
    Then the OpenCart forgotten password page should be loaded