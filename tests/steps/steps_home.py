import pytest
from pytest_bdd import scenarios, given, when, then
from main.pages.page_home import HomePage

scenarios("home.feature")

@then("I should see 'Fast forward to the future'")
def assert_heading_fast_forward_to_the_future(home_page: HomePage):
    home_page.assert_heading_fast_forward_to_the_future()