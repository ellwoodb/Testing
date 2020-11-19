from firebase_admin import db, credentials
import firebase_admin
from firebase import firebase

firebase = firebase.FirebaseApplication(
    'https://rafflescripts-key.firebaseio.com/', None)

cred = credentials.Certificate('./rafflescripts-key-firebase-adminsdk.json')
firebase_admin = firebase_admin.initialize_app(
    cred, {'databaseURL': 'https://rafflescripts-key.firebaseio.com/'})


class main():
    def __init__(self):
        pass

    def check_if_key_bound(firebase, key):
        result_keys = firebase.get('Keys', None)
        # print(result_keys)

        result_list = list(result_keys.keys())
        # print(result_list[1])

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
                    ref = db.reference()
                    ref_ref = ref.child(f"Keys/{_}")
                    ref_ref.update({
                        "bound_to": "not none anymore!"
                    })
                    print("Bound key.")
                    break
                else:
                    pass
            else:
                pass

        return None


# key = "RS-SwYK-wsEH-WqUC"

# main.check_if_key_bound(firebase, key)
