Feature: Order Page - Restaurant Order Page with Delivery Selection
  As a customer
  I want to open the restaurant order page, select delivery option, and confirm address
  So that I can start placing my order

  @successful_order_page_load @order_page
  Scenario: Open Food Ordering company page
    Given I open the Food Ordering company page
    Then the page should load successfully
    And the page should display the company's food ordering options and relevant information

  @successful_delivery_selection @order_page
  Scenario: Select delivery option from Delivery/Takeout switcher
    Given I have opened the Food Ordering page
    Then the Delivery/Takeout switcher should be visible
    And the switcher should allow me to select my desired service type
    When I select "Delivery"
    Then the delivery prompt message should be visible
    When I select "Takeout"
    Then the delivery prompt message should not be visible
  

  @successful_postal_code_confirmation @order_page
  Scenario: Input postal code and confirm delivery address
    Given I have selected "Delivery" option
    When I click edit button at address picker
    And I input postal code "049561" at address picker
    Then the system should use the postal code to locate the place
    When I select the searched address and confirm address
    Then I should be able to successfully select and confirm the address
    And the interface should reflect the chosen delivery address
    And an "Edit" option should be provided after confirming the address
