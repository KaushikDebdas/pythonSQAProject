import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# web driver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.google.com")
driver.maximize_window()
time.sleep(2) # 2secnd
driver.get("https://trytestingthis.netlify.app/")

# select range button
range_button = driver.find_element(By.XPATH, "//input[@type='range']")
time.sleep(5)
size_of_range = range_button.size
print(size_of_range)
# create ActionChains class
action = ActionChains(driver)
# drag and drop by offset for right sight
action.drag_and_drop_by_offset(range_button,20,0).perform()
time.sleep(5)
# drag and drop by offset for left sight
action.drag_and_drop_by_offset(range_button,-20,0).perform()
time.sleep(5)