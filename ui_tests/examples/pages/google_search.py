from selenium.webdriver.common.by import By
from ui_tests.examples.helpers import SeleniumHelpers


class GoogleSearchPage:

    url = "https://www.google.com"

    textfield_search_input = (By.NAME, "q")
    button_do_search = (By.NAME, "btnK")

    def __init__(self, browser):
        self.browser = browser
        self.selenium = SeleniumHelpers(browser)

    def load(self):
        self.browser.get(self.url)

    def perform_search(self, query):
        self.selenium.send_keys(self.textfield_search_input, query)
        self.selenium.click(self.button_do_search)
