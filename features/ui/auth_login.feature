@capability_auth @ui
Feature: Authentication - Login

  @smoke @trace=REQ-AUTH-LOGIN-001
  Scenario: Login page renders required elements
    Given I open the login page
    Then the login form should be visible
    And the returning customer header should be visible
    And the email input should be visible
    And the password input should be visible
    And the login button should be visible
    And the forgotten password link should be visible

  @regression @trace=REQ-AUTH-LOGIN-001
  Scenario: Navigate to forgotten password from login
    Given I open the login page
    When I click the forgotten password link
    Then the forgot password page header should be visible