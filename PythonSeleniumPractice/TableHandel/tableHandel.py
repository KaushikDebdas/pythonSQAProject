import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

# web driver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.google.com")
driver.maximize_window()
driver.get("https://trytestingthis.netlify.app/")
time.sleep(2) # 2secnd

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


# close browser
driver.close()
driver.quit()
print("Test Complete")


