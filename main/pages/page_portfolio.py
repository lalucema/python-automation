from playwright.sync_api import Page
from main.base.base_page import BasePage
from main.locators.locator_portfolio import PortfolioPageLocators

class PortfolioPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.loc = PortfolioPageLocators(page)

    def click_portfolio(self):
        self.click(self.loc.navigation_portfolio, "Portfolio")     

    def assert_heading_portfolio(self):
        self.click(self.loc.heading_portfolio, "PORTFOLIO")  
    
  