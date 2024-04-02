from selenium.webdriver.common.by import By


class AccountDetailsPage:
    def __init__(self,driver): # constructor
        self.driver = driver

    edit_your_account_info_link_text = "Edit your account information"

    def display_status_of_edit_your_account_info_option(self):
        return self.driver.find_element(By.LINK_TEXT, self.edit_your_account_info_link_text).is_displayed()