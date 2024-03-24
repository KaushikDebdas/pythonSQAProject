import time

from selenium import webdriver
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

search_box = driver.find_element(By.ID, "APjFqb").send_keys("demo opencart")
action = ActionChains(driver)
action.send_keys(Keys.ENTER).perform()
time.sleep(2)

click_opencart_demo = driver.find_element(By.XPATH, "//h3[contains(text(),'OpenCart - Demo')]")
click_opencart_demo.click()
time.sleep(2)

click_adminstration = driver.find_element(By.XPATH, "//body/div[@id='cms-demo']/div[2]/div[1]/div[2]/div[1]/a[1]")
action.move_to_element(click_adminstration).perform()
time.sleep(2)
action.click(click_adminstration).perform()
time.sleep(2)

# Switch to the new window
all_windows = driver.window_handles
driver.switch_to.window(all_windows[1])  # Switch to the new window
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
for this, we need to first select customer column, then match the customer name
'''
# dynamic table handel
# driver.find_element(By.XPATH, "//form[@id='form-order']//table//tr[3]//td[1]/input[1]")
expected_customer_name = "Test User"
customer_name = driver.find_elements(By.XPATH, "//form[@id='form-order']//table//tr//td[4]") # print customer column

xpath_text = driver.find_element(By.XPATH, "//form[@id='form-order']//table//tr/td[contains(text(),"
                                           "'"+expected_customer_name+"')]")
driver.find_element(By.XPATH, xpath_text+"/preceding-sibling::td[3]").click()
time.sleep(5)
print(xpath_text)


# close browser
driver.close()
driver.quit()
print("Test Complete")


