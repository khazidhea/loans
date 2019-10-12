Feature: Loans

Scenario: Loans list
    Given I visit loans list
    Then I should see loans

Scenario: Add loan
    Given I visit loans create
    And I have filled out a loan form
    When I press submit button
    Then I should see a new loan
