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
time.sleep(2)

# retrieving attribute from HTML
getAttribute = driver.find_element(By.NAME, "message").get_attribute("rows")
print("ROWS:", getAttribute)

# close browser
driver.close()
driver.quit()
print("Test Complete")
