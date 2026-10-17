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