from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie

from settings import settings
from models.user import User


async def startDB():
    client = AsyncIOMotorClient(settings.DATABASE_URL)

    await init_beanie(database=client.users, document_models=[User])
