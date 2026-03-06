Feature: Careers Page

@careers @smoke @regression
Scenario: Validate Careers Page Heading
  Given I am on the home page
  When I accept all cookies
  When I click Careers
  Then I should see 'Fast forward to your future'
