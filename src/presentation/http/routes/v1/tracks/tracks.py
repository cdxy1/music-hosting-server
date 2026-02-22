from base64 import b64encode
from uuid import UUID

from fastapi import APIRouter, Depends, File, Form, UploadFile

from src.presentation.http.dependencies.track_usecases import (
    get_all_tracks_usecase,
    get_create_track_usecase,
    get_delete_track_usecase,
    get_track_usecase,
)
from src.presentation.http.mappers.track_mapper import (
    dto_to_pydantic,
    many_dto_to_pydantic,
    pydantic_to_dto,
)
from src.presentation.http.schemas.track import CreateTrackRequest

router = APIRouter(prefix="/tracks", tags=["tracks"])

@router.post("/")
async def create_track(
    title: str = Form(...),
    release_id: UUID = Form(...),
    file: UploadFile = File(...), usecase = Depends(get_create_track_usecase)):
    file_bytes = await file.read()
    encode_file = b64encode(file_bytes).decode("utf-8")
    
    track = CreateTrackRequest(title=title, release_id=release_id)
    
    input_data = pydantic_to_dto(track, encode_file)
    response = await usecase(input_data)
    
    return response

@router.get("/")
async def get_all_tracks(usecase = Depends(get_all_tracks_usecase)):
    tracks = await usecase()
    response = many_dto_to_pydantic(tracks)

    return response

@router.get("/{track_id}")
async def get_track(track_id: UUID, usecase = Depends(get_track_usecase)):
    track = await usecase(track_id)
    response = dto_to_pydantic(track)

    return response

@router.delete("/{track_id}")
async def delete_track(track_id: UUID, usecase = Depends(get_delete_track_usecase)):
    response = await usecase(track_id)
    
    return response
