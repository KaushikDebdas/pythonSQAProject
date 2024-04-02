import time

import pytest
from selenium.webdriver.common.by import By
@pytest.mark.usefixtures("test_setup_and_tearDown")
class TestSearch:
    def test_search_for_valid_product(self):
        # search_field
        self.driver.find_element(By.NAME, "search").send_keys("Hp")
        time.sleep(3)
        print("Hp")
        # search_button
        self.driver.find_element(By.XPATH, "//div[contains(@class,'input-group')]/span/button").click()
        time.sleep(3)
        print("Click")
        # display search product
        assert self.driver.find_element(By.LINK_TEXT, "HP LP3065").is_displayed()

    def test_search_for_invalid_product(self):
        # search_field
        self.driver.find_element(By.NAME, "search").send_keys("Mobile")
        time.sleep(3)
        print("Mobile")
        # search_button
        self.driver.find_element(By.XPATH, "//div[contains(@class,'input-group')]/span/button").click()
        time.sleep(3)
        print("Click")
        # display search product
        expected_text = "There is no product that matches the search criteria."
        assert self.driver.find_element(By.XPATH, "//input[@id='button-search']/following-sibling::p").text.__eq__(expected_text)

    def test_search_without_entering_productName(self):
        # search_field
        self.driver.find_element(By.NAME, "search")
        time.sleep(3)
        # search_button
        self.driver.find_element(By.XPATH, "//div[contains(@class,'input-group')]/span/button").click()
        time.sleep(3)
        print("Click")
        # display search product
        expected_text = "There is no product that matches the search criteria."
        assert self.driver.find_element(By.XPATH, "//input[@id='button-search']/following-sibling::p").text.__eq__(expected_text)