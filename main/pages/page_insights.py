from playwright.sync_api import Page
from main.base.base_page import BasePage
from main.locators.locator_insights import InsightsPageLocators
from main.utility.logger import logger

class InsightsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.loc = InsightsPageLocators(page)

    def click_navigation_insights(self):
        self.click(self.loc.navigation_insights, "Insights")

    def click_insights(self, insights_name: str):
        insights_map = {
            "BLOGS": self.loc.navigation_blogs,
            "E-BOOKS": self.loc.navigation_e_books,
            "MEDIA": self.loc.navigation_media,
            "WEBINARS": self.loc.navigation_webinars,
        }

        locator = insights_map.get(insights_name)
        if not locator:
            raise ValueError(f"Unknown insights '{insights_name}'")
        self.click(locator, insights_name)

    def assert_heading_insights(self, expected_text: str):
        heading_map = {
            "BLOGS": self.loc.heading_blogs,
            "E-BOOKS": self.loc.heading_e_books,
            "MEDIA": self.loc.heading_media,
            "WEBINARS": self.loc.heading_webinars      
        }

        locator = heading_map.get(expected_text)
        if not locator:
            raise ValueError(f"Unknown expected heading '{expected_text}' — add to heading_map.")
        self.assert_visible_and_text(locator, expected_text, expected_text)
