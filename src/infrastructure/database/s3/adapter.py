from src.application.file_storage.contract import IFileStorage


class S3Adapter(IFileStorage):
    def __init__(self, s3_storage):
        self.s3_storage = s3_storage
        
    def get_file_url(self, key: str) -> str:
        return self.s3_storage.create_presigned_url(key)
