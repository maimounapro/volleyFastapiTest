from fastapi import FastAPI
from pymongo.mongo_client import MongoClient
from API.routes.route import router 

app = FastAPI()

app.include_router(router, prefix="/api/v1")