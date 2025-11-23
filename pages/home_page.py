from playwright.sync_api import Page
from pages.base_actions.base_action import BaseAction
from locators.home_page_locators import HomePageLocators


class HomePage(BaseAction):
    def __init__(self, page: Page):
        super().__init__(page)
        self.home_locators = HomePageLocators(page)
    
    def open(self):
        self.open_url()
        self.wait_for_page_loaded()
    
    def click_services(self):
        self.click_element(self.home_locators.SERVICES_LINK)
    
 