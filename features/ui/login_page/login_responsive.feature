@ui @login_page @responsive @opencart
Feature: OpenCart Authentication - Login Page Responsive Layout
  As a visitor
  I want the login page to remain usable across screen sizes
  So that I can log in from desktop, tablet, and mobile devices

  @PY-LPR-001 @desktop @trace=REQ-LPR-001
  Scenario: Login page displays correctly on desktop
    Given the user opens the OpenCart login page
    When the user sets the browser viewport to desktop size
    Then the OpenCart login page should be loaded
    And the login page form should remain usable
    And the login page primary elements should be visible

  @PY-LPR-002 @tablet @trace=REQ-LPR-002
  Scenario: Login page displays correctly on tablet
    Given the user opens the OpenCart login page
    When the user sets the browser viewport to tablet size
    Then the OpenCart login page should be loaded
    And the login page form should remain usable
    And the login page primary elements should be visible

  @PY-LPR-003 @mobile @trace=REQ-LPR-003
  Scenario: Login page displays correctly on mobile
    Given the user opens the OpenCart login page
    When the user sets the browser viewport to mobile size
    Then the OpenCart login page should be loaded
    And the login page form should remain usable
    And the login page primary elements should be visible