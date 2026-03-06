Feature: Partners Page
  As a user
  I want to navigate the Partners menu
  So I can view each partner's service page

@partners @smoke
  Scenario Outline: Navigate to a Partner page
    Given I am on the home page
    When I accept all cookies
    When I click Partners then <Partner>
    Then I should see '<ExpectedHeader>'

    Examples:
      | Partner          | ExpectedHeader                          |
      | AWS Data         | Be a data hero Not a zero!              |
      | AWS Cloud MSP    | Cloud Managed Services                  |
      | Confluent        | Unlock the power of data streaming      |
      | MongoDB          | Liberate your data                      |
      | nOps             | Reduce cloudcosts by up to 50%          |
      | OutSystems       | Innovate fastwith low-code development  |
