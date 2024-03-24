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

# Execute JavaScript to get the total height of the page
total_height = driver.execute_script("return document.body.scrollHeight")

# Print the total height
print("Total Height of the Page:", total_height)

# Close the browser
driver.quit()