@ui @change_password_page @navigation @opencart
Feature: OpenCart Account - Change Password Navigation
  As an authenticated user
  I want to navigate correctly from the change password page
  So that I can reach related account pages

  Background:
    Given the user is logged in
    And the user navigates to the change password page

  @PAS-15 @PY-CPN-001 @smoke @trace=REQ-CPN-001
  Scenario: Back button navigates to My Account page
    When the user clicks the back button on change password page
    Then the my account page should be loaded from change password flow

  @PAS-17 @PY-CPN-002 @navigation @trace=REQ-CPN-002
  Scenario: Breadcrumb is displayed correctly on change password page
    Then the change password page breadcrumb should display "Account"
    And the change password page breadcrumb should display "Change Password"

  @PAS-19 @PY-CPN-003 @navigation @trace=REQ-CPN-003
  Scenario: User navigates to My Account page from side menu
    When the user clicks the side menu my account link on change password page
    Then the my account page should be loaded from change password flow

  @PAS-16 @PY-CPN-004 @navigation @trace=REQ-CPN-004
  Scenario: User navigates to Edit Account page from side menu
    When the user clicks the side menu edit account link on change password page
    Then the edit account page should be loaded from change password flow

  @PAS-14 @PY-CPN-005 @navigation @trace=REQ-CPN-005
  Scenario: User clicks Password self-link from side menu
    When the user clicks the side menu password link on change password page
    Then the OpenCart change password page should be loaded

  @PAS-18 @PY-CPN-006 @navigation @trace=REQ-CPN-006
  Scenario: User logs out from side menu on change password page
    When the user clicks the side menu logout link on change password page
    Then the user should be logged out successfully from change password flow