from pydantic import BaseModel
import datetime as _datetime


class UserBase(BaseModel):
    email: str
    name: str
    phone: str


class UserRequest(UserBase):
    password: str

    class Config:
        orm_mode = True


class UserResponse(UserBase):
    id: int
    created_at: _datetime.datetime

    class Config:
        orm_mode = True
