from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.presetntation.http.routes.root import get_root_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    

app = FastAPI(lifespan=lifespan)

root_router = get_root_router()
app.include_router(root_router)
