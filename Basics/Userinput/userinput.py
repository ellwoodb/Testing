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


# import base64
# import getpass
#
# password_input = getpass.getpass()
# password_encoded = base64.b64encode(password_input.encode("utf-8"))
# print(password_encoded)
# file = open("test.txt", "w")
# file.write(str(password_encoded))
# # cGFzc3dvcmQ =
#
# file_reading = open("test.txt", "r")
# password_encoded_read = file_reading.read()
# password_encoded_one = password_encoded_read.replace("'", "")
# password_encoded_two = password_encoded_one.replace("b", "")
# password_decoded = base64.b64decode(password_encoded_two).decode("utf-8")
# print(password_decoded)
# # password
