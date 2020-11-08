'''
Written by: Daniel Lee
Last updated: Nov 7, 2020
Description: setup drivers
'''
# Keys class provide keys in the keyboard like RETURN, F1, ALT, etc
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime


webLink = "https://onlinebusiness.icbc.com/qmaticwebbooking/#/"
driver = webdriver.Chrome()
driver.get(webLink)
assert "Driver Licensing" in driver.title 

# First Step: select a serivce
# choose the second option
step1 = driver.find_element_by_id("da8488da9b5df26d32ca58c6d6a7973bedd5d98ad052d62b468d3b04b080ea25")
driver.execute_script("arguments[0].click()", step1)

# Second Step: select a location
# choose the first option
driver.implicitly_wait(2)
step2 = driver.find_element_by_css_selector("input[type='radio'][name='v-radio-79']")
driver.execute_script("arguments[0].click()", step2)

# Thrid step: select a date and time
# Get the current Mnnth and Year in May YYYY
x = datetime.datetime.now()
currentYear = x.strftime("%Y")
currentMonth = x.strftime("%B")
currentDay = x.strftime("%d")

# Go to date Page
monthYearCalendarHeaderSelector = '#step3 > div.v-expansion-panel__body > div > div.time-selection-wrapper > div.v-picker.v-card.v-picker--date.date-picker.time-selection-step.v-picker--full-width.theme--light > div > div > div.v-date-picker-header.theme--light > div > div > button'
monthYearDivBtn = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, monthYearCalendarHeaderSelector)))
driver.execute_script("arguments[0].click()", monthYearDivBtn[0])
# BUG? Somehow I had to do it twice
monthYearDivBtn2 = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, monthYearCalendarHeaderSelector)))
driver.execute_script("arguments[0].click()", monthYearDivBtn2[0])

# Select a Year - 2022
yearsSelectionCalendarBodySelector = '#step3 > div.v-expansion-panel__body > div > div.time-selection-wrapper > div.v-picker.v-card.v-picker--date.date-picker.time-selection-step.v-picker--full-width.theme--light > div > div > ul > li:nth-child(100)'
yearSelected = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, yearsSelectionCalendarBodySelector)))
driver.execute_script("arguments[0].click()", yearSelected)

# Select a Month - January
monthsSelectionCalendarBodySelector = '#step3 > div.v-expansion-panel__body > div > div.time-selection-wrapper > div.v-picker.v-card.v-picker--date.date-picker.time-selection-step.v-picker--full-width.theme--light > div > div > div.v-date-picker-table.v-date-picker-table--month.theme--light > table > tbody > tr:nth-child(1) > td:nth-child(1) > button'
monthSelected = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, monthsSelectionCalendarBodySelector)))
driver.execute_script("arguments[0].click()", monthSelected)

# Select a available date

assert "No results found." not in driver.page_source
# driver.close()