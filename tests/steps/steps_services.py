import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from main.pages.page_services import ServicesPage
# from tests.steps.steps_home import *

scenarios("services.feature")

@when(parsers.parse("I click Services then {service}"))
def click_services(services_page: ServicesPage, service: str):
    services_page.click_services()
    services_page.click_service(service)

@then(parsers.parse("I should see '{expected_header}'"))
def assert_heading_services(services_page: ServicesPage, expected_header: str):
    services_page.assert_heading_services(expected_header)
