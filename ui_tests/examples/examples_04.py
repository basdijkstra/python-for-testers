from selenium import webdriver
from ui_tests.examples.pages import GoogleSearchPage, GoogleResultsPage
import pytest


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_google_search(browser):
    gsp = GoogleSearchPage(browser)
    gsp.load()
    gsp.perform_search("Maserati")
    assert GoogleResultsPage(browser).result_stats_are_displayed() is True
