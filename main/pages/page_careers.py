from playwright.sync_api import Page
from main.base.base_page import BasePage
from main.locators.locator_careers import CareersPageLocators
from main.utility.logger import logger

class CareersPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.loc = CareersPageLocators(page)
        
    def click_navigation_careers(self):
        self.click(self.loc.navigation_careers, "Careers")

    def assert_heading_careers(self):
        self.assert_visible_and_text(self.loc.heading_careers, "Fast forward to your future", "Fast forward to your future")     
