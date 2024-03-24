import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# web driver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.google.com")
driver.maximize_window()
time.sleep(2) # 2secnd
driver.get("https://trytestingthis.netlify.app/")
time.sleep(2) # 2secnd

# radio button select
# gender select
male = driver.find_element(By.ID, "male").click()
time.sleep(2) # 5secnd
female = driver.find_element(By.ID, "female").click()
time.sleep(2) # 5secnd
other = driver.find_element(By.ID, "other").click()
time.sleep(2) # 5secnd
male = driver.find_element(By.ID, "male").click()
time.sleep(2) # 5secnd

driver.close()
driver.quit()
print("Open")
