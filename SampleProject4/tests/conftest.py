import pytest
from selenium import webdriver


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