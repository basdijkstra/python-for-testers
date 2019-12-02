from selenium import webdriver


def test_successful_google_search():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.google.com")
    driver.find_element_by_name("q").send_keys("Maserati")
    driver.find_element_by_name("btnK").click()
    assert driver.title == "Maserati - Google zoeken"
    driver.quit()
