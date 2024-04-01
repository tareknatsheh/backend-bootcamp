import utils.db_helper as db
import jwt
import json

AUTH_USERS_DB = "./data/auth_db.json"

def add_auth_user(new_user):
    with open(AUTH_USERS_DB, "r+") as f:
        f.seek(0)
        all_users = json.load(f)

        if new_user["username"] in all_users:
            raise Exception("User already exists")
        # add the user
        user_obj = {
            "username": new_user["username"],
            "password": new_user["password"]
        }
        all_users[new_user["username"]] = user_obj
        
        f.seek(0)        
        json.dump(all_users,f, indent=4)
        f.truncate()
        
        return new_user

def get_data(file_path):
    with open(file_path) as f:
        data = json.load(f)
        return data

def find_user(username) -> dict:
    all_users: dict = get_data(AUTH_USERS_DB)
    if username not in all_users:
        raise Exception("User not found")
    return all_users[username]

def verify_password(stored, from_user) -> bool:
    return stored == from_user

# def verify_password(stored_pass, user_pass):
#     return stored_pass == user_pass

# def prepare_new_user_data(password,username):

#     current_db = db.get_all(AUTH_USERS_DB, "")
#     current_db[username] = {
#         "username":username,
#         "password": hashed_password
#     }
#     return current_db

# def generate_jwt(payload):
#     SECRET_KEY = "your-secret-key"
#     encoded_jwt = jwt.encode(payload, SECRET_KEY, algorithm="HS256")   
#     print('encoded_jwt: ', encoded_jwt)
#     return encoded_jwt

# def verify_jwt(user_jwt):
#     try:
#         SECRET_KEY = "your-secret-key"
#         data = jwt.decode(user_jwt, SECRET_KEY, algorithms="HS256")
#         return data["user role"]
#     except Exception as e:
#         print('e: ', e)
#         print("bad token")
#         return False

# def check_token(request):
#         auth_header = request.headers.get('authorization')
#         if auth_header and auth_header.startswith("Bearer "):
#             token = auth_header.split(" ")[1]
#             try:
#                 if verify_jwt(token):
#                     return request
#             except Exception as e:
#                 raise e
#         return