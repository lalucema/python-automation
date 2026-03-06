import pytest
from pytest_bdd import scenarios, when, then, given, parsers

scenarios("google_sheets.feature")

@pytest.fixture
def context():
    return {}

# -------------------------------
# GET
# -------------------------------
@when("I send a GET request to Google Sheets")
def send_get_request(google_sheets_service, context):
    context["response"] = google_sheets_service.get_records()

@then("the response status code should be 200")
def assert_200(context):
    assert context["response"].status_code == 200

@then(parsers.parse('the returned record id should be "{expected_id}"'))
def assert_record_id(context, expected_id):
    json_res = context["response"].json()
    if isinstance(json_res, list) and json_res:
        json_res = json_res[0]
    assert json_res.get("id") == expected_id

# -------------------------------
# POST
# -------------------------------

@when(parsers.parse(
    'I send a POST request to Google Sheets with id "{id}", username "{username}", email "{email}", password "{password}"'
))
def send_post_request(google_sheets_service, context, id, username, email, password):
    body = {
        "id": id,
        "username": username,
        "email": email,
        "password": password,
    }

    context["response"] = google_sheets_service.create_record(body)


@then("the response status code should be 201")
def assert_201(context):
    assert context["response"].status_code == 201


# -------------------------------
# PATCH
# -------------------------------
@given(parsers.parse('the row id "{row_id}"'))
def given_row_id(context, row_id):
    context["row_id"] = row_id

@when(parsers.parse(
    'I send a PATCH request to Google Sheets with id "{id}", username "{username}", email "{email}", password "{password}"'
))
def send_patch_request(google_sheets_service, context, id, username, email, password):
    body = {
        "id": id,
        "username": username,
        "email": email,
        "password": password,
    }

    row_id = context["row_id"]
    context["response"] = google_sheets_service.update_record(row_id, body)
# -------------------------------
# DELETE
# -------------------------------
@when("I send a DELETE request to Google Sheets")
def send_delete_request(google_sheets_service, context):
    context["response"] = google_sheets_service.delete_record(
        context["row_id"]
    )
