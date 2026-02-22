from base64 import b64decode

from src.infrastructure.background_tasks.app import celery_app, storage


@celery_app.task(name="tasks.upload_file")
def upload_file(file_key, file_data_b64):
    bytes_data = b64decode(file_data_b64)
    storage.upload_file(file_key, bytes_data)
