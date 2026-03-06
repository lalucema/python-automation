Feature: Home Page

@home @smoke
Scenario: Validate Home Page Heading
  Given I am on the home page
  When I accept all cookies
  Then I should see 'Fast forward to the future'

