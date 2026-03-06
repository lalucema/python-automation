Feature: Portfolio Page

@portfolio @smoke
Scenario: Validate Portfolio Page Heading
  Given I am on the home page
  When I accept all cookies
  When I click Portfolio
  Then I should see 'PORTFOLIO'



