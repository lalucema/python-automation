Feature: Contact Us Page

  @smoke
  Scenario: Validate Contact Us Heading
    Given I am on the home page
    When I accept all cookies
    When I click Contact Us
    Then I should see 'CONTACT US'

   