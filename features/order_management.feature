Feature: Order Management - Order Confirmation and Cancellation
  As a customer
  I want to view order confirmation, cancel order, and manage order status
  So that I can track and manage my orders

  @successful_order_confirmation_verification @order_management
  Scenario: Verify order confirmation page after successful payment
    Given I have completed 3D Secure authentication successfully
    When the order confirmation page is displayed after successful 3D Secure authentication
    Then the confirmation page should inform me that the order has been submitted but not yet accepted
    And the page should provide an estimated delivery time range
    And it should indicate that I will receive a confirmation text or notification when the order has been accepted
    And delivery information, including the address and the name of the patron, should be correctly displayed as provided earlier in the order process

  @successful_order_cancellation @order_management
  Scenario: Cancel order and verify cancellation status
    Given I have a confirmed order displayed on the order confirmation page
    When I click "Cancel order" to cancel the order
    Then the system should immediately respond to the cancellation request
    And the order status should be updated to indicate that the order has been canceled
    And an option should be presented to me to undo the cancellation
    And the option should be labeled "Canceled by accident?"
    And there should be a clear indication of the steps or time available to reverse the cancellation
    And if I take no action to undo the cancellation within the specified steps or time frame, the cancellation should remain in effect

  @successful_undo_option_verification @order_management
  Scenario: Verify undo cancellation option availability
    Given I have canceled my order
    When I observe the interface for an option to undo the cancellation after clicking "Cancel order"
    Then the system should display a clickable option or button labeled "Canceled by accident?"
    And the option should indicate that I have a way to reverse the cancellation
    And the number "(5)" should suggest there may be a limited number of attempts or a limited time frame to undo the cancellation
    And the limitation should be clear and understandable
    And I should be able to undo the cancellation
