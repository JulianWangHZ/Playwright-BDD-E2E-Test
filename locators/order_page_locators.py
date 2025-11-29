from playwright.sync_api import Page, Locator


class OrderPageLocators:
    def __init__(self, page: Page):
        self.RESTAURANT_HEADING = page.locator('[data-cy="branch-name-order-page"]')
        self.DELIVERY_PROMPT = page.locator('[data-testid="GeneralIndicator"]')
        self.BRANCH_ADDRESS = page.locator('[data-cy="branch-address-order-page"]')
        self.MENU_NAVIGATION = page.locator('#category-navbar')
        self.SERVICE_SWITCHER = page.locator('[data-cy="online-order-switch"]')
        self.DELIVERY_SWITCHER_BUTTON = page.locator('[data-cy="bt-delivery"]')
        self.TAKEOUT_SWITCHER_BUTTON = page.locator('[data-cy="bt-takeout"]')
        self.ADDRESS_PICKER_TRIGGER = page.locator('[data-cy="go-to-address-and-date-picker"]')
        self.ADDRESS_PICKER_MODAL = page.locator('[class*="AddressTimePicker__Picker"]')
        self.ADDRESS_CLEAR_BUTTON = page.locator('[data-cy="address-clear-button"]')
        self.ADDRESS_SEARCH_INPUT = page.locator('input[placeholder="Please ONLY enter the street address."]')
        self.ADDRESS_SUGGESTION_ITEMS = page.locator('[class*="AddressTimePicker__AddressPickerBlock"] li.cursor-pointer')
        self.ADDRESS_CONFIRM_BUTTON = page.locator('[data-cy="bt-confirm-date-address"]')
        self.DELIVERY_ADDRESS_TEXT = page.locator('[data-cy="delivery-address-order-page"]')
        self.ADDRESS_EDIT_TEXT = page.locator('[data-testid="GeneralIndicator"] span[data-i18n-key="takeoutOrderPage.edit"]')
