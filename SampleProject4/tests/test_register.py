import datetime
import random
import string
import time

import pytest
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("test_setup_and_tearDown")
class TestRegister:
    # every time generate new email
    def generate_email_with_timestamp(self, prefix="user", domain="example.com"):
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
    def generate_random_password(self, length=12):
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

    def generate_bd_mobile_number(self):
        """
        Generate a random Bangladeshi mobile number with country code +880.
        Returns:
            str: The generated mobile number.
        """
        # Bangladeshi mobile numbers have a fixed length of 11 digits
        mobile_number = "+880"
        for _ in range(8):
            mobile_number += str(random.randint(0, 9))
        return mobile_number
    # Generate and print a random Bangladeshi mobile number

    def test_register(self):
        self.driver.find_element(By.XPATH, "//span[contains(text(),'My Account')]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//a[contains(text(),'Register')]").click()
        time.sleep(2)
        # First Name
        self.driver.find_element(By.ID, "input-firstname").send_keys("Kaushik")
        time.sleep(2)
        # Last Name
        self.driver.find_element(By.ID, "input-lastname").send_keys("Debdas")
        time.sleep(2)
        # Email
        email = self.generate_email_with_timestamp()
        print("Randm Email: " + email)
        self.driver.find_element(By.ID, "input-email").send_keys(email)
        time.sleep(2)
        # Telephone
        bd_mobile = self.generate_bd_mobile_number()
        print("Bangladeshi Mobile Number:", bd_mobile)
        self.driver.find_element(By.ID, "input-telephone").send_keys(bd_mobile)
        time.sleep(2)
        # Password
        random_password = self.generate_random_password()
        print("Random Password: " + random_password)
        self.driver.find_element(By.ID, "input-password").send_keys(random_password)
        time.sleep(2)
        # Confirm Password
        self.driver.find_element(By.ID, "input-confirm").send_keys(random_password)
        time.sleep(2)
        # Newsletter Radio Button
        self.driver.find_element(By.XPATH, "//label[@class='radio-inline'][1]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//label[@class='radio-inline'][2]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//label[@class='radio-inline'][1]").click()
        time.sleep(2)
        # Privacy Policy Check Mark
        self.driver.find_element(By.XPATH, "//input[@type='checkbox']").click()
        time.sleep(2)
        # Continue Button
        self.driver.find_element(By.XPATH, "//input[@value='Continue']").click()
        time.sleep(2)
        account_creation_confirm_msg = "Your Account Has Been Created!"
        assert self.driver.find_element(By.XPATH, "//h1[contains(text(),'Your Account Has Been Created!')]").text.__contains__(account_creation_confirm_msg)

    def test_register_with_duplicate_email(self):
        self.driver.find_element(By.XPATH, "//span[contains(text(),'My Account')]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//a[contains(text(),'Register')]").click()
        time.sleep(2)
        # First Name
        self.driver.find_element(By.ID, "input-firstname").send_keys("Kaushik")
        time.sleep(2)
        # Last Name
        self.driver.find_element(By.ID, "input-lastname").send_keys("Debdas")
        time.sleep(2)
        # Email
        self.driver.find_element(By.ID, "input-email").send_keys("wokeb44453@irnini.com")
        time.sleep(2)
        # Telephone
        bd_mobile = self.generate_bd_mobile_number()
        print("Bangladeshi Mobile Number:", bd_mobile)
        self.driver.find_element(By.ID, "input-telephone").send_keys(bd_mobile)
        time.sleep(2)
        # Password
        random_password = self.generate_random_password()
        print("Random Password: " + random_password)
        self.driver.find_element(By.ID, "input-password").send_keys(random_password)
        time.sleep(2)
        # Confirm Password
        self.driver.find_element(By.ID, "input-confirm").send_keys(random_password)
        time.sleep(2)
        # Newsletter Radio Button
        self.driver.find_element(By.XPATH, "//label[@class='radio-inline'][1]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//label[@class='radio-inline'][2]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//label[@class='radio-inline'][1]").click()
        time.sleep(2)
        # Privacy Policy Check Mark
        self.driver.find_element(By.XPATH, "//input[@type='checkbox']").click()
        time.sleep(2)
        # Continue Button
        self.driver.find_element(By.XPATH, "//input[@value='Continue']").click()
        time.sleep(2)
        expected_warning = "Warning: E-Mail Address is already registered!"
        assert self.driver.find_element(By.XPATH, "//body/div[@id='account-register']/div[1]").text.__eq__(expected_warning)

    def test_register_without_entering_any_field(self):
        self.driver.find_element(By.XPATH, "//span[contains(text(),'My Account')]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//a[contains(text(),'Register')]").click()
        time.sleep(2)
        # First Name
        self.driver.find_element(By.ID, "input-firstname").send_keys("")
        time.sleep(2)
        # Last Name
        self.driver.find_element(By.ID, "input-lastname").send_keys("")
        time.sleep(2)
        # Email
        self.driver.find_element(By.ID, "input-email").send_keys("")
        time.sleep(2)
        # Telephone
        self.driver.find_element(By.ID, "input-telephone").send_keys()
        time.sleep(2)
        # Password
        self.driver.find_element(By.ID, "input-password").send_keys()
        time.sleep(2)
        # Confirm Password
        self.driver.find_element(By.ID, "input-confirm").send_keys()
        time.sleep(2)
        # Newsletter Radio Button
        self.driver.find_element(By.XPATH, "//label[@class='radio-inline'][1]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//label[@class='radio-inline'][2]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//label[@class='radio-inline'][1]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//label[@class='radio-inline'][2]").click()
        time.sleep(2)
        # Privacy Policy Check Mark
        # driver.find_element(By.XPATH, "//input[@type='checkbox']").click()
        # time.sleep(2)
        # Continue Button
        self.driver.find_element(By.XPATH, "//input[@value='Continue']").click()
        time.sleep(2)
        # assert privacy policy
        expected_privacy_policy_warning_msg = "Warning: You must agree to the Privacy Policy!"
        assert self.driver.find_element(By.XPATH, "//body/div[@id='account-register']/div[1]").text.__eq__(
            expected_privacy_policy_warning_msg)
        # assert firstname
        expected_firstname_warning_msg = "First Name must be between 1 and 32 characters!"
        assert self.driver.find_element(By.XPATH, "//input[@id='input-firstname']/following-sibling::div").text.__contains__(
            expected_firstname_warning_msg)
        # assert lastname
        expected_lastname_warning_msg = "Last Name must be between 1 and 32 characters!"
        assert self.driver.find_element(By.XPATH, "//input[@id='input-lastname']/following-sibling::div").text.__contains__(
            expected_lastname_warning_msg)
        # assert email
        expected_email_warning_msg = "E-Mail Address does not appear to be valid!"
        assert self.driver.find_element(By.XPATH, "//input[@id='input-email']/following-sibling::div").text.__contains__(
            expected_email_warning_msg)
        # assert telephone
        expected_telephone_warning_msg = "Telephone must be between 3 and 32 characters!"
        assert self.driver.find_element(By.XPATH, "//input[@id='input-telephone']/following-sibling::div").text.__eq__(
            expected_telephone_warning_msg)
        # assert password
        expected_password_warning_msg = "Password must be between 4 and 20 characters!"
        assert self.driver.find_element(By.XPATH, "//input[@id='input-password']/following-sibling::div").text.__contains__(
            expected_password_warning_msg)
