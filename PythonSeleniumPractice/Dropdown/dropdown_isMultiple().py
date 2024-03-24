import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

# web driver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.google.com")
driver.maximize_window()
driver.get("https://trytestingthis.netlify.app/")

# Choose multiple option from DROPDOWN:
# Lets you select Multiple option
dropdown = driver.find_element(By.ID, "owc")
# Create a Select object
select = Select(dropdown)
# Click on the dropdown to open the options
dropdown.click()
time.sleep(3)

select.select_by_value("option 1")
time.sleep(5)
select.select_by_value("option 2")
time.sleep(5)
select.select_by_value("option 3")
time.sleep(5)

print(select.is_multiple)

driver.close()
driver.quit()
print("Open")
