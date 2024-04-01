from fastapi import APIRouter
from decouple import config
from models.auth import Auth_Model
from utils import auth_helper as auth

JWT_SECRET = config("secret")
JWT_HASH = config("hash")

AUTH_USERS_DB = "./data/auth_db.json"

router = APIRouter()

@router.post('/auth/sign_up')
def sign_up(body:Auth_Model):
    new_user = {
        "username": body.username,
        "password": body.password
    }
    user_creation_result = auth.add_auth_user(new_user)

    return user_creation_result

@router.post('/auth/sign_in')
def sign_in(body:Auth_Model):
    user = auth.find_user(body.username)

    if user:
        stored_password = user["password"]
        is_password_correct = auth.verify_password(stored_password, body.password)
        if not is_password_correct:
            return {"msg":"Wrong password","token":None}
        return {"msg":"user sign in successfully","token":None}



# @router.post('/auth/sign_in')
# def sign_in(body:Auth_Model):
#     try:
#         stored_user = auth_helper.find_user_in_db(body.username)
#         if stored_user:
#             stored_pass = stored_user["password"]
#             if auth_helper.verify_password(stored_pass,body.password):
#                 auth_token = auth_helper.generate_jwt({"user role":"guest"})
#                 return {"msg":"user sign in successfully","token":auth_token}
#             else:
#                 return {"msg":"invalid creds"}
#     except Exception as e:
#         print(e)
#         return {"msg": "no such username"}