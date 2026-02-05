from fastapi import APIRouter

router = APIRouter(prefix="/author")

@router.get("/")
async def get_authors():
    ...

@router.get("/{author_id}")
async def get_author():
    ...

@router.post("/")
async def create_author():
    ...
