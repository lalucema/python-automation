from playwright.sync_api import Page

class SolutionsPageLocators:

    def __init__(self, page: Page):
        self.page = page

        self.navigation_solutions = page.locator("#top-menu").get_by_text("Solutions")
        self.navigation_retails = page.get_by_role("link", name="Retail")
        self.heading_retails = page.get_by_role("heading", name="SELL SMART, SELL MORE")

    