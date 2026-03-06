from playwright.sync_api import Page
from main.base.base_page import BasePage
from main.locators.locator_about import AboutPageLocators

class AboutPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.loc = AboutPageLocators(page)

    def click_navigation_about(self):
        self.click(self.loc.navigation_about, "About")    
  
    def assert_heading_about(self):
        self.assert_visible_and_text(self.loc.heading_about, "About Us", "About Us")     
    