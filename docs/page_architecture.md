# TransGlobal Page Object Model Architecture Design

## 📁 Directory Structure

```
pages/
├── base_actions/
│   ├── base_action.py          # Base action class (existing)
│   └── base_utils.py            # Utility class (existing)
│
├── components/                  # Base component layer (shared across pages)
│   ├── __init__.py
│   ├── header.py               # Header navigation component
│   ├── footer.py               # Footer component
│   ├── navigation.py           # Navigation menu component
│   ├── chat_widget.py          # Chat widget component
│   └── social_links.py         # Social media links component
│
├── base_page.py                # Base page class (includes Header/Footer)
│
├── home_page.py                # Home page
├── contact_us_page.py          # Contact Us page
│
├── services/                   # Services module
│   ├── __init__.py
│   ├── services_base_page.py  # Services base page
│   ├── real_estate_page.py     # Real estate service page
│   ├── lending_page.py         # Lending service page
│   ├── insurance_page.py       # Insurance service page
│   ├── investment_page.py      # Investment service page
│   └── tax_services_page.py    # Tax services page
│
├── events/                     # Events module
│   ├── __init__.py
│   ├── events_base_page.py     # Events base page
│   ├── webinar_page.py         # Webinar page
│   └── seminars_page.py         # Seminar series page
│
├── media/                      # Media module
│   ├── __init__.py
│   ├── media_page.py           # Media center page
│   └── transglobal_tv_page.py  # TransGlobal TV page
│
├── news/                       # News module
│   ├── __init__.py
│   ├── news_page.py            # News list page
│   └── news_detail_page.py      # News detail page
│
└── about_us/                   # About Us module
    ├── __init__.py
    ├── about_us_page.py        # About Us page
    ├── our_story_page.py       # Our Story page
    ├── our_staff_page.py       # Our Staff page
    └── locations_page.py       # Office locations page
```

## 🔗 Inheritance Relationship Diagram

```
BaseAction (Base action class)
    │
    ├── BaseComponent (Base component class)
    │       │
    │       ├── Header (Header navigation)
    │       ├── Footer (Footer)
    │       ├── Navigation (Navigation menu)
    │       ├── ChatWidget (Chat widget)
    │       └── SocialLinks (Social media links)
    │
    └── BasePage (Base page class)
            │
            ├── HomePage (Home page)
            ├── ContactUsPage (Contact Us page)
            │
            ├── ServicesBasePage (Services base page)
            │       │
            │       ├── RealEstatePage (Real estate service)
            │       ├── LendingPage (Lending service)
            │       ├── InsurancePage (Insurance service)
            │       ├── InvestmentPage (Investment service)
            │       └── TaxServicesPage (Tax services)
            │
            ├── EventsBasePage (Events base page)
            │       │
            │       ├── WebinarPage (Webinar)
            │       └── SeminarsPage (Seminar series)
            │
            ├── MediaPage (Media center)
            ├── TransGlobalTVPage (TransGlobal TV)
            │
            ├── NewsPage (News list)
            ├── NewsDetailPage (News detail)
            │
            └── AboutUsBasePage (About Us base page)
                    │
                    ├── OurStoryPage (Our Story)
                    ├── OurStaffPage (Our Staff)
                    └── LocationsPage (Office locations)
```

## 🧩 Component Composition Relationship

```
┌─────────────────────────────────────────────────────────┐
│                    BasePage                              │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐              │
│  │  Header  │  │ Navigation│ │  Footer  │              │
│  └──────────┘  └──────────┘  └──────────┘              │
│                                                          │
│  ┌──────────────────────────────────────────────────┐  │
│  │         Page Specific Content                     │  │
│  │  (e.g., ContactUsPage contains form logic)        │  │
│  └──────────────────────────────────────────────────┘  │
│                                                          │
│  ┌──────────┐  ┌──────────┐                           │
│  │  Chat    │  │  Social  │                           │
│  │  Widget  │  │  Links   │                           │
│  └──────────┘  └──────────┘                           │
└─────────────────────────────────────────────────────────┘
```

## 📋 Locators Corresponding Structure

