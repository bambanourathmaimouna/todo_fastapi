import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from fastapi import Depends
from typing import Annotated
from sqlalchemy.ext.asyncio import  create_async_engine , AsyncSession , async_sessionmaker

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_async_engine(DATABASE_URL)

async_session= async_sessionmaker(engine, expire_on_commit=False)


class Base(DeclarativeBase):
    pass

async def get_db():
    db = async_session()

    try:
        yield db
    finally:
        await db.close()


db_dependency = Annotated[AsyncSession , Depends(get_db)]

async	def	init_db(): 
    async	with	engine.begin()	as	conn:
        await	conn.run_sync(Base.metadata.create_all)

