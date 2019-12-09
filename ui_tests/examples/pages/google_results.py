from selenium.webdriver.common.by import By
from ui_tests.examples.helpers import SeleniumHelpers


class GoogleResultsPage:

    textfield_result_stats = (By.ID, "resultStats")

    def __init__(self, browser):
        self.browser = browser
        self.selenium = SeleniumHelpers(browser)

    def result_stats_are_displayed(self):
        return self.selenium.is_displayed(self.textfield_result_stats)
