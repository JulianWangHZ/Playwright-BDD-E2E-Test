Feature: Checkout - Order Review and Delivery Scheduling
  As a customer
  I want to review my order details and schedule delivery time
  So that I can proceed to payment

  @successful_checkout_navigation @checkout
  Scenario: Navigate to checkout page and verify order details
    Given I have items in my cart
    When I click "Checkout" after adding items to the cart
    Then the checkout page should display all the pertinent order details
    And the delivery address should be displayed
    And the estimated arrival time should be displayed
    And the order details with items added should be displayed
    And the total price should be displayed
    And a note that this is an ASAP order with the estimated preparation time should be displayed
    And options to either continue ordering or proceed to checkout should be available

  @successful_schedule_delivery_time @checkout
  Scenario: Edit estimated arrival time and schedule for later
    Given I am on the checkout page with items in my cart
    When I click "Edit" to change the Estimated arrival time
    Then I should be able to select "Scheduled for later"
    And the system should provide an option to choose a date and time
    
    When I set the date and time to 3 days later at 7:30 PM
    Then I should be able to set a specific date and confirm the delivery time

  @successful_schedule_confirmation @checkout
  Scenario: Confirm scheduled delivery time
    Given I have set the delivery time to 3 days later at 7:30 PM
    When I confirm the scheduled time
    And I click "Confirm" to finalize the selection
    Then the system should display a confirmation window
    And the confirmation window should include the precise pick-up date and time previously selected by me
    And the window should prompt me to verify the accuracy of the information before checking out
    And the confirmation window should provide a conspicuous "Confirm" button for me to finalize
    And I should be able to complete the order process
