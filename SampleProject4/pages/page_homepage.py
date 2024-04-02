from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self,driver): # constructor
        self.driver = driver

    search_box_field_name = "search"
    search_button_xpath = "//div[contains(@class,'input-group')]/span/button"
    my_account_dropdown_menu_xpath = "//span[contains(text(),'My Account')]"
    login_option_xpath = "//a[contains(text(),'Login')]"

    def enter_search_box_field_name(self, productName):
        self.driver.find_element(By.NAME, self.search_box_field_name).click()
        self.driver.find_element(By.NAME, self.search_box_field_name).clear()
        self.driver.find_element(By.NAME, self.search_box_field_name).send_keys(productName)

    def click_on_search_button(self):
        self.driver.find_element(By.XPATH, self.search_button_xpath).click()

    def click_my_account_dropdown_menu(self):
        self.driver.find_element(By.XPATH, self.my_account_dropdown_menu_xpath).click()

    def click_login_option(self):
        self.driver.find_element(By.XPATH, self.login_option_xpath).click()