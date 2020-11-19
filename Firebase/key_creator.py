import time

import firebase_admin
from firebase_admin import credentials, db
import string
import random

letters = string.ascii_letters

cred = credentials.Certificate('./rafflescripts-key-firebase-adminsdk.json')

firebase_admin = firebase_admin.initialize_app(
    cred, {'databaseURL': 'https://rafflescripts-key.firebaseio.com/'})


ref = db.reference()
keys_ref = ref.child('Keys')

amount_input = int(input("Please enter the amount:\n"))


def new_key():
    key = "RS-" + str(''.join(random.choice(letters) for i in range(4))) + "-" + str(''.join(
        random.choice(letters) for i in range(4))) + "-" + str(''.join(random.choice(letters) for i in range(4)))
    return key


for _ in range(amount_input):
    new_key = str(new_key())
    keys_ref.push({
        "key": new_key,
        "bound_to": "None"
    })
    print(f"Key: [ {new_key} ] pushed to database.")
time.sleep(30)
