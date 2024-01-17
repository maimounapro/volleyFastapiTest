from fastapi import FastAPI
from pymongo.mongo_client import MongoClient
from API.routes.route import router 
from API.routes.usersRoutes import usersRoutes

app = FastAPI(title="Volley-Backend",description = "CRUD API")


app.include_router(router, prefix="/api/v1")
app.include_router(usersRoutes, prefix="/api/v1")