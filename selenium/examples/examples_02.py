from selenium import webdriver
from selenium.webdriver.support.ui import Select
import pytest


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_successful_google_search(browser):
    browser.get("https://www.google.com")
    browser.find_element_by_name("q").send_keys("Maserati")
    browser.find_element_by_name("btnK").click()
    assert browser.title == "Maserati - Google zoeken"
    assert browser.find_element_by_id("resultStats").is_displayed() is True


def test_select_example(browser):
    browser.get("https://html.com/tags/select/")
    dropdown = Select(browser.find_element_by_xpath("(//select)[1]"))
    dropdown.select_by_visible_text("Chilean flamingo")
    assert dropdown.first_selected_option.text == "Chilean flamingo"
