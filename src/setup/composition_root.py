from contextlib import asynccontextmanager

from fastapi import FastAPI

# from src.infrastructure.config.postgres import PostgresConfig
# from src.infrastructure.database.postgres import PostgresDatabase
from src.presetntation.http.routes.root import get_root_router


@asynccontextmanager
async def lifespan(app: FastAPI):    
    # database_config = PostgresConfig()
    # database = PostgresDatabase(database_config)
    yield
    # database.close_all_connections()

app = FastAPI(lifespan=lifespan)

root_router = get_root_router()
app.include_router(root_router)
