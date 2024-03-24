from selenium.webdriver.common.by import By

class HomePage():

    def __init__(self, driver):
        self.driver = driver

        self.homepageBody = "//body"
        self.hompageProfileDropdown = "//i[@class='oxd-icon bi-caret-down-fill oxd-userdropdown-icon']"
        self.logoutDropdown = "Logout"

    def click_HomepageProfile(self):
        self.driver.find_element(By.XPATH, self.hompageProfileDropdown).click()

    def click_Logout(self):
        self.driver.find_element(By.LINK_TEXT, self.logoutDropdown)