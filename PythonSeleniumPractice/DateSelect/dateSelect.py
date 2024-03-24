import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# web driver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.google.com")
driver.maximize_window()
driver.get("https://trytestingthis.netlify.app/")
time.sleep(2) # 2secnd

# date select
date = driver.find_element(By.ID, "day")
time.sleep(2) # 2secnd
# Set the date using JavaScript in the format "YYYY-MM-DD"
driver.execute_script("arguments[0].value = arguments[1]", date, "2024-07-15")
time.sleep(5) # 2secnd


driver.close()
driver.quit()
print("Open")
