@ui @forgot_password_page @security @opencart
Feature: OpenCart Authentication - Forgotten Password Security
  As a visitor
  I want forgotten password security controls to behave correctly
  So that password recovery remains safe and stable

  Background:
    Given the user opens the OpenCart forgotten password page

  @PAS-56 @PY-FPS-001 @security @trace=REQ-FPS-001
  Scenario: Forgotten password page is served over HTTPS
    Then the forgotten password page URL should use HTTPS

  @PAS-53 @PY-FPS-002 @security @negative @trace=REQ-FPS-002
  Scenario: Forgotten password form safely handles malicious email input
    When the user enters malicious email input on forgotten password page
    And the user submits the forgotten password form
    Then the forgotten password page should remain stable
    And no PYaScript alert should be displayed on forgotten password page

  @PAS-55 @PY-FPS-003 @security @negative @trace=REQ-FPS-003
  Scenario: Forgotten password form safely handles very long email input
    When the user enters a very long email on forgotten password page
    And the user submits the forgotten password form
    Then the forgotten password page should remain stable

  @PAS-54 @PY-FPS-004 @security @stability @trace=REQ-FPS-004
  Scenario: Repeated forgotten password submissions are handled safely
    When the user submits the forgotten password form multiple times with unregistered email
    Then the email validation error should be displayed on forgotten password page