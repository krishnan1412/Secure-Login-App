import bcrypt
import jwt
import os

users = {'admin': bcrypt.hashpw(b'secret', bcrypt.gensalt())}

def verify_user(username, password):
    if username in users:
        return bcrypt.checkpw(password.encode(), users[username])
    return False
