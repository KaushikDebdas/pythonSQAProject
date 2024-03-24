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

# retrieving text
# xpath
# //tagname[@attributeName='']
text_of_element = driver.find_element(By.XPATH, "//div[@class='row']/div[1]/h2").text
time.sleep(5)  # 5secnd
print(text_of_element)

driver.close()
driver.quit()
print("Test Complete")
