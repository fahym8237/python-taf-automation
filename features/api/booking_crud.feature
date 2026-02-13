@capability_booking @api
Feature: Booking API - CRUD

  @smoke @trace=REQ-BOOKING-CRUD-001
  Scenario: Create and Read booking
    When I create a booking via API with valid data
    Then the booking should be created successfully
    And I can retrieve the booking by id

  @regression @trace=REQ-BOOKING-CRUD-001
  Scenario: Update booking with PUT
    Given I have an existing booking via API
    When I update the booking using PUT
    Then the booking data should be updated

  @regression @trace=REQ-BOOKING-CRUD-001
  Scenario: Partial update booking with PATCH
    Given I have an existing booking via API
    When I update the booking using PATCH
    Then the booking data should be partially updated

  @regression @trace=REQ-BOOKING-CRUD-001
  Scenario: Delete booking
    Given I have an existing booking via API
    When I delete the booking
    Then the booking should not be retrievable