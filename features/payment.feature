Feature: Payment - Payment Information and 3D Secure Authentication
  As a customer
  I want to input payment information and complete 3D Secure authentication
  So that I can complete my order

  @successful_payment_complete @payment
  Scenario: Complete payment process with successful 3D Secure authentication
    Given I have confirmed the scheduled delivery time
    When I proceed to checkout the cart
    And I input credit card information:
      | Credit Card Number | 4000 0027 6000 3184 |
      | Cardholder Name    | testing qa          |
      | Expiration Date    | 12/34                |
      | Security Code      | 123                  |
    Then I should be able to input the provided credit card details
    And the credit card details should include the credit card number, cardholder name, expiration date, and security code
    
    When I input contact information:
      | Name           | Test User        |
      | Contact Number | +886-0912345678  |
      | Email          | test@example.com |
    And I select country code "+886" from the contact number dropdown
    And I input contact number "0912345678"
    Then I should be able to input my contact information
    And the contact information should include name, contact number with country code, and email address
    
    When I check the agree checkbox
    And I click "Confirm" to submit the order
    Then the order should be submitted to the system for processing
    And the system should redirect me to the 3D Secure 2 authentication page as part of the payment verification process
    
    When the test authentication page for 3D Secure 2 is displayed
    Then the test authentication page for 3D Secure 2 should be displayed with clear instructions for verification
    And I should have the option to complete or fail the verification process
    
    When I perform the required action on the 3D Secure 2 test page by selecting "COMPLETE"
    Then the transaction should proceed
    And a confirmation of the order completion should be displayed

  @failed_payment_3d_secure @payment
  Scenario: Handle payment process with failed 3D Secure authentication
    Given I have confirmed the scheduled delivery time
    When I proceed to checkout the cart
    And I input credit card information:
      | Credit Card Number | 4000 0027 6000 3184 |
      | Cardholder Name    | testing qa          |
      | Expiration Date    | 12/34                |
      | Security Code      | 123                  |
    Then I should be able to input the provided credit card details
    And the credit card details should include the credit card number, cardholder name, expiration date, and security code
    
    When I input contact information:
      | Name           | Test User        |
      | Contact Number | +886-0912345678  |
      | Email          | test@example.com |
    And I select country code "+886" from the contact number dropdown
    And I input contact number "0912345678"
    Then I should be able to input my contact information
    And the contact information should include name, contact number with country code, and email address
    
    When I check the agree checkbox
    And I click "Confirm" to submit the order
    Then the order should be submitted to the system for processing
    And the system should redirect me to the 3D Secure 2 authentication page as part of the payment verification process
    
    When the test authentication page for 3D Secure 2 is displayed
    Then the test authentication page for 3D Secure 2 should be displayed with clear instructions for verification
    And I should have the option to complete or fail the verification process
    And failure should provide appropriate feedback or instructions based on the bank's chosen method
    
    When I perform the required action on the 3D Secure 2 test page by selecting "FAIL"
    Then the transaction should not proceed
    And I should see the order declined page with the reason of the failure
