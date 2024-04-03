from pydantic import BaseModel


class UserBase(BaseModel):
    rut: str
    email: str
    phone_number: str
    address: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    user_id: int

    class Config:
        orm_mode = True
