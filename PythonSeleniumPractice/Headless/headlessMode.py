import time


from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# web driver setup MANUAL options
# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# driver.get("https://www.google.com")
# driver.maximize_window()
# driver.get("https://opensource-demo.orangehrmlive.com")
# driver.implicitly_wait(10)


'''
chrome open in headless mode:
in headless mode chorme is running on the background.
it is not showing the UI
'''
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://trytestingthis.netlify.app/")
driver.implicitly_wait(10)
get_title = driver.title
print(get_title)

# close browser
driver.close()