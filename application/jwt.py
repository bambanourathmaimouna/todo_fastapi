from jose import jwt, JWTError
from datetime import datetime, timezone, timedelta

TIME_ACCESS = 5

SECRET_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"
ALGORITHM = "HS256"


def create_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=TIME_ACCESS)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY,algorithm=ALGORITHM)


def decode_token(token: str):
    try:
        payload = jwt.decode(token,SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
     return None