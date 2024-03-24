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

# find size of an element
find_size_of_image = driver.find_element(By.XPATH, "//div[@class='fakeimg']").size
time.sleep(2)
print(find_size_of_image)

# close browser
driver.close()
driver.quit()
print("Test Complete")

