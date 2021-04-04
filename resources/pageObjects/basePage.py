from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


from selenium.common.exceptions import TimeoutException
from resources.utilities.ExpectedConditionCssClass import ExpectedConditionCssClass
from resources.utilities.ExpectedConditionJavascript import ExpectedConditionJavascript


class BasePage:
    URL = ''

    def __init__(self, context):
        self.context = context
        self.driver = context.browser  # An alias to make it quicker to access the WebDriver from pages

    def open(self):
        self.context.logger.info('Opening: ' + self.URL)
        self.driver.get(self.URL)

    def click(self, by_locator, timeout=15):
        """Performs a mouse click on the element passed to it by locator"""
        WebDriverWait(self.driver, timeout).until(
            expected_conditions.element_to_be_clickable(by_locator)).click()

    def enter_text(self, by_locator, text, timeout=150):
        self.context.logger.info(f'Enter text "{text}" in Element located by {by_locator}')
        return WebDriverWait(self.driver, timeout).until(
            expected_conditions.visibility_of_element_located(by_locator)).send_keys(text)

    def clear_and_enter_text(self, by_locator, text, timeout=5):
        self.context.logger.info(f'Clear field and enter text "{text}" in Element located by {by_locator}')
        form_input = WebDriverWait(self.driver, timeout).until(
            expected_conditions.visibility_of_element_located(by_locator)
        )
        form_input.clear()
        form_input.send_keys(text)

    def clear_and_enter_value(self, by_locator, value, timeout=5):
        self.context.logger.info(f'Clear field and enter text "{value}" in Element located by {by_locator}')
        form_input = WebDriverWait(self.driver, timeout).until(
            expected_conditions.visibility_of_element_located(by_locator)
        )
        form_input.clear()
        form_input.send_keys(value)

    def get_text(self, by_locator):
        """Returns element's text if selenium can handle it well

        :return: string
        """
        return self.driver.find_element(*by_locator).text

    def get_value(self, by_locator):
        """Returns element's value if selenium can handle it well

        :return: string
        """
        return self.driver.find_element(*by_locator).get_attribute('value')

    def get_text_content(self, by_locator):
        """Returns the content of "textContent" attribute

        :return: string
        """
        return self.driver.find_element(*by_locator).get_attribute('textContent')

    def switch_back_to_main_page(self):
        self.driver.switch_to.default_content()

    def wait_for_element(self, located_by, timeout=5):
        return WebDriverWait(self.driver, timeout).until(
            expected_conditions.visibility_of_element_located(located_by)
        )

    def wait_for_element_to_be_not_visible(self, located_by, timeout=5):
        return WebDriverWait(self.driver, timeout).until_not(
            expected_conditions.visibility_of_element_located(located_by)
        )

    def wait_for_element_to_have_class(self, by_locator, css_class, timeout=10):
        self.context.logger.info(f"Waiting {timeout}s for an element located by {by_locator} to have class '{css_class}'")
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(ExpectedConditionCssClass(by_locator, css_class))

    def wait_for_angular_load(self, timeout=5):
        self.context.logger.info(f"Waiting {timeout}s for a script to run")
        angular_ready_script = "return angular.element(document).injector().get('$http').pendingRequests.length === 0"
        try:
            WebDriverWait(self.driver, timeout).until(
                ExpectedConditionJavascript((By.NAME, 'body'), angular_ready_script),
                'A script should execute in the browser')
        except TimeoutException:
            self.context.logger.error('There was a timeout waiting for a script to execute in the browser')

    def wait_for_element_to_be_clickable(self, located_by, timeout=15):
        self.context.logger.info(f"Waiting {timeout}s for an element {located_by} to be clickable")
        WebDriverWait(self.driver, timeout).until(
            expected_conditions.element_to_be_clickable(located_by),
            f'Expected to be able to click on element {located_by}'
        )

    def wait_for_element_to_be_not_clickable(self, located_by, timeout=15):
        return WebDriverWait(self.driver, timeout).until_not(
            expected_conditions.element_to_be_clickable(located_by)
        )

    def new_locator(self, locator_prefix, index=0):
        return (locator_prefix[0], locator_prefix[1]+str(index))

    def page_refresh(self):
        self.driver.refresh()

    def get_primary_window_index(self):
        primary_window = self.driver.window_handles[0]
        return primary_window

    def switch_to_secondary_window(self):
        secondary_window = self.driver.window_handles[1]
        self.driver.switch_to_window(secondary_window)

    def switch_to_third_window(self):
        third_window = self.driver.window_handles[2]
        self.driver.switch_to_window(third_window)

    def switch_to_first_window(self):
        first_window = self.driver.window_handles[0]
        self.driver.switch_to_window(first_window)

    def switch_back_to_primary_window(self, window):
        self.driver.switch_to_window(window)

    def close_current_tab(self):
        self.driver.close()

    def maximize_window(self):
        self.driver.maximize_window()