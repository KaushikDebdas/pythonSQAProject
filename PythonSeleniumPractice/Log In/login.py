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

# input select
username = driver.find_element(By.ID, "uname").send_keys("test")
time.sleep(2) # 5secnd
password = driver.find_element(By.ID, "pwd").send_keys("test")
time.sleep(2) # 5secnd

# submit button
login = driver.find_element(By.XPATH, "//body/div[3]/div[1]/fieldset[1]/form[1]/div[1]/input[3]").click()
time.sleep(2) # 5secnd

driver.close()
driver.quit()
print("Open")
