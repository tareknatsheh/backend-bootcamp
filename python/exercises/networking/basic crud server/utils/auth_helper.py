import utils.db_helper as db
from decouple import config
import bcrypt
import json
import jwt
from fastapi import  Header, HTTPException
from typing import Annotated


JWT_SECRET = config("secret")
AUTH_USERS_DB = "./data/auth_db.json"

def hash_password(password: str) -> bytes:
    bytes = password.encode('utf-8') 
    salt = bcrypt.gensalt() 
    hash = bcrypt.hashpw(bytes, salt)
    return hash


def get_user(username) -> dict | None:
    all_users = db.get_data(AUTH_USERS_DB)
    if username in all_users:
        return all_users[username]
    return None

def add_new_user(username: str, password: str, role: str = "guest") -> bool:
    try:
        all_users = db.get_data(AUTH_USERS_DB)
        all_users[username] = {
            "username": username,
            "password": hash_password(password).decode('utf-8'),
            "role": role
        }
        db.write_data(AUTH_USERS_DB, all_users)
        return True
    except Exception as error:
        print(f"Error: {error}")
        return False


def generate_jwt_token(payload) -> str:
    token: str = jwt.encode(payload, JWT_SECRET, algorithm="HS256")
    return token

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
    return bcrypt.checkpw(from_user.encode('utf-8'), stored.encode('utf-8'))


def verify_jwt(user_jwt):
    try:
        data = jwt.decode(user_jwt, JWT_SECRET, algorithms=["HS256"])
        return data["role"]
    except Exception as e:
        print('error: ', e)
        print("bad token")
        raise HTTPException(status_code=498, detail="Invalid token")


async def verify_admin(token: Annotated[str, Header(...)]):
    role = verify_jwt(token)
    return role == "admin"
        # raise HTTPException(status_code=401, detail="You don't have permission")
    
async def verify_user(token: Annotated[str, Header(...)]):
    verify_jwt(token)
    


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