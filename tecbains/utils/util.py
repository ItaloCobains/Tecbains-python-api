import bcrypt

def verify_password(plain_password: bytes, hashed_password: bytes):
    return bcrypt.checkpw(plain_password, hashed_password)
