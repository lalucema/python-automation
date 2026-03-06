from playwright.sync_api import Page

class InsightsPageLocators:

    def __init__(self, page: Page):
        self.page = page

        self.navigation_insights = page.locator("#top-menu").get_by_text("Insights")

        self.navigation_blogs = page.get_by_role("link", name="Blogs")
        self.navigation_e_books = page.get_by_role("link", name="E-books")
        self.navigation_media = page.get_by_role("link", name="Media")
        self.navigation_webinars = page.get_by_role("link", name="Webinars")

        self.heading_blogs = page.get_by_role("heading", name="BLOGS")
        self.heading_e_books = page.get_by_role("heading", name="E-BOOKS")
        self.heading_media = page.get_by_role("heading", name="MEDIA")
        self.heading_webinars = page.get_by_role("heading", name="WEBINARS")
