'''
first we need to create a config.ini file in a folder, then
in the config file we have to write our configuration.
We can read and write data from config file.

then, from configparser import ConfigParser..
use ConfigParser()

to read data use config.read("fileName")
to get data use config.get("categoryName", "categoryInputName")
'''
from configparser import ConfigParser

def get_config(category,key):
    config = ConfigParser()
    config.read("config.ini")
    return config.get(category,key)

url_retrieved = get_config("basic info", "url")
print(url_retrieved)

browser_retrieved = get_config("basic info", "browser")
print(browser_retrieved)

search_field_retrieved = get_config("locator search" , "search_field")
print(search_field_retrieved)

search_button_retrieved = get_config("locator search" , "search_button")
print(search_button_retrieved)