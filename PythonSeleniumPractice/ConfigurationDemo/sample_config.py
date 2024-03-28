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

config = ConfigParser()
config.read("config.ini")

url_retrieved = config.get("basic info" , "url")
print(url_retrieved)
browser_retrieved = config.get("basic info" , "browser")
print(browser_retrieved)

search_field_retrieved = config.get("locator search" , "search_field")
print(search_field_retrieved)
search_button_retrieved = config.get("locator search", "search_button")
print(search_button_retrieved)