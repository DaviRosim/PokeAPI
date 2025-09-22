from pymongo.database import Database
from pymongo.collection import Collection

from app.config.database import get_mongo_database, get_mongo_collection
from app.models.pokemon import Pokemon


class PokeRepository:

    def __init__(self):
        self.db: Database = get_mongo_database()
        self.collection: Collection = get_mongo_collection()

    def get_by_id(self, pokemon_id: int):
        return self.collection.find_one({"id": pokemon_id}, {"_id": 0})

    def get(self, page: int = 1, page_size: int = 50):
        skip = (page - 1) * page_size
        return list(self.collection
                    .find({}, {"_id": 0})
                    .skip(skip)
                    .limit(page_size))

    def create(self, pokemon: Pokemon):
        result = self.collection.insert_one(pokemon.model_dump())
        return result.inserted_id

    def update(self, pokemon_id: int, pokemon: Pokemon):
        result = self.collection.update_one(
            {"id": pokemon_id},
            {"$set": pokemon.model_dump()})
        return result.modified_count

    def delete(self, pokemon_id: int):
        result = self.collection.delete_one({"id": pokemon_id})
        return result.deleted_count
