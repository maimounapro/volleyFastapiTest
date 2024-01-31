from fastapi import APIRouter, Depends, HTTPException, status
from API.services import usersServices as service
from API.routes.utils import getResponse, riseHttpExceptionIfNotFound
from API.models.users import UserTemp, User
from bson import objectid
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from API.models.token import Token, TokenData
from datetime import datetime, timedelta
from API.config.settings import settings

usersRoutes = APIRouter()
base = "/users"
_notFoundMessage = "Could not find user with the given Id."

@usersRoutes.get(base)
async def getAll():
    return await service.getAllUser()

@usersRoutes.get(base+'/{id}')
async def getById(id):
    return await resultVerification(id)

@usersRoutes.post(base)
async def insertUser(userData: UserTemp):
    return await service.insertUser(userData)

@usersRoutes.post(f"{base}/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = service.authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = service.create_access_token(
        data={"sub": user["pseudo"]}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")

@usersRoutes.get(f"{base}/me/", response_model=User)
async def read_users_me(current_user: User = Depends(service.get_current_active_user)):
    return current_user

async def resultVerification(id: objectid) -> dict:
    result = await service.getById(id)
    await riseHttpExceptionIfNotFound(result, message=_notFoundMessage)
    return result