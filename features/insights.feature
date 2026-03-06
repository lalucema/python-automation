Feature: Insights Page

@insights @smoke
Scenario Outline: Validate Insights Page Heading
  Given I am on the home page
  When I accept all cookies
  When I click Insights then <Insights>
  Then I should see '<ExpectedHeader>'

Examples:
  | Insights | ExpectedHeader |
  | BLOGS    | BLOGS          |
  | E-BOOKS  | E-BOOKS        |
  | MEDIA    | MEDIA          |
  | WEBINARS | WEBINARS       |