from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

from contextlib import contextmanager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import staleness_of

from pathlib import Path
import os


def construct_headless_chrome_driver():
    options = Options()
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    return webdriver.Chrome(options=options)


@contextmanager
def wait_for_page_load(driver, timeout=30):
    old_page = driver.find_element_by_tag_name('html')
    yield
    WebDriverWait(driver, timeout).until( staleness_of(old_page) )


def test_nonsecret_scenario():
    landing_page = 'https://onlinebusiness.icbc.com/qmaticwebbooking/#/'
    driver = construct_headless_chrome_driver()
    driver.get(landing_page)
    print(driver.title)


    driver.quit()

test_nonsecret_scenario()
# You may want to add additional tests....

