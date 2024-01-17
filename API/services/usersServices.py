from bson import ObjectId
from API.config.database import db
from API.models.users import User, UserInDB
from API.schemas.serializeObjects import serializeDict, serializeList
from passlib.context import CryptContext
from fastapi import HTTPException, status


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

async def getAllUser() -> list:
    users = serializeList(db.usersData.find())

    return {
        "taille": len(users),
        "users": users
    }

async def getById(id):
    return serializeDict(db.usersData.find_one({"_id": ObjectId(id)}))    

async def insertUser(userData: dict):
    required_fields = ["age", "pseudo", "taille", "email", "poste", "mdp"]
    for field in required_fields:
        if field not in userData:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Le champ '{field}' est obligatoire.",
            )
    # check if pseudo already exists
    if db.usersData.find_one({"pseudo": userData["pseudo"]}):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Pseudo already exists",
        )
    hashedPassword = get_password_hash(userData["mdp"])
    userInDb = UserInDB(
        pseudo=userData["pseudo"],
        age=int(userData["age"]),
        email=userData["email"],
        taille=int(userData["taille"]),
        poste=userData["poste"],
        hashedPassword=hashedPassword
    )
    
    result = db.usersData.insert_one(dict(userInDb))

    return serializeDict(db.usersData.find_one({"_id": ObjectId(result.inserted_id)}))

# Security

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)