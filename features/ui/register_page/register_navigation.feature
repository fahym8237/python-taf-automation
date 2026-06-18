@ui @register_page @navigation @opencart
Feature: OpenCart Authentication - Register Page Navigation
  As a visitor
  I want to navigate correctly from the register page
  So that I can reach related authentication pages

  Background:
    Given the user opens the OpenCart register page

  @PAS-103 @PY-RPN-001 @smoke @trace=REQ-RPN-001
  Scenario: User navigates to login page from register intro link
    When the user clicks the login link on register page
    Then the OpenCart login page should be loaded from register flow

  @PAS-104 @PY-RPN-002 @navigation @trace=REQ-RPN-002
  Scenario: Breadcrumb is displayed correctly on register page
    Then the register page breadcrumb should display "Account"
    And the register page breadcrumb should display "Register"

  @PAS-44 @PY-RPN-003 @navigation @trace=REQ-RPN-003
  Scenario: User navigates to login page from side menu
    When the user clicks the side menu login link on register page
    Then the OpenCart login page should be loaded from register flow

  @PAS-105 @PY-RPN-004 @navigation @trace=REQ-RPN-004
  Scenario: User clicks register self-link from side menu
    When the user clicks the side menu register link on register page
    Then the OpenCart register page should be loaded

  @PAS-106 @PY-RPN-005 @navigation @trace=REQ-RPN-005
  Scenario: User navigates to forgotten password page from side menu
    When the user clicks the side menu forgotten password link on register page
    Then the OpenCart forgotten password page should be loaded from register flow

  @PAS-107 @PY-RPN-006 @navigation @trace=REQ-RPN-006
  Scenario: User opens privacy policy from register page
    When the user clicks the privacy policy link on register page
    Then the privacy policy should be opened from register page