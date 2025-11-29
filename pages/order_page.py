from playwright.sync_api import Page, TimeoutError as PlaywrightTimeoutError

from pages.base_actions.base_action import BaseAction
from locators.order_page_locators import OrderPageLocators
from url import BASE_URL


class OrderPage(BaseAction):
    def __init__(self, page: Page):
        super().__init__(page)
        self.order_locators = OrderPageLocators(page)
    
    def open(self):
        self.open_url(url=BASE_URL)
        self.wait_for_page_loaded()
    
    def wait_for_page_loaded(self):
        self.wait_for_element_visible(self.order_locators.RESTAURANT_HEADING)
        self.wait_for_element_visible(self.order_locators.DELIVERY_PROMPT)
        self.wait_for_element_visible(self.order_locators.MENU_NAVIGATION)
    
    def get_restaurant_name(self) -> str:
        return self.get_element_text(self.order_locators.RESTAURANT_HEADING)
    
    def is_delivery_prompt_visible(self) -> bool:
        return self.is_element_visible(self.order_locators.DELIVERY_PROMPT)
    
    def is_menu_navigation_visible(self) -> bool:
        return self.is_element_visible(self.order_locators.MENU_NAVIGATION)
    
    def get_branch_address_text(self) -> str:
        return self.get_element_text(self.order_locators.BRANCH_ADDRESS)
    
    def get_delivery_prompt_text(self) -> str:
        return self.get_element_text(self.order_locators.DELIVERY_PROMPT)
    
    def is_delivery_prompt_message_visible(self) -> bool:
        try:
            self.wait_for_element_text_contains(
                self.order_locators.DELIVERY_PROMPT,
                expected_text="Please enter your delivery address.",
                timeout=5,
            )
            return True
        except (AssertionError, PlaywrightTimeoutError):
            return False
    
    def is_delivery_prompt_message_hidden(self) -> bool:
        try:
            self.wait_for_element_text_not_contains(
                self.order_locators.DELIVERY_PROMPT,
                unexpected_text="Please enter your delivery address.",
                timeout=5,
            )
            return True
        except (AssertionError, PlaywrightTimeoutError):
            return False
    
    def is_switcher_button_visible(self) -> bool:
        return self.is_element_visible(self.order_locators.SERVICE_SWITCHER)
    
    def are_switcher_options_visible(self) -> bool:
        return (
            self.is_element_visible(self.order_locators.DELIVERY_SWITCHER_BUTTON)
            and self.is_element_visible(self.order_locators.TAKEOUT_SWITCHER_BUTTON)
        )
    
    def select_service_type(self, option: str):
        normalized_option = option.strip().lower()
        if normalized_option == "delivery":
            self.click_element(self.order_locators.DELIVERY_SWITCHER_BUTTON)
            self.wait_for_element_text_contains(
                self.order_locators.DELIVERY_PROMPT,
                expected_text="Please enter your delivery address.",
            )
        elif normalized_option == "takeout":
            self.click_element(self.order_locators.TAKEOUT_SWITCHER_BUTTON)
            self.wait_for_element_text_not_contains(
                self.order_locators.DELIVERY_PROMPT,
                unexpected_text="Please enter your delivery address.",
            )
        else:
            raise ValueError(f"Unsupported service type: {option}")
    
    def is_delivery_option_selected(self) -> bool:
        try:
            element = self.order_locators.DELIVERY_SWITCHER_BUTTON
            classes = element.get_attribute("class") or ""
            return "border-orange" in classes or "shadow-xl" in classes
        except Exception:
            return False
    
    def open_address_picker(self):
        self.wait_for_element_clickable(self.order_locators.ADDRESS_PICKER_TRIGGER)
        self.click_element(self.order_locators.ADDRESS_PICKER_TRIGGER)
        self.wait_for_element_visible(self.order_locators.ADDRESS_PICKER_MODAL)
    
    def input_postal_code(self, postal_code: str):
        self.wait_for_element_visible(self.order_locators.ADDRESS_SEARCH_INPUT)
        self.send_keys_to_element(self.order_locators.ADDRESS_SEARCH_INPUT, postal_code)
    
    def wait_for_postal_code_results(self):
        self.wait_for_element_visible(self.order_locators.ADDRESS_SUGGESTION_ITEMS)
    
    def select_first_address_suggestion(self):
        suggestions = self.order_locators.ADDRESS_SUGGESTION_ITEMS
        count = suggestions.count()
        if count == 0:
            raise AssertionError("No address suggestions are available to select.")
        suggestions.first.click()
    
    def get_first_address_suggestion_text(self):
        suggestions = self.order_locators.ADDRESS_SUGGESTION_ITEMS
        count = suggestions.count()
        if count == 0:
            raise AssertionError("No address suggestions are available to read.")
        return suggestions.first.inner_text().strip()
    
    def confirm_selected_address(self):
        self.wait_for_element_clickable(self.order_locators.ADDRESS_CONFIRM_BUTTON)
        self.click_element(self.order_locators.ADDRESS_CONFIRM_BUTTON)
        self.wait_for_element_disappears(self.order_locators.ADDRESS_PICKER_MODAL)
    
    def get_current_delivery_address(self):
        return self.get_element_text(self.order_locators.DELIVERY_ADDRESS_TEXT)
    
    def is_address_edit_option_visible(self):
        return self.is_element_visible(self.order_locators.ADDRESS_EDIT_TEXT)
