from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from configparser import ConfigParser
import time
import sys

driver = webdriver.Firefox()
driver.get("")  # Cart page

while True:
    driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 'r')
