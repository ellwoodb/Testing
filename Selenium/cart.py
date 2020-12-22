# START 10 SECONDS BEFORE DROP!!!

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from configparser import ConfigParser
import time
import sys

driver = webdriver.Firefox()

config = ConfigParser()
config.read("./data.ini")

mail = config.get("main", "mail")
password = config.get("main", "password")
product = config.get("main", "product")
size = config.get("main", "size")
loop = config.get("main", "loop")


def Login():
    print("Logging in...")

    driver.get("https://www.zalando.de/login/")

    time.sleep(1)

    Mail_Field = driver.find_element_by_xpath('//*[@id="login.email"]')
    Mail_Field.send_keys(mail)

    Password_Field = driver.find_element_by_xpath('//*[@id="login.password"]')
    Password_Field.send_keys(password)
    Password_Field.send_keys(Keys.ENTER)
    print("Logged in!\n")


def GetSize():
    print("Starting to cart...")
    driver.get(
        "https://www.zalando.de/jordan-air-1-retro-sneaker-high-sailblackdark-mocha-joc11a01l-b11.html")

    time.sleep(1)

    Size_Picker = driver.find_element_by_xpath(
        '//*[@id="picker-trigger"]/span/span')

    Size_Picker.click()

    print("You chose size " + size)

    if size == "40":
        Size = driver.find_element_by_xpath(
            '/html/body/div[5]/div/div[3]/div/form/div/div[7]/div/label/span/div/span')
    if size == "40.5":
        Size = driver.find_element_by_xpath(
            '/html/body/div[5]/div/div[3]/div/form/div/div[8]/div/label/span/div/span')
    if size == "41":
        Size = driver.find_element_by_xpath(
            '/html/body/div[5]/div/div[3]/div/form/div/div[9]/div/label/span/div/span')
    if size == "42":
        Size = driver.find_element_by_xpath(
            '/html/body/div[5]/div/div[3]/div/form/div/div[10]/div/label/span/div/span')

    Size.click()

    print("Size " + size + " chosen!")


def Cart():

    Bag = driver.find_element_by_xpath(
        '/html/body/div[2]/div/div[1]/div/div[2]/div[1]/x-wrapper-re-1-5/div[2]/button/span')

    Bag.click()

    print("Carted!\n")


Login()
GetSize()

if loop == "True":
    for _ in range(2):
        start = time.time()
        Cart()
        end = time.time()
        time_taken = end - start
        print("Process took " + str(round(time_taken, 4)) + " seconds")
elif loop == "False":
    start = time.time()
    Cart()
    end = time.time()
    time_taken = end - start
    print("Process took " + str(round(time_taken, 4)) + " seconds")
