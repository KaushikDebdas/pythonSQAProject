import time

from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

# web driver setup
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.google.com")
driver.maximize_window()

# test a testing page
# input field first name and last name
driver.get("https://trytestingthis.netlify.app/")
firstName = driver.find_element(By.ID, "fname").send_keys("Rahul")
time.sleep(2) # 5secnd
lastName = driver.find_element(By.ID, "lname").send_keys("Sharkar")
time.sleep(2) # 5secnd

# radio button select
# gender select
male = driver.find_element(By.ID, "male").click()
time.sleep(2) # 5secnd
female = driver.find_element(By.ID, "female").click()
time.sleep(2) # 5secnd
other = driver.find_element(By.ID, "other").click()
time.sleep(2) # 5secnd
male = driver.find_element(By.ID, "male").click()
time.sleep(2) # 5secnd

# Choose an option from DROPDOWN:
# Lets you select only one option
dropdown = driver.find_element(By.ID, "option")
# Create a Select object
select = Select(dropdown)
# Click on the dropdown to open the options
dropdown.click()
# Wait for a bit to ensure the options are loaded
time.sleep(3)
select.select_by_value("option 1")
time.sleep(5)
select.select_by_value("option 2")
time.sleep(5)
select.select_by_value("option 3")
time.sleep(5)
# Lets you select Multiple option
dropdown = driver.find_element(By.ID, "owc")
# Create a Select object
select = Select(dropdown)
# Click on the dropdown to open the options
dropdown.click()
# Wait for a bit to ensure the options are loaded
time.sleep(3)
select.select_by_value("option 1")
time.sleep(5)
select.select_by_value("option 2")
time.sleep(5)
select.select_by_value("option 3")
time.sleep(5)

# checkbox
checkbox = driver.find_element(By.NAME, "option1").click()
time.sleep(5)
checkbox = driver.find_element(By.NAME, "option2").click()
time.sleep(5)
checkbox = driver.find_element(By.NAME, "option3").click()
time.sleep(5)

# date select
# Method 1
# date = driver.find_element(By.ID, "day")
# time.sleep(2) # 2secnd
# Set the date using JavaScript in the format "YYYY-MM-DD"
# driver.execute_script("arguments[0].value = arguments[1]", date, "2024-07-15")
# Method 2
driver.execute_script("document.getElementById('day').value='2023-11-25'") # Method 2
time.sleep(5) # 2secnd

# quantity range select
quantityRange = driver.find_element(By.ID, "quantity")
quantityRange.send_keys("1")
time.sleep(2) # 2secnd
quantityRange.clear()
quantityRange.send_keys("2")
time.sleep(2) # 2secnd
quantityRange.clear()
quantityRange.send_keys("3")
time.sleep(2) # 2secnd
quantityRange.clear()
quantityRange.send_keys("4")
time.sleep(2) # 2secnd
quantityRange.clear()
quantityRange.send_keys("5")
time.sleep(2) # 2secnd

# Long Message
# text area input
longMessage = driver.find_element(By.XPATH, "//textarea[@name='message']")
time.sleep(2) # 5secnd
longMessage.clear()
time.sleep(2) # 5secnd
longMessage.send_keys("Hi, I am Kaushik Debdas. Nice to meet you")
time.sleep(2) # 5secnd

# entire table select
entire_table = driver.find_elements(By.XPATH, "//table")
print("Print Full Table:")
for fullTable in entire_table:
    print(fullTable.text)

# enitre table heading
enitre_table_heading = driver.find_elements(By.XPATH, "//table/tbody/tr/th")
print ("Print Table Heading:")
for tableHeading in enitre_table_heading:
    print(tableHeading.text)

# enitre table data
enitre_table_data = driver.find_elements(By.XPATH, "//table//tbody/tr/td")
print("Print Full Table Data:")
for fullData in enitre_table_data:
    print(fullData.text)

# first row data
firstRow_table_data = driver.find_elements(By.XPATH, "//table/tbody/tr[2]/td")
print("Print First Row Data:")
for firstRow in firstRow_table_data:
    print(firstRow.text)

# third column data
thirdColumn_table_data = driver.find_elements(By.XPATH, "//table/tbody/tr/td[3]")
print("Print Third Column Data:")
for thirdColumn in thirdColumn_table_data:
    print(thirdColumn.text)


# using JavaScript
# Set the date using JavaScript in the format "YYYY-MM-DD"
driver.execute_script("document.getElementById('day').value='2023-11-25'")
time.sleep(5) # 2secnd

# file upload
selectFileOption = driver.find_element(By.ID, "myfile")
time.sleep(5)
selectFileOption.send_keys("E:\\My Documents\\RedDot Digital Limited\\Test Meta Report.xlsx")
time.sleep(5)


# button
# xpath
# //tagname[@attributeName='']
#driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/form/fieldset/button")
# relative xpath
driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
time.sleep(5) # 5secnd

# mouse left click action
action = ActionChains(driver)
hoverHome = driver.find_element(By.XPATH, "//a[contains(text(),'Contact')]")
time.sleep(5) # 2secnd
action.move_to_element(hoverHome).perform()
time.sleep(5) # 2secnd

action.click(hoverHome).perform()
time.sleep(5)

# mouse right click action
action = ActionChains(driver)
hoverHome = driver.find_element(By.XPATH, "//a[contains(text(),'Contact')]")
time.sleep(5) # 2secnd
action.move_to_element(hoverHome).perform()
time.sleep(5) # 2secnd
# for right click use this context_click command
action.context_click(hoverHome).perform()
time.sleep(5)

# double click action
action = ActionChains(driver)
doubleClickbutton = driver.find_element(By.XPATH, "//button[contains(text(),'Double-click me')]")
action.double_click(doubleClickbutton).perform()
time.sleep(5) # 2secnd

# drag and drop action
action = ActionChains(driver)
dragImage = driver.find_element(By.ID, "drag1")
time.sleep(5) # 5secnd
dropImage = driver.find_element(By.XPATH, "//div[@id='div1']")
time.sleep(5) # 5secnd
action.drag_and_drop(dragImage,dropImage).perform()
time.sleep(5)

# select range button
range_button = driver.find_element(By.XPATH, "//input[@type='range']")
time.sleep(5)
size_of_range = range_button.size
print(size_of_range)
# create ActionChains class
action = ActionChains(driver)
# drag and drop by offset for right sight
action.drag_and_drop_by_offset(range_button,20,0).perform()
time.sleep(5)
# drag and drop by offset for left sight
action.drag_and_drop_by_offset(range_button,-20,0).perform()
time.sleep(5)
