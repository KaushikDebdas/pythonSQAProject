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
driver.get("https://omayo.blogspot.com/")

# find multiple elements
find_multiple_elements = driver.find_elements(By.XPATH, "//select[@id='multiselect1']/option")
time.sleep(2)
print(len(find_multiple_elements)) #print number of elements
for option in find_multiple_elements:
    print(option.text)

# close browser
driver.close()
driver.quit()
print("Test Complete")

