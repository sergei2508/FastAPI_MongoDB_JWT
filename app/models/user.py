from typing import Optional
from beanie import Document
from pydantic import Field, EmailStr

class User(Document):
    id: int
    first_name: str
    last_name: str
    date_birth: str
    address: str
    token: Optional[str] = None
    password: str = Field(..., max_length=120)
    mobile_phone: str
    email: EmailStr

    class Settings:
        collection = "users"

    class Config:
        arbitrary_types_allowed = True
