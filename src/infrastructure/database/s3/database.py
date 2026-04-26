from io import BytesIO

from boto3 import Session
from botocore.exceptions import ClientError

from src.infrastructure.config.contract import IDatabaseConfig


class S3Storage:
    def __init__(self, config: IDatabaseConfig):
        self.config = config
        
        self.session = Session(
            aws_access_key_id=self.config.credentials.user,
            aws_secret_access_key=self.config.credentials.password,
        )
        
        if not self._is_bucket_exists():
            self.create_bucket()
    
    
    def upload_file(self, key, file_data):
        file = BytesIO(file_data)
        session = self.session.client(
            "s3",
            endpoint_url=self.config.database_uri
        )
        
        response = session.upload_fileobj(
            file, self.config.bucket_name, key
        )
        
        return response
        
    def create_presigned_url(self, key):
        session = self.session.client(
            "s3",
            endpoint_url=self.config.database_uri
        )
        
        response = session.generate_presigned_url(
            'get_object',
            Params={'Bucket': self.config.bucket_name, 'Key': key},
            ExpiresIn=30*60
        )
            
        return response
    
    
    def create_bucket(self):
        session = self.session.client(
            "s3",
            endpoint_url=self.config.database_uri
        )
        
        if not self._is_bucket_exists():
            session.create_bucket(
                Bucket=self.config.bucket_name,
            )

    def _is_bucket_exists(self):
        try:
            session = self.session.client(
                "s3",
                endpoint_url=self.config.database_uri
            )
            session.head_bucket(
                Bucket=self.config.bucket_name,
            )
            return True
        except ClientError:
            return False
