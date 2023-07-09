from time import time
from decouple import config
from jose import jwt, jwe
from typing import Dict

JWE_SECRET = str(config("JWE_SECRET"))
JWT_SECRET = str(config("JWT_SECRET"))
JWT_ALGORITHM = 'HS512'


def sign_jwt(info: str) -> Dict[str, str]:
    timestamp = int(time())
    payload = {
        "sub": jwe.encrypt(info, JWE_SECRET, algorithm="dir", encryption="A128GCM").decode("utf-8"),
        "iat": timestamp,
        "exp": timestamp * 3600 * 24
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return {"access_token": token}

def decode_jwt(token: str) -> str:
    decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
    return jwe.decrypt(decoded_token['sub'], JWE_SECRET).decode("utf-8")

def validate_jwt_format(token: str) -> str | None:
    if not token.startswith("Bearer"):
        return None
    
    return token.replace("Bearer ", "")