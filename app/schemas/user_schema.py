from pydantic import BaseModel, EmailStr, validator
from datetime import date
from typing import Optional


class UserResponse(BaseModel):
    first_name: str
    last_name: str
    date_birth: date
    mobile_phone: str
    email: EmailStr
    password: str
    address: str

class UserResponseId(BaseModel):
    id: int
    first_name: str
    last_name: str
    date_birth: date
    mobile_phone: str
    email: EmailStr
    password: str
    address: str

class UserResponseSession(BaseModel):
    id: int
    first_name: str
    last_name: str
    date_birth: date
    mobile_phone: str
    email: EmailStr
    address: str
    session_active: bool = True

class Register(BaseModel):
    first_name: str
    last_name: str
    date_birth: date
    mobile_phone: str
    email: EmailStr
    password: str
    address: str

class Login(BaseModel):
    mobile_phone: str
    password: str


class TokenResponse(BaseModel):
    user: UserResponseId
    access_token: str
    token_type: str