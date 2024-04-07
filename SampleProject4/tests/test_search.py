import time

import pytest
from SampleProject4.pages.page_homepage import HomePage
from SampleProject4.pages.page_search import SearchPage
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("test_setup_and_tearDown")
class TestSearch:
    def test_search_for_valid_product(self):
        # HomePage Class call
        home_page = HomePage(self.driver)
        # search_field
        home_page.enter_search_box_field_name("Hp")
        # self.driver.find_element(By.NAME, "search").send_keys("Hp")
        time.sleep(3)
        print("Hp")
        # search_button
        home_page.click_on_search_button()
        # self.driver.find_element(By.XPATH, "//div[contains(@class,'input-group')]/span/button").click()
        time.sleep(3)
        print("Click")
        # display search product
        search_page = SearchPage(self.driver)
        assert search_page.display_status_of_valid_product()
        # assert self.driver.find_element(By.LINK_TEXT, "HP LP3065").is_displayed()

    def test_search_for_invalid_product(self):
        # HomePage Class call
        home_page = HomePage(self.driver)
        # search_field
        home_page.enter_search_box_field_name("Mobile")
        # self.driver.find_element(By.NAME, "search").send_keys("Mobile")
        time.sleep(3)
        print("Mobile")
        # search_button
        home_page.click_on_search_button()
        # self.driver.find_element(By.XPATH, "//div[contains(@class,'input-group')]/span/button").click()
        time.sleep(3)
        print("Click")
        # display search product
        search_page = SearchPage(self.driver)
        expected_text = "There is no product that matches the search criteria."
        assert search_page.display_status_of_invalid_product().__eq__(expected_text)
        # assert self.driver.find_element(By.XPATH, "//input[@id='button-search']/following-sibling::p").text.__eq__(expected_text)

    def test_search_without_entering_productName(self):
        # HomePage Class call
        home_page = HomePage(self.driver)
        # search_field
        home_page.enter_search_box_field_name("")
        # self.driver.find_element(By.NAME, "search")
        time.sleep(3)
        # search_button
        home_page.click_on_search_button()
        # self.driver.find_element(By.XPATH, "//div[contains(@class,'input-group')]/span/button").click()
        time.sleep(3)
        print("Click")
        # display search product
        search_page = SearchPage(self.driver)
        expected_text = "There is no product that matches the search criteria."
        assert search_page.display_status_of_invalid_product().__eq__(expected_text)
        # assert self.driver.find_element(By.XPATH, "//input[@id='button-search']/following-sibling::p").text.__eq__(expected_text)
