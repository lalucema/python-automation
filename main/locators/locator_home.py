from playwright.sync_api import Page

class HomePageLocators:

    def __init__(self, page: Page):
        self.page = page

        self.button_accept_all = page.get_by_role("button", name="Accept All")
     
        self.heading_fast_forward_to_the_future = page.get_by_role("heading", name="Fast forward to the future")
       

