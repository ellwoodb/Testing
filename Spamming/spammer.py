## Version 0.1.1 ##

import pyautogui, time, datetime
from termcolor import colored
from art import *
import sys

tprint("SPAMMER")
time.sleep(3)

print(colored("Usage of the spammer at own risk!\nUsing the spammer can get you banned on the platform you are using it on.\n", "red"))

time.sleep(1)

platform_input = input("Which platform do you want to use the spammer on?\n1) Discord\n2) WhatsApp\nPlatform: ")
if platform_input == "1":
    print("Discord platform choosen (default delay: 1).\n")
    global send_delay
    send_delay = 1
elif platform_input == "2":
    print("WhatsApp platform choosen (default delay: 0).\n")
    send_delay = 0
else:
    print(colored("Wrong input. Closing programm now.", "red"))
    time.sleep(1)
    sys.exit(0)

time.sleep(1)

delay_y_n_input = input("Do you want to use a custom delay? (y/n)\n")
if delay_y_n_input == "y":
    custom_delay_input = input("\nWhich delay do you want to set? (secods)\nDelay: ")
    send_delay = int(custom_delay_input)
elif delay_y_n_input == "n":
    print("Default delay for choosen platform will be used.")
else:
    print(colored("Wrong input. Closing programm now.", "red"))
    time.sleep(1)
    sys.exit(0)

time.sleep(1)

sys.stdout.write("\nStarting 5 sec timer.\r")
time.sleep(1)
sys.stdout.write("Starting 5 sec timer..\r")
time.sleep(1)
sys.stdout.write("Starting 5 sec timer...\n")
time.sleep(1)

print("5")
time.sleep(1)
print("4")
time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1\n")
time.sleep(1)

print(colored("Starting spammer!", "red"))
f = open("Spam_Text.txt", "r")
start = time.time()
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
    # print("test")
    time.sleep(send_delay)
    # print(f"Sleept for {send_delay} seconds.")
end = time.time()
time_taken = end - start
print(colored(f"\nFinished in {round(time_taken)} seconds.", "green"))
time.sleep(10)
print(colored("Closing programm now.", "red"))
time.sleep(3)
sys.exit(0)
