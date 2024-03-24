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

# mouse left click action
action = ActionChains(driver)
hoverHome = driver.find_element(By.XPATH, "//a[contains(text(),'Contact')]")
time.sleep(5) # 2secnd
action.move_to_element(hoverHome).perform()
time.sleep(5) # 2secnd

action.click(hoverHome).perform()
time.sleep(5)

# browser close
driver.close()