import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
@pytest.fixture()
def test_setup_and_tearDown():
    global driver
    chromeOptions = webdriver.ChromeOptions()
    #chromeOptions.add_argument("--headless")
    driver = webdriver.Chrome(options=chromeOptions)
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo/")
    driver.implicitly_wait(10)
    yield
    driver.close()
    driver.quit()
    print("Test Complete")

def test_logout(test_setup_and_tearDown):
    driver.find_element(By.XPATH, "//span[contains(text(),'My Account')]").click()
    time.sleep(2)
    driver.find_element(By.XPATH,"//a[contains(text(),'Logout')]").click()
    time.sleep(2)
    logout_msg = "Account Logout"
    assert driver.find_element(By.XPATH, "//h1[contains(text(),'Account Logout')]").text.__contains__(logout_msg)