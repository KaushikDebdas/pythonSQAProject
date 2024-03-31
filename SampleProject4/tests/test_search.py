import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture()
def test_setup_and_tearDown():
    global driver
    chromeOptions = webdriver.ChromeOptions()
    chromeOptions.add_argument("--headless")
    driver = webdriver.Chrome(options=chromeOptions)
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo/")
    driver.implicitly_wait(10)
    yield
    driver.close()
    driver.quit()
    print("Test Complete")
def test_search_for_valid_product(test_setup_and_tearDown):
    # search_field
    driver.find_element(By.NAME, "search").send_keys("Hp")
    time.sleep(3)
    print("Hp")
    # search_button
    driver.find_element(By.XPATH, "//div[contains(@class,'input-group')]/span/button").click()
    time.sleep(3)
    print("Click")
    # display search product
    assert driver.find_element(By.LINK_TEXT, "HP LP3065").is_displayed()

def test_search_for_invalid_product(test_setup_and_tearDown):
    # search_field
    driver.find_element(By.NAME, "search").send_keys("Mobile")
    time.sleep(3)
    print("Mobile")
    # search_button
    driver.find_element(By.XPATH, "//div[contains(@class,'input-group')]/span/button").click()
    time.sleep(3)
    print("Click")
    # display search product
    expected_text = "There is no product that matches the search criteria."
    assert driver.find_element(By.XPATH, "//input[@id='button-search']/following-sibling::p").text.__eq__(expected_text)

def test_search_without_entering_productName():
    # search_field
    driver.find_element(By.NAME, "search")
    time.sleep(3)
    # search_button
    driver.find_element(By.XPATH, "//div[contains(@class,'input-group')]/span/button").click()
    time.sleep(3)
    print("Click")
    # display search product
    expected_text = "There is no product that matches the search criteria."
    assert driver.find_element(By.XPATH, "//input[@id='button-search']/following-sibling::p").text.__eq__(expected_text)