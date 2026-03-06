Feature: Services Page

@services @smoke
Scenario Outline: Validate Services page heading
  Given I am on the home page
  When I accept all cookies
  When I click Services then <Service>
  Then I should see '<ExpectedHeader>'

Examples:
  | Service                 | ExpectedHeader                               |
  | Software Services       | Elevate your software                        |
  | Quality Assurance       | Race your Journey to the finish line         |
  | Cloud                   | Accelerate your Journey to the Cloud         |
  | Data                    | Discover new data frontiers                  |
  | Artificial Intelligence | Innovate with AI-powered solutions           |
