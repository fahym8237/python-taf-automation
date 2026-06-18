@ui @register_page @security @opencart
Feature: OpenCart Authentication - Register Page Security
  As a visitor
  I want registration security controls to behave correctly
  So that account creation remains safe and robust

  Background:
    Given the user opens the OpenCart register page

  @PAS-115 @PY-RPS-001 @security @trace=REQ-RPS-001
  Scenario: Register page is served over HTTPS
    Then the register page URL should use HTTPS

  @PAS-97 @PY-RPS-002 @security @trace=REQ-RPS-002
  Scenario: Password field masks entered value on register page
    When the user fills the registration form with a generated valid user
    Then the password field should mask the entered value on register page

  @PAS-116 @PY-RPS-003 @security @negative @trace=REQ-RPS-003
  Scenario: Register form safely handles malicious input
    When the user enters malicious first name input on register page
    And the user enters malicious last name input on register page
    And the user enters malicious email input on register page
    And the user enters malicious password input on register page
    And the user agrees to the privacy policy
    And the user submits the registration form
    Then the register page should remain stable

  @PAS-114 @PY-RPS-004 @security @negative @trace=REQ-RPS-004
  Scenario: Register form safely handles very long values
    When the user enters a very long first name on register page
    And the user enters a very long last name on register page
    And the user enters a very long email on register page
    And the user enters a very long password on register page
    And the user agrees to the privacy policy
    And the user submits the registration form
    Then the register page should remain stable

  @PAS-113 @PY-RPS-005 @security @trace=REQ-RPS-005
  Scenario: Privacy policy must be accepted before registration
    When the user fills the registration form with a generated valid user
    And the user submits the registration form
    Then a privacy policy warning should be displayed