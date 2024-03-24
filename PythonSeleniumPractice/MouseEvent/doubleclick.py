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

# double click action
action = ActionChains(driver)
doubleClickbutton = driver.find_element(By.XPATH, "//button[contains(text(),'Double-click me')]")
action.double_click(doubleClickbutton).perform()
time.sleep(5) # 2secnd