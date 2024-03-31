import time
import datetime
import random
import string

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture()
def test_setup_and_tearDown():
    global driver
    chromeOptions = webdriver.ChromeOptions()
    #chromeOptions.add_argument("--headless")
    driver = webdriver.Chrome(options=chromeOptions)
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo/")
    driver.implicitly_wait(10)
    yield
    driver.close()
    driver.quit()
    print("Test Complete")
def test_login(test_setup_and_tearDown):
    driver.find_element(By.XPATH, "//span[contains(text(),'My Account')]").click()
    time.sleep(2)
    driver.find_element(By.XPATH,"//a[contains(text(),'Login')]").click()
    time.sleep(2)
    # email
    driver.find_element(By.ID, "input-email").send_keys("wokeb44453@irnini.com")
    time.sleep(2)
    # password
    driver.find_element(By.ID, "input-password").send_keys("r6r@635cLzGJae")
    time.sleep(2)
    # login button
    driver.find_element(By.XPATH, "//input[@value='Login']").click()
    time.sleep(2)
    assert driver.find_element(By.LINK_TEXT, "Edit your account information").is_displayed()

# every time generate new email
def generate_email_with_timestamp(prefix="user", domain="example.com"):
    """
    Generate a new email address with a timestamp appended to it.
    Args:
        prefix (str): The prefix part of the email address. Default is "user".
        domain (str): The domain part of the email address. Default is "example.com".
    Returns:
        str: The generated email address with timestamp.
    """
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    email = f"{prefix}_{timestamp}@{domain}"
    return email

# every time generate new password
def generate_random_password(length=12):
    """
    Generate a random password.
    Args:
        length (int): Length of the password. Default is 12.
    Returns:
        str: The generated random password.
    """
    # Define the characters to use for the password
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def test_login_with_invalid_email_and_invalid_password(test_setup_and_tearDown):
    driver.find_element(By.XPATH, "//span[contains(text(),'My Account')]").click()
    time.sleep(2)
    driver.find_element(By.XPATH,"//a[contains(text(),'Login')]").click()
    time.sleep(2)
    # email
    driver.find_element(By.ID, "input-email").send_keys(generate_email_with_timestamp())
    time.sleep(2)
    # password
    driver.find_element(By.ID, "input-password").send_keys(generate_random_password())
    time.sleep(2)
    # login button
    driver.find_element(By.XPATH, "//input[@value='Login']").click()
    time.sleep(2)
    expected_warning_msg = "Warning: No match for E-Mail Address and/or Password."
    assert driver.find_element(By.XPATH, "//body/div[@id='account-login']/div[1]").text.__contains__(expected_warning_msg)

def test_login_with_valid_email_and_invalid_password(test_setup_and_tearDown):
    driver.find_element(By.XPATH, "//span[contains(text(),'My Account')]").click()
    time.sleep(2)
    driver.find_element(By.XPATH,"//a[contains(text(),'Login')]").click()
    time.sleep(2)
    # email
    driver.find_element(By.ID, "input-email").send_keys("wokeb44453@irnini.com")
    time.sleep(2)
    # password
    driver.find_element(By.ID, "input-password").send_keys(generate_random_password())
    time.sleep(2)
    # login button
    driver.find_element(By.XPATH, "//input[@value='Login']").click()
    time.sleep(2)
    expected_warning_msg = "Warning: No match for E-Mail Address and/or Password."
    assert driver.find_element(By.XPATH, "//body/div[@id='account-login']/div[1]").text.__contains__(expected_warning_msg)

def test_login_with_invalid_email_and_valid_password(test_setup_and_tearDown):
    driver.find_element(By.XPATH, "//span[contains(text(),'My Account')]").click()
    time.sleep(2)
    driver.find_element(By.XPATH,"//a[contains(text(),'Login')]").click()
    time.sleep(2)
    # email
    driver.find_element(By.ID, "input-email").send_keys(generate_email_with_timestamp())
    time.sleep(2)
    # password
    driver.find_element(By.ID, "input-password").send_keys("r6r@635cLzGJae")
    time.sleep(2)
    # login button
    driver.find_element(By.XPATH, "//input[@value='Login']").click()
    time.sleep(2)
    expected_warning_msg = "Warning: No match for E-Mail Address and/or Password."
    assert driver.find_element(By.XPATH, "//body/div[@id='account-login']/div[1]").text.__contains__(expected_warning_msg)