```
locators/
├── components/
│   ├── header_locators.py
│   ├── footer_locators.py
│   ├── navigation_locators.py
│   ├── chat_widget_locators.py
│   └── social_links_locators.py
│
├── home_page_locators.py
├── contact_us_locators.py
│
├── services/
│   ├── real_estate_locators.py
│   ├── lending_locators.py
│   ├── insurance_locators.py
│   ├── investment_locators.py
│   └── tax_services_locators.py
│
├── events/
│   ├── events_locators.py
│   ├── webinar_locators.py
│   └── seminars_locators.py
│
├── media/
│   ├── media_locators.py
│   └── transglobal_tv_locators.py
│
├── news/
│   ├── news_locators.py
│   └── news_detail_locators.py
│
└── about_us/
    ├── about_us_locators.py
    ├── our_story_locators.py
    ├── our_staff_locators.py
    └── locations_locators.py
```

## 🎯 Usage Examples

### 1. Base Component Usage

```python
# pages/components/header.py
from pages.base_actions.base_action import BaseAction
from locators.components.header_locators import HeaderLocators

class Header(BaseAction):
    def click_logo(self):
        self.click_element(HeaderLocators.LOGO)
    
    def get_navigation_menu(self):
        return Navigation(self.page)
```

### 2. Base Page Usage

```python
# pages/base_page.py
from pages.base_actions.base_action import BaseAction
from pages.components.header import Header
from pages.components.footer import Footer

class BasePage(BaseAction):
    def __init__(self, page):
        super().__init__(page)
        self.header = Header(page)
        self.footer = Footer(page)
    
    def wait_for_page_loaded(self):
        self.header.wait_for_loaded()
        self.footer.wait_for_loaded()
```

### 3. Specific Page Usage

```python
# pages/home_page.py
from pages.base_page import BasePage
from locators.home_page_locators import HomePageLocators

class HomePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
    
    def open(self):
        self.open_url()
        self.wait_for_page_loaded()
    
    def get_services_section_title(self):
        return self.get_element_text(HomePageLocators.SERVICES_SECTION_TITLE)
```

### 4. Contact Us Page Usage (Form logic directly in the page)

```python
# pages/contact_us_page.py
from pages.base_page import BasePage
from locators.contact_us_locators import ContactUsLocators

class ContactUsPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
    
    def fill_contact_form(self, form_data: dict):
        """Fill contact form - form logic directly in the page"""
        self.send_keys_to_element(ContactUsLocators.FIRST_NAME, form_data.get('first_name'))
        self.send_keys_to_element(ContactUsLocators.LAST_NAME, form_data.get('last_name'))
        self.send_keys_to_element(ContactUsLocators.EMAIL, form_data.get('email'))
        # ... other form fields
    
    def submit_form(self):
        """Submit the form"""
        self.click_element(ContactUsLocators.SUBMIT_BUTTON)
```

### 5. Service Page Usage

```python
# pages/services/real_estate_page.py
from pages.services.services_base_page import ServicesBasePage
from locators.services.real_estate_locators import RealEstateLocators

class RealEstatePage(ServicesBasePage):
    def __init__(self, page):
        super().__init__(page)
    
    def wait_for_loaded(self):
        super().wait_for_loaded()
        self.wait_for_element_visible(RealEstateLocators.PAGE_TITLE)
```

## 🔄 Component Interaction Flow

```
Test Step
    ↓
Page Object (HomePage, ContactUsPage, etc.)
    ↓
BasePage (provides Header/Footer functionality)
    ↓
Components (Header, Footer, Navigation, etc.)
    ↓
BaseAction (base action methods)
    ↓
Playwright API
```

## 📊 Modularization Advantages

1. **Component Reusability**: Header, Footer, Navigation are shared across all pages
2. **Easy Maintenance**: Modifying components only requires updating one place
3. **Clear Structure**: Organized by business modules, easy to find
4. **Strong Extensibility**: Adding new pages only requires inheriting the corresponding base class
5. **Test-Friendly**: Components can be tested independently

## 💡 Design Decision Explanation

### Why is Contact Form not a Component?

- **Single Use Case**: Contact Form is only used on the Contact Us page, with no cross-page reuse requirements
- **Avoid Over-Engineering**: If other pages need similar forms in the future, consider extracting as a component then
- **Simplify Architecture**: Form logic directly written in `ContactUsPage` is more intuitive and easier to maintain
- **Follow YAGNI Principle**: "You Aren't Gonna Need It" - don't design features you don't need yet

### When Should a Form be Extracted as a Component?

- When the form appears on multiple pages (e.g., multiple service pages have contact forms)
- When the form logic is very complex and needs independent testing
- When the form needs to be called as an independent module by other systems
