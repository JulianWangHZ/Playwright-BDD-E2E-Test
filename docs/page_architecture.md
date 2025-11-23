# TransGlobal Page Object Model Architecture Design

## 📁 Directory Structure

```
pages/
├── base_actions/
│   ├── base_action.py          # Base action class (Playwright-based)
│   └── base_utils.py            # Utility class
│
├── components/                  # Components directory (for future use)
│   └── __init__.py
│
└── home_page.py                # Home page

locators/
└── home_page_locators.py       # Home page locators
```

## 🔗 Inheritance Relationship Diagram

```
BaseAction (Base action class - Playwright-based)
    │
    └── HomePage (Home page)
```

## 📋 Locators Structure

```
locators/
└── home_page_locators.py       # Home page locators
```

## 🎯 Usage Examples

### 1. Locator Definition (Using Playwright Locator Objects)

```python
# locators/home_page_locators.py
from playwright.sync_api import Page, Locator

class HomePageLocators:
    """Playwright locators using Locator objects - stored in separate file."""
    
    def __init__(self, page: Page):
        # Use Playwright's semantic locators when possible
        # Use UPPERCASE for locator property names
        self.SERVICES_LINK = page.get_by_role("link", name="SERVICES")
        self.HEADER_LOGO = page.locator('[data-testid="header-logo"]')
        self.SERVICES_MENU = page.get_by_test_id('services-menu')
        self.CONTACT_BUTTON = page.locator('[data-testid="contact-button"]')
        
        # CSS selectors when semantic locators aren't available
        self.RESTAURANT_HEADING = page.locator('[data-testid="restaurant-heading"]')
```

### 2. Page Object Usage (Direct inheritance from BaseAction)

```python
# pages/home_page.py
from playwright.sync_api import Page
from pages.base_actions.base_action import BaseAction
from locators.home_page_locators import HomePageLocators

class HomePage(BaseAction):
    def __init__(self, page: Page):
        super().__init__(page)
        # Initialize locators with page instance - use page-specific name for better readability
        self.home_locators = HomePageLocators(page)
    
    def open(self):
        self.open_url()
        self.wait_for_page_loaded()
    
    def click_services(self):
        # Use locators instance - locator properties are in UPPERCASE
        self.click_element(self.home_locators.SERVICES_LINK)
    
    def get_header_logo_text(self):
        return self.get_element_text(self.home_locators.HEADER_LOGO)
```

## 🔄 Component Interaction Flow

```
Test Step
    ↓
Page Object (HomePage)
    ↓
BaseAction (base action methods - Playwright-based)
    ↓
Playwright API
```

## 📊 Key Design Principles

### 1. **Playwright Locator Objects**
- All locators are Playwright `Locator` objects, not strings
- Locators stored in separate `locators/` classes
- Locator properties use **UPPERCASE** naming (e.g., `self.SERVICES_LINK`)
- Page Object variables use **lowercase** naming (e.g., `self.home_locators`)

### 2. **Direct Inheritance from BaseAction**
- All Page Objects directly inherit from `BaseAction`
- No intermediate `BasePage` class (removed for simplicity)
- `wait_for_page_loaded()` is available in `BaseAction`

### 3. **Locator Organization**
- Locators stored in `locators/` folder, separate from Page Objects
- Each page has its own locator class
- Locator classes initialize with `page` instance in `__init__`
- Locator properties defined in **UPPERCASE** for clarity

### 4. **Naming Convention**
- **Locator properties**: UPPERCASE (e.g., `self.SERVICES_LINK`, `self.CHECKOUT_BUTTON`)
- **Page Object locator variables**: lowercase with page prefix (e.g., `self.home_locators`, `self.order_locators`)
- **Usage**: `self.{page}_locators.ELEMENT_NAME` (e.g., `self.home_locators.SERVICES_LINK`)

## 💡 Design Decision Explanation

### Why Direct Inheritance from BaseAction?

- **Simplicity**: Removes unnecessary abstraction layer
- **Playwright Native**: Direct access to Playwright features
- **Flexibility**: Each page can implement its own `wait_for_page_loaded()` logic if needed
- **Maintainability**: Less inheritance hierarchy means easier to understand and maintain

### Why Separate Locator Classes?

- **Organization**: Centralized locator management
- **Reusability**: Locators can be shared across multiple Page Objects if needed
- **Maintainability**: Update locators in one place
- **Type Safety**: Full Playwright Locator type support with IDE autocomplete

### Why UPPERCASE for Locator Properties?

- **Clarity**: Distinguishes locators from regular instance variables
- **Consistency**: Follows constant naming convention
- **Readability**: `self.home_locators.SERVICES_LINK` is more readable than `self.home_locators.services_link`
- **Industry Standard**: Common practice in test automation frameworks

## 🚀 Playwright-Specific Features

### Auto-Waiting
- Playwright automatically waits for elements to be actionable
- No need for explicit waits in most cases
- Methods like `click()`, `fill()`, `inner_text()` auto-wait

### Locator Methods
- `page.get_by_role()` - Semantic locators (preferred)
- `page.get_by_test_id()` - For `data-testid` attributes
- `page.get_by_text()` - Text-based locators
- `page.get_by_label()` - Form label locators
- `page.locator()` - CSS/XPath selectors (when needed)

### Type Safety
- Full type support with Playwright Locator objects
- IDE autocomplete and type checking
- Better error messages and debugging

## 🔮 Future Extensibility

As the project grows, you can add:

- **Components**: Add reusable components in `pages/components/` (e.g., Header, Footer)
- **More Pages**: Add new page objects following the same pattern
- **Service Modules**: Organize related pages in subdirectories (e.g., `pages/services/`)
- **Shared Locators**: Create common locator classes for shared elements

### Example: Adding a New Page

```python
# locators/contact_us_locators.py
from playwright.sync_api import Page

class ContactUsLocators:
    def __init__(self, page: Page):
        self.FIRST_NAME = page.get_by_label('First Name')
        self.SUBMIT_BUTTON = page.get_by_role('button', name='Submit')

# pages/contact_us_page.py
from playwright.sync_api import Page
from pages.base_actions.base_action import BaseAction
from locators.contact_us_locators import ContactUsLocators

class ContactUsPage(BaseAction):
    def __init__(self, page: Page):
        super().__init__(page)
        self.contact_locators = ContactUsLocators(page)
    
    def fill_form(self, first_name: str):
        self.send_keys_to_element(self.contact_locators.FIRST_NAME, first_name)
    
    def submit(self):
        self.click_element(self.contact_locators.SUBMIT_BUTTON)
```
