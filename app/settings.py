from pydantic import BaseSettings
import os


class Settings(BaseSettings):
    DATABASE_URL: str = os.environ.get("DATABASE_URL")
    MONGO_INITDB_DATABASE: str = os.environ.get("MONGO_INITDB_DATABASE")

    JWT_PUBLIC_KEY: str = os.environ.get("JWT_PUBLIC_KEY")
    JWT_PRIVATE_KEY: str = os.environ.get("JWT_PRIVATE_KEY")
    ACCESS_TOKEN_EXPIRES_IN: int = int(os.environ.get("ACCESS_TOKEN_EXPIRES_IN", 3600))
    JWT_ALGORITHM: str = os.environ.get("JWT_ALGORITHM", "HS256")


settings = Settings()
