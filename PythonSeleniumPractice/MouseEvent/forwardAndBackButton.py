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

action = ActionChains(driver)
driver.get("https://trytestingthis.netlify.app/")
time.sleep(2) # 2secnd
#driver.refresh()
action.click(driver.refresh())
time.sleep(2) # 2secnd
print("Reload")
#driver.back()
action.click(driver.back())
time.sleep(2) # 2secnd
print("Go Back")
driver.get("https://www.google.com")
time.sleep(2) # 2secnd
print("Open New")
#driver.forward()
action.click(driver.forward())
time.sleep(2) # 2secnd
print("Go Forward")
#driver.back()
action.click(driver.back())
time.sleep(2) # 2secnd
print("Go Back")
