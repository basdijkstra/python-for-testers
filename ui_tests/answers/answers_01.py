from selenium import webdriver
import pytest

# Exercise 1.1
# Write a test that performs the following actions:
# 1. Open a new Chrome instance
# 2. Maximize the window
# 3. Navigate to http://parabank.parasoft.com
# 4. Enter 'john' in the username text field
# 5. Enter 'demo' in the password text field
# 6. Click the 'Log In' button
# 7. Assert that the browser tab title text equals 'ParaBank | Accounts Overview'
# 8. Close the browser
def test_successful_login_to_parabank():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://parabank.parasoft.com")
    driver.find_element_by_name("username").send_keys("john")
    driver.find_element_by_name("password").send_keys("demo")
    driver.find_element_by_xpath("//input[@value='Log In']").click()
    assert driver.title == "ParaBank | Accounts Overview"
    driver.quit()


# Exercise 1.2
# Write a pytest fixture method that performs the following actions:
# 1. Open a new Chrome instance
# 2. Maximize the window
# 3. Yield the browser object
# 4. Close the browser
@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


# Exercise 1.3
# Duplicate the test from 1.1 (or rewrite it) so that the
# pytest fixture is used to open and close the browser
def test_successful_login_to_parabank_with_fixture(browser):
    browser.get("http://parabank.parasoft.com")
    browser.find_element_by_name("username").send_keys("john")
    browser.find_element_by_name("password").send_keys("demo")
    browser.find_element_by_xpath("//input[@value='Log In']").click()
    assert browser.title == "ParaBank | Accounts Overview"
