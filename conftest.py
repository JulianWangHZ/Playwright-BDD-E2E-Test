import os
import sys
import time
import subprocess
from datetime import datetime
import traceback

import pytest
from playwright.sync_api import sync_playwright, Browser, BrowserContext, Page

from config.config import Config
from config.devices import BaseDevice, IPhone17ProMax, IPhone17, IPadPro, Pixel9Pro


def pytest_configure(config):
    config.addinivalue_line("markers", "bdd: BDD tests")
    config.addinivalue_line("filterwarnings", "ignore::pytest.PytestUnknownMarkWarning")
    
    env = config.getoption("--env")
    if env:
        os.environ['ENV'] = env


def pytest_addoption(parser):
    config = Config()
    parser.addoption("--headless", action="store_true", default=False,
                    help="Run tests in headless mode")
    parser.addoption("--env", action="store", default=config.ENV,
                    help=f"Environment: {', '.join(['dev', 'staging', 'prod'])}")
    parser.addoption("--browser", action="store", default=config.BROWSER,
                    help=f"Browser: {', '.join(['chromium', 'firefox', 'webkit'])}")
    parser.addoption("--device", action="store", default=config.DEVICE_TYPE,
                    help="Device type: desktop, iphone17promax, iphone17, ipadpro, pixel9pro")


def get_device_class(device_type: str) -> BaseDevice:
    devices = {
        "desktop": BaseDevice,
        "iphone17promax": IPhone17ProMax,
        "iphone17": IPhone17,
        "ipadpro": IPadPro,
        "pixel9pro": Pixel9Pro
    }
    device_class = devices.get(device_type.lower())
    if not device_class:
        raise ValueError(f"Unsupported device type: {device_type}")
    return device_class()


@pytest.fixture(scope="session")
def device(request):
    device_type = request.config.getoption("--device")
    return get_device_class(device_type)


@pytest.fixture(scope="session")
def playwright():
    with sync_playwright() as p:
        yield p


@pytest.fixture(scope="function")
def browser(request, device, playwright):
    browser_type = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    
    # Map browser names to Playwright browser types
    browser_map = {
        'chrome': 'chromium',
        'chromium': 'chromium',
        'firefox': 'firefox',
        'safari': 'webkit',
        'webkit': 'webkit'
    }
    
    playwright_browser_type = browser_map.get(browser_type.lower(), browser_type.lower())
    
    # Launch browser
    if playwright_browser_type == 'chromium':
        browser_instance = playwright.chromium.launch(headless=headless)
    elif playwright_browser_type == 'firefox':
        browser_instance = playwright.firefox.launch(headless=headless)
    elif playwright_browser_type == 'webkit':
        browser_instance = playwright.webkit.launch(headless=headless)
    else:
        raise ValueError(f"Unsupported browser type: {browser_type}")
    
    yield browser_instance
    
    browser_instance.close()


@pytest.fixture(scope="function")
def page(browser, device, request):
    # Create context with device settings
    context = browser.new_context(
        viewport={'width': device.width, 'height': device.height},
        user_agent=device.user_agent,
        is_mobile=device.is_mobile,
        has_touch=device.is_mobile or device.is_tablet
    )
    
    page_instance = context.new_page()
    
    # Set default timeout from config
    config = Config()
    page_instance.set_default_timeout(config.DEFAULT_TIMEOUT * 1000)
    
    yield page_instance
    
    context.close()


@pytest.fixture(scope="session")
def test_config():
    return Config()


@pytest.fixture(scope="session")
def base_url(test_config):
    return test_config.BASE_URL


