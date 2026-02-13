@capability_auth @ui
Feature: Authentication - Forgot Password

  @smoke @trace=REQ-AUTH-FORGOT-001
  Scenario: Forgot password page renders required elements
    Given I open the forgot password page
    Then the forgot password content container should be visible
    And the forgot password header should be visible
    And the instruction paragraph should be visible
    And the forgotten form should be visible
    And the email legend should be visible
    And the email input should be visible
    And the continue button should be visible
    And the back button should be visible