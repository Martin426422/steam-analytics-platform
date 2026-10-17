import bcrypt
from jose import jwt
from datetime import datetime, timedelta

def hash_password(password: str):

    salt = bcrypt.gensalt()

    password_hash = bcrypt.hashpw(
        password.encode("utf-8"),
        salt
    )

    return password_hash.decode("utf-8")


def verify_password(
    plain_password: str,
    password_hash: str
):

    return bcrypt.checkpw(
        plain_password.encode("utf-8"),
        password_hash.encode("utf-8")
    )

SECRET_KEY = "steamanalyticssecretkey123"

ALGORITHM = "HS256"

ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(data: dict):

    to_encode = data.copy()

    expire = (
        datetime.utcnow()
        + timedelta(
            minutes=ACCESS_TOKEN_EXPIRE_MINUTES
        )
    )

    to_encode.update(
        {"exp": expire}
    )

    return jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )