@ui @edit_account_page @opencart
Feature: OpenCart Account - Edit Account Information
  As an authenticated user
  I want to update my account information
  So that my profile details remain accurate

  Background:
    Given the user is logged in to edit account
    And the user navigates to the edit account page

  @PAS-129 @PY-EA-001 @smoke @trace=REQ-EA-001
  Scenario: Edit account page is displayed correctly
    Then the OpenCart edit account page should be loaded
    And the first name field should be displayed on edit account page
    And the last name field should be displayed on edit account page
    And the email field should be displayed on edit account page
    And the continue button should be displayed on edit account page
    And the back button should be displayed on edit account page

  @PAS-128 @PY-EA-002 @validation @trace=REQ-EA-002
  Scenario: Edit account fields are prefilled with current customer data
    Then the first name field should contain the current customer first name
    And the last name field should contain the current customer last name
    And the email field should contain the current customer email

  @PAS-132 @PY-EA-003 @smoke @trace=REQ-EA-003
  Scenario: User updates all editable fields with valid values
    When the user updates the first name on edit account page with a valid value
    And the user updates the last name on edit account page with a valid value
    And the user updates the email on edit account page with a unique valid value
    And the user submits the edit account form
    Then the account information should be updated successfully

  @PAS-134 @PY-EA-004 @positive @trace=REQ-EA-004
  Scenario: User updates only the first name
    When the user updates the first name on edit account page with a valid value
    And the user submits the edit account form
    Then the account information should be updated successfully

  @PAS-131 @PY-EA-005 @positive @trace=REQ-EA-005
  Scenario: User updates only the last name
    When the user updates the last name on edit account page with a valid value
    And the user submits the edit account form
    Then the account information should be updated successfully

  @PAS-125 @PY-EA-006 @positive @trace=REQ-EA-006
  Scenario: User updates only the email
    When the user updates the email on edit account page with a unique valid value
    And the user submits the edit account form
    Then the account information should be updated successfully

  @PAS-133 @PY-EA-007 @negative @trace=REQ-EA-007
  Scenario: Edit account with empty first name
    When the user clears the first name field on edit account page
    And the user submits the edit account form
    Then a first name validation error should be displayed on edit account page

  @PAS-126 @PY-EA-008 @negative @trace=REQ-EA-008
  Scenario: Edit account with empty last name
    When the user clears the last name field on edit account page
    And the user submits the edit account form
    Then a last name validation error should be displayed on edit account page

  @PAS-135 @PY-EA-009 @negative @trace=REQ-EA-009
  Scenario: Edit account with empty email
    When the user clears the email field on edit account page
    And the user submits the edit account form
    Then an email validation error should be displayed on edit account page

  @PAS-127 @PY-EA-010 @negative @trace=REQ-EA-010
  Scenario: Edit account with invalid email format
    When the user updates the email on edit account page with an invalid value
    And the user submits the edit account form
    Then an email validation error should be displayed on edit account page

  @PAS-124 @PY-EA-011 @negative @trace=REQ-EA-011
  Scenario: Edit account with duplicate email
    When the user updates the email on edit account page with a duplicate value
    And the user submits the edit account form
    Then no email business validation error should be displayed on edit account page

  @PAS-130 @PY-EA-012 @navigation @trace=REQ-EA-012
  Scenario: User navigates back to my account page from edit account page
    When the user clicks the back button on edit account page
    Then the my account page should be loaded from edit account flow