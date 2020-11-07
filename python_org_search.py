'''
Written by: Daniel Lee
Last updated: Nov 7, 2020
Description: setup drivers
'''
# Keys class provide keys in the keyboard like RETURN, F1, ALT, etc
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

webLink = "https://onlinebusiness.icbc.com/qmaticwebbooking/#/"
driver = webdriver.Chrome()
driver.get(webLink)
assert "Driver Licensing" in driver.title 

# First Step: service option
optionB = driver.find_element_by_id("da8488da9b5df26d32ca58c6d6a7973bedd5d98ad052d62b468d3b04b080ea25")
driver.execute_script("arguments[0].click()", optionB)

# Second Step: location
# location = driver.find_element_by_name("v-radio-79")

# Thrid step: date







assert "No results found." not in driver.page_source
driver.close()