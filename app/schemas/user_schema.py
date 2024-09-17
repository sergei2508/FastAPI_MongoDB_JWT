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

class Login(BaseModel):
    mobile_phone: str
    password: str
