from playwright.sync_api import Page
from main.base.base_page import BasePage
from main.locators.locator_services import ServicesPageLocators
from main.utility.logger import logger


class ServicesPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.loc = ServicesPageLocators(page)

    def click_services(self):
        self.click(self.loc.navigation_services, "Services")

    def click_service(self, service_name: str):
        service_map = {
            "Software Services": self.loc.navigation_software_services,
            "Quality Assurance": self.loc.navigation_quality_assurance,
            "Cloud": self.loc.navigation_cloud,
            "Data": self.loc.navigation_data,
            "Artificial Intelligence": self.loc.navigation_artificial_intelligence,
        }

        locator = service_map.get(service_name)
        if not locator:
            raise ValueError(f"Unknown service '{service_name}'")
        self.click(locator, service_name)

    def assert_heading_services(self, expected_text: str):
        heading_map = {
            "Elevate your software": self.loc.heading_software_services,
            "Race your Journey to the finish line": self.loc.heading_quality_assurance,
            "Accelerate your Journey to the Cloud": self.loc.heading_cloud,
            "Discover new data frontiers": self.loc.heading_data,
            "Innovate with AI-powered solutions": self.loc.heading_artificial_intelligence,
        }

        locator = heading_map.get(expected_text)
        if not locator:
            raise ValueError(f"Unknown expected heading '{expected_text}' — add to heading_map.")
        self.assert_visible_and_text(locator, expected_text, expected_text)
