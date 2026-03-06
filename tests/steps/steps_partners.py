import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from main.pages.page_partners import PartnersPage
# from tests.steps.steps_home import *

scenarios("partners.feature")

@when(parsers.parse("I click Partners then {partner}"))
def click_partners(partners_page: PartnersPage, partner: str):
    partners_page.click_partners()
    partners_page.click_partner(partner)

@then(parsers.parse("I should see '{expected_header}'"))
def assert_heading(partners_page: PartnersPage, expected_header: str):
    partners_page.assert_heading_partners(expected_header)
