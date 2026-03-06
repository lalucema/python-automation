import pytest
from pytest_bdd import scenarios, given, when, then
from main.pages.page_careers import CareersPage
# from tests.steps.steps_home import *

scenarios("careers.feature")

@when("I click Careers")
def click_navigation_careers(careers_page: CareersPage):
    careers_page.click_navigation_careers()

@then("I should see 'Fast forward to your future'")
def assert_heading_careers(careers_page: CareersPage):
    careers_page.assert_heading_careers()