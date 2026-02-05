from fastapi import APIRouter

router = APIRouter(prefix="/authors", tags=["authors"])

@router.get("/")
async def get_authors():
    ...

@router.post("/")
async def create_author():
    ...

@router.get("/{author_id}")
async def get_author():
    ...
