from pydantic import BaseModel, Field


class PokeName(BaseModel):
    english: str = Field(..., examples="Bulbasaur")
    japanese: str = Field(..., examples="フシギダネ")
    chinese: str = Field(..., examples="妙蛙种子")
    french: str = Field(..., examples="Bulbizarre")


class PokeStats(BaseModel):
    hp: int = Field(..., example=45)
    attack: int = Field(..., example=49)
    defense: int = Field(..., example=49)
    sp_Attack: int = Field(..., alias="Sp. Attack", example=65)
    sp_Defense: int = Field(..., alias="Sp. Defense", example=65)
    speed: int = Field(..., example=45)


class PokeType(BaseModel):
    types: list[str] = Field(..., examples=["Grass", "Poison"])


class Pokemon(BaseModel):
    id: int
    name: PokeName
    type: PokeType
    stats: PokeStats
