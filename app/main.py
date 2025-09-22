from fastapi import FastAPI
from app.routes.pokemon import router


app = FastAPI()
app.include_router(router)


@app.get("/")
def root():
    return {"message": "Welcome to PokeAPI!"}
