from playwright.sync_api import Page

class AboutPageLocators:
    def __init__(self, page: Page):
        self.page = page

        self.navigation_about = page.get_by_role("link", name="About 3")
        self.heading_about = page.get_by_role("heading", name="About Us")
