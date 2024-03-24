import time
# import pytest
import unittest

from selenium import webdriver

from SampleProject3_POM.LogFiles.logfile import LogDetails
from SampleProject3_POM.pages.home_page import HomePage
from SampleProject3_POM.pages.login_page import LoginPage
# from SampleProject3_POM.LogFiles.logfile import log_details

from SampleProject3_POM.LogFiles.logfileSunjid import Logger
logger = Logger()

# log_obj = LogDetails()
# logger = log_obj.get_logger()
# logger.info("This is a sample log message.")



class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # web driver setup MANUAL options
        # cls.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        # cls.driver.get("https://www.google.com")
        # cls.driver.maximize_window()
        # cls.driver.get("https://opensource-demo.orangehrmlive.com")
        # cls.driver.i mplicitly_wait(10)
        '''
        chrome open in headless mode:
        in headless mode chorme is running on the background.
        it is not showing the UI
        '''
        cls.chorme_options = webdriver.ChromeOptions()
        cls.chorme_options.add_argument("--headless")
        cls.driver = webdriver.Chrome(options=cls.chorme_options)
        cls.driver.maximize_window()
        cls.driver.get("https://opensource-demo.orangehrmlive.com")
        cls.driver.implicitly_wait(10)
        cls.log_obj = LogDetails()
        cls.logger = cls.log_obj.get_logger()

    def test_login_valid(self):
        driver = self.driver
        logger.info(driver.title)
        print("printing title"+driver.title )
        logger.info("Starting Login Test.....")

        # login Test
        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login_button()
        time.sleep(10)  # 2secnd
        logger.info("Login Successfully")

        # Take a screenshot of the full homepage
        # first need to know width and height of this page
        # height = driver.execute_script('return document.body.scrollHeight')
        # width = driver.execute_script('return document.body.scrollWidth')
        # driver.set_window_size(width, height)  # the trick
        # take the screenshot
        # driver.save_screenshot("homepage_full_screenshot.png")
        # print("Take Screenshot Successfully")

        # take the screenshot using function
        self.take_fullPageScreenshot(driver, "homepage_full_screenshot.png")
        logger.info("Take Screenshot Successfully")

        # homepage Test
        homepage = HomePage(driver)
        homepage.click_HomepageProfile()
        time.sleep(5)  # 2secnd
        logger.info("Profile Click Successfully")
        # print("Profile Click Successfully")
        homepage.click_Logout()
        time.sleep(10)  # 2secnd
        logger.info("Logout Successfully")
        # print("Logout Successfully")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Complete")

    def take_fullPageScreenshot(self, driver, filename):
        # Take a screenshot of the full homepage
        # first need to know width and height of this page
        height = driver.execute_script('return document.body.scrollHeight')
        width = driver.execute_script('return document.body.scrollWidth')
        driver.set_window_size(width, height)  # the trick

        # take screenshot
        driver.save_screenshot(filename)