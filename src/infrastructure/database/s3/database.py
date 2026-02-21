from io import BytesIO
from contextlib import contextmanager

from boto3 import Session

from src.infrastructure.config.contract import IDatabaseConfig


class ObjectStorage:
    def __init__(self, config: IDatabaseConfig):
        self.config = config
        
        self.session = Session(
            aws_access_key_id=self.config.credentials.user,
            aws_secret_access_key=self.config.credentials.password,
        )
    
    
    def upload_file(self, key, file):
        file_content = BytesIO(file)
        with self.get_s3minio_session() as session:
            response = session.upload_fileobj(
                file_content, self.config.bucket_name, key
            )
            return response
        
    def create_presigned_url(self, key):
        with self.get_s3minio_session() as session:
            response = session.generate_presigned_url(
            'get_object',
            Params={'Bucket': self.config.bucket_name, 'Key': key}, ExpiresIn=30*60)
            
        return response
    
    @contextmanager
    def get_s3minio_session(self):
        with self.session.client(
            "s3", endpoint_url=self.config.database_uri
        ) as s3minio:
            yield s3minio
