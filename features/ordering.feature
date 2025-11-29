Feature: Ordering - Branch Selection and Cart Management
  As a customer
  I want to browse restaurant branch, select menu items, and add them to cart
  So that I can prepare my order for checkout


  @successful_add_to_cart @ordering
  Scenario: Add items to cart and verify cart contents
    Given I am viewing the restaurant menu
    When I add "Waffle with ice cream and honey" to the cart
    Then the "Waffle with ice cream and honey" item should be successfully added to the cart
    
    When I add "Latte with Hot" to the cart
    Then the "Latte with Hot" should be added to the cart
    And the cart should reflect the items with their descriptions, prices, and any selected options or add-ons

