Feature: Google Sheets API

  @api_get_record
  Scenario: Retrieve the first Google Sheets record
    When I send a GET request to Google Sheets
    Then the response status code should be 200
    And the returned record id should be "1"

  Scenario: Create a new Google Sheets record - ID 30
    When I send a POST request to Google Sheets with id "30", username "user30", email "user30@example.com", password "pass030"
    Then the response status code should be 201
 
  @api_create_record
  Scenario: Create a new Google Sheets record - ID 31
    When I send a POST request to Google Sheets with id "31", username "user31", email "user31@example.com", password "pass031"
    Then the response status code should be 201
 
  Scenario: Update an existing Google Sheets row - ID 30
    Given the row id "30"
    When I send a PATCH request to Google Sheets with id "30", username "user30", email "user30@example.com", password "passthirty"
    Then the response status code should be 200

  @api_update_record
  Scenario: Update an existing Google Sheets row - ID 31
    Given the row id "31"
    When I send a PATCH request to Google Sheets with id "31", username "user31", email "user31@example.com", password "passthirtyone"
    Then the response status code should be 200
 
  @api_delete_record
  Scenario: Delete an existing Google Sheets row - ID 30
    Given the row id "30"
    When I send a DELETE request to Google Sheets
    Then the response status code should be 200

  Scenario: Delete an existing Google Sheets row - ID 31
    Given the row id "31"
    When I send a DELETE request to Google Sheets
    Then the response status code should be 200
