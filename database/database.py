from os import getenv

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from dotenv import load_dotenv


load_dotenv()
DATABASE_URL = getenv("DATABASE_URL")
async_engine = create_async_engine(DATABASE_URL, echo=True)
async_session_factory = async_sessionmaker(async_engine)