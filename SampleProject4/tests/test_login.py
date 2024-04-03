import time
import datetime
import random
import string

import pytest
from SampleProject4.pages.page_accountDetails import AccountDetailsPage
from SampleProject4.pages.page_homepage import HomePage
from SampleProject4.pages.page_login import LoginPage
from SampleProject4.tests.BaseTest import BaseTest
from SampleProject4.utilites import ExcelUtilites
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("test_setup_and_tearDown")
class TestLogin(BaseTest):
    def test_login_with_valid_field(self):
        # log file
        self.log_info("** Starting Test Login with Valid Field **")
        # HomePage Class Calling
        home_page = HomePage(self.driver)
        # My Account Dropdown Click
        home_page.click_my_account_dropdown_menu()
        # self.driver.find_element(By.XPATH, "//span[contains(text(),'My Account')]").click()
        time.sleep(2)
        self.log_info("Click My Account Dropdown")
        # Login Option Select
        home_page.click_login_option()
        # self.driver.find_element(By.XPATH,"//a[contains(text(),'Login')]").click()
        time.sleep(2)
        self.log_info("Click Login Option")

        # LoginPage Class Calling
        login_page = LoginPage(self.driver)
        # email
        valid_email = "wokeb44453@irnini.com"
        login_page.enter_valid_email(valid_email)
        # self.driver.find_element(By.ID, "input-email").send_keys("wokeb44453@irnini.com")
        time.sleep(2)
        self.log_info("Enter Valid Email Address: "+valid_email)
        # password
        valid_password = "r6r@635cLzGJae"
        login_page.enter_valid_password(valid_password)
        # self.driver.find_element(By.ID, "input-password").send_keys("r6r@635cLzGJae")
        time.sleep(2)
        self.log_info("Enter Valid Password: "+valid_password)
        # login button
        login_page.click_login_button()
        # self.driver.find_element(By.XPATH, "//input[@value='Login']").click()
        time.sleep(2)
        self.log_info("Click Login Button")

        # AccountDetailsPage Calling
        account_details = AccountDetailsPage(self.driver)
        # assert self.driver.find_element(By.LINK_TEXT, "Edit your account information").is_displayed()
        assert account_details.display_status_of_edit_your_account_info_option()
        self.log_info("Assertion Successful")
        self.log_info("** Ending Test Login with Valid Field **")

    def test_login_with_invalid_email_and_invalid_password(self):
        self.log_info("** Starting Test Login with Invalid Email and Invalid Password **")
        # HomePage Class Calling
        home_page = HomePage(self.driver)
        # My Account Dropdown Click
        home_page.click_my_account_dropdown_menu()
        # self.driver.find_element(By.XPATH, "//span[contains(text(),'My Account')]").click()
        time.sleep(2)
        self.log_info("Click My Account Dropdown")
        # Login Option Select
        home_page.click_login_option()
        # self.driver.find_element(By.XPATH,"//a[contains(text(),'Login')]").click()
        time.sleep(2)
        self.log_info("Click Login Option")

        # LoginPage Class Calling
        login_page = LoginPage(self.driver)
        # email
        random_email = self.generate_email_with_timestamp()
        print("Random Email: " +random_email)
        login_page.enter_valid_email(random_email)
        # self.driver.find_element(By.ID, "input-email").send_keys(email)
        time.sleep(2)
        self.log_info("Enter Random Email Address: " +random_email)
        # password
        random_password = self.generate_random_password()
        print("Random Password: " + random_password)
        login_page.enter_valid_password(random_password)
        # self.driver.find_element(By.ID, "input-password").send_keys(random_password)
        time.sleep(2)
        self.log_info("Enter Random Password: " +random_password)
        # login button
        login_page.click_login_button()
        # self.driver.find_element(By.XPATH, "//input[@value='Login']").click()
        time.sleep(2)
        self.log_info("Click Login Button")

        expected_warning_msg = "Warning: No match for E-Mail Address and/or Password."
        # assert self.driver.find_element(By.XPATH, "//body/div[@id='account-login']/div[1]").text.__contains__(expected_warning_msg)
        assert login_page.retrieved_warning_msg().__contains__(expected_warning_msg)
        self.log_info("Assertion Successful")
        self.log_info("** Ending Test Login with Invalid Email and Invalid Password **")

    def test_login_with_valid_email_and_invalid_password(self):
        self.log_info("** Starting Test Login with Valid Email and Invalid Password **")
        # HomePage Class Calling
        home_page = HomePage(self.driver)
        # My Account Dropdown Click
        home_page.click_my_account_dropdown_menu()
        # self.driver.find_element(By.XPATH, "//span[contains(text(),'My Account')]").click()
        time.sleep(2)
        self.log_info("Click My Account Dropdown")
        # Login Option Select
        home_page.click_login_option()
        # self.driver.find_element(By.XPATH,"//a[contains(text(),'Login')]").click()
        time.sleep(2)
        self.log_info("Click Login Option")

        # LoginPage Class Calling
        login_page = LoginPage(self.driver)
        # email
        valid_email = "wokeb44453@irnini.com"
        login_page.enter_valid_email(valid_email)
        # self.driver.find_element(By.ID, "input-email").send_keys("wokeb44453@irnini.com")
        time.sleep(2)
        self.log_info("Enter Valid Email Address: " + valid_email)
        # password
        random_password = self.generate_random_password()
        print("Random Password: ", random_password)
        login_page.enter_valid_password(random_password)
        # self.driver.find_element(By.ID, "input-password").send_keys(random_password)
        time.sleep(2)
        self.log_info("Enter Random Password: " +random_password)

        # login button
        self.driver.find_element(By.XPATH, "//input[@value='Login']").click()
        time.sleep(2)
        self.log_info("Click Login Button")

        expected_warning_msg = "Warning: No match for E-Mail Address and/or Password."
        # assert self.driver.find_element(By.XPATH, "//body/div[@id='account-login']/div[1]").text.__contains__(expected_warning_msg)
        assert login_page.retrieved_warning_msg().__contains__(expected_warning_msg)
        self.log_info("Assertion Successful")
        self.log_info("** Ending Test Login with Valid Email and Invalid Password **")

    def test_login_with_invalid_email_and_valid_password(self):
        self.log_info("** Starting Login Test with Invalid Email and Valid Password **")
        # HomePage Class Calling
        home_page = HomePage(self.driver)
        # My Account Dropdown Click
        home_page.click_my_account_dropdown_menu()
        # self.driver.find_element(By.XPATH, "//span[contains(text(),'My Account')]").click()
        time.sleep(2)
        self.log_info("Click My Account Dropdown")
        # Login Option Select
        home_page.click_login_option()
        # self.driver.find_element(By.XPATH,"//a[contains(text(),'Login')]").click()
        time.sleep(2)
        self.log_info("Click Login Option")

        # LoginPage Class Calling
        login_page = LoginPage(self.driver)
        # email
        random_email = self.generate_email_with_timestamp()
        print("Random Email: " + random_email)
        login_page.enter_valid_email(random_email)
        # self.driver.find_element(By.ID, "input-email").send_keys(email)
        time.sleep(2)
        self.log_info("Enter Random Email Address: " + random_email)
        # password
        valid_password = "r6r@635cLzGJae"
        login_page.enter_valid_password(valid_password)
        # self.driver.find_element(By.ID, "input-password").send_keys("r6r@635cLzGJae")
        time.sleep(2)
        self.log_info("Enter Valid Password: " + valid_password)
        # login button
        self.driver.find_element(By.XPATH, "//input[@value='Login']").click()
        time.sleep(2)
        self.log_info("Click Login Button")

        expected_warning_msg = "Warning: No match for E-Mail Address and/or Password."
        # assert self.driver.find_element(By.XPATH, "//body/div[@id='account-login']/div[1]").text.__contains__(expected_warning_msg)
        assert login_page.retrieved_warning_msg().__contains__(expected_warning_msg)
        self.log_info("Assertion Successful")
        self.log_info("** Ending Login Test with Invalid Email and Valid Password **")

    @pytest.mark.parametrize("email_address,password",ExcelUtilites.get_data_from_excel(
        "D:/Study Videos/SQA/Python/pythonSQAProject/SampleProject4/ExcelFiles/DemoLoginExcel.xlsx","LoginTest"))

    def test_login_with_excelFile_data(self,email_address,password):
        self.log_info("** Starting Login Test with Excel File Data **")
        # HomePage Class Calling
        home_page = HomePage(self.driver)
        # My Account Dropdown Click
        home_page.click_my_account_dropdown_menu()
        # self.driver.find_element(By.XPATH, "//span[contains(text(),'My Account')]").click()
        time.sleep(2)
        self.log_info("Click My Account Dropdown")
        # Login Option Select
        home_page.click_login_option()
        # self.driver.find_element(By.XPATH,"//a[contains(text(),'Login')]").click()
        time.sleep(2)
        self.log_info("Click Login Option")

        # LoginPage Class Calling
        login_page = LoginPage(self.driver)
        # email
        login_page.enter_valid_email(email_address)
        # self.driver.find_element(By.ID, "input-email").send_keys("wokeb44453@irnini.com")
        time.sleep(2)
        self.log_info("Read Email from Excel")
        # password
        login_page.enter_valid_password(password)
        # self.driver.find_element(By.ID, "input-password").send_keys("r6r@635cLzGJae")
        time.sleep(2)
        self.log_info("Read Password from Excel")
        # login button
        login_page.click_login_button()
        # self.driver.find_element(By.XPATH, "//input[@value='Login']").click()
        time.sleep(2)
        self.log_info("Click Login Button")

        # AccountDetailsPage Calling
        account_details = AccountDetailsPage(self.driver)
        # assert self.driver.find_element(By.LINK_TEXT, "Edit your account information").is_displayed()
        assert account_details.display_status_of_edit_your_account_info_option()
        self.log_info("Assertion Successful")
        self.log_info("** Ending Login Test with Excel File Data **")