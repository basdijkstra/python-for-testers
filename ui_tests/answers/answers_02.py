from selenium import webdriver
from selenium.webdriver.support.ui import Select
import pytest
import time


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

# Exercise 2.1
# Extend this test with the following actions:
# 1. Select the menu item 'Request Loan' from the side menu bar
# 2. Specify '1000' as the requested loan amount
# 3. Specify '100' as the down payment
# 4. Select '12456' as the from account ID
# 5. Click the 'Apply Now' button
# 6. Check that the element containing the result of the loan application is displayed
#    (you might need to add a time.sleep(x) statement here, which
#     makes the test wait for x seconds before proceeding with the
#     next statement)
# 7. Check that the result of the loan application equals 'Denied'
def test_successful_loan_request(browser):
    browser.get("http://parabank.parasoft.com")
    browser.find_element_by_name("username").send_keys("john")
    browser.find_element_by_name("password").send_keys("demo")
    browser.find_element_by_xpath("//input[@value='Log In']").click()
    browser.find_element_by_link_text("Request Loan").click()
    browser.find_element_by_id("amount").send_keys("1000")
    browser.find_element_by_id("downPayment").send_keys("100")
    Select(browser.find_element_by_id("fromAccountId")).select_by_visible_text("12456")
    browser.find_element_by_xpath("//input[@value='Apply Now']").click()
    time.sleep(3)
    assert browser.find_element_by_id("loanStatus").is_displayed()
    assert browser.find_element_by_id("loanStatus").text == "Denied"
