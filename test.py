# x, y, z = "orange", "banana", "cherry"
# print(x)
# print(y)
# print(z)


# x = y = z = "orange"
# print(x)
# print(y)
# print(z)


# def myfunc():
#     global x
#     x = "awsome"
#     print("in func " + x)
# myfunc()
# print(x)


# import random
# print(random.randrange(1, 10))


# x = """Hallo,
# das ist ein Text.
# Gruesse Matthias"""
# print(x)


# x = "Hello, World"
# print(x[1], x[2])


# x = "Hello, World"
# print(x[0:5])


# x = "Hello, World"
# print(x[-5:-2])


# x = "Hello, World"
# print(len(x))


# x = "Hello, World"
# print(x.lower()+"; "+x.upper())


# x = "Hello, World"
# print(x.replace("H", "J"))


# x = "Hello, World"
# print(x.split(","))
# print(x.split(", "))
# y = x.split(",")
# z = y[0].strip(), y[1].strip()
# print(z)


# x = "Hello"
# y = "l" in x
# z = "l" not in x
# print(y)
# print(z)

# x = 5
# y = "Test {}"
# print(y.format(x))


# x = 2
# y = 3
# z = 1
# txt = "Ich haette gerne die {2}, {0} mal mit der {1}"
# print(txt.format(x, y, z))


# \'	Single Quote
# \\	Backslash
# \n	New Line
# \r	Carriage Return
# \t	Tab
# \b	Backspace
# \f	Form Feed
# \ooo	Octal value
# \xhh	Hex value
# txt = "We are the so-called \"Vikings\" from the north."
# print(txt)


# thislist = ["apple", "banana", "cherry"]
# for x in thislist:
#     print(x)


# thisdict = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }
# print(thisdict)
# print(thisdict["brand"])
# for x in thisdict:
#     print(x)
# for x in thisdict:
#     print(thisdict[x])


# username = input("Enter username: ")
# print("Your username is " + username)


# import os
# try:
#     f = open("username.txt", "r")
#     user = f.read()
#     print(f"Hello, {user}!")
# except:
#     username = input("Enter username: ")
#     try:
#         f = open("username.txt", "x")
#         f.write(username)
#         user = f.read()
#         print(f"Hello, {username}")
#         f.write(username)
#     except:
#         f.close()
#         print("Please enter a valid username.")
#         os.remove("username.txt")


# import getpass

# password = getpass.getpass()
# print(f"Dein Password ist: {password}")


import base64
import getpass

password_input = getpass.getpass()
password_encoded = base64.b64encode(password_input.encode("utf-8"))
print(password_encoded)
file = open("test.txt", "w")
file.write(str(password_encoded))
# cGFzc3dvcmQ =

file_reading = open("test.txt", "r")
password_encoded_read = file_reading.read()
password_encoded_one = password_encoded_read.replace("'", "")
password_encoded_two = password_encoded_one.replace("b", "")
password_decoded = base64.b64decode(password_encoded_two).decode("utf-8")
print(password_decoded)
# password


test = "Test"
