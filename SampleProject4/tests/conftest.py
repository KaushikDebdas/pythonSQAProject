import pytest
from SampleProject4.utilites import ReadingConfigurations
from selenium import webdriver

@pytest.fixture()
def test_setup_and_tearDown(request):
    browserName = ReadingConfigurations.read_configuration("basic info","browser")
    if browserName.__eq__("chrome"):
        # Headless Mode
        chromeOptions = webdriver.ChromeOptions()
        #chromeOptions.add_argument("--headless")
        driver = webdriver.Chrome(options=chromeOptions)
    elif browserName.__eq__("firefox"):
        firefoxOptions = webdriver.FirefoxOptions
        # firefoxOptions.add_argument("--headless")
        driver = webdriver.Firefox(options=firefoxOptions)
    elif browserName.__eq__("edge"):
        edgeOptions = webdriver.EdgeOptions
        # edgeOptions.add_argument("--headless")
        driver = webdriver.Firefox(options=edgeOptions)
    else:
        print("provide a valid browser name from chrome/firefox/edge")

    driver.maximize_window()

    app_url = ReadingConfigurations.read_configuration("basic info" , "url")
    driver.get(app_url)
    driver.implicitly_wait(10)

    request.cls.driver = driver # class calling

    yield
    driver.close()
    driver.quit()
    print("Test Complete")