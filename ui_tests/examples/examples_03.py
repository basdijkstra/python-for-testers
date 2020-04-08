from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import pytest


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_successful_google_search(browser):
    browser.get("https://www.google.com")
    send_keys(browser, By.NAME, "q", "Maserati")
    click(browser, By.NAME, "btnK")
    assert browser.title == "Maserati - Google zoeken"
    assert browser.find_element_by_id("resultStats").is_displayed() is True


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
