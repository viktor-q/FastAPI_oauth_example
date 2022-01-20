import hashlib
import json
import jwt

key = "This is secret key"


class CustomSecurity:
    def registration_new_user(self, login, password):
        pass_hash = hashlib.sha256(password.encode())
        password_hash_to_db = pass_hash.hexdigest()

        new_data = {"login": login, "password": password_hash_to_db}

        with open("database.json") as all_users_in_json:
            all_data_about_users = json.load(all_users_in_json)
            all_data_about_users[login] = new_data

        with open("database.json", "w") as database:
            json.dump(all_data_about_users, database)

    def check_user(self, login, password):
        with open("database.json") as all_users_in_json:
            all_data_about_users = json.load(all_users_in_json)

            pass_hash = hashlib.sha256(password.encode())
            password_hash_to_db = pass_hash.hexdigest()

            all_data_one_user = all_data_about_users[login]

            if password_hash_to_db == all_data_one_user["password"]:
                jwtmaker = JwtWorker()
                user_jwt = jwtmaker.generate_jwt(login)
                return {"status": "OK", "jwt": user_jwt}
            else:
                return f"Bad password"

class JwtWorker:
    def generate_jwt(self, login):
        payload_data = {"name": login}
        token = jwt.encode(payload_data, key, algorithm="HS256")
        return token

    def decode_jwt(self, input_jwt):
        decoded_jwt = jwt.decode(input_jwt, key, algorithms="HS256")
        return decoded_jwt
