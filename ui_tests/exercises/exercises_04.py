from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from ui_tests.exercises.pages import LoginPage, AccountsOverviewPage
import pytest


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


# Exercise 3.1
# Rewrite this test so that it uses the LoginPage and AccountsOverview page
# and the methods load(), login_as() and get_page_header() therein
def test_successful_login(browser):
    browser.get("http://parabank.parasoft.com")
    send_keys(browser, By.NAME, "username", "john")
    send_keys(browser, By.NAME, "password", "demo")
    click(browser, By.XPATH, "//input[@value='Log In']")
    assert (
        get_element_text(browser, By.XPATH, "//h1[@class='title']")
        == "Accounts Overview"
    )


# Exercise 3.2
# Rewrite this test so that it uses the LoginPage, AccountsOverviewPage as
# well as the RequestLoanPage. You will need to define the locators and methods
# in the RequestLoanPage yourself (see description in there).
# Don't forget to make the RequestLoanPage available through the __init__.py file
# in the pages package and to import it in this module
def test_successful_loan_request(browser):
    browser.get("http://parabank.parasoft.com")
    send_keys(browser, By.NAME, "username", "john")
    send_keys(browser, By.NAME, "password", "demo")
    click(browser, By.XPATH, "//input[@value='Log In']")
    click(browser, By.LINK_TEXT, "Request Loan")
    send_keys(browser, By.ID, "amount", "1000")
    send_keys(browser, By.ID, "downPayment", "100")
    select(browser, By.ID, "fromAccountId", "12456")
    click(browser, By.XPATH, "//input[@value='Apply Now']")
    assert get_element_text(browser, By.ID, "loanStatus") == "Denied"


# Exercise 3.3
# If all went well, we don't need the methods defined below anymore..
# Remove them and rerun your tests to see if that's true
def send_keys(driver, locator_strategy, locator, text_to_type):
    element = WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable((locator_strategy, locator))
    )
    element.send_keys(text_to_type)


def click(driver, locator_strategy, locator):
    element = WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable((locator_strategy, locator))
    )
    element.click()


def select(driver, locator_strategy, locator, value_to_select):
    element = Select(
        WebDriverWait(driver, 10).until(
            ec.element_to_be_clickable((locator_strategy, locator))
        )
    )
    element.select_by_visible_text(value_to_select)


def get_element_text(driver, locator_strategy, locator):
    element = WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located((locator_strategy, locator))
    )
    return element.text
