from fastapi import APIRouter, Depends, HTTPException, Response, status
from datetime import datetime
from typing import List
from utils import utils
from pymongo.errors import DuplicateKeyError

from schemas.user_schema import UserResponse, UserResponseSession, Register, TokenResponse
from models.user import User
from auth.jwt_config import AuthJWT
from auth.auth_service import create_token, set_cookies, auth_user
from services.user_service import get_user_by_phone, get_user_by_email, delete_user, update_user, get_user, get_all_users, get_next_user_id

router = APIRouter()


@router.get('/users', response_model=List[UserResponseSession])
async def get_users(user_auth: str = Depends(auth_user)):
    users = await get_all_users()
    return [
        UserResponseSession(
            id=user.id,
            first_name=user.first_name,
            last_name=user.last_name,
            date_birth=user.date_birth,
            mobile_phone=user.mobile_phone,
            email=user.email,
            address=user.address,
            session_active=True
        )
        for user in users
    ]


@router.delete('/users/{id_user}', response_model=UserResponse)
async def delete_user_by_id(id_user: int, user_auth: str = Depends(auth_user)):
    deleted_user=await delete_user(id_user)
    return UserResponse(
        first_name=deleted_user.first_name,
        last_name=deleted_user.last_name,
        date_birth=deleted_user.date_birth,
        mobile_phone=deleted_user.mobile_phone,
        email=deleted_user.email,
        password=deleted_user.password,
        address=deleted_user.address,
        session_active=True
    )


@router.put('/users/{id_user}', response_model=UserResponse)
async def update_user_by_id(id_user: int, update_data: Register,user_auth: str = Depends(auth_user)):
    updated_user = await update_user(id_user, update_data.dict())
    return UserResponse(
        first_name=updated_user.first_name,
        last_name=updated_user.last_name,
        date_birth=updated_user.date_birth,
        mobile_phone=updated_user.mobile_phone,
        email=updated_user.email,
        password=updated_user.password,
        address=updated_user.address,
        session_active=True
    )


@router.get('/users/{id_user}', response_model=UserResponseSession)
async def get_user_by_id(id_user: int, user_auth: str = Depends(auth_user)):
    user = await get_user(id_user)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    return UserResponseSession(
        id=user.id,
        first_name=user.first_name,
        last_name=user.last_name,
        date_birth=user.date_birth,
        mobile_phone=user.mobile_phone,
        email=user.email,
        address=user.address,
        session_active=True
    )


@router.post('/users', status_code=status.HTTP_201_CREATED, response_model=UserResponse)
async def create_user(
    credentials: Register, response: Response, Authorize: AuthJWT = Depends(), user_auth: str = Depends(auth_user)
):
    if not utils.is_valid_email(credentials.email):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Invalid email'
        )

    user = await get_user_by_phone(credentials.mobile_phone) or await get_user_by_email(credentials.email)
    if user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail='Account already exists'
        )

    new_user = User(
        id=await get_next_user_id(),
        first_name=credentials.first_name,
        last_name=credentials.last_name,
        date_birth=credentials.date_birth.strftime('%Y-%m-%d'),
        mobile_phone=credentials.mobile_phone,
        email=credentials.email.lower(),
        password=utils.hash_password(credentials.password),
        address=credentials.address,
        created_at=datetime.utcnow()
    )
    try:
        await new_user.create()
    except DuplicateKeyError:
        # Si ocurre un DuplicateKeyError, intentamos con un nuevo ID
        new_user_id = await get_next_user_id() + 1
        new_user.id = new_user_id
        await new_user.create()

    access_token = await create_token(new_user, Authorize)
    await set_cookies(access_token,response)
    new_user.token = access_token
    await new_user.save()

    return UserResponse(
        first_name=new_user.first_name,
        last_name=new_user.last_name,
        date_birth=new_user.date_birth,
        mobile_phone=new_user.mobile_phone,
        email=new_user.email,
        password=new_user.password,
        address=new_user.address,
    )
