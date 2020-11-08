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
# choose the second option
step1 = driver.find_element_by_id("da8488da9b5df26d32ca58c6d6a7973bedd5d98ad052d62b468d3b04b080ea25")
driver.execute_script("arguments[0].click()", step1)

# Second Step:
# choose the first option
driver.implicitly_wait(3)
step2 = driver.find_element_by_css_selector("input[type='radio'][name='v-radio-79']")
driver.execute_script("arguments[0].click()", step2)

#Fourth step
driver.implicitly_wait(5)
last_name= driver.find_element_by_id('LastName')
last_name.clear()
last_name.send_keys("Singh")
first_name= driver.find_element_by_id('FirstName')
first_name.clear()
first_name.send_keys("Sukhwinder")
date_of_birth= driver.find_element_by_id('DOB')
date_of_birth.clear()
date_of_birth.send_keys("19990327")
email= driver.find_element_by_id('Email')
email.clear()
email.send_keys("sukh.dhaliwal.9678@gmail.com")
confirm_email= driver.find_element_by_id('ConfirmEmail')
confirm_email.clear()
confirm_email.send_keys("sukh.dhaliwal.9678@gmail.com")
phone= driver.find_element_by_id('Phone')
phone.clear()
phone.send_keys('0000000000')




assert "No results found." not in driver.page_source
# driver.close()