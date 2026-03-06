# main/base/base_page.py
from playwright.sync_api import Page, Locator, expect
from main.utility.logger import logger

class BasePage:
    """
    Base class for all Page Objects. 
    Contains wrapper methods for common Playwright actions with logging and synchronization.
    """

    def __init__(self, page: Page):
        self.page = page
        # Standard default timeout for actions (in ms). 
        # 15000ms (15s) is safer for CI environments than 5000ms.
        self.DEFAULT_TIMEOUT = 15000 

    # ---------------------------------------------------------
    # NAVIGATION
    # ---------------------------------------------------------
    def open(self, url: str):
        """Navigate to a URL"""
        logger.info(f"Open | {url}")
        self.page.goto(url)

    def assert_url(self, expected_url: str):
        """Validate the current URL matches expected"""
        logger.info(f"Assert URL | Should be: {expected_url}")
        expect(self.page).to_have_url(expected_url, timeout=self.DEFAULT_TIMEOUT)

    # def reload(self):
    #     logger.info("Reload Page")
    #     self.page.reload()

    # ---------------------------------------------------------
    # INTERACTIONS (Click, Fill, Hover)
    # ---------------------------------------------------------
    def click(self, locator: Locator, name: str, timeout: int = None):
        """
        Wait for element to be visible and enabled, then click.
        """
        timeout = timeout or self.DEFAULT_TIMEOUT
        logger.info(f"Click | {name}")
        try:
            # wait_for is implicit in click(), but calling it explicitly 
            # helps separate 'element not found' from 'element not clickable' errors
            locator.wait_for(state="visible", timeout=timeout)
            locator.click(timeout=timeout)
        except Exception as e:
            logger.error(f"Failed to click '{name}'")
            raise e

    def hover(self, locator: Locator, name: str, timeout: int = None):
        """
        Hover over an element (Essential for dropdown menus).
        """
        timeout = timeout or self.DEFAULT_TIMEOUT
        logger.info(f"Hover | {name}")
        try:
            locator.wait_for(state="visible", timeout=timeout)
            locator.hover(timeout=timeout)
        except Exception as e:
            logger.error(f"Failed to hover over '{name}'")
            raise e

    def fill(self, locator: Locator, value: str, name: str, timeout: int = None):
        """Fill a form field"""
        timeout = timeout or self.DEFAULT_TIMEOUT
        logger.info(f"Fill | {name} = '{value}'")
        try:
            locator.wait_for(state="visible", timeout=timeout)
            locator.fill(value, timeout=timeout)
        except Exception as e:
            logger.error(f"Failed to fill '{name}'")
            raise e

    def select_option(self, locator: Locator, name: str, value: str = None, label: str = None, index: int = None, timeout: int = None):
        """Select an option from a dropdown"""
        timeout = timeout or self.DEFAULT_TIMEOUT
        logger.info(f"Select | {name} (Value: {value}, Label: {label}, Index: {index})")
        
        try:
            locator.wait_for(state="visible", timeout=timeout)
            if value:
                locator.select_option(value=value, timeout=timeout)
            elif label:
                locator.select_option(label=label, timeout=timeout)
            elif index is not None:
                locator.select_option(index=index, timeout=timeout)
            else:
                raise ValueError("Must provide 'value', 'label', or 'index'.")
        except Exception as e:
            logger.error(f"Failed to select option for '{name}'")
            raise e

    def scroll_to(self, locator: Locator, name: str):
        """Scroll element into view"""
        logger.info(f"Scroll | {name}")
        locator.scroll_into_view_if_needed()

    # ---------------------------------------------------------
    # ASSERTIONS & WAITS
    # ---------------------------------------------------------
    def assert_visible(self, locator: Locator, name: str, timeout: int = None):
        timeout = timeout or self.DEFAULT_TIMEOUT
        logger.info(f"Assert | '{name}' is visible")
        expect(locator).to_be_visible(timeout=timeout)

    def assert_text(self, locator: Locator, expected: str, name: str, exact: bool = False, timeout: int = None):
        """
        Assert element contains specific text.
        Use exact=True for strict matching.
        """
        timeout = timeout or self.DEFAULT_TIMEOUT
        match_type = "exactly" if exact else "contains"
        logger.info(f"Assert | '{name}' text {match_type} '{expected}'")
        
        if exact:
            expect(locator).to_have_text(expected, timeout=timeout)
        else:
            expect(locator).to_contain_text(expected, timeout=timeout)

    def assert_visible_and_text(self, locator: Locator, expected: str, name: str, timeout: int = None):
        """Combined check: Is it there? Does it say the right thing?"""
        self.assert_visible(locator, name, timeout)
        self.assert_text(locator, expected, name, timeout=timeout)

    def wait_for_element(self, locator: Locator, state="visible", timeout: int = None):
        """Generic wait wrapper"""
        timeout = timeout or self.DEFAULT_TIMEOUT
        logger.info(f"Wait | For element state '{state}'")
        locator.wait_for(state=state, timeout=timeout)