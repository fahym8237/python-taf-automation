@ui @edit_account_page @responsive @opencart
Feature: OpenCart Account - Edit Account Responsive Layout
  As an authenticated user
  I want the edit account page to remain usable across screen sizes
  So that I can update my account information on desktop, tablet, and mobile

  Background:
    Given the user is logged in to edit account
    And the user navigates to the edit account page

  @PAS-142 @PY-EAR-001 @desktop @trace=REQ-EAR-001
  Scenario: Edit account page displays correctly on desktop
    When the user sets the browser viewport to desktop size on edit account page
    Then the OpenCart edit account page should be loaded
    And the edit account form should remain usable
    And the edit account page primary elements should be visible

  @PAS-144 @PY-EAR-002 @tablet @trace=REQ-EAR-002
  Scenario: Edit account page displays correctly on tablet
    When the user sets the browser viewport to tablet size on edit account page
    Then the OpenCart edit account page should be loaded
    And the edit account form should remain usable
    And the edit account page primary elements should be visible

  @PAS-143 @PY-EAR-003 @mobile @trace=REQ-EAR-003
  Scenario: Edit account page displays correctly on mobile
    When the user sets the browser viewport to mobile size on edit account page
    Then the OpenCart edit account page should be loaded
    And the edit account form should remain usable
    And the edit account page primary elements should be visible