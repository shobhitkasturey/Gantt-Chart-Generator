import bcrypt
import sqlite3
from database import add_user, validate_user

def register(username, password):
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    try:
        add_user(username, hashed_password) 
        print("User Registered SuccessFully")
    except sqlite3.IntegrityError:
        print("User Already Exists")

def login(username, password):
    user = validate_user(username)
    if user and bcrypt.checkpw(password.encode('utf-8'), user[0]):
        print("Login Successful")
        return True
    else:
        print("Invalid Credentials")
        return False