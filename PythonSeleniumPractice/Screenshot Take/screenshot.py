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

# take a screenshot of a visible web page screen
driver.save_screenshot("visiblePage.png")

# we can also use this command
# driver.get_screenshot_as_file(fullpage.png)

# screenshot of a single web element
headerSS = driver.find_element(By.XPATH, "//div[@class='header']")
headerSS.screenshot("header.png")