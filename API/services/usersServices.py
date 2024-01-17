from bson import ObjectId
from API.config.database import db
from API.models.users import CreateUser
from API.schemas.serializeObjects import serializeDict, serializeList


async def getAllUser() -> list:
    users = serializeList(db.usersData.find())

    return {
        "taille": len(users),
        "users": users
    }


async def getById(id):
    return serializeDict(db.usersData.find_one({"_id": ObjectId(id)}))    


async def InsertUser(data: CreateUser):
    result = db.usersData.insert_one(dict(data))
    
    return serializeDict(db.usersData.find_one({"_id": ObjectId(result.inserted_id)}))