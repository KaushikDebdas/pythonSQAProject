import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager



driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.google.com")
driver.maximize_window()
# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# driver.get("https://www.google.com")
# driver.maximize_window()
# test a testing page
driver.get("https://trytestingthis.netlify.app/")
firstName = driver.find_element(By.ID, "fname").send_keys("Rahul")
time.sleep(5) # 5secnd
lastName = driver.find_element(By.ID, "lname").send_keys("Sharkar")
time.sleep(5) # 5secnd
# gender select
male = driver.find_element(By.ID, "male").click()
time.sleep(5) # 5secnd
female = driver.find_element(By.ID, "female").click()
time.sleep(5) # 5secnd
other = driver.find_element(By.ID, "other").click()
time.sleep(5) # 5secnd
male = driver.find_element(By.ID, "male").click()
time.sleep(5) # 5secnd
# Choose an option from DROPDOWN:
# Lets you select only one option
dropdown = driver.find_element(By.ID, "option").click()
time.sleep(5)
dropdown.driver.find_element(By.XPATH, "//option[. = 'Option 1']").click()
time.sleep(5)
dropdown = driver.find_element(By.ID, "option").click()
time.sleep(5)
dropdown.driver.find_element(By.XPATH, "//option[. = 'Option 2']").click()
time.sleep(5)
# select by visible text
#option.select_by_visible_text('Banana')

# select by value
# oneOption.select_by_value('option 1')
time.sleep(5)
# Lets you select multiple options


# xpath
#driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/form/fieldset/button")
# relative xpath
# driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
# time.sleep(5) # 5secnd