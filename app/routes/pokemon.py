from fastapi import APIRouter

from app.services import PokeService
from app.models import Pokemon


router = APIRouter(
    prefix="/pokemons",
    tags=["pokemons"],
)

poke_service = PokeService()


@router.get("/")
async def get_all(page: int = 1, page_size: int = 50):
    return poke_service.get(page, page_size)


@router.get("/{pokemon_id}")
async def get_pokemon(pokemon_id: int):
    return poke_service.get_by_id(pokemon_id)


@router.post("/", status_code=201)
async def add_pokemon(pokemon_input: Pokemon):
    return poke_service.create(pokemon_input)


@router.put("/{pokemon_id}")
async def update_pokemon(pokemon_id: int, pokemon: Pokemon):
    return poke_service.update(pokemon_id, pokemon)


@router.delete("/{pokemon_id}")
async def delete_pokemon(pokemon_id: int):
    return poke_service.delete(pokemon_id)
