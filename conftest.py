import os
import pytest
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from applitools.common import BatchInfo, MatchLevel, DeviceName, ScreenOrientation
from applitools.common.selenium import Configuration, BrowserType
from applitools.selenium import Eyes, VisualGridRunner
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Enter preferred browser")
    parser.addoption("--device", action="store", default="laptop", help="Enter the device type")


@pytest.fixture
def browser(request):
    """Initiates the browser and sets the viewport size."""
    browser = request.config.getoption("--browser").lower()
    device = request.config.getoption("--device").lower()
    if browser == "chrome":
        driver = webdriver.Chrome(ChromeDriverManager().install())
        set_viewport_size(driver, device)
    elif browser == "firefox":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        set_viewport_size(driver, device)
    elif browser == "edge_chromium":
        driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    elif browser == "ie":
        driver = webdriver.Ie(IEDriverManager().install())
    else:
        raise Exception(f"{request.param} is not supported.")
    yield driver
    driver.quit()


def set_viewport_size(driver, device):
    """Helper to set the viewport size."""
    if device == "laptop":
        window_size = driver.execute_script("""return [window.outerWidth - window.innerWidth + arguments[0], 
                                            window.outerHeight - window.innerHeight + arguments[1]];""", 1200, 700)
        driver.set_window_size(*window_size)
    elif device == "tablet":
        window_size = driver.execute_script("""return [window.outerWidth - window.innerWidth + arguments[0], 
                                            window.outerHeight - window.innerHeight + arguments[1]];""", 768, 700)
        driver.set_window_size(*window_size)
    elif device == "mobile":
        window_size = driver.execute_script("""return [window.outerWidth - window.innerWidth + arguments[0], 
                                            window.outerHeight - window.innerHeight + arguments[1]];""", 500, 700)
        driver.set_window_size(*window_size)
    else:
        raise Exception("The device is not supported.")


@pytest.fixture(scope="module")
def batch_info():
    """Use one BatchInfo for all tests inside a module."""
    return BatchInfo("UFG Hackathon")


@pytest.fixture(name="runner", scope="session")
def runner_setup():
    """One test runner for all tests."""
    concurrent_sessions = 5
    runner = VisualGridRunner(concurrent_sessions)
    yield runner


@pytest.fixture(name="eyes", scope="function")
def eyes_setup(runner, batch_info):
    """Eyes setup."""
    eyes = Eyes(runner)
    suite_config = (Configuration()
                    .add_browser(1200, 700, BrowserType.CHROME_ONE_VERSION_BACK)
                    .add_browser(1200, 700, BrowserType.FIREFOX)
                    .add_browser(1200, 700, BrowserType.EDGE_CHROMIUM)
                    .add_browser(768, 700, BrowserType.CHROME_ONE_VERSION_BACK)
                    .add_browser(768, 700, BrowserType.FIREFOX)
                    .add_browser(768, 700, BrowserType.EDGE_CHROMIUM)
                    .add_device_emulation(DeviceName.iPhone_X, ScreenOrientation.PORTRAIT))
    eyes.set_configuration(suite_config)
    eyes.api_key = os.getenv("API_KEY")
    eyes.configure.batch = batch_info
    yield eyes


def validate_window(driver, eyes, test_name, step_name):
    """Validates window."""
    eyes.open(driver, "Applifashion", test_name=test_name)
    eyes.match_level = MatchLevel.STRICT
    eyes.check_window(step_name)
    eyes.close()


def validate_element(driver, eyes, element, test_name, step_name):
    """Validates element."""
    eyes.open(driver, "Applifashion", test_name=test_name)
    eyes.match_level = MatchLevel.STRICT
    eyes.check_region(element, step_name)
    eyes.close()
