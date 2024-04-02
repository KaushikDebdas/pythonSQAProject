from selenium.webdriver.common.by import By


class RegisterPage:
    def __init__(self,driver): # constructor
        self.driver = driver

    firstName_field_id = "input-firstname"
    lastName_field_id = "input-lastname"
    email_field_id = "input-email"
    telephone_field_id = "input-telephone"
    password_field_id = "input-password"
    confirm_password_field_id = "input-confirm"
    newsletter_radio_button_yes_xpath = "//label[@class='radio-inline'][1]"
    newsletter_radio_button_no_xpath = "//label[@class='radio-inline'][2]"
    privacy_policy_checkbox_xpath = "//input[@type='checkbox']"
    continue_button_xpath = "//input[@value='Continue']"

    expected_warning_msg_for_duplicate_email_xpath = "//body/div[@id='account-register']/div[1]"
    expected_warning_msg_for_privacy_policy_xpath = "//body/div[@id='account-register']/div[1]"
    expected_warning_msg_for_firstName_xpath = "//input[@id='input-firstname']/following-sibling::div"
    expected_warning_msg_for_lastName_xpath = "//input[@id='input-lastname']/following-sibling::div"
    expected_warning_msg_for_email_xpath = "//input[@id='input-email']/following-sibling::div"
    expected_warning_msg_for_telephone_xpath = "//input[@id='input-telephone']/following-sibling::div"
    expected_warning_msg_for_password_xpath = "//input[@id='input-password']/following-sibling::div"

    def enter_first_name(self, firstname):
        self.driver.find_element(By.ID, self.firstName_field_id).click()
        self.driver.find_element(By.ID, self.firstName_field_id).clear()
        self.driver.find_element(By.ID, self.firstName_field_id).send_keys(firstname)
    def enter_last_name(self, lastname):
        self.driver.find_element(By.ID, self.lastName_field_id).click()
        self.driver.find_element(By.ID, self.lastName_field_id).clear()
        self.driver.find_element(By.ID, self.lastName_field_id).send_keys(lastname)
    def enter_email(self, emailAddress):
        self.driver.find_element(By.ID, self.email_field_id).click()
        self.driver.find_element(By.ID, self.email_field_id).clear()
        self.driver.find_element(By.ID, self.email_field_id).send_keys(emailAddress)
    def enter_telephone(self, telephone):
        self.driver.find_element(By.ID, self.telephone_field_id).click()
        self.driver.find_element(By.ID, self.telephone_field_id).clear()
        self.driver.find_element(By.ID, self.telephone_field_id).send_keys(telephone)
    def enter_password(self, password):
        self.driver.find_element(By.ID, self.password_field_id).click()
        self.driver.find_element(By.ID, self.password_field_id).clear()
        self.driver.find_element(By.ID, self.password_field_id).send_keys(password)
    def enter_confirm_password(self, confirmPassword):
        self.driver.find_element(By.ID, self.confirm_password_field_id).click()
        self.driver.find_element(By.ID, self.confirm_password_field_id).clear()
        self.driver.find_element(By.ID, self.confirm_password_field_id).send_keys(confirmPassword)
    def click_newsletter_yes_radio_button(self):
        self.driver.find_element(By.XPATH, self.newsletter_radio_button_yes_xpath).click()
    def click_newsletter_no_radio_button(self):
        self.driver.find_element(By.XPATH, self.newsletter_radio_button_no_xpath).click()
    def click_privacy_policy_checkbox(self):
        self.driver.find_element(By.XPATH, self.privacy_policy_checkbox_xpath).click()
    def click_continue_button(self):
        self.driver.find_element(By.XPATH, self.continue_button_xpath).click()
    def retrieved_expected_warning_msg_for_duplicate_email(self):
        self.driver.find_element(By.XPATH, self.expected_warning_msg_for_duplicate_email_xpath).text
    def retrieved_expected_warning_msg_for_privacy_policy(self):
        self.driver.find_element(By.XPATH, self.expected_warning_msg_for_privacy_policy_xpath).text
    def retrieved_expected_warning_msg_for_firstName(self):
        self.driver.find_element(By.XPATH, self.expected_warning_msg_for_firstName_xpath).text
    def retrieved_expected_warning_msg_for_lastName(self):
        self.driver.find_element(By.XPATH, self.expected_warning_msg_for_lastName_xpath).text
    def retrieved_expected_warning_msg_for_email(self):
        self.driver.find_element(By.XPATH, self.expected_warning_msg_for_email_xpath).text
    def retrieved_expected_warning_msg_for_telephone(self):
        self.driver.find_element(By.XPATH, self.expected_warning_msg_for_telephone_xpath).text
    def retrieved_expected_warning_msg_for_password(self):
        self.driver.find_element(By.XPATH, self.expected_warning_msg_for_password_xpath).text