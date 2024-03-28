'''
Soft assertion is used for if any assertion fails then test don't stop.
- first we need to install a package
    - pip install pytest-soft-assertions
- In command line we have to use
    - pytest -rA --soft-asserts
'''

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

'''
chrome open in headless mode:
in headless mode chorme is running on the background.
it is not showing the UI
'''
def test_tutorialsNinja():
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo/")
    driver.implicitly_wait(10)

    expected_title = "Your Store 123"
    get_title = driver.title
    assert get_title.__eq__(expected_title)
    time.sleep(2)
    print(get_title)

    driver.find_element(By.NAME, "search").send_keys("Hp")
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[contains(@class, 'btn-default')]").click()
    time.sleep(2)
    assert driver.find_element(By.LINK_TEXT, "HP LP3065").is_displayed()
    time.sleep(2)
    # close browser
    driver.close()