Feature: Solutions Page

@solutions @smoke
Scenario: Validate Solutions Page Heading
  Given I am on the home page
  When I accept all cookies
  When I click Solutions then Retails
  Then I should see 'SELL SMART, SELL MORE'



