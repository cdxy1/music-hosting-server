from fastapi import APIRouter

from src.presetntation.http.routes.v1.v1_root import get_root_v1_router

def get_root_router():
    router = APIRouter(prefix="/api")
    
    v1_router = get_root_v1_router()
    router.include_router(v1_router)
    
    return router
