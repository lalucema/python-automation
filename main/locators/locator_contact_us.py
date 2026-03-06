from playwright.sync_api import Page

class ContactUsPageLocators:
    def __init__(self, page: Page):
        self.page = page

        self.navigation_contact_us = page.get_by_role("link", name="Contact Us")
        self.heading_contact_us = page.get_by_role("heading", name="CONTACT US")

        # self.subject_field = page.get_by_text("Subject")
        # self.name_input = page.get_by_role("textbox", name="Name")
        # self.email_input = page.get_by_role("textbox", name="Email Address")
        # self.contact_number_input = page.get_by_role("textbox", name="Contact Number")
        # self.company_input = page.get_by_role("textbox", name="Company")
        # self.job_title_input = page.get_by_role("textbox", name="Job Title")
        # self.inquiry_type_dropdown = page.get_by_label("Type of Inquiry -- Type of")
        # self.subject_input = page.get_by_role("textbox", name="Subject")
        # self.message_input = page.get_by_role("textbox", name="Message")
        
