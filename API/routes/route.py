from fastapi import APIRouter, status, File, UploadFile
from API.models.tournoi import Tournois, UpdateTournois
from API.config.database import tournois_collection
from API.schemas.schemas import list_tournois
from API.services import tournoisServices as service
from API.services import aws_s3 as s3
from API.helpers.save_picture import save_picture
from API.routes.utils import getResponse, riseHttpExceptionIfNotFound
from bson import objectid
# from datetime import time
import time

router = APIRouter()

base = '/tournois/'
UploadImage = f'{base}image-upload/'

_notFoundMessage = "Could not find tourney with the given Id."

# GET REQUEST
@router.get("/tournois")
async def getTournois():
    return await service.getAllTourney()

@router.get("/tournois/"+"{id}")
async def getTournoi(id):
    return await resultVerification(id)

@router.get("/tournois/"+"{id}"+"/image_url")
def get_tournament_image(id):
    return s3.get_object_url(object_name=id)

@router.post("/tournois")
async def postTournoi(tournoi:Tournois):
    return await service.add_tournament(tournoi)

@router.patch("/tournois/"+"{id}")
async def modifyTournois(id, data: UpdateTournois):
    await resultVerification(id)
    done : bool = await service.modifyTournoi(id, data)
    return getResponse(done, errorMessage="An error occurred while editing the user information.")

@router.delete("/tournois/"+"{id}")
async def deleteTournoi(id):
    await resultVerification(id)
    done : bool = await service.deleteTournoi(id)
    return getResponse(done, errorMessage="An error occurred while editing the user information.")

@router.post(UploadImage+'{id}', status_code=status.HTTP_204_NO_CONTENT)
async def uploadTourneyImage(id, file: UploadFile = File(...)):
    result = await resultVerification(id)
    imageUrl = save_picture(file=file, folderName='tournois', fileName=result["nom"]+"-"+str(result["date"]))
    done = await service.savePicture(id, imageUrl)
    return getResponse(done, errorMessage="An error occurred while saving user image.")



async def resultVerification(id: objectid) -> dict:
    result = await service.getById(id)
    await riseHttpExceptionIfNotFound(result, message=_notFoundMessage)
    return result

# TODO : - microservice pour la recherche et filtre de tournois
# TODO : microservice pour le stockage des flyers








    