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
driver.get("https://the-internet.herokuapp.com/javascript_alerts")

# JS Alert handel
js_Alert = driver.find_element(By.XPATH, "//button[contains(text(),'Click for JS Prompt')]").click()
time.sleep(2)
# Switch to alert IMPORTANT
prompt_alert = driver.switch_to.alert
# print the description of an alert
print(prompt_alert.text)

# send keys in the prompt
prompt_alert.send_keys("Hi, I am Kaushik")
time.sleep(5)

# accept the alert
prompt_alert.accept()
# dismiss the alert
# prompt_alert.dismiss()
time.sleep(2)

# after accept print the result
result = driver.find_element(By.XPATH, "//p[@id='result']").text
time.sleep(2)
print(result)
# close browser
driver.close()
driver.quit()
print("Test Complete")

