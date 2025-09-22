import json
from fastapi import HTTPException
from bson.json_util import dumps

from app.repositories.pokemon import PokeRepository
from app.models.pokemon import Pokemon


class PokeService:

    def __init__(self):
        self.__repository: PokeRepository = PokeRepository()

    def get_by_id(self, pokemon_id: int):
        pokemon = self.__repository.get_by_id(pokemon_id)
        pokemon = json.loads(dumps(pokemon))

        if not pokemon:
            raise HTTPException(status_code=404,
                                detail="Pokemon not found")

        return pokemon

    def get(self, page: int, page_size: int):
        pokemons = self.__repository.get(page, page_size)
        pokemons = json.loads(dumps(pokemons))
        return pokemons

    def create(self, pokemon: Pokemon):
        created_pokemon = str(self.__repository.create(pokemon))
        if not created_pokemon:
            raise HTTPException(status_code=400,
                                detail="Error creating pokemon")

        return created_pokemon

    def update(self, pokemon_id: int, pokemon: Pokemon):
        updated_pokemon = self.__repository.update(pokemon_id, pokemon)
        if not updated_pokemon:
            raise HTTPException(status_code=404,
                                detail="Pokemon not found")

        return updated_pokemon

    def delete(self, pokemon_id: int):
        deleted_pokemon = self.__repository.delete(pokemon_id)
        if not deleted_pokemon:
            raise HTTPException(status_code=404,
                                detail="Pokemon not found")

        return deleted_pokemon
