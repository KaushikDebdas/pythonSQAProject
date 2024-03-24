import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# web driver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.google.com")
driver.maximize_window()
time.sleep(2) # 2secnd
driver.get("https://tutorialsninja.com/demo/index.php?route=product/product&product_id=47&search=HP")

# lightbox / Popup
popup_image = driver.find_element(By.XPATH, "(//img[@title='HP LP3065'])[1]").click()
time.sleep(2)

close_popup_image = driver.find_element(By.XPATH, "//button[@title='Close (Esc)']").click()
print("Close the image")

# close browser
driver.close()
driver.quit()
print("Test Complete")

