from fastapi import FastAPI
from pydantic import BaseModel

from API.database import SessionLocal
from API.models import User
from API.auth import hash_password

from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from API.auth import verify_token

app = FastAPI()


class UserRegister(BaseModel):
    username: str
    email: str
    password: str

security = HTTPBearer()


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):

    token = credentials.credentials

    payload = verify_token(token)

    if payload is None:

        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )

    return payload

@app.get("/views")
def get_views(
    user=Depends(get_current_user)
):

    return [
        "vw_gold_latest_game_performance",
        "vw_gold_publisher_stats",
        "vw_gold_game_performance"
    ]


@app.post("/register")
def register(user: UserRegister):

    db = SessionLocal()

    hashed_password = hash_password(
        user.password
    )

    new_user = User(
        username=user.username,
        email=user.email,
        password_hash=hashed_password
    )

    db.add(new_user)
    db.commit()

    return {
        "message": "User registered successfully"
    }

class UserLogin(BaseModel):

    email: str

    password: str

from API.auth import (
    hash_password,
    verify_password,
    create_access_token
)

@app.post("/login")
def login(user: UserLogin):

    db = SessionLocal()

    db_user = (
        db.query(User)
        .filter(
            User.email == user.email
        )
        .first()
    )

    if not db_user:

        return {
            "message": "Invalid credentials"
        }

    if not verify_password(
        user.password,
        db_user.password_hash
    ):

        return {
            "message": "Invalid credentials"
        }

    token = create_access_token(
        {
            "sub": db_user.email
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }