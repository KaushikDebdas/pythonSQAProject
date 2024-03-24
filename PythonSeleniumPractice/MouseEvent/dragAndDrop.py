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

# drag and drop action
action = ActionChains(driver)
dragImage = driver.find_element(By.ID, "drag1")
time.sleep(5) # 5secnd
dropImage = driver.find_element(By.XPATH, "//div[@id='div1']")
time.sleep(5) # 5secnd
action.drag_and_drop(dragImage,dropImage).perform()
time.sleep(5)