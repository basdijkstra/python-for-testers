from selenium.webdriver.common.by import By
from ui_tests.answers.helpers import SeleniumHelpers


class AccountsOverviewPage:

    link_request_loan = (By.LINK_TEXT, "Request Loan")
    textfield_page_header = (By.XPATH, "//h1[@class='title']")

    def __init__(self, browser):
        self.browser = browser
        self.selenium = SeleniumHelpers(browser)

    def goto_request_loan(self):
        self.selenium.click(self.link_request_loan)

    def get_page_header(self):
        return self.selenium.get_element_text(self.textfield_page_header)
