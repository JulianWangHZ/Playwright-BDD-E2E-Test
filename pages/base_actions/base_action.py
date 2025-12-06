import time
from typing import Union

from playwright.sync_api import Page, TimeoutError as PlaywrightTimeoutError, Locator
from config.config import Config
from pages.base_actions.base_utils import BaseUtils


class BaseAction:
    def __init__(self, page: Page):
        self.page = page
        self.config = Config()
        self.utils = BaseUtils()
        
    def wait_for_page_loaded(self):
        # Wait for DOM to be ready first
        self.page.wait_for_load_state('domcontentloaded')
        # Then wait for load, but don't wait for networkidle as it can cause timeouts
        self.page.wait_for_load_state('load')

    def _resolve_locator(self, locator: Union[Locator, str]) -> Locator:
        """
        Resolve locator to Playwright Locator object.
        
        **Preferred**: Pass Playwright Locator objects directly.
        String format (CSS selector) is supported for backward compatibility only.
        
        Args:
            locator: Playwright Locator object (preferred) or CSS selector string
            
        Returns:
            Playwright Locator object
        """
        if isinstance(locator, Locator):
            return locator
        if isinstance(locator, str):
            return self.page.locator(locator)
        raise TypeError(f"Unsupported locator type: {type(locator)}. Expected Locator or str.")


    def open_url(self, url=None, path=None):
        """
        Opens the specified URL in the browser.
        
        Args:
            url: Full URL to open. If None, uses BASE_URL from config
            path: Path to append to BASE_URL, e.g. 'login' or 'products'
        """
        if url:
            target_url = url
        else:
            target_url = self.config.get_page_url(path or '')
            
        # Use 'domcontentloaded' instead of 'networkidle' to avoid hanging on dynamic sites
        # 'networkidle' can wait indefinitely for sites
        self.page.goto(target_url, wait_until='domcontentloaded', timeout=self.config.DEFAULT_TIMEOUT * 1000)

    def find_element(self, locator: Union[Locator, str]):
        resolved_locator = self._resolve_locator(locator)
        resolved_locator.wait_for(state='attached', timeout=self.config.DEFAULT_TIMEOUT * 1000)
        return resolved_locator

    def is_element_visible(self, locator: Union[Locator, str]):
        try:
            resolved_locator = self._resolve_locator(locator)
            resolved_locator.wait_for(state='visible', timeout=self.config.DEFAULT_TIMEOUT * 1000)
            return True
        except PlaywrightTimeoutError:
            return False

    def click_element(self, locator: Union[Locator, str]):
        """
        Note: Playwright's click() automatically waits for element to be actionable:
        - Attached to DOM
        - Visible
        - Stable (not animating)
        - Receives events (not covered)
        - Enabled
        """
        resolved_locator = self._resolve_locator(locator)
        resolved_locator.click(timeout=self.config.DEFAULT_TIMEOUT * 1000)

    def click_if_exists(self, locator: Union[Locator, str]):
        if self.is_element_visible(locator):
            self.click_element(locator)
            return True
        return False

    def send_keys_to_element(self, locator: Union[Locator, str], text: str):
        """
        Note: Playwright's input_value(), clear(), and fill() automatically wait for elements to be:
        - Visible (for input_value and fill)
        - Actionable (for clear and fill)
        """
        resolved_locator = self._resolve_locator(locator)
        
        # Get the current field value (auto-waits for element to be visible)
        current_value = resolved_locator.input_value()
        
        # Only clear the field if it has a value
        if current_value:
            resolved_locator.clear()
            
            # After clearing, verify that the field has been cleared
            max_attempts = 5
            attempts = 0
            while attempts < max_attempts:
                cleared_value = resolved_locator.input_value()
                if not cleared_value or cleared_value.strip() == '':
                    break  # Successfully cleared, the field is empty
                
                # Try to clear again
                resolved_locator.clear()
                attempts += 1
                
            if attempts == max_attempts:
                # If the field cannot be cleared after multiple attempts, record a warning and continue
                print(f"Warning: Unable to clear field, current value: {resolved_locator.input_value()}")
        
        # Ensure the input is a string type and fill the field
        text = str(text)
        resolved_locator.fill(text)

    def get_element_text(self, locator: Union[Locator, str]):
        """
        Note: Playwright's inner_text() automatically waits for element to be visible.
        """
        resolved_locator = self._resolve_locator(locator)
        return resolved_locator.inner_text()

    def wait_for_element_visible(self, locator: Union[Locator, str]):
        try:
            resolved_locator = self._resolve_locator(locator)
            resolved_locator.wait_for(state='visible', timeout=self.config.DEFAULT_TIMEOUT * 1000)
        except PlaywrightTimeoutError:
            raise PlaywrightTimeoutError(f"Element not found or not visible: {locator}")

    def wait_for_element_clickable(self, locator: Union[Locator, str], timeout=10):
        try:
            resolved_locator = self._resolve_locator(locator)
            resolved_locator.wait_for(state='visible', timeout=timeout * 1000)
            # Check if element is enabled (not disabled)
            is_disabled = resolved_locator.get_attribute('disabled')
            if is_disabled is not None:
                return False
            return True
        except PlaywrightTimeoutError:
            return False

    def wait_for_element_not_clickable(self, locator: Union[Locator, str], timeout=5):
        try:
            resolved_locator = self._resolve_locator(locator)
            # Wait for element to be disabled or hidden
            resolved_locator.wait_for(state='hidden', timeout=timeout * 1000)
            return True
        except PlaywrightTimeoutError:
            # Check if element is disabled
            try:
                resolved_locator = self._resolve_locator(locator)
                is_disabled = resolved_locator.get_attribute('disabled')
                if is_disabled is not None:
                    return True
            except Exception:
                pass
            return False

    def is_element_clickable(self, locator: Union[Locator, str]):
        """
        Note: 
        - is_visible() returns immediately (no waiting)
        - get_attribute() waits for element to be attached to DOM (but not necessarily visible)
        """
        try:
            resolved_locator = self._resolve_locator(locator)
            # Check if visible and enabled
            if not resolved_locator.is_visible():
                return False
            is_disabled = resolved_locator.get_attribute('disabled')
            return is_disabled is None
        except Exception:
            return False

    def verify_element_not_clickable(self, locator: Union[Locator, str], timeout=10):
        # First check if element exists
        try:
            resolved_locator = self._resolve_locator(locator)
            resolved_locator.wait_for(state='attached', timeout=timeout * 1000)
        except PlaywrightTimeoutError:
            raise AssertionError(f"Element not found: {locator}")
        
        # Wait for element to become not clickable
        if not self.wait_for_element_not_clickable(locator, timeout):
            raise AssertionError(f"Element is still clickable in {timeout} seconds: {locator}")
        
        # Double check by verifying element is disabled or not clickable
        resolved_locator = self._resolve_locator(locator)
        is_disabled = resolved_locator.get_attribute('disabled')
        if is_disabled is None:
            # Element is enabled but might be covered, check if it's actually clickable
            if self.is_element_clickable(locator):
                raise AssertionError(f"Element exists but should not be clickable: {locator}")
        
        return True

    def wait_for_element_present(self, locator: Union[Locator, str], timeout=3):
        resolved_locator = self._resolve_locator(locator)
        resolved_locator.wait_for(state='attached', timeout=timeout * 1000)
        return True

    def verify_element_text(self, locator: Union[Locator, str], expected_text: str):
        actual_text = self.get_element_text(locator)
        return actual_text == expected_text

    def verify_element_visible(self, locator: Union[Locator, str]):
        return self.is_element_visible(locator)

    def verify_element_clickable(self, locator: Union[Locator, str], timeout=10):
        if not self.wait_for_element_clickable(locator, timeout):
            raise AssertionError(f"Element is not clickable in {timeout} seconds: {locator}")
        return True

    def scroll_to_element(self, locator: Union[Locator, str]):
        """
        Note: Playwright's scroll_into_view_if_needed() automatically waits for element to be attached to DOM.
        """
        resolved_locator = self._resolve_locator(locator)
        resolved_locator.scroll_into_view_if_needed()
        return resolved_locator

    def wait_for_element_disappears(self, locator: Union[Locator, str], timeout=10):
        try:
            resolved_locator = self._resolve_locator(locator)
            resolved_locator.wait_for(state='hidden', timeout=timeout * 1000)
            return True
        except PlaywrightTimeoutError:
            raise AssertionError(f"Element does not disappear in {timeout} seconds: {locator}")

    def wait_for_element_text_contains(self, locator: Union[Locator, str], expected_text: str, timeout=10):
        try:
            resolved_locator = self._resolve_locator(locator)
            resolved_locator.wait_for(state='visible', timeout=timeout * 1000)
            
            # Wait for text to appear
            end_time = timeout
            while end_time > 0:
                actual_text = resolved_locator.inner_text()
                if expected_text in actual_text:
                    return True
                self.page.wait_for_timeout(100)  # Wait 100ms
                end_time -= 0.1
            
            raise AssertionError(
                f"Element text does not contain the expected text: {expected_text} in {timeout} seconds. "
                f"Locator: {locator}"
            )
        except PlaywrightTimeoutError as exc:
            raise AssertionError(
                f"Element text does not contain the expected text: {expected_text} in {timeout} seconds. "
                f"Locator: {locator}"
            ) from exc

    def wait_for_element_text_not_contains(self, locator: Union[Locator, str], unexpected_text: str, timeout=10):
        try:
            resolved_locator = self._resolve_locator(locator)
            resolved_locator.wait_for(state='visible', timeout=timeout * 1000)
            
            # Wait for text to disappear
            end_time = timeout
            while end_time > 0:
                actual_text = resolved_locator.inner_text()
                if unexpected_text not in actual_text:
                    return True
                self.page.wait_for_timeout(100)  # Wait 100ms
                end_time -= 0.1
            
            raise AssertionError(
                f"Element text still contains the unexpected text: {unexpected_text} in {timeout} seconds. "
                f"Locator: {locator}"
            )
        except PlaywrightTimeoutError as exc:
            raise AssertionError(
                f"Element text still contains the unexpected text: {unexpected_text} in {timeout} seconds. "
                f"Locator: {locator}"
            ) from exc

    def refresh_page(self):
        # Use 'domcontentloaded' instead of 'networkidle' to avoid hanging on dynamic sites
        self.page.reload(wait_until='domcontentloaded', timeout=self.config.DEFAULT_TIMEOUT * 1000)

    def refresh_and_wait_for_element(self, locator: Union[Locator, str], timeout=10):
        # Use 'domcontentloaded' instead of 'networkidle' to avoid hanging on dynamic sites
        self.page.reload(wait_until='domcontentloaded', timeout=self.config.DEFAULT_TIMEOUT * 1000)
        resolved_locator = self._resolve_locator(locator)
        resolved_locator.wait_for(state='visible', timeout=timeout * 1000)

    def wait_for_element_has_value(self, locator: Union[Locator, str], timeout=10):
        # First ensure the element exists and is visible
        self.wait_for_element_visible(locator)
        
        # Get the locator
        resolved_locator = self._resolve_locator(locator)
        
        # Wait for element to have a value by polling
        end_time = time.time() + timeout
        while time.time() < end_time:
            try:
                current_value = resolved_locator.input_value()
                if current_value and current_value.strip():
                    return True
            except Exception:
                pass
            self.page.wait_for_timeout(100)  # Wait 100ms
        
        raise PlaywrightTimeoutError(f"Element in {timeout} seconds did not get a value: {locator}")

    def go_back(self, wait_until='domcontentloaded', timeout=None):
        if timeout is None:
            timeout = self.config.DEFAULT_TIMEOUT * 1000
        self.page.go_back(wait_until=wait_until, timeout=timeout)

    def go_forward(self, wait_until='domcontentloaded', timeout=None):
        if timeout is None:
            timeout = self.config.DEFAULT_TIMEOUT * 1000
        self.page.go_forward(wait_until=wait_until, timeout=timeout)
