from playwright.sync_api import Page

class ServicesPageLocators:

    def __init__(self, page: Page):
        self.page = page

        self.navigation_services = page.locator("#top-menu").get_by_text("Services", exact=True)

        self.navigation_software_services = page.get_by_role("link", name="Software Services")
        self.navigation_quality_assurance = page.get_by_role("link", name="Quality Assurance")
        self.navigation_cloud = page.get_by_role("link", name="Cloud", exact=True)
        self.navigation_data = page.get_by_role("link", name="Data")
        self.navigation_artificial_intelligence = page.get_by_role("link", name="Artificial Intelligence")

        self.heading_software_services = page.get_by_role("heading", name="Elevate your software")
        self.heading_quality_assurance = page.get_by_role("heading", name="Race your Journey to the")
        self.heading_cloud = page.get_by_role("heading", name="Accelerate your Journey to")
        self.heading_data = page.get_by_role("heading", name="Discover new data frontiers")
        self.heading_artificial_intelligence = page.get_by_role("heading", name="Innovate with AI-powered")
       