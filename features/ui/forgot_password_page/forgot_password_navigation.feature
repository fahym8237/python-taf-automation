@ui @forgot_password_page @navigation @opencart
Feature: OpenCart Authentication - Forgotten Password Navigation
  As a visitor
  I want to navigate correctly from the forgotten password page
  So that I can reach related authentication pages

  Background:
    Given the user opens the OpenCart forgotten password page

  @PY-FPN-001 @smoke @trace=REQ-FPN-001
  Scenario: Back button navigates to login page
    When the user clicks the back button on forgotten password page
    Then the OpenCart login page should be loaded

  @PY-FPN-002 @navigation @trace=REQ-FPN-002
  Scenario: Breadcrumb is displayed correctly on forgotten password page
    
    Then the forgotten password page breadcrumb should display "Account"
    And the forgotten password page breadcrumb should display "Forgotten Password"

  @PY-FPN-003 @navigation @trace=REQ-FPN-003
  Scenario: User navigates to login page from side menu
    When the user clicks the side menu login link on forgotten password page
    Then the OpenCart login page should be loaded

  @PY-FPN-004 @navigation @trace=REQ-FPN-004
  Scenario: User navigates to register page from side menu
    When the user clicks the side menu register link on forgotten password page
    Then the register account page should be loaded from forgotten password flow

  @PY-FPN-005 @navigation @trace=REQ-FPN-005
  Scenario: User clicks forgotten password self-link from side menu
    When the user clicks the side menu forgotten password link on forgotten password page
    Then the OpenCart forgotten password page should be loaded