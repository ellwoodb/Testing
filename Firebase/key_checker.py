from firebase import firebase
import os

firebase = firebase.FirebaseApplication(
    'https://rafflescripts-ef450.firebaseio.com/', None)
result = firebase.get('Keys', None)

result_list = list(result.values())

key_list = []

for i in range(len(result_list)):
    x = result_list[i]["key"]
    key_list.append(x)

print(key_list)


def key_checker(keys):
    if not app.key_exists:
        key_input = input("Please enter your key:\n")
        if not key_input in keys:
            KeyError.KeyWrong()
        else:
            file = open("key.txt", "w")
            file.write(key_input)
            print("Right Key!")
            file.close()

    else:
        file = open("key.txt", "r")
        key = file.read()
        if not key in keys:
            KeyError.KeyWrong()
        else:
            print("Key right!")
        file.close()


key_checker(key_list)
