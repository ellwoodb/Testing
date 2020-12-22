userinput = input("Select a number:\n1.\n2.\n3.\n\n")

try:
    x = int(userinput)
except ValueError:
    print("Not a number!")
