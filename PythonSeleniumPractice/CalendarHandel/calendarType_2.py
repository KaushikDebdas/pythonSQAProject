import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

# web driver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.google.com")
driver.maximize_window()
driver.get("https://trytestingthis.netlify.app/")
time.sleep(2) # 2secnd

# using JavaScript
# Set the date using JavaScript in the format "YYYY-MM-DD"
driver.execute_script("document.getElementById('day').value='2023-11-25'")
time.sleep(5) # 2secnd


driver.close()
driver.quit()
print("Test Complete")


