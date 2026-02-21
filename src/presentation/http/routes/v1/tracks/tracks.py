from fastapi import APIRouter, Depends

from src.presentation.http.dependencies.track_usecases import get_create_release_usecase
from src.presentation.http.mappers.track_mapper import pydantic_to_dto
from src.presentation.http.schemas.track import CreateTrackRequest

router = APIRouter(prefix="/tracks", tags=["tracks"])

@router.post("/")
async def create_track(track: CreateTrackRequest, usecase = Depends(get_create_release_usecase)):
    input_data = pydantic_to_dto(track)
    response = await usecase(input_data)
    
    return response
