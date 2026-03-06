from pytest_bdd import given, when
from main.pages.page_home import HomePage

@given("I am on the home page")
def go_to_home_page(home_page: HomePage, base_url: str):
    home_page.open_home_page(base_url)

@when("I accept all cookies")
def accept_all_cookies(home_page: HomePage):
    home_page.click_accept_all_button()
