from playwright.sync_api import Page
from main.base.base_page import BasePage
from main.locators.locator_contact_us import ContactUsPageLocators

class ContactUsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.loc = ContactUsPageLocators(page)

    def click_navigation_contact_us(self):
        self.click(self.loc.navigation_contact_us, "Contact Us")

    def assert_heading_contact_us(self):
        self.scroll_to(self.loc.heading_contact_us, "CONTACT US")
