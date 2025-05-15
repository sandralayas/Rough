from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict

app = FastAPI()

users = {
    "sandra": {
        "username": "johndoe",
        "age": 20,
        "password": "1234",
    },
    "alice": {
        "username": "alice",
        "age": 25,
        "password": "5678",
    },
}

class User(BaseModel):
    username: str
    age: int
    password: str

# class Password(BaseModel):
#     password: str

@app.get("/")
async def start():
    return {"User Login" : "Password"}

@app.post("/user")
async def login(user: User):
    users[user.username] = user.dict()
    return {"message": f"User '{user.username}' created successfully", "user": user}


@app.get("/addition/num1={num1}num2={num2}")
async def root(num1: int ,num2: int ):
    return {"The summation is": num1 + num2}
