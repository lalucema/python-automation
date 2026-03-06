from playwright.sync_api import Page

class CareersPageLocators:

    def __init__(self, page: Page):
        self.page = page

        self.navigation_careers = page.get_by_role("link", name="Careers")
        self.heading_careers = page.get_by_text("Fast forward to your future")
    