from fastapi import FastAPI
from pymongo.mongo_client import MongoClient
from API.routes.route import router
from API.routes.usersRoutes import usersRoutes
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Volley-Backend", description="CRUD API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(router, prefix="/api/v1")
app.include_router(usersRoutes, prefix="/api/v1")
