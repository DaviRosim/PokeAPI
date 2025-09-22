from pymongo import MongoClient
from pymongo.database import Database

from settings import get_settings


def get_mongo_client() -> MongoClient:
    mongo_client = MongoClient(get_settings().MONGO_URI)
    return mongo_client


def get_mongo_database() -> Database:
    return get_mongo_client()[get_settings().MONGO_DATABASE]


def close_connection() -> None:
    get_mongo_client().close()
