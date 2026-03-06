from playwright.sync_api import Page

class PortfolioPageLocators:

    def __init__(self, page: Page):
        self.page = page

        self.navigation_portfolio = page.get_by_role("link", name="Portfolio", exact=True)
        self.heading_portfolio = page.get_by_role("heading", name="PORTFOLIO")