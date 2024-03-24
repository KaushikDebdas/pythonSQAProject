import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

# web driver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.google.com")
driver.maximize_window()
time.sleep(2) # 2secnd

driver.get("https://demo.opencart.com/admin/")
time.sleep(2)

username = driver.find_element(By.ID, "input-username").send_keys('demo')
password = driver.find_element(By.ID, "input-password").send_keys('demo')
submit_button = driver.find_element(By.XPATH, "//button[@class='btn btn-primary']").click()
time.sleep(5)


button_close = driver.find_element(By.XPATH, "//button[@class='btn-close']").click()
time.sleep(2)

sales_open = driver.find_element(By.XPATH, "//a[contains(text(),'Sales')]").click()
time.sleep(2)

order_open = driver.find_element(By.XPATH, "//a[contains(text(),'Orders')]").click()
time.sleep(2)

'''
In real life, If I want to select CustomerName=Test User. It may not be happend because xpath may be
changed in other day. So how can we do that? 
for this, we need to first select customer column, then match the customer name.
sometime name can be found in table pagination side.
1. Dynamically get how many table pages are there

'''
# dynamic table handel
# driver.find_element(By.XPATH, "//form[@id='form-order']//table//tr[3]//td[1]/input[1]")
expected_customer_name = "dummy dummy"
customer_name = driver.find_elements(By.XPATH, "//form[@id='form-order']//table//tr//td[4]") # print customer column

xpath_text = "//form[@id='form-order']//table//tr/td[contains(text(),'" + expected_customer_name + "')]"

pages_text = driver.find_element(By.XPATH, "//div[contains(text(),'Showing 1 to 10')]").text
start_index = pages_text.index("(")+1
end_index = pages_text.index("Pages)")-1

# print(pages_text[start_index:end_index])
pages = int(pages_text[start_index:end_index])
for page in range(1,pages+1):
    try:
        if driver.find_element(By.XPATH, xpath_text).is_displayed():
            driver.find_element(By.XPATH, xpath_text + "/preceding-sibling::td[3]").click()
            break
    except NoSuchElementException:
        pass

    driver.find_element(By.XPATH, "//li[contains(@class,'active')]/span/following::a[1]")
    time.sleep(5)
# driver.find_element(By.XPATH, xpath_text + "/preceding-sibling::td[3]").click()


time.sleep(5)

# Pause the script and wait for manual intervention
# input("Please solve the CAPTCHA and press Enter to continue...")

# close browser
driver.close()
driver.quit()
print("Test Complete")


