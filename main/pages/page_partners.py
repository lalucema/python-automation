from playwright.sync_api import Page
from main.base.base_page import BasePage
from main.locators.locator_partners import PartnersPageLocators

class PartnersPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.loc = PartnersPageLocators(page)

    def click_partners(self):
        self.click(self.loc.navigation_partners, "Partners")

    # ---------------------------------------------------------
    # Dynamic click based on partner name
    # ---------------------------------------------------------
    def click_partner(self, partner_name: str):
        partner_map = {
            "AWS Data": ("aws", self.loc.navigation_aws_data),
            "AWS Cloud MSP": ("aws", self.loc.navigation_aws_cloud_msp),
            "Confluent": ("top", self.loc.navigation_confluent),
            "MongoDB": ("top", self.loc.navigation_mongodb),
            "nOps": ("top", self.loc.navigation_n0ps),
            "OutSystems": ("top", self.loc.navigation_OutSystems),
        }

        partner_entry = partner_map.get(partner_name)
        if not partner_entry:
            raise ValueError(f"Unknown partner '{partner_name}' — add to partner_map.")

        group, locator = partner_entry

        # AWS submenu requires parent click first
        if group == "aws":
            self.click(self.loc.navigation_aws, "AWS")

        # Then click the actual item
        self.click(locator, partner_name)

    # ---------------------------------------------------------
    # Dynamic heading assertion
    # ---------------------------------------------------------
    def assert_heading_partners(self, expected_text: str):
        heading_map = {
            "Be a data hero Not a zero!": self.loc.heading_aws_data,
            "Cloud Managed Services": self.loc.heading_aws_cloud_msp,
            "Unlock the power of data streaming": self.loc.heading_confluent,
            "Liberate your data": self.loc.heading_mongodb,
            "Reduce cloudcosts by up to 50%": self.loc.heading_n0ps,
            "Innovate fastwith low-code development": self.loc.heading_OutSystems,
        }

        locator = heading_map.get(expected_text)
        if not locator:
            raise ValueError(
                f"Unknown expected heading '{expected_text}' — add to heading_map."
            )

        self.assert_visible_and_text(locator, expected_text, expected_text)
