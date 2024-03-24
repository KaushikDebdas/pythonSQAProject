from selenium.webdriver.common.by import By

class LoginPage():

    def __init__(self, driver):
        self.driver = driver

        self.username_textbox = "username"
        self.password_textbox = "password"
        self.login_button = "//button[@type='submit']"

    def enter_username(self, username):
        self.driver.find_element(By.NAME, self.username_textbox).clear()
        self.driver.find_element(By.NAME, self.username_textbox).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.NAME, self.password_textbox).clear()
        self.driver.find_element(By.NAME, self.password_textbox).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(By.XPATH, self.login_button).click()