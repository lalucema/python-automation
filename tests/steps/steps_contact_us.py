import pytest
from pytest_bdd import scenarios, given, when, then
from main.pages.page_contact_us import ContactUsPage
# from tests.steps.steps_home import *

scenarios("contact_us.feature")

@when("I click Contact Us")
def click_navigation_contact_us(contact_us_page: ContactUsPage):
    contact_us_page.click_navigation_contact_us()

@then("I should see 'CONTACT US'")
def assert_heading_contact_us(contact_us_page: ContactUsPage):
    contact_us_page.assert_heading_contact_us()
