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

submitButton = driver.find_element(By.XPATH, "//button[@class='btn btn-success']")
time.sleep(5)
# for this we need to write JS code
driver.execute_script("arguments[0].scrollIntoView(true)", submitButton)
time.sleep(5)