from pydantic import BaseModel

class User(BaseModel):
    name: str
    id: int


class FeedBack(BaseModel):
    name: str
    message: str

class UserCreate(BaseModel):
    name: str
    email: str
    age: int
    is_subscribed: bool = None
