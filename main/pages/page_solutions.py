from playwright.sync_api import Page
from main.base.base_page import BasePage
from main.locators.locator_solutions import SolutionsPageLocators

class SolutionsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.loc = SolutionsPageLocators(page)

    def click_solutions(self):
        self.click(self.loc.navigation_solutions, "Solutions")

    def click_retails(self):
        self.click(self.loc.navigation_retails, "Retails")          

    def assert_heading_retails(self):
        self.assert_visible_and_text(self.loc.heading_retails, "SELL SMART,SELL MORE", "SELL SMART, SELL MORE")  
    
  