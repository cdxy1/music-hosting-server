from fastapi import APIRouter

def get_root_router():
    router = APIRouter(prefix="/api")
