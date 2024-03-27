'''
In Pytest,
- pytest.fixture() by using this, it will mean before run any test, the fixture portion is run first
- marker is: @pytest.fixture()
'''
import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# @pytest.fixture()
# def test_setup():
#     # web driver setup
#     global driver
#     driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#     driver.get("https://www.google.com")
#     driver.maximize_window()
#     driver.get("https://trytestingthis.netlify.app/")
#     yield
#     driver.close()
#     driver.quit()
#     print("Test Complete")

# @pytest.mark.parametrize("username,password",[
#     ("admin" , "admin"),
#     ("test" , "test"),
#     ("kaushik" , "1234"),
#     ("user1" , "pass1")
# ])

# def test_login(test_setup, username, password):
#     # print(username+"-"+password)
#     # input select
#     username = driver.find_element(By.ID, "uname").send_keys(username)
#     time.sleep(2)  # 2secnd
#     password = driver.find_element(By.ID, "pwd").send_keys(password)
#     time.sleep(2)  # 2secnd
#     # submit button
#     login = driver.find_element(By.XPATH, "//body/div[3]/div[1]/fieldset[1]/form[1]/div[1]/input[3]").click()
#     time.sleep(2)  # 2secnd

# SAMPLE TEST
@pytest.fixture()
def test_setup():
    print("Launch Browser")
    print("Open Application")

def test_login_with_valid_credentials(test_setup):
    print("Testing test_login_with_valid_credentials")
def test_login_with_valid_email_and_invalid_password(test_setup):
    print("Testing test_login_with_valid_email_and_invalid_password")
def test_login_with_invalid_email_and_valid_password(test_setup):
    print("Testing test_login_with_invalid_email_and_valid_password")