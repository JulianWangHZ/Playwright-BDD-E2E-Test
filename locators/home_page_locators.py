from playwright.sync_api import Page, Locator


class HomePageLocators:
    def __init__(self, page: Page):
        # Example locators - update based on actual page structure
        self.SERVICES_LINK = page.get_by_role("link", name="SERVICES")
        self.HEADER_LOGO = page.locator('[data-testid="header-logo"]')
        