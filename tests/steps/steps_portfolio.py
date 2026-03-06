import pytest
from pytest_bdd import scenarios, given, when, then
from main.pages.page_portfolio import PortfolioPage
# from tests.steps.steps_home import *

scenarios("portfolio.feature")

@when("I click Portfolio")
def click_portfolio(portfolio_page: PortfolioPage):
    portfolio_page.click_portfolio()

@then("I should see 'PORTFOLIO'")
def assert_heading_portfolio(portfolio_page: PortfolioPage):
    portfolio_page.assert_heading_portfolio()

