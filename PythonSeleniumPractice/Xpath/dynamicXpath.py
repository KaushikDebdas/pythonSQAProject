import time

from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# web driver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.google.com")
driver.maximize_window()
time.sleep(2) # 2secnd
driver.get("https://omayo.blogspot.com/")
time.sleep(2) # 2secnd

'''
Dynamic Xpath make:
find all the links = //div[@id='LinkList1']//a
find first link = (//div[@id='LinkList1']//a)[1]
find second link = (//div[@id='LinkList1']//a)[2]
'''

links = driver.find_elements(By.XPATH, "//div[@id='LinkList1']//a")

for link in links:
    action = ActionChains(driver)
    action.key_down(Keys.CONTROL).click(link).key_up(Keys.CONTROL).perform()
    time.sleep(5) # 5secnd

# close the browser
driver.close()
driver.quit()
print("Test Complete")
