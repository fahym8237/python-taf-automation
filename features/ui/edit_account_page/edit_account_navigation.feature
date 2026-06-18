@ui @edit_account_page @navigation @opencart
Feature: OpenCart Account - Edit Account Navigation
  As an authenticated user
  I want to navigate correctly from the edit account page
  So that I can reach related account pages

  Background:
    Given the user is logged in to edit account
    And the user navigates to the edit account page

  @PAS-15 @PY-EAN-001 @smoke @trace=REQ-EAN-001
  Scenario: Back button navigates to My Account page
    When the user clicks the back button on edit account page
    Then the my account page should be loaded from edit account flow

  @PAS-139 @PY-EAN-002 @navigation @trace=REQ-EAN-002
  Scenario: Breadcrumb is displayed correctly on edit account page
    
    Then the edit account page breadcrumb should display "Account"
    And the edit account page breadcrumb should display "Edit Information"

  @PAS-19 @PY-EAN-003 @navigation @trace=REQ-EAN-003
  Scenario: User navigates to My Account page from side menu
    When the user clicks the side menu my account link on edit account page
    Then the my account page should be loaded from edit account flow

  @PAS-138 @PY-EAN-004 @navigation @trace=REQ-EAN-004
  Scenario: User clicks Edit Account self-link from side menu
    When the user clicks the side menu edit account link on edit account page
    Then the OpenCart edit account page should be loaded

  @PAS-140 @PY-EAN-005 @navigation @trace=REQ-EAN-005
  Scenario: User navigates to Password page from side menu
    When the user clicks the side menu password link on edit account page
    Then the change password page should be loaded from edit account flow

  @PAS-137 @PY-EAN-006 @navigation @trace=REQ-EAN-006
  Scenario: User logs out from side menu on edit account page
    When the user clicks the side menu logout link on edit account page
    Then the user should be logged out successfully from edit account flow