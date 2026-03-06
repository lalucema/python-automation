from playwright.sync_api import Page

class PartnersPageLocators:

    def __init__(self, page: Page):
        self.page = page

        self.navigation_partners = page.locator("#top-menu").get_by_text("Partners")
        self.navigation_aws = page.locator("#top-menu").get_by_text("AWS", exact=True)

        self.navigation_aws_data = page.get_by_role("link", name="AWS Data")
        self.navigation_aws_cloud_msp = page.get_by_role("link", name="AWS Cloud MSP")
        self.navigation_confluent = page.get_by_role("link", name="Confluent")
        self.navigation_mongodb =  page.get_by_role("link", name="MongoDB")
        self.navigation_n0ps = page.get_by_role("link", name="nOps")
        self.navigation_OutSystems = page.get_by_role("link", name="OutSystems")

        self.heading_aws_data = page.get_by_role("heading", name="Be a data hero Not a zero!")
        self.heading_aws_cloud_msp = page.get_by_role("heading", name="Cloud Managed Services")
        self.heading_confluent = page.get_by_role("heading", name="Unlock the power of data")
        self.heading_mongodb = page.get_by_role("heading", name="Liberate your data")
        self.heading_n0ps = page.get_by_role("heading", name="Reduce cloud costs by up to")
        self.heading_OutSystems = page.get_by_role("heading", name="Innovate fast with low-code")

    