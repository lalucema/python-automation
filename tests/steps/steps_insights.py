import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from main.pages.page_insights import InsightsPage
# from tests.steps.steps_home import *

scenarios("insights.feature")

@when(parsers.parse("I click Insights then {insights}"))
def click_insights(insights_page: InsightsPage, insights: str):
    insights_page.click_navigation_insights()
    insights_page.click_insights(insights)

@then(parsers.parse("I should see '{expected_header}'"))
def assert_heading_insights(insights_page: InsightsPage, expected_header: str):
    insights_page.assert_heading_insights(expected_header)
