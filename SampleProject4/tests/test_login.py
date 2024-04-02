import time
import datetime
import random
import string

import pytest
from SampleProject4.pages.page_accountDetails import AccountDetailsPage
from SampleProject4.pages.page_homepage import HomePage
from SampleProject4.pages.page_login import LoginPage
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("test_setup_and_tearDown")
class TestLogin:
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

    def test_login_with_valid_field(self):
        # HomePage Class Calling
        home_page = HomePage(self.driver)
        # My Account Dropdown Click
        home_page.click_my_account_dropdown_menu()
        # self.driver.find_element(By.XPATH, "//span[contains(text(),'My Account')]").click()
        time.sleep(2)
        # Login Option Select
        home_page.click_login_option()
        # self.driver.find_element(By.XPATH,"//a[contains(text(),'Login')]").click()
        time.sleep(2)

        # LoginPage Class Calling
        login_page = LoginPage(self.driver)
        # email
        login_page.enter_valid_email("wokeb44453@irnini.com")
        # self.driver.find_element(By.ID, "input-email").send_keys("wokeb44453@irnini.com")
        time.sleep(2)
        # password
        login_page.enter_valid_password("r6r@635cLzGJae")
        # self.driver.find_element(By.ID, "input-password").send_keys("r6r@635cLzGJae")
        time.sleep(2)
        # login button
        login_page.click_login_button()
        # self.driver.find_element(By.XPATH, "//input[@value='Login']").click()
        time.sleep(2)

        # AccountDetailsPage Calling
        account_details = AccountDetailsPage(self.driver)
        # assert self.driver.find_element(By.LINK_TEXT, "Edit your account information").is_displayed()
        assert account_details.display_status_of_edit_your_account_info_option()

    def test_login_with_invalid_email_and_invalid_password(self):
        # HomePage Class Calling
        home_page = HomePage(self.driver)
        # My Account Dropdown Click
        home_page.click_my_account_dropdown_menu()
        # self.driver.find_element(By.XPATH, "//span[contains(text(),'My Account')]").click()
        time.sleep(2)
        # Login Option Select
        home_page.click_login_option()
        # self.driver.find_element(By.XPATH,"//a[contains(text(),'Login')]").click()
        time.sleep(2)

        # LoginPage Class Calling
        login_page = LoginPage(self.driver)
        # email
        email = self.generate_email_with_timestamp()
        print("Random Email: " + email)
        login_page.enter_valid_email(email)
        # self.driver.find_element(By.ID, "input-email").send_keys(email)
        time.sleep(2)
        # password
        random_password = self.generate_random_password()
        print("Random Password: " + random_password)
        login_page.enter_valid_password(random_password)
        # self.driver.find_element(By.ID, "input-password").send_keys(random_password)
        time.sleep(2)
        # login button
        login_page.click_login_button()
        # self.driver.find_element(By.XPATH, "//input[@value='Login']").click()
        time.sleep(2)

        expected_warning_msg = "Warning: No match for E-Mail Address and/or Password."
        # assert self.driver.find_element(By.XPATH, "//body/div[@id='account-login']/div[1]").text.__contains__(expected_warning_msg)
        assert login_page.retrieved_warning_msg().__contains__(expected_warning_msg)

    def test_login_with_valid_email_and_invalid_password(self):
        # HomePage Class Calling
        home_page = HomePage(self.driver)
        # My Account Dropdown Click
        home_page.click_my_account_dropdown_menu()
        # self.driver.find_element(By.XPATH, "//span[contains(text(),'My Account')]").click()
        time.sleep(2)
        # Login Option Select
        home_page.click_login_option()
        # self.driver.find_element(By.XPATH,"//a[contains(text(),'Login')]").click()
        time.sleep(2)

        # LoginPage Class Calling
        login_page = LoginPage(self.driver)
        # email
        login_page.enter_valid_email("wokeb44453@irnini.com")
        # self.driver.find_element(By.ID, "input-email").send_keys("wokeb44453@irnini.com")
        time.sleep(2)
        # password
        random_password = self.generate_random_password()
        print("Random Password: ", random_password)
        login_page.enter_valid_password(random_password)
        # self.driver.find_element(By.ID, "input-password").send_keys(random_password)
        time.sleep(2)

        # login button
        self.driver.find_element(By.XPATH, "//input[@value='Login']").click()
        time.sleep(2)
        expected_warning_msg = "Warning: No match for E-Mail Address and/or Password."
        # assert self.driver.find_element(By.XPATH, "//body/div[@id='account-login']/div[1]").text.__contains__(expected_warning_msg)
        assert login_page.retrieved_warning_msg().__contains__(expected_warning_msg)

    def test_login_with_invalid_email_and_valid_password(self):
        # HomePage Class Calling
        home_page = HomePage(self.driver)
        # My Account Dropdown Click
        home_page.click_my_account_dropdown_menu()
        # self.driver.find_element(By.XPATH, "//span[contains(text(),'My Account')]").click()
        time.sleep(2)
        # Login Option Select
        home_page.click_login_option()
        # self.driver.find_element(By.XPATH,"//a[contains(text(),'Login')]").click()
        time.sleep(2)

        # LoginPage Class Calling
        login_page = LoginPage(self.driver)
        # email
        email = self.generate_email_with_timestamp()
        print("Random Email: ", email)
        login_page.enter_valid_email(email)
        # self.driver.find_element(By.ID, "input-email").send_keys(email)
        time.sleep(2)
        # password
        login_page.enter_valid_password("r6r@635cLzGJae")
        # self.driver.find_element(By.ID, "input-password").send_keys("r6r@635cLzGJae")
        time.sleep(2)
        # login button
        self.driver.find_element(By.XPATH, "//input[@value='Login']").click()
        time.sleep(2)

        expected_warning_msg = "Warning: No match for E-Mail Address and/or Password."
        # assert self.driver.find_element(By.XPATH, "//body/div[@id='account-login']/div[1]").text.__contains__(expected_warning_msg)
        assert login_page.retrieved_warning_msg().__contains__(expected_warning_msg)