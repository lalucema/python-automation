Feature: Wookie API
  As an API tester
  I want to validate Wookie reservation and office endpoints
  So that API responses are correct and reliable

  @api
  Scenario Outline: Successfully retrieve reservation details for a user_id
    Given I have a user_id <user_id>
    When I send a request to get reservation details by user_id
    Then the response status code should be 200
    And the response should contain at least one record
    And the returned user_id should match the requested user_id

    Examples:
      | user_id |
      | 7839    |

  
  Scenario Outline: Successfully retrieve office data by date and period
    Given I have date "<date_input>"
    And I have period "<period>"
    And I have office_id <office_id>
    When I send a request to get office data by date and period
    Then the response status code should be 200
    And the returned office_id should match the requested office_id

    Examples:
      | date_input  | period    | office_id |
      | 2025-12-09  | Whole Day | 2         |
