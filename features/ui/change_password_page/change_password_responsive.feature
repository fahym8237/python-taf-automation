@ui @change_password_page @responsive @opencart
Feature: OpenCart Account - Change Password Responsive Layout
  As an authenticated user
  I want the change password page to remain usable across screen sizes
  So that I can securely update my password on desktop, tablet, and mobile

  Background:
    Given the user is logged in
    And the user navigates to the change password page

  @PY-CPR-001 @desktop @trace=REQ-CPR-001
  Scenario: Change password page displays correctly on desktop
    When the user sets the browser viewport to desktop size on change password page
    Then the OpenCart change password page should be loaded
    And the change password form should remain usable
    And the change password page primary elements should be visible

  @PY-CPR-002 @tablet @trace=REQ-CPR-002
  Scenario: Change password page displays correctly on tablet
    When the user sets the browser viewport to tablet size on change password page
    Then the OpenCart change password page should be loaded
    And the change password form should remain usable
    And the change password page primary elements should be visible

  @PY-CPR-003 @mobile @trace=REQ-CPR-003
  Scenario: Change password page displays correctly on mobile
    When the user sets the browser viewport to mobile size on change password page
    Then the OpenCart change password page should be loaded
    And the change password form should remain usable
    And the change password page primary elements should be visible