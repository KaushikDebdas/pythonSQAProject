import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# web driver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.google.com")
driver.maximize_window()
driver.get("https://trytestingthis.netlify.app/")
time.sleep(2) # 2secnd

# quantity range select
quantityRange = driver.find_element(By.ID, "quantity")
quantityRange.send_keys("1")
time.sleep(2) # 2secnd
quantityRange.clear()
quantityRange.send_keys("2")
time.sleep(2) # 2secnd
quantityRange.clear()
quantityRange.send_keys("3")
time.sleep(2) # 2secnd
quantityRange.clear()
quantityRange.send_keys("4")
time.sleep(2) # 2secnd
quantityRange.clear()
quantityRange.send_keys("5")
time.sleep(2) # 2secnd

driver.close()
driver.quit()
print("Open")
