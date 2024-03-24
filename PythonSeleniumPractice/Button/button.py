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

# button
# xpath
# //tagname[@attributeName='']
# driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/form/fieldset/button")
# relative xpath
driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
time.sleep(5)  # 5secnd

driver.close()
driver.quit()
print("Open")
