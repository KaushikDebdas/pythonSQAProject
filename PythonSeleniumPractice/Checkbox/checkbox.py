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

# checkbox
checkbox = driver.find_element(By.NAME, "option1").click()
time.sleep(5)
checkbox = driver.find_element(By.NAME, "option2").click()
time.sleep(5)
checkbox = driver.find_element(By.NAME, "option3").click()
time.sleep(5)

driver.close()
driver.quit()
print("Test Complete")
