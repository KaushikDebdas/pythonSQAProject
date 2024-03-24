import time
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture()
def test_setup():
    # web driver setup
    global driver
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://www.google.com")
    driver.maximize_window()
    yield # run the last segment
    # close browser
    driver.close()
    driver.quit()
    print("Test Completed")

def test_GoogleSearch(test_setup):
    # search
    searchField = driver.find_element(By.ID, "APjFqb").send_keys("Automation Step by step")
    time.sleep(5)
    searchButton = driver.find_element(By.NAME, "btnK").click()
    time.sleep(5)
    title = driver.title
    assert title == "Automation Step by step - Google Search"


# def tear_down():
#     # close browser
#     driver.close()
#     driver.quit()
#     print("Test Completed")
