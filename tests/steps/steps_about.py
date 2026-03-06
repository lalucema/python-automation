import pytest
from pytest_bdd import scenarios, given, when, then
from main.pages.page_about import AboutPage

scenarios("about.feature")

@when("I click About")
def click_navigation_about(about_page: AboutPage):
    about_page.click_navigation_about()

@then("I should see 'About Us'")
def assert_heading_about(about_page: AboutPage):
    about_page.assert_heading_about()