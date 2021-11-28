from pydantic import BaseModel,EmailStr
from datetime import datetime
from pydantic.types import conint
from sqlalchemy.sql.sqltypes import Boolean, String
from typing import Optional
# This is from pydantic library
# Schema/Pydantic model defines the structure of a requrest and the response. 
# This ensures that when a user wants to create a post, the requrest will only go through if it has a title and content in the body. 
# Pydantic model just provides the validation. 

class PostBase(BaseModel):
    title: str
    content: str
    published: bool =True

class PostCreate(PostBase):
    pass

class PostUpdate(PostBase):
    pass

class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True

class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut
    class Config:
        orm_mode = True

class PostOut(BaseModel):
    Post: Post
    votes: int
    class Config:
        orm_mode = True

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None

class Vote(BaseModel):
    post_id: int
    # Less than equal to
    dir: conint(le=1)