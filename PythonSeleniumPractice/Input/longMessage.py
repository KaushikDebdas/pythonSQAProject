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

# text area input
longMessage = driver.find_element(By.XPATH, "//textarea[@name='message']")
time.sleep(2) # 5secnd
longMessage.clear()
time.sleep(2) # 5secnd
longMessage.send_keys("Hi, I am Kaushik Debdas. Nice to meet you")
time.sleep(2) # 5secnd