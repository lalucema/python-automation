import pytest
from pytest_bdd import scenarios, given, when, then, parser, parsers
from main.pages.page_solutions import SolutionsPage
# from tests.steps.steps_home import *

scenarios("solutions.feature")

@when("I click Solutions then Retails")
def click_solutions(solutions_page: SolutionsPage):
    solutions_page.click_solutions()
    solutions_page.click_retails()

@then("I should see 'SELL SMART, SELL MORE'")
def assert_heading_retails(solutions_page: SolutionsPage):
    solutions_page.assert_heading_retails()

