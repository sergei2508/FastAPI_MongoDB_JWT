from fastapi import HTTPException
from models.user import User

async def get_user_by_phone(mobile_phone: str,login: bool=False) -> User:
    try:    
        user = await User.find_one(User.mobile_phone == mobile_phone)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"{e}")
    if login and not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


async def get_user_by_email(email: str) -> User:
    user = await User.find_one(User.email == email)
    if not user:
        return None
    return user
