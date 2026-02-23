import asyncio
from base64 import b64decode

import src.infrastructure.models  #NOQA
from src.application.dto.track_dto import UpdateTrackDTO
from src.infrastructure.background_tasks.app import celery_app, storage
from src.infrastructure.background_tasks.dependencies.track import (
    get_update_track_usecase,
)


@celery_app.task(name="tasks.upload_file")
def upload_file(file_key, file_data_b64):
    bytes_data = b64decode(file_data_b64)
    storage.upload_file(str(file_key), bytes_data)
    usecase = get_update_track_usecase()
    
    asyncio.run(usecase(file_key, UpdateTrackDTO(audio_key=file_key)))
