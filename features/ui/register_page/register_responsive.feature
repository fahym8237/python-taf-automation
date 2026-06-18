@ui @register_page @responsive @opencart
Feature: OpenCart Authentication - Register Page Responsive Layout
  As a visitor
  I want the register page to remain usable across screen sizes
  So that I can create an account from desktop, tablet, and mobile

  Background:
    Given the user opens the OpenCart register page

  @PAS-109 @PY-RPR-001 @desktop @trace=REQ-RPR-001
  Scenario: Register page displays correctly on desktop
    When the user sets the browser viewport to desktop size on register page
    Then the OpenCart register page should be loaded
    And the register form should remain usable
    And the register page primary elements should be visible

  @PAS-111 @PY-RPR-002 @tablet @trace=REQ-RPR-002
  Scenario: Register page displays correctly on tablet
    When the user sets the browser viewport to tablet size on register page
    Then the OpenCart register page should be loaded
    And the register form should remain usable
    And the register page primary elements should be visible

  @PAS-110 @PY-RPR-003 @mobile @trace=REQ-RPR-003
  Scenario: Register page displays correctly on mobile
    When the user sets the browser viewport to mobile size on register page
    Then the OpenCart register page should be loaded
    And the register form should remain usable
    And the register page primary elements should be visible