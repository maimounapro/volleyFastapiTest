from bson import ObjectId
from API.config.database import db
from API.schemas.serializeObjects import serializeDict, serializeList
from API.models.tournoi import Tournois, UpdateTournois
from pymongo.collection import ReturnDocument
from .aws_s3 import upload_file_into_s3

async def getAllTourney() -> list:
    tournois = serializeList(db.tournois_collection.find())
    return {
        "taille": len(tournois),
        "tournois": tournois
    }

async def getById(id):
    return serializeDict(db.tournois_collection.find_one({"_id": ObjectId(id)})) 

async def savePicture(id, imageUrl: str) -> bool:
    db.tournois_collection.find_one_and_update({"_id": ObjectId(id)}, {"$set": { "imageUrl": imageUrl }})
    return True

async def add_tournament(data: Tournois):
    result = db.tournois_collection.insert_one(dict(data))
    tournoi_id = str(result.inserted_id)
    if data.imageUrl:
        await upload_file_into_s3(image_path=data.imageUrl, object_name=tournoi_id, tournoi_id=tournoi_id)
    return serializeDict(db.tournois_collection.find_one({"_id": ObjectId(result.inserted_id)}))

async def modifyTournoi(id, data: UpdateTournois):
    serializeDict(db.tournois_collection.find_one_and_update(
        {"_id": ObjectId(id)}, 
        {"$set": data.model_dump(exclude_none=True, exclude_unset=True)}, 
        return_document=ReturnDocument.AFTER))
    # TODO : modify imageUrlName
    return True

async def deleteTournoi(id):
    db.tournois_collection.delete_one({"_id": ObjectId(id)})
    return True