def get_test_info(item):
    test_file = os.path.basename(item.module.__file__)
    feature_file = None
    scenario_name = None
    
    if test_file.startswith('test_'):
        feature_name = ''.join(c for c in test_file[5:-8] if not c.isdigit())
        if feature_name:
            feature_file = f"{feature_name}.feature"
    
    if hasattr(item, 'function'):
        scenario_name = item.function.__name__
        if scenario_name.startswith('test_'):
            scenario_name = scenario_name[5:]
    
    return {
        "test_file": test_file,
        "feature_file": feature_file or "unknown",
        "scenario_name": scenario_name or item.name,
        "env": item.config.getoption("--env"),
        "browser": item.config.getoption("--browser"),
        "device": item.config.getoption("--device")
    }


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    
    if report.when == 'call':
        start_time = getattr(report, 'start_time', datetime.now())
        duration = (datetime.now() - start_time).total_seconds()
        
        test_info = get_test_info(item)
        screenshot_path = None
        
        if report.failed and hasattr(item, 'funcargs') and 'page' in item.funcargs:
            scenario_name = test_info['scenario_name']
            clean_name = ''.join(c if c.isalnum() else '_' for c in scenario_name)
            config = Config()
            
            # Create screenshot directory if it doesn't exist
            os.makedirs(config.SCREENSHOT_PATH, exist_ok=True)
            
            screenshot_path = f"{config.SCREENSHOT_PATH}/{clean_name}.png"
            page = item.funcargs['page']
            page.screenshot(path=screenshot_path)

        tags = []
        if test_info['test_file'].startswith('test_'):
            test_name = test_info['test_file'][5:-8]
            main_feature = ''.join(c for c in test_name if not c.isdigit())
            if main_feature:
                tags.append(main_feature)


def pytest_bdd_before_step(request, feature, scenario, step, step_func):
    if not hasattr(request.node, 'feature_printed'):
        feature_file = os.path.basename(feature.filename)
        print(f"\n\033[36m{'─' * 70}\033[0m")
        print(f"\033[36mFeature:\033[0m \033[97m{feature_file}\033[0m")
        print(f"\033[36mScenario:\033[0m \033[97m{scenario.name}\033[0m")
        
        if hasattr(scenario, 'tags'):
            tags = [tag for tag in scenario.tags if isinstance(tag, str)]
            if tags:
                print(f"\033[35mTags:\033[0m \033[97m{', '.join(tags)}\033[0m")
        
        print(f"\033[36m{'─' * 70}\033[0m")
        setattr(request.node, 'feature_printed', True)
    
    # GIVEN(Blue) / WHEN(Yellow) / THEN(Green) / AND(Purple)
    color_map = {
        'given': '\033[34m',
        'when': '\033[33m',
        'then': '\033[32m',
        'and': '\033[35m',
    }
    style_type = (step.type or '').lower()
    color = color_map.get(style_type, '\033[37m') 
    print(f"{color}{step.type.upper()}\033[0m \033[97m{step.name}\033[0m")


def pytest_bdd_step_error(request, feature, scenario, step, step_func, exception):
    """When a step fails, display detailed error information"""
    print(f"\n\033[31m{'!' * 70}\033[0m")
    print(f"\033[31m❌ Step execution failed\033[0m")
    print(f"\033[31mStep:\033[0m \033[97m{step.type.upper()} {step.name}\033[0m")
    print(f"\033[31mError type:\033[0m \033[97m{type(exception).__name__}\033[0m")
    print(f"\033[31mError message:\033[0m \033[97m{str(exception)}\033[0m")
    print(f"\033[31m\nFull error:\033[0m")
    traceback.print_exc()


def pytest_sessionfinish(session, exitstatus):
    if os.environ.get("CI") or os.environ.get("GITHUB_ACTIONS"):
        return
    
    worker_id = os.environ.get("PYTEST_XDIST_WORKER")
    if worker_id is None:
        try:
            subprocess.run(["pkill", "-f", "ms-playwright.*chromium.*remote-debugging"], check=False, timeout=5)
            subprocess.run(["pkill", "-f", "Chromium.*--remote-debugging-pipe"], check=False, timeout=5)
            subprocess.run(["pkill", "-f", "Chromium.*--remote-debugging-port"], check=False, timeout=5)
            
            time.sleep(1)
        except (subprocess.TimeoutExpired, subprocess.SubprocessError, OSError):
            pass
    
    sys.exit(exitstatus)
