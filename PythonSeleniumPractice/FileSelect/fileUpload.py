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

# file upload
selectFileOption = driver.find_element(By.ID, "myfile")
time.sleep(5)
selectFileOption.send_keys("E:\\My Documents\\RedDot Digital Limited\\Test Meta Report.xlsx")
time.sleep(5)

driver.close()
driver.quit()
print("Testing Complete")
