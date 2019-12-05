from selenium import webdriver
from ui_tests.answers.pages import LoginPage, AccountsOverviewPage, RequestLoanPage
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
    plp = LoginPage(browser)
    plp.load()
    plp.login_as("john", "demo")
    assert AccountsOverviewPage(browser).get_page_header() == "Accounts Overview"


# Exercise 3.2
# Rewrite this test so that it uses the LoginPage, AccountsOverviewPage as
# well as the RequestLoanPage. You will need to define the locators and methods
# in the RequestLoanPage yourself (see description in there).
# Don't forget to make the RequestLoanPage available through the __init__.py file
# in the pages package and to import it in this module
def test_successful_loan_request(browser):
    lp = LoginPage(browser)
    lp.load()
    lp.login_as("john", "demo")

    aop = AccountsOverviewPage(browser)
    aop.goto_request_loan()

    rlp = RequestLoanPage(browser)
    rlp.request_loan("1000", "100", "12456")
    assert rlp.get_application_result() == "Denied"
