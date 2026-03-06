Feature: About Page

@regression
Scenario: Validate About Page Heading
  Given I am on the home page
  When I accept all cookies
  When I click About
  Then I should see 'About Us'