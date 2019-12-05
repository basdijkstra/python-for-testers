from selenium.webdriver.common.by import By
from ui_tests.answers.helpers import SeleniumHelpers


class LoginPage:

    url = "http://parabank.parasoft.com"

    textfield_username = (By.NAME, "username")
    textfield_password = (By.NAME, "password")
    button_do_login = (By.XPATH, "//input[@value='Log In']")

    def __init__(self, browser):
        self.browser = browser
        self.selenium = SeleniumHelpers(browser)

    def load(self):
        self.browser.get(self.url)

    def login_as(self, username, password):
        self.selenium.send_keys(self.textfield_username, username)
        self.selenium.send_keys(self.textfield_password, password)
        self.selenium.click(self.button_do_login)
