from fastapi import FastAPI
from app.models.models import User

app = FastAPI()

user = User(name="John Due", id=1)


@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/custom")
def read_custom_message():
    return {"message": "This is a custom message!"}

@app.get("/users")
def read_users():
    return user