from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as ec


class SeleniumHelpers:

    def __init__(self, browser):
        self.browser = browser

    def send_keys(self, locator, text_to_type):
        element = WebDriverWait(self.browser, 10).until(ec.element_to_be_clickable(locator))
        element.send_keys(text_to_type)

    def click(self, locator):
        element = WebDriverWait(self.browser, 10).until(ec.element_to_be_clickable(locator))
        element.click()

    def select(self, locator, value_to_select):
        element = Select(WebDriverWait(self.browser, 10).until(ec.element_to_be_clickable(locator)))
        element.select_by_visible_text(value_to_select)

    def is_displayed(self, locator):
        element = WebDriverWait(self.browser, 10).until(ec.visibility_of_element_located(locator))
        return element.is_displayed()

    def get_element_text(self, locator):
        element = WebDriverWait(self.browser, 10).until(ec.visibility_of_element_located(locator))
        return element.text
