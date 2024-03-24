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

# alert action
popUp = driver.find_element(By.XPATH, "//button[contains(text(),'Your Sample Alert Button!')]").click()
time.sleep(2) # 2secnd
print("Open Alert")
alert = driver.switch_to.alert
# alert.accept()
# time.sleep(2) # 2secnd
# print("OK Button Pressed")
alert.dismiss()
time.sleep(2) # 2secnd
print("Cancel Button Pressed")