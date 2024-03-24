import time


from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# web driver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.google.com")
driver.maximize_window()
time.sleep(2) # 2secnd
driver.get("https://trytestingthis.netlify.app/")

# type some keyword and suggest option select
keyword = driver.find_element(By.XPATH, "//input[@list='datalists']").send_keys('stra')
time.sleep(5) # 2secnd
# Create an ActionChains object
actions = ActionChains(driver)
# actions.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
actions.send_keys(Keys.ARROW_DOWN).perform()
time.sleep(2)
actions.send_keys(Keys.ENTER).perform()
# suggestion = driver.find_element(By.XPATH, "//option[@value='Strawberry']")
time.sleep(2) # 2secnd



driver.quit()
print("Test Complete")
