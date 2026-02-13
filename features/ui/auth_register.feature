@capability_auth @ui
Feature: Authentication - Register

  @smoke @trace=REQ-AUTH-REGISTER-001
  Scenario: Register page renders required elements
    Given I open the register page
    Then the register content container should be visible
    And the register header should be visible
    And the register form should be visible
    And the personal details legend should be visible
    And the first name input should be visible
    And the last name input should be visible
    And the email input should be visible
    And the password legend should be visible
    And the password input should be visible
    And the newsletter legend should be visible
    And the newsletter checkbox should be visible
    And the privacy policy checkbox should be visible
    And the privacy policy link should be visible
    And the register continue button should be visible
    And the login page link should be visible

  @regression @dataset=register_invalid.csv @trace=REQ-AUTH-REGISTER-001
  Scenario: Register validation errors from dataset
    Given I open the register page
    When I submit registration from dataset "register_invalid.csv"
    Then I should see the expected validation errors