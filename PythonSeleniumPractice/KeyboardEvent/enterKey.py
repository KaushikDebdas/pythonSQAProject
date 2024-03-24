import time

from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
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

# press Enter key
# Method 1
# password = driver.find_element(By.ID, "pwd").send_keys(Keys.ENTER)
# time.sleep(2) # 2secnd
# Method 2
action = ActionChains(driver)
action.send_keys(Keys.ENTER).perform()
time.sleep(2) # 2secnd

# close the browser
driver.close()
driver.quit()
print("Test Complete")
