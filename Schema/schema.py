from pydantic import BaseModel

class User(BaseModel):
    name: str
    email: str
    age: int

class Bot(BaseModel):
    prompt: str

class Register(BaseModel):
    name: str
    address: str
    email: str
    age: int
    city: str