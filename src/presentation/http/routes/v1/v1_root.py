from fastapi import APIRouter

from src.presentation.http.routes.v1.authors.authors import router as author_router
from src.presentation.http.routes.v1.genre.genre import router as genre_router
from src.presentation.http.routes.v1.release.release import router as release_router

INTERNAL_ROUTERS = (author_router, genre_router, release_router)

def get_root_v1_router():
    router = APIRouter(prefix="/v1")
    for internal_router in INTERNAL_ROUTERS:
        router.include_router(internal_router)

    return router
