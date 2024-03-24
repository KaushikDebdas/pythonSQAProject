# find element = driver.find_element(BY.ID, "")
# enter text = findelementName.send_keys("Text to Enter")
# Clear text = element.clear()
# Click element = driver.find_element(BY.XPATH, "//button[@class='classValue']".click()
# Enter Key = driver.find_element(BY.ID, "element_id").send_keys(Keys.RETURN)
import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.google.com")
driver.maximize_window()

# find elements
# googleSearchBox = driver.find_element(By.ID, "APjFqb")
# googleSearchBox.send_keys("Web Automation") #send_keys is used for sending data
# #driver.find_element(By.NAME, "q").click()
# googleSearchBox.send_keys(Keys.RETURN) # eta diye auto enter button press kortesi
# time.sleep(5) # 5secnd
# driver.close()
# driver.quit()
# print("Open")

# test a testing page
driver.get("https://trytestingthis.netlify.app/")
firstName = driver.find_element(By.ID, "fname").send_keys("Rahul")
time.sleep(5) # 5secnd
lastName = driver.find_element(By.ID, "lname").send_keys("Sharkar")
time.sleep(5) # 5secnd

# xpath
#driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/form/fieldset/button")
# relative xpath
driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
time.sleep(5) # 5secnd