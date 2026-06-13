@ui @register_page @opencart
Feature: OpenCart Authentication - Register Page
  As a visitor
  I want to create a new account
  So that I can access my customer account

  Background:
    Given the user opens the OpenCart register page

  @PY-RP-001 @smoke @trace=REQ-RP-001
  Scenario: Register page is displayed correctly
    Then the OpenCart register page should be loaded
    And the first name field should be displayed on register page
    And the last name field should be displayed on register page
    And the email field should be displayed on register page
    And the password field should be displayed on register page
    And the continue button should be displayed on register page
    And the privacy policy link should be displayed on register page
    And the login link should be displayed on register page

  @PY-RP-002 @positive @trace=REQ-RP-002
  Scenario: Register with generated valid user data
    When the user fills the registration form with a generated valid user
    And the user agrees to the privacy policy
    And the user submits the registration form
    Then the success message "Your Account Has Been Created!" should be visible

  @PY-RP-003 @negative @trace=REQ-RP-003
  Scenario: Submit registration form without filling any fields
    When the user submits the registration form without filling any fields
    Then all mandatory field validation errors should be displayed

  @PY-RP-004 @negative @trace=REQ-RP-004
  Scenario: Submit registration form without accepting privacy policy
    When the user fills the registration form with a generated valid user
    And the user submits the registration form
    Then a privacy policy warning should be displayed

  @PY-RP-005 @negative @trace=REQ-RP-005
  Scenario: Submit registration form with invalid email
    When the user fills the registration form with a generated valid user
    And the user enters an invalid email on register page
    And the user agrees to the privacy policy
    And the user submits the registration form
    Then the email validation error should be displayed on register page

  @PY-RP-006 @validation @trace=REQ-RP-006
  Scenario: Password field masks entered value on register page
    When the user fills the registration form with a generated valid user
    Then the password field should mask the entered value on register page
  
  @ui @register_page @data_driven @trace=REQ-RP-007
  Scenario: Registration validation using CSV dataset
    When the user executes the registration dataset "register_data.csv"
    Then all registration dataset rows should pass