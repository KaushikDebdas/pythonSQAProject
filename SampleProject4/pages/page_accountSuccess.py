from selenium.webdriver.common.by import By


class AccountSuccessPage:
    def __init__(self,driver): # constructor
        self.driver = driver

    account_creation_msg_success_xpath = "//div[@id='content']/h1"

    def display_status_of_account_creation_msg(self):
        return self.driver.find_element(By.XPATH, self.account_creation_msg_success_xpath).text