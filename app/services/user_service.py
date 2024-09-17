from typing import Optional
from beanie import PydanticObjectId
from fastapi import HTTPException
from typing import List

from models.user import User
from schemas.user_schema import UserResponseSession

async def create_user(user_data: dict) -> User:
    user = User(**user_data)
    await user.insert()
    return user


async def get_user_by_phone(mobile_phone: str,login: bool=False) -> User:
    try:    
        user = await User.find_one(User.mobile_phone == mobile_phone)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"{e}")
    if login and not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

async def get_all_users() -> List[UserResponseSession]:
    return await User.find_all().to_list()


async def get_user_by_email(email: str) -> User:
    user = await User.find_one(User.email == email)
    if not user:
        return None
    return user


async def get_user(user_id: int) -> Optional[User]:
    try:
        user = await User.find_one(User.id == user_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail="Invalid user ID")
    return user


async def update_user(user_id: PydanticObjectId, update_data: dict) -> User:
    try:
        user = await User.find_one(User.id == user_id)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid user ID")
    
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if date_birth:=update_data.get("date_birth",False):
        update_data["date_birth"]=date_birth.strftime('%Y-%m-%d')

    if 'email' in update_data:
        existing_user = await get_user_by_email(update_data['email'])
        if existing_user and existing_user.id != user_id:
            raise HTTPException(
                status_code=400, detail="Email already registered")

    if 'mobile_phone' in update_data:
        existing_user = await get_user_by_phone(update_data['mobile_phone'])
        if existing_user and existing_user.id != user_id:
            raise HTTPException(
                status_code=400, detail="Mobile phone already registered")

    for key, value in update_data.items():
        setattr(user, key, value)

    await user.save()
    return user


async def delete_user(user_id: int):
    try:
        user = await User.find_one(User.id == user_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail="Invalid user ID")
    if user:
        await user.delete()
    else:
        raise HTTPException(status_code=404, detail="User not found")
    return user

async def get_next_user_id():
    max_user = await User.find_one(sort=[("id", -1)])
    return max_user.id + 1 if max_user else 1
