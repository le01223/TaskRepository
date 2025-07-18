from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import delete_tables, create_tables
import uvicorn
from router import router as tasks_router
from schemas import STaskAdd


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("База очищена")
    await create_tables()
    print("База готова к работе")
    yield
    print("Выключение")


app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)



if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)