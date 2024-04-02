from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self,driver): # constructor
        self.driver = driver

    email_field_id = "input-email"
    password_field_id = "input-password"
    login_button_click_xpath = "//input[@value='Login']"
    warning_msg_xpath = "//body/div[@id='account-login']/div[1]"

    def enter_valid_email(self,email_address):
        self.driver.find_element(By.ID, self.email_field_id).click()
        self.driver.find_element(By.ID, self.email_field_id).clear()
        self.driver.find_element(By.ID, self.email_field_id).send_keys(email_address)
    def enter_valid_password(self,password):
        self.driver.find_element(By.ID, self.password_field_id).click()
        self.driver.find_element(By.ID, self.password_field_id).clear()
        self.driver.find_element(By.ID, self.password_field_id).send_keys(password)
    def click_login_button(self):
        self.driver.find_element(By.XPATH, self.login_button_click_xpath).click()
    def retrieved_warning_msg(self):
        return self.driver.find_element(By.XPATH, self.warning_msg_xpath).text