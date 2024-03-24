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

# Scroll to the bottom of the page to ensure all elements are loaded
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)  # Wait for the page to settle

# take a screenshot of a full web page
driver.save_screenshot("fullpage.png")

# we can also use this command
# driver.get_screenshot_as_file(fullpage.png)

# screenshot of a single web element
headerSS = driver.find_element(By.XPATH, "//div[@class='header']")
headerSS.screenshot("header.png")