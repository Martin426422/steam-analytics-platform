from fastapi import FastAPI
from pydantic import BaseModel

from API.database import SessionLocal
from API.models import User
from API.auth import hash_password

app = FastAPI()


class UserRegister(BaseModel):
    username: str
    email: str
    password: str


@app.get("/")
def root():
    return {
        "message": "Steam Analytics API is running"
    }


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