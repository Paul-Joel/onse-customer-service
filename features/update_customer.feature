Feature: Update customer

  Scenario: An existing customer changes name
    Given customer "Nicole Forsgren" with ID "12345" exists
    When I update customer "12345" to "Nicole Jones"
    And I fetch customer "12345"
    Then I should see customer "Nicole Jones"
