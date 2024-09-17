from datetime import timedelta
from typing import Callable
from functools import wraps
from fastapi import Response, Depends, HTTPException, status

from models.user import User
from auth.jwt_config import AuthJWT
from settings import settings
from models.user import User
from utils import utils


ACCESS_TOKEN_EXPIRES_IN = settings.ACCESS_TOKEN_EXPIRES_IN


class UserNotFound(Exception):
        pass

async def create_token(user: User,  Authorize: AuthJWT):
    access_token = Authorize.create_access_token(
        subject=str(user.id),
        expires_time=timedelta(minutes=ACCESS_TOKEN_EXPIRES_IN)
    )
    return access_token


async def set_cookies(access_token: str, response: Response):
    if not access_token:
        raise ValueError("Failed to generate access token")

    response.set_cookie(
        key='access_token',
        value=access_token,
        max_age=ACCESS_TOKEN_EXPIRES_IN * 60,
        expires=ACCESS_TOKEN_EXPIRES_IN * 60,
        path='/',
        secure=False,  
        httponly=True,
        samesite='lax'
    )
    response.set_cookie(
        key='logged_in',
        value='True',
        max_age=ACCESS_TOKEN_EXPIRES_IN * 60,
        expires=ACCESS_TOKEN_EXPIRES_IN * 60,
        path='/',
        secure=False,
        httponly=False,
        samesite='lax'
    )

async def verify_user_password(user: User, password: str) -> bool:
    return utils.verify_password(password, user.password)


async def auth_user(Authorize: AuthJWT = Depends()):
    try:
        Authorize.jwt_required()
        user_id = Authorize.get_jwt_subject()

        user = await User.get(str(user_id))

        if not user:
            raise UserNotFound('User no longer exist')

    except Exception as e:
        error = e.__class__.__name__
        print(e)
        if error == 'MissingTokenError':
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail='You are not logged in')
        if error == 'UserNotFound':
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail='User no longer exist')
        if error == 'NotVerified':
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail='Please verify your account')
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail='Token is invalid or has expired')
    return user_id

