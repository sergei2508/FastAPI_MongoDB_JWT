from fastapi_jwt_auth import AuthJWT
from fastapi import APIRouter, Depends, HTTPException, Response, status

from schemas.user_schema import UserResponse, Login
from auth.jwt_config import AuthJWT
from auth.auth_service import create_token, set_cookies, verify_user_password, auth_user
from services.user_service import get_user_by_phone


router = APIRouter()


@router.post('/users/login')
async def login(credentials: Login, response: Response, Authorize: AuthJWT = Depends()):
    user = await get_user_by_phone(credentials.mobile_phone,True)
    if user and not await verify_user_password(user, credentials.password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Incorrect username or password'
        )
    
    access_token = await create_token(user, Authorize)
    await set_cookies(access_token,response)

    user_data = UserResponse(
        first_name=user.first_name,
        last_name=user.last_name,
        session_active=True,
        date_birth=user.date_birth,
        email=user.email,
        mobile_phone=user.mobile_phone,
        password=user.password,
        address=user.address
    )

    return {
        'user': user_data.dict(),
        'access_token': access_token,
        'token_type': 'bearer'
    }


@router.get('/users/logout', status_code=status.HTTP_200_OK)
def logout(response: Response, Authorize: AuthJWT = Depends(), user: str = Depends(auth_user)):
    Authorize.unset_jwt_cookies()
    response.set_cookie('logged_in', '', -1)

    return {'status': 'success'}
