from pymongo import MongoClient
from pymongo.database import Database
from pymongo.collection import Collection

from app.config import get_settings


def get_mongo_client() -> MongoClient:
    return MongoClient(get_settings().MONGO_URI)


def get_mongo_database() -> Database:
    return get_mongo_client().get_database(get_settings().MONGO_DATABASE)


def get_mongo_collection() -> Collection:
    return (get_mongo_client()
            .get_database(get_settings().MONGO_DATABASE)
            .get_collection(get_settings().MONGO_COLLECTION))


def close_connection() -> None:
    get_mongo_client().close()
