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

# Choose an option from DROPDOWN:
# Lets you select only one option
dropdown = driver.find_element(By.ID, "option")
# Create a Select object
select = Select(dropdown)

dropdownOptions = select.options # optoins command is used

for op in dropdownOptions:
    op.click() # Click on ALL option
    time.sleep(3)
    print(op.text)

# After clicking all options, select "Option 2"
select.select_by_value("option 2")
time.sleep(3)

# Get the selected option and print it
selected_option = select.first_selected_option.text
print("Selected Option is:", selected_option)
time.sleep(3)

driver.close()
driver.quit()
print("Test Complete")
