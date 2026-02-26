from base64 import b64decode

from src.infrastructure.background_tasks.app import celery_app, storage
from src.infrastructure.background_tasks.utils.db import run_sql

@celery_app.task(name="tasks.upload_file")
def upload_file(prefix, file_key, file_data_b64):    
    bytes_data = b64decode(file_data_b64)
    full_file_key = f"{prefix}/{file_key}"
    storage.upload_file(full_file_key, bytes_data)
    
    run_sql("""UPDATE track SET audio_key=%s WHERE track_id=%s::UUID""", (full_file_key, str(file_key)))
