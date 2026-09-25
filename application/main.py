from fastapi import FastAPI

from application.database import engine, Base
from application.routes.user import user_router
from application.routes.task import task_router

app = FastAPI()


@app.on_event("startup")
async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


app.include_router(user_router)
app.include_router(task_router)