import time

import pytest
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
driver.implicitly_wait(10)
# time.sleep(2) # 2secnd

# using diffenet values
@pytest.mark.parametrize("username,password",[
    ("test", "test"),
    ("user1", "pass1"),
    ("user2", "pass2")
])
# @pytest.mark.parametrize("username, password", [
#
# ])

def test_login(username, password):
    # input select
    username = driver.find_element(By.ID, "uname").send_keys(username)
    time.sleep(2)  # 2secnd
    password = driver.find_element(By.ID, "pwd").send_keys(password)
    time.sleep(2)  # 2secnd
    # submit button
    login = driver.find_element(By.XPATH, "//body/div[3]/div[1]/fieldset[1]/form[1]/div[1]/input[3]").click()
    time.sleep(2)  # 2secnd


driver.close()
driver.quit()
print("Open")
