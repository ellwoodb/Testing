from firebase import firebase
from firebase_admin import db


firebase_read = firebase.FirebaseApplication(
    'https://rafflescripts-key.firebaseio.com/', None)


key = input("Enter key:\n")


def check_if_key_bound(firebase, key):
    result_keys = firebase.get('Keys', None)
    # print(result_keys)

    result_list = list(result_keys.keys())
    # print(result_list)

    for _ in result_list:
        in_result = firebase.get(f'Keys/{_}', None)
        # print(in_result)
        key_in_result = list(in_result.values())[1]

        if key == key_in_result:
            result_users = firebase.get(f'Keys/{_}', None)
            # print(list(result_users.keys()))
            bound_to_check = list(result_users.values())[0]
            # print(bound_to_check)

            if bound_to_check == "None":
                return _
            else:
                return True
        else:
            return "Wrong key!"


def bind_key_to_user(firebase_read, key):
    if check_if_key_bound(firebase_read, key) is True:
        print("Already bound!")

    elif check_if_key_bound(firebase_read, key) == "Wrong key!":
        print("Wrong key!")

    else:
        right_one = check_if_key_bound(firebase_read, key)
        ref = db.reference()
        ref_ref = ref.child(f"Keys/{right_one}")
        ref_ref.update({
            "bound_to": "not none anymore!"
        })


bind_key_to_user(firebase_read, key)
