import datetime
import random
import string
import time

import pytest
from SampleProject4.pages.page_accountSuccess import AccountSuccessPage
from SampleProject4.pages.page_homepage import HomePage
from SampleProject4.pages.page_register import RegisterPage
from SampleProject4.tests.BaseTest import BaseTest
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("test_setup_and_tearDown")
class TestRegister(BaseTest):
    def test_register(self):
        # HomePage Class Calling
        home_page = HomePage(self.driver)
        # My Account Dropdown Click
        home_page.click_my_account_dropdown_menu()
        # self.driver.find_element(By.XPATH, "//span[contains(text(),'My Account')]").click()
        time.sleep(2)
        # Register Option select
        home_page.click_register_option()
        # self.driver.find_element(By.XPATH,"//a[contains(text(),'Register')]").click()
        time.sleep(2)
        # RegisterPage Class Calling
        register_page = RegisterPage(self.driver)
        # First Name
        register_page.enter_first_name("Kaushik")
        # self.driver.find_element(By.ID, "input-firstname").send_keys("Kaushik")
        time.sleep(2)
        # Last Name
        register_page.enter_last_name("Debdas")
        # self.driver.find_element(By.ID, "input-lastname").send_keys("Debdas")
        time.sleep(2)
        # Email
        random_email = self.generate_email_with_timestamp()
        print("Random Email: " + random_email)
        register_page.enter_email(random_email)
        # self.driver.find_element(By.ID, "input-email").send_keys(random_email)
        time.sleep(2)
        # Telephone
        bd_mobile = self.generate_bd_mobile_number()
        print("Bangladeshi Mobile Number:", bd_mobile)
        register_page.enter_telephone(bd_mobile)
        # self.driver.find_element(By.ID, "input-telephone").send_keys(bd_mobile)
        time.sleep(2)
        # Password
        random_password = self.generate_random_password()
        print("Random Password: " + random_password)
        register_page.enter_password(random_password)
        # self.driver.find_element(By.ID, "input-password").send_keys(random_password)
        time.sleep(2)
        # Confirm Password
        register_page.enter_confirm_password(random_password)
        # self.driver.find_element(By.ID, "input-confirm").send_keys(random_password)
        time.sleep(2)
        # Newsletter Radio Button
        register_page.click_newsletter_yes_radio_button()
        # self.driver.find_element(By.XPATH, "//label[@class='radio-inline'][1]").click()
        time.sleep(2)
        register_page.click_newsletter_no_radio_button()
        # self.driver.find_element(By.XPATH, "//label[@class='radio-inline'][2]").click()
        time.sleep(2)
        register_page.click_newsletter_yes_radio_button()
        # self.driver.find_element(By.XPATH, "//label[@class='radio-inline'][1]").click()
        time.sleep(2)
        # Privacy Policy Check Mark
        register_page.click_privacy_policy_checkbox()
        # self.driver.find_element(By.XPATH, "//input[@type='checkbox']").click()
        time.sleep(2)
        # Continue Button
        register_page.click_continue_button()
        # self.driver.find_element(By.XPATH, "//input[@value='Continue']").click()
        time.sleep(2)

        # AccountSuccessPage Class Calling
        account_create_success_page = AccountSuccessPage(self.driver)
        account_creation_confirm_msg = "Your Account Has Been Created!"
        assert account_create_success_page.display_status_of_account_creation_msg().__contains__(account_creation_confirm_msg)
        # assert self.driver.find_element(By.XPATH, "//div[@id='content']/h1").text.__contains__(account_creation_confirm_msg)

    def test_register_with_duplicate_email(self):
        # HomePage Class Calling
        home_page = HomePage(self.driver)
        # My Account Dropdown Click
        home_page.click_my_account_dropdown_menu()
        # self.driver.find_element(By.XPATH, "//span[contains(text(),'My Account')]").click()
        time.sleep(2)
        # Register Option select
        home_page.click_register_option()
        # self.driver.find_element(By.XPATH,"//a[contains(text(),'Register')]").click()
        time.sleep(2)
        # RegisterPage Class Calling
        register_page = RegisterPage(self.driver)
        # First Name
        register_page.enter_first_name("Kaushik")
        # self.driver.find_element(By.ID, "input-firstname").send_keys("Kaushik")
        time.sleep(2)
        # Last Name
        register_page.enter_last_name("Debdas")
        # self.driver.find_element(By.ID, "input-lastname").send_keys("Debdas")
        time.sleep(2)
        # Email
        register_page.enter_email("wokeb44453@irnini.com")
        # self.driver.find_element(By.ID, "input-email").send_keys("wokeb44453@irnini.com")
        time.sleep(2)
        # Telephone
        bd_mobile = self.generate_bd_mobile_number()
        print("Bangladeshi Mobile Number:", bd_mobile)
        register_page.enter_telephone(bd_mobile)
        # self.driver.find_element(By.ID, "input-telephone").send_keys(bd_mobile)
        time.sleep(2)
        # Password
        random_password = self.generate_random_password()
        print("Random Password: " + random_password)
        register_page.enter_password(random_password)
        # self.driver.find_element(By.ID, "input-password").send_keys(random_password)
        time.sleep(2)
        # Confirm Password
        register_page.enter_confirm_password(random_password)
        # self.driver.find_element(By.ID, "input-confirm").send_keys(random_password)
        time.sleep(2)
        # Newsletter Radio Button
        register_page.click_newsletter_yes_radio_button()
        # self.driver.find_element(By.XPATH, "//label[@class='radio-inline'][1]").click()
        time.sleep(2)
        register_page.click_newsletter_no_radio_button()
        # self.driver.find_element(By.XPATH, "//label[@class='radio-inline'][2]").click()
        time.sleep(2)
        register_page.click_newsletter_yes_radio_button()
        # self.driver.find_element(By.XPATH, "//label[@class='radio-inline'][1]").click()
        time.sleep(2)
        # Privacy Policy Check Mark
        register_page.click_privacy_policy_checkbox()
        # self.driver.find_element(By.XPATH, "//input[@type='checkbox']").click()
        time.sleep(2)
        # Continue Button
        register_page.click_continue_button()
        # self.driver.find_element(By.XPATH, "//input[@value='Continue']").click()
        time.sleep(2)

        expected_warning_for_duplicate_email = "Warning: E-Mail Address is already registered!"
        # assert self.driver.find_element(By.XPATH, "//body/div[@id='account-register']/div[1]").text.__eq__(expected_warning_for_duplicate_email)
        assert register_page.retrieved_expected_warning_msg_for_duplicate_email().__eq__(expected_warning_for_duplicate_email)

    def test_register_without_entering_any_field(self):
        # HomePage Class Calling
        home_page = HomePage(self.driver)
        # My Account Dropdown Click
        home_page.click_my_account_dropdown_menu()
        # self.driver.find_element(By.XPATH, "//span[contains(text(),'My Account')]").click()
        time.sleep(2)
        # Register Option select
        home_page.click_register_option()
        # self.driver.find_element(By.XPATH,"//a[contains(text(),'Register')]").click()
        time.sleep(2)
        # RegisterPage Class Calling
        register_page = RegisterPage(self.driver)
        # First Name
        register_page.enter_first_name("")
        # self.driver.find_element(By.ID, "input-firstname").send_keys("")
        time.sleep(2)
        # Last Name
        register_page.enter_last_name("")
        # self.driver.find_element(By.ID, "input-lastname").send_keys("")
        time.sleep(2)
        # Email
        register_page.enter_email("")
        # self.driver.find_element(By.ID, "input-email").send_keys("")
        time.sleep(2)
        # Telephone
        register_page.enter_telephone("")
        # self.driver.find_element(By.ID, "input-telephone").send_keys("")
        time.sleep(2)
        # Password
        register_page.enter_password("")
        # self.driver.find_element(By.ID, "input-password").send_keys("")
        time.sleep(2)
        # Confirm Password
        register_page.enter_confirm_password("")
        # self.driver.find_element(By.ID, "input-confirm").send_keys("")
        time.sleep(2)
        # Newsletter Radio Button
        register_page.click_newsletter_yes_radio_button()
        # self.driver.find_element(By.XPATH, "//label[@class='radio-inline'][1]").click()
        time.sleep(2)
        register_page.click_newsletter_no_radio_button()
        # self.driver.find_element(By.XPATH, "//label[@class='radio-inline'][2]").click()
        time.sleep(2)
        register_page.click_newsletter_yes_radio_button()
        # self.driver.find_element(By.XPATH, "//label[@class='radio-inline'][1]").click()
        time.sleep(2)
        # Privacy Policy Check Mark
        register_page.click_privacy_policy_checkbox()
        # self.driver.find_element(By.XPATH, "//input[@type='checkbox']").click()
        time.sleep(2)
        # Continue Button
        register_page.click_continue_button()
        # self.driver.find_element(By.XPATH, "//input[@value='Continue']").click()
        time.sleep(2)

        # assert privacy policy
        expected_privacy_policy_warning_msg = "Warning: You must agree to the Privacy Policy!"
        assert register_page.retrieved_expected_warning_msg_for_privacy_policy().__eq__(
            expected_privacy_policy_warning_msg)
        # assert self.driver.find_element(By.XPATH, "//body/div[@id='account-register']/div[1]").text.__eq__(expected_privacy_policy_warning_msg)
        # assert firstname
        expected_firstname_warning_msg = "First Name must be between 1 and 32 characters!"
        assert register_page.retrieved_expected_warning_msg_for_firstName().__eq__(
            expected_firstname_warning_msg)
        # assert self.driver.find_element(By.XPATH, "//input[@id='input-firstname']/following-sibling::div").text.__contains__(expected_firstname_warning_msg)
        # assert lastname
        expected_lastname_warning_msg = "Last Name must be between 1 and 32 characters!"
        assert register_page.retrieved_expected_warning_msg_for_lastName().__eq__(
            expected_lastname_warning_msg)
        # assert self.driver.find_element(By.XPATH, "//input[@id='input-lastname']/following-sibling::div").text.__contains__(
        #     expected_lastname_warning_msg)
        # assert email
        expected_email_warning_msg = "E-Mail Address does not appear to be valid!"
        assert register_page.retrieved_expected_warning_msg_for_email().__eq__(
            expected_email_warning_msg)
        # assert self.driver.find_element(By.XPATH, "//input[@id='input-email']/following-sibling::div").text.__contains__(
        #     expected_email_warning_msg)
        # assert telephone
        expected_telephone_warning_msg = "Telephone must be between 3 and 32 characters!"
        assert register_page.retrieved_expected_warning_msg_for_telephone().__eq__(
            expected_telephone_warning_msg)
        # assert self.driver.find_element(By.XPATH, "//input[@id='input-telephone']/following-sibling::div").text.__eq__(
        #     expected_telephone_warning_msg)
        # assert password
        expected_password_warning_msg = "Password must be between 4 and 20 characters!"
        assert register_page.retrieved_expected_warning_msg_for_password().__eq__(
            expected_password_warning_msg)
        # assert self.driver.find_element(By.XPATH, "//input[@id='input-password']/following-sibling::div").text.__contains__(
        #     expected_password_warning_msg)
