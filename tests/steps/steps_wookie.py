import pytest
from pytest_bdd import given, when, then, scenarios, parsers
from main.services.service_wookie import WookieService
from main.utility.logger import automation_logger as logger

scenarios("wookie.feature")

@pytest.fixture
def context():
    return {}

@given(parsers.parse("I have a user_id {user_id:d}"))
def given_user_id(context, user_id):
    logger.info(f"Given user_id: {user_id}")
    context["user_id"] = user_id

@when("I send a request to get reservation details by user_id")
def send_request(context, wookie_base_url, wookie_auth_headers):
    logger.info("Calling WookieService.get_reservation_by_user_id()")

    service = WookieService(wookie_base_url, wookie_auth_headers)
    response = service.get_reservation_by_user_id(context["user_id"])

    context["response"] = response
    context["json"] = response.json()

    logger.info("API call completed")

@then("the response status code should be 200")
def assert_status_code(context):
    logger.info("Validating status code...")
    assert context["response"].status_code == 200

@then("the response should contain at least one record")
def assert_record_exists(context):
    logger.info("Checking JSON record count...")
    result = context["json"]
    assert len(result) > 0

@then("the returned user_id should match the requested user_id")
def assert_user_id_matches(context):
    logger.info("Validating user_id match...")
    record = context["json"][0]
    assert record["user_id"] == context["user_id"]

@given(parsers.parse("I have date \"{date_input}\""))
def given_date(context, date_input):
    logger.info(f"Given date: {date_input}")
    context["date_input"] = date_input

@given(parsers.parse("I have period \"{period}\""))
def given_period(context, period):
    logger.info(f"Given period: {period}")
    context["period"] = period

@given(parsers.parse("I have office_id {office_id:d}"))
def given_office_id(context, office_id):
    logger.info(f"Given office_id: {office_id}")
    context["office_id"] = office_id

@when("I send a request to get office data by date and period")
def send_request(context, wookie_base_url, wookie_auth_headers):
    logger.info("Calling WookieService.get_offices()")

    service = WookieService(wookie_base_url, wookie_auth_headers)
    response = service.get_offices(
        context["date_input"],
        context["period"],
        context["office_id"]
    )

    context["response"] = response
    context["json"] = response.json()

    logger.info("API call completed")

@then("the response status code should be 200")
def assert_status_code(context):
    logger.info("Validating status code...")
    assert context["response"].status_code == 200

@then("the returned office_id should match the requested office_id")
def assert_office_id(context):
    logger.info("Validating office_id match...")
    
    result = context["json"]
    if isinstance(result, list) and result:
        result = result[0]

    assert result.get("office_id") == context["office_id"]