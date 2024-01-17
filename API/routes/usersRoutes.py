from fastapi import APIRouter
from API.services import usersServices as service
from API.routes.utils import getResponse, riseHttpExceptionIfNotFound
from API.models.users import CreateUser
from bson import objectid

usersRoutes = APIRouter()
base = "/users/"
_notFoundMessage = "Could not find user with the given Id."

@usersRoutes.get(base)
async def getAll():
    return await service.getAllUser()

@usersRoutes.get(base+'{id}')
async def getById(id):
    return await resultVerification(id)

@usersRoutes.post(base)
async def InsertUser(data: CreateUser):
    return await service.InsertUser(data)

async def resultVerification(id: objectid) -> dict:
    result = await service.getById(id)
    await riseHttpExceptionIfNotFound(result, message=_notFoundMessage)
    return result