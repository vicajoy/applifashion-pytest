from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def wait_for(self, condition, timeout=10):
        """Wait for specific ExpectedCondition for the given amount of time in seconds"""
        wait = WebDriverWait(self.driver, timeout)
        wait.until(condition)

    def wait_for_visibility_of(self, locator):
        """Wait for given number of seconds for element with given locator to be visible"""
        try:
            self.wait_for(ec.visibility_of_element_located(locator))
        except (StaleElementReferenceException, TimeoutException):
            return f"Element located at {locator} is not visible."

    def find(self, locator, index=1):
        """Find element using given locator, index starts at 1"""
        try:
            return self.driver.find_elements(*locator)[index-1]
        except IndexError:
            raise Exception(f'Element with {locator} not found')

    def find_all(self, locator):
        """Find all elements using given locator"""
        return self.driver.find_elements(*locator)

    def click(self, locator, index=1):
        """Click on element with given locator when it's visible"""
        self.wait_for_visibility_of(locator)
        self.find(locator, index).click()

    def get_text(self, locator):
        """Get element text with given locator when it's visible"""
        self.wait_for_visibility_of(locator)
        return self.find(locator).text

    def get_browser_name(self):
        """Returns the name of the current browser."""
        return self.driver.capabilities['browserName'].capitalize()

    def get_viewport_size(self):
        """Returns the viewport size of the current browser in the <widthxheight> format."""
        viewport_size = self.driver.execute_script("return [window.innerWidth, window.innerHeight];")
        return str(viewport_size[0]) + "x" + str(viewport_size[1])

    def get_device_name(self):
        """Returns the device name based on the viewport size."""
        if self.get_viewport_size() == "1200x700":
            return "Laptop"
        elif self.get_viewport_size() == "768x700":
            return "Tablet"
        elif self.get_viewport_size() == "500x700":
            return "Mobile"

    def get_page_url(self):
        """Gets current page url."""
        return self.driver.current_url

    def go_to_page(self, url):
        """Navigates via the url."""
        self.driver.get(url)

    def report(self, task, test_name, dom_id, result):
        """A Helper to print the test result in the following format:
         Task: <Task Number>, Test Name: <Test Name>, DOM Id:: <id>, Browser: <Browser>, Viewport: <Width x Height>,
         Device: <Device Type>, Status: <Pass | Fail>
         Example: Task: 1, Test Name: Search field is displayed, DOM Id: DIV__customsear__41, Browser: Chrome,
         Viewport: 1200 x 700, Device: Laptop, Status: Pass

         @param task                    int - 1, 2 or 3
         @param test_name               string - For example, Search field is displayed
         @param dom_id                  string - DOM ID of the element
         @param result       boolean - The result of comparing the "Expected" value and the "Actual" value
        """
        if "V1" in self.get_page_url():
            f = open("traditional-V1-TestResults.txt", "a")
        else:
            f = open("traditional-V2-TestResults.txt", "a")
        report_content = "Task: {task}, Test Name: {test_name}, DOM Id: {dom_id}, Viewport: {viewport}, " \
                         "Device: {device}, Browser: {browser}, " \
                         "Status: {status}\n".format(task=task, test_name=test_name, dom_id=dom_id,
                                                     viewport=self.get_viewport_size(), device=self.get_device_name(),
                                                     browser=self.get_browser_name(),
                                                     status=("Pass" if (result is True) else "Fail"))

        print(report_content)
        f.write(report_content)
        f.close()
        return result
