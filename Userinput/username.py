import os.path
from os import write
import time
from termcolor import colored
import sys
import base64
import getpass

from PyQt5.QtWidgets import QWidget
from Test_App import *
import sys

## Test if username.txt exists
username_file_exists = os.path.isfile("Userfiles/username.txt")

## If username.txt exists read it an print "Willkommen zurück, {username}!"
if username_file_exists is True:
    readable_file = open("Userfiles/username.txt", "r")
    read_file = readable_file.read()
    print(f"Willkommen zurück, {read_file}!")

## If username.txt doesn't exist create it and ask user for name
elif username_file_exists is False:
    file = open("Userfiles/username.txt", "w")
    writeable_file = open("Userfiles/username.txt", "w")
    userinput = input("Bitte gib deinen Namen ein: ")
    writeable_file.write(userinput)
    writeable_file.close()
    new_readable_file = open("Userfiles/username.txt", "r")
    new_read_file = new_readable_file.read()
    print(f"Willkommen, {new_read_file}!")

## Test if password.txt exist
password_file_exists = os.path.isfile("Userfiles/password.txt")

## Get password input from user
password_input = getpass.getpass()

## If password.txt exists read it and decode it from base64
if password_file_exists is True:
    file_reading = open("Userfiles/password.txt", "r")
    password_encoded_read = file_reading.read()
    password_encoded_pre_decode = password_encoded_read.replace(
        "'", "").replace("b", "")
    password_decoded = base64.b64decode(
        password_encoded_pre_decode).decode("utf-8")

    ##  If pasword input from user is the same as the decoded password from password.txt
    if password_input == password_decoded:
        print("Password korrect.")

        ## Create TestApp class
        class TestApp(Ui_MainWindow):
            def __init__(self, window):
                self.setupUi(window)

        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()

        ui = TestApp(MainWindow)

        ## Show MainWindow
        MainWindow.show()

        ## Execute App
        app.exec_()

    ## If password input from user isn't the same as the decoded password from password.txt
    else:
        print("Password falsch!")

        ## Exit script
        sys.exit(0)

## If password.txt doesn't exist create it and ask for password input from user
elif password_file_exists is False:
    file_writeing = open("Userfiles/password.txt", "w")
    password_encoded = base64.b64encode(password_input.encode("utf-8"))
    file_writeing.write(str(password_encoded))
    print("Willkommen!")
