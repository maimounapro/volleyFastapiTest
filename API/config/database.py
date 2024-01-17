from pymongo import MongoClient
from API.config.settings import settings

client = MongoClient = MongoClient(settings.DATABASE_URL)
print('Connected to MongoDB...')

db = client[settings.MONGO_INITDB_DATABASE]

tournois_collection = db["tournois_collection"]
usersData = db["usersData"]