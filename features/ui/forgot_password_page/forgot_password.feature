@ui @forgot_password_page @opencart
Feature: OpenCart Authentication - Forgotten Password
  As a visitor
  I want to request a password reset
  So that I can recover my account

  Background:
    Given the user opens the OpenCart forgotten password page

  @PY-FP-001 @smoke @trace=REQ-FP-001
  Scenario: Forgotten password page is displayed correctly
    Then the OpenCart forgotten password page should be loaded
    And the forgotten password instruction text should be displayed
    And the email field should be displayed on forgotten password page
    And the continue button should be displayed on forgotten password page
    And the back button should be displayed on forgotten password page

  @PY-FP-002 @positive @trace=REQ-FP-002
  Scenario: Submit forgotten password request with registered email
    When the user enters a registered email on forgotten password page
    And the user submits the forgotten password form
    Then the forgotten password request should be accepted

  @PY-FP-003 @negative @trace=REQ-FP-003
  Scenario: Submit forgotten password form without email
    When the user submits the forgotten password form without email
    Then the email validation error should be displayed on forgotten password page

  @PY-FP-004 @negative @trace=REQ-FP-004
  Scenario: Submit forgotten password form with unregistered email
    When the user enters an unregistered email on forgotten password page
    And the user submits the forgotten password form
    Then the email validation error should be displayed on forgotten password page

  @PY-FP-005 @negative @trace=REQ-FP-005
  Scenario: Submit forgotten password form with invalid email format
    When the user enters an invalid email on forgotten password page
    And the user submits the forgotten password form
    Then the email validation error should be displayed on forgotten password page

  @PY-FP-006 @navigation @trace=REQ-FP-006
  Scenario: User navigates back to login page from forgotten password page
    When the user clicks the back button on forgotten password page
    Then the OpenCart login page should be loaded