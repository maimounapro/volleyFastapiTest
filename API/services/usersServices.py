from bson import ObjectId
from API.config.database import db
from API.models.users import UserInDB, UserTemp, User
from API.schemas.serializeObjects import serializeDict, serializeList
from passlib.context import CryptContext
from fastapi import HTTPException, status, Depends
from typing import Optional
from datetime import datetime, timedelta
from API.config.settings import settings
from jose import JWTError, jwt
from API.models.token import TokenData
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

async def getAllUser() -> list:
    users = serializeList(db.usersData.find())

    return {
        "taille": len(users),
        "users": users
    }

async def getById(id):
    return serializeDict(db.usersData.find_one({"_id": ObjectId(id)}))    

async def insertUser(userData: UserTemp):
    # check if pseudo already exists
    if db.usersData.find_one({"pseudo": userData.pseudo}):
        raise HTTPException(
            status_code=409,
            detail="Pseudo already exists",
        )
    hashedPassword = get_password_hash(userData.mdp)
    userInDb = UserInDB(
        pseudo=userData.pseudo,
        age=int(userData.age),
        email=userData.email,
        taille=int(userData.taille),
        poste=userData.poste,
        hashedPassword=hashedPassword
    )
    
    result = db.usersData.insert_one(dict(userInDb))

    return serializeDict(db.usersData.find_one({"_id": ObjectId(result.inserted_id)}))

# Security

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password).encode('utf-8')
    
def authenticate_user(pseudo: str, password: str):
    user = db.usersData.find_one({"pseudo": pseudo})
    if not user:
        return False
    if not verify_password(password, user["hashedPassword"]):
        return False
    return user


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, key=settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    print("encoded_jwt:" + encoded_jwt)
    return encoded_jwt


async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        print("token :", token)
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=settings.ALGORITHM)
        print(payload)
        # TODO : make the decode work
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = db.usersData.find_one({"pseudo":token_data.username})
    if user is None:
        raise credentials_exception
    return user

async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if not current_user.isActive:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user