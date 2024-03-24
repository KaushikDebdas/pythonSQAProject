import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

# web driver setup
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.google.com")
driver.maximize_window()
driver.get("https://trytestingthis.netlify.app/")

# input field first name and last name
firstName = driver.find_element(By.ID, "fname").send_keys("Rahul")
time.sleep(2) # 5secnd
lastName = driver.find_element(By.ID, "lname").send_keys("Sharkar")
time.sleep(2) # 5secnd