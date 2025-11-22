# TransGlobal Web Automation Test Suite

> 🌐 This guide is also available in [繁體中文](README.zh-TW.md).

An enterprise-grade end-to-end testing framework engineered with **Playwright** and **pytest-bdd** to ensure quality and reliability of [TransGlobal](https://www.transglobalus.com/) web platform. Built on modern browser automation principles, this framework implements Page Object Model architecture with Behavior-Driven Development methodology, enabling maintainable, scalable, and robust test automation. The framework capitalizes on Playwright's intelligent auto-waiting mechanisms, eliminating flaky tests while providing seamless integration with Playwright MCP for accelerated test development and interactive debugging workflows.

---

## 📑 Table of Contents

1. [Overview](#-overview)
2. [Architecture](#-architecture)
3. [Tech Stack](#-tech-stack)
4. [Key Features](#-key-features)
5. [Quick Start](#-quick-start)
6. [Installation](#-installation)
7. [Running Tests](#-running-tests)
8. [Playwright MCP Integration](#-playwright-mcp-integration)
9. [Development Guide](#-development-guide)
10. [Best Practices](#-best-practices)
11. [Troubleshooting](#-troubleshooting)

---

## 🎯 Overview

This test automation framework is designed to ensure the quality and reliability of TransGlobal's web platform, covering critical user journeys across multiple services including Real Estate, Lending, Insurance, Investment, and Tax Services.

### Target Application
- **Website**: [https://www.transglobalus.com/](https://www.transglobalus.com/)
- **Focus Areas**: User interface validation, cross-browser compatibility, responsive design testing, and critical business flows

---

## 🏗️ Architecture

### Design Patterns
- **Page Object Model (POM)**: Encapsulates page-specific logic and locators
- **Behavior-Driven Development (BDD)**: Test scenarios written in Gherkin syntax
- **Fixture-based Test Structure**: Reusable test fixtures for common setup/teardown
- **Locator Management**: Centralized locator definitions in dedicated classes

### Project Structure
```
Playwright-BDD-E2E-Test/
├── config/              # Configuration and device profiles
│   ├── config.py        # Main configuration settings
│   └── devices/         # Device emulation profiles
├── locators/            # Page locator definitions
├── pages/               # Page Object classes
│   └── base_actions/    # Base action utilities
├── features/            # BDD feature files (.feature)
├── tests/               # Test step definitions
│   └── steps/          # Step implementation files
├── utils/               # Utility functions
├── conftest.py         # Pytest configuration and fixtures
└── pytest.ini          # Pytest settings
```

---

## 🛠️ Tech Stack

| Component | Technology | Version |
|-----------|-----------|---------|
| **Test Framework** | pytest | 8.0.2+ |
| **BDD Framework** | pytest-bdd | 6.1.1+ |
| **Browser Automation** | Playwright | 1.40.0+ |
| **Language** | Python | 3.13+ |
| **Reporting** | pytest-html, allure-pytest | Latest |
| **Parallel Execution** | pytest-xdist | 3.5.0+ |
| **Retry Mechanism** | pytest-rerunfailures | 12.0+ |

---

## ✨ Key Features

### 1. **Playwright-Powered Automation**
- **Auto-waiting**: Automatic element waiting eliminates flaky tests
- **Multi-browser Support**: Chromium, Firefox, and WebKit (Safari)
- **Network Interception**: Advanced network request/response handling
- **Screenshot & Video**: Built-in screenshot and video recording on failures

### 2. **Multi-Device Testing**
- **Device Profiles**: Pre-configured profiles for desktop, tablet, and mobile devices
- **Custom Devices**: Easy to add new device configurations
- **Viewport Management**: Automatic viewport and user-agent configuration

### 3. **BDD Test Structure**
- **Gherkin Syntax**: Human-readable test scenarios
- **Step Reusability**: Shared step definitions across features
- **Tag-based Execution**: Organize and filter tests using tags

### 4. **Professional Test Infrastructure**
- **Parallel Execution**: Run tests in parallel using `pytest-xdist`
- **Retry Mechanism**: Automatic retry for flaky tests
- **Rich Reporting**: HTML and Allure reports with screenshots
- **CI/CD Ready**: Headless mode support for continuous integration

### 5. **Playwright MCP Integration**
- **Rapid Test Development**: Use Playwright MCP for quick test script generation
- **Interactive Debugging**: Live browser interaction for troubleshooting
- **Code Generation**: Generate locators and test code directly from browser actions

---

## 🚀 Quick Start

### Prerequisites

- **Python**: 3.13 or higher
- **Node.js**: 18+ (for Playwright MCP integration)
- **Playwright Browsers**: Automatically installed via `playwright install`

### Installation

1. **Clone the repository**
```bash
git clone <repository-url>
cd Playwright-BDD-E2E-Test
```

2. **Create virtual environment**
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

4. **Install Playwright browsers**
```bash
playwright install
# Or install specific browsers:
playwright install chromium firefox webkit
```

---

## 🎬 Running Tests

### Basic Test Execution

```bash
# Run all tests
pytest

# Run tests with specific marker
pytest -m "bdd"

# Run specific test file
pytest tests/test_home_page.py

# Run with verbose output
pytest -v
```

### Browser Selection

```bash
# Use Chromium (default)
pytest --browser=chromium

# Use Firefox
pytest --browser=firefox

# Use WebKit (Safari)
pytest --browser=webkit
```

### Device Emulation

```bash
# Desktop (default)
pytest --device=desktop

# iPhone 17 Pro Max
pytest --device=iphone17promax

# iPhone 17
pytest --device=iphone17

# iPad Pro
pytest --device=ipadpro

# Google Pixel 9 Pro
pytest --device=pixel9pro
```

### Advanced Options

```bash
# Headless mode
pytest --headless

# Parallel execution (3 workers)
pytest -n 3

# Retry failed tests (2 retries)
pytest --reruns 2

# Combine options
pytest -m "bdd" \
  --browser=chromium \
  --device=iphone17 \
  --headless \
  --reruns=2 \
  -n 4 \
  -v
```

### Environment Configuration

```bash
# Set environment (dev, staging, prod)
pytest --env=staging

# Or use environment variable
export ENV=staging
pytest
```

---

## 🎭 Playwright MCP Integration

### Setup

1. **Install Playwright MCP**
```bash
pnpm add -D @playwright/mcp
# or
npm install --save-dev @playwright/mcp
```

2. **Configure MCP in Cursor**
Add to `~/.cursor/mcp.json`:
```json
{
  "playwright": {
    "command": "npx",
    "args": ["@playwright/mcp@latest"]
  }
}
```

### Usage Guidelines

1. **Test Development Workflow**
   - Use Playwright MCP to interactively explore the TransGlobal website
   - Generate locators and test code directly from browser actions
   - Validate UI elements before writing test scenarios

2. **Best Practices**
   - Describe target URL and objective before navigation
   - Execute steps exactly as written in feature files
   - Capture UI state after critical actions
   - Report results in format: `Navigate → Actions → Verification`

### Official Resources

- [Playwright Documentation](https://playwright.dev/)
- [Playwright GitHub](https://github.com/microsoft/playwright)
- [Cursor MCP Guide](https://cursor.sh/docs/mcp)

---

## 📚 Development Guide

### 1. Adding a New Device Profile

1. Create a new device class in `config/devices/`:
```python
# config/devices/custom_device.py
from .base_device import BaseDevice

class CustomDevice(BaseDevice):
    def __init__(self):
        super().__init__()
        self.name = "Custom Device"
        self.width = 1920
        self.height = 1080
        self.pixel_ratio = 2.0
        self.user_agent = "Mozilla/5.0 ..."
```

2. Register in `conftest.py`:
```python
def get_device_class(device_type: str) -> BaseDevice:
    devices = {
        # ... existing devices
        "custom": CustomDevice
    }
```

### 2. Creating Page Objects

1. **Define Locators** (`locators/home_page_locators.py`):
```python
class HomePageLocators:
    """Locators for TransGlobal home page."""
    
    SERVICES_MENU = 'test_id:services-menu'
    CONTACT_BUTTON = 'css:[data-testid="contact-button"]'
    LANGUAGE_SWITCHER = 'test_id:language-switcher'
```

2. **Create Page Object** (`pages/home_page.py`):
```python
from pages.base_actions.base_action import BaseAction
from locators.home_page_locators import HomePageLocators
from playwright.sync_api import Page

class HomePage(BaseAction):
    def __init__(self, page: Page):
        super().__init__(page)
    
    def navigate_to_services(self):
        self.click_element(HomePageLocators.SERVICES_MENU)
    
    def switch_language(self, language: str):
        self.click_element(HomePageLocators.LANGUAGE_SWITCHER)
        # Additional logic for language selection
```

### 3. Writing BDD Tests

1. **Feature File** (`features/home_page.feature`):
```gherkin
Feature: TransGlobal Home Page
  As a user
  I want to navigate the TransGlobal website
  So that I can access various services

  @home_page @smoke
  Scenario: User can access home page
    Given I navigate to the TransGlobal home page
    When I view the page content
    Then I should see the main navigation menu
    And I should see the services section
```

2. **Step Definitions** (`tests/test_home_page.py`):
```python
from pytest_bdd import given, when, then, scenarios
from pages.home_page import HomePage

scenarios("../features/home_page.feature")

@given("I navigate to the TransGlobal home page")
def navigate_to_home_page(page):
    home_page = HomePage(page)
    home_page.open_url()
    home_page.wait_for_loaded()

@when("I view the page content")
def view_page_content(page):
    # Page is already loaded from previous step
    pass

@then("I should see the main navigation menu")
def verify_navigation_menu(page):
    home_page = HomePage(page)
    assert home_page.is_navigation_menu_visible()

@then("I should see the services section")
def verify_services_section(page):
    home_page = HomePage(page)
    assert home_page.is_services_section_visible()
```

---

## 💡 Best Practices

### Locator Strategy
- **Prefer stable selectors**: Use `data-testid` attributes when available
- **Semantic locators**: Leverage `get_by_role()`, `get_by_text()`, `get_by_label()`
- **Centralized management**: Store all locators in `locators/` package
- **String format**: Use prefix format (`test_id:`, `css:`, `xpath:`) for clarity

### Test Design
- **One assertion per test**: Keep tests focused and maintainable
- **Page Object Pattern**: Encapsulate page logic in Page Objects
- **Reusable steps**: Share common step definitions across features
- **Meaningful names**: Use descriptive names for tests and steps

### Playwright Auto-Waiting
- **Leverage auto-waiting**: No need for explicit waits before actions
- **Actions auto-wait**: `click()`, `fill()`, `type()` automatically wait
- **Read operations auto-wait**: `inner_text()`, `input_value()` wait for visibility
- **State checks**: Use `is_visible()` for immediate checks, `wait_for()` for assertions

### Code Quality
- **Follow PEP8**: Maintain consistent code style
- **DRY principle**: Avoid code duplication
- **SOLID principles**: Design maintainable, extensible code
- **Documentation**: Include docstrings for all public methods

---

## 🔧 Troubleshooting

### Common Issues

#### 1. Browser Not Found
```bash
# Install missing browsers
playwright install chromium
playwright install firefox
playwright install webkit
```

#### 2. Timeout Errors
- Increase timeout in `config/config.py`: `DEFAULT_TIMEOUT`
- Check network connectivity to TransGlobal website
- Verify element locators are correct

#### 3. Element Not Found
- Use Playwright MCP to verify locators
- Check if element is in iframe (use `frame_locator()`)
- Ensure element is visible (not hidden by CSS)

#### 4. Headless Mode Issues
- Some features may behave differently in headless mode
- Use `--headless=false` for debugging
- Check browser console logs for errors

### Debug Mode

```bash
# Run with debug output
pytest --log-cli-level=DEBUG

# Run with Playwright debug mode
PWDEBUG=1 pytest

# Run specific test with verbose output
pytest tests/test_home_page.py::test_specific_scenario -v -s
```

### Screenshots and Videos

Screenshots are automatically captured on test failures and saved to `screenshots/` directory (configurable via `SCREENSHOT_PATH` in config).

---

## 📊 Test Execution Examples

### Parallel Execution Matrix

| Scenario | Command |
|----------|---------|
| Run all BDD tests in parallel | `pytest -m bdd -n 4` |
| Run specific feature | `pytest tests/test_home_page.py -n 2` |
| Keyword-based filtering | `pytest -k "navigation" -n 3` |
| Browser + Device matrix | `pytest --browser=chromium --device=iphone17 -n 2` |
| Retry failed tests | `pytest --last-failed --reruns 2` |

### CI/CD Integration

```yaml
# Example GitHub Actions workflow
- name: Run E2E Tests
  run: |
    pip install -r requirements.txt
    playwright install --with-deps chromium
    pytest --headless -n 4 --html=report.html
```

---

## 📝 Configuration

### Environment Variables

Create a `.env` file (see `.env.example`):

```env
# Browser Configuration
BROWSER=chromium
HEADLESS=false

# Timeout Settings
DEFAULT_TIMEOUT=20
POLL_FREQUENCY=0.5

# Environment
ENV=staging

# Logging
LOG_LEVEL=INFO
SCREENSHOT_PATH=screenshots
```

### Command-Line Options

```bash
# Browser selection
--browser {chromium,firefox,webkit}

# Device emulation
--device {desktop,iphone17promax,iphone17,ipadpro,pixel9pro}

# Execution mode
--headless          # Run in headless mode
--env {dev,staging,prod}  # Set environment

# Test selection
-m MARKER           # Run tests with marker
-k KEYWORD          # Run tests matching keyword
```

---

## 🤝 Contributing

### Code Standards
- Follow PEP8 guidelines
- Maintain cognitive complexity < 15
- Include docstrings for all public methods
- Write meaningful test descriptions

### Pull Request Process
1. Create feature branch
2. Write tests for new functionality
3. Ensure all tests pass
4. Update documentation if needed
5. Submit pull request with description

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- [Playwright](https://playwright.dev/) - Modern browser automation
- [pytest](https://docs.pytest.org/) - Testing framework
- [pytest-bdd](https://pytest-bdd.readthedocs.io/) - BDD for pytest

---

**Happy Testing!** 🚀

For questions or issues, please open an issue in the repository.
