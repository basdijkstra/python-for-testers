from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import pytest
import time


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

# Exercise 3.1
# Rewrite the remaining send_keys() and click() actions in this test
# so that they now use the helper methods defined below
# Run your test again to see if it keeps working
def test_successful_loan_request(browser):
    browser.get("http://parabank.parasoft.com")
    send_keys(browser, By.NAME, "username", "john")
    send_keys(browser, By.NAME, "password", "demo")
    click(browser, By.XPATH, "//input[@value='Log In']")
    browser.find_element_by_link_text("Request Loan").click()
    browser.find_element_by_id("amount").send_keys("1000")
    browser.find_element_by_id("downPayment").send_keys("100")
    Select(browser.find_element_by_id("fromAccountId")).select_by_visible_text("12456")
    browser.find_element_by_xpath("//input[@value='Apply Now']").click()
    time.sleep(3)
    assert browser.find_element_by_id("loanStatus").text == "Denied"


def send_keys(driver, locator_strategy, locator, text_to_type):
    element = WebDriverWait(driver, 10).until(ec.element_to_be_clickable((locator_strategy, locator)))
    element.send_keys(text_to_type)


def click(driver, locator_strategy, locator):
    element = WebDriverWait(driver, 10).until(ec.element_to_be_clickable((locator_strategy, locator)))
    element.click()

# Exercise 3.2
# Add a helper method that performs the select action, but now waits properly for the
# dropdown element to become clickable first
# Use it in the test above to see if it works

# Exercise 3.3
# Add a method that returns the visible text of the specified element, but now waits
# properly for the element to become visible (not necessarily clickable!)
# Use it in the test to see if it works
# Does this mean you can remove the time.sleep(3) command now? Test it!