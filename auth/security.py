import hashlib
import json

import jwt

from auth import dao

key = "This is secret key"


class CustomSecurity:
    def registration_new_user(self, login, password):
        pass_hash = hashlib.sha256(password.encode())
        password_hash_to_db = pass_hash.hexdigest()

        newclass = dao.DAO()
        new_user = newclass.create_user_in_db(login, password_hash_to_db)
        return new_user

    def check_user(self, login, password):
        pass_hash = hashlib.sha256(password.encode())
        password_hash_to_db = pass_hash.hexdigest()

        newclass = dao.DAO()
        user_data = newclass.extract_userdata_from_db(login)

        if password_hash_to_db == user_data["hashed_pass"]:
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
