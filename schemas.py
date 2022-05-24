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


class PostBase(BaseModel):
    title: str
    content: str


class PostRequest(PostBase):
    pass

    class Config:
        orm_mode = True


class PostResponse(PostBase):
    id: int
    user_id: int
    created_at: _datetime.datetime

    class Config:
        orm_mode = True
