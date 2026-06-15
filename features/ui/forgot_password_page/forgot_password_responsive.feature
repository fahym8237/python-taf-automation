@ui @forgot_password_page @responsive @opencart
Feature: OpenCart Authentication - Forgotten Password Responsive Layout
  As a visitor
  I want the forgotten password page to remain usable across screen sizes
  So that I can request password reset from desktop, tablet, and mobile

  Background:
    Given the user opens the OpenCart forgotten password page

  @PY-FPR-001 @desktop @trace=REQ-FPR-001
  Scenario: Forgotten password page displays correctly on desktop
    When the user sets the browser viewport to desktop size on forgotten password page
    Then the OpenCart forgotten password page should be loaded
    And the forgotten password form should remain usable
    And the forgotten password page primary elements should be visible

  @PY-FPR-002 @tablet @trace=REQ-FPR-002
  Scenario: Forgotten password page displays correctly on tablet
    When the user sets the browser viewport to tablet size on forgotten password page
    Then the OpenCart forgotten password page should be loaded
    And the forgotten password form should remain usable
    And the forgotten password page primary elements should be visible

  @PY-FPR-003 @mobile @trace=REQ-FPR-003
  Scenario: Forgotten password page displays correctly on mobile
    When the user sets the browser viewport to mobile size on forgotten password page
    Then the OpenCart forgotten password page should be loaded
    And the forgotten password form should remain usable
    And the forgotten password page primary elements should be visible