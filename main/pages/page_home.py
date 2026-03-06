from playwright.sync_api import Page, expect
from main.base.base_page import BasePage
from main.locators.locator_home import HomePageLocators
from main.utility.logger import logger

class HomePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.loc = HomePageLocators(page)

    def open_home_page(self, base_url):
        self.open(base_url)

    def click_accept_all_button(self):
        self.click(self.loc.button_accept_all, "Accept All")

    def assert_heading_fast_forward_to_the_future(self):
        self.assert_visible_and_text(self.loc.heading_fast_forward_to_the_future, "Fast forward to the future", "Fast forward to the future")     
    
  