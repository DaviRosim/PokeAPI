import os


class Settings:
    MONGO_URI: str = os.getenv("MONGO_URI")
    MONGO_DATABASE: str = os.getenv("MONGO_DATABASE")
    MONGO_COLLECTION: str = os.getenv("MONGO_COLLECTION")


def get_settings() -> Settings:
    return Settings()
