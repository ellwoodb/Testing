import os.path
from os import write
import time
from termcolor import colored
import sys
import base64
import getpass


username_file_exists = os.path.isfile("username.txt")

if username_file_exists is True:
    readable_file = open("username.txt", "r")
    read_file = readable_file.read()
    print(f"Willkommen zurück, {read_file}!")
elif username_file_exists is False:
    file = open("username.txt", "w")
    writeable_file = open("username.txt", "w")
    userinput = input("Bitte gib deinen Namen ein: ")
    writeable_file.write(userinput)
    writeable_file.close()
    new_readable_file = open("username.txt", "r")
    new_read_file = new_readable_file.read()
    print(f"Willkommen, {new_read_file}!")

password_file_exists = os.path.isfile("password.txt")
password_input = getpass.getpass()

if password_file_exists is True:
    file_reading = open("password.txt", "r")
    password_encoded_read = file_reading.read()
    password_encoded_pre_decode = password_encoded_read.replace(
        "'", "").replace("b", "")
    password_decoded = base64.b64decode(
        password_encoded_pre_decode).decode("utf-8")
    if password_input == password_decoded:
        print("Password korrect.")
    else:
        print("Password falsch!")
        sys.exit(0)
elif password_file_exists is False:
    file_writeing = open("password.txt", "w")
    password_encoded = base64.b64encode(password_input.encode("utf-8"))
    file_writeing.write(str(password_encoded))
    print("Willkommen!")
