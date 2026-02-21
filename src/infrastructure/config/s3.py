import os
from collections import namedtuple

from src.infrastructure.config.contract import IDatabaseConfig


class S3Config(IDatabaseConfig):
    @property
    def database_uri(self) -> str:
        s3_host = os.environ.get("S3_HOST")
        s3_port = os.environ.get("S3_PORT")
        
        return f"http://{s3_host}:{s3_port}"

    @property
    def bucket_name(self):
        s3_bucket = os.environ.get("S3_HOST")
        
        return s3_bucket
    
    @property
    def credentials():
        s3_user = os.environ.get("S3_HOST")
        s3_password = os.environ.get("S3_PORT")
        
        Creds = namedtuple("Creds", ["user", "password"])
        cred = Creds(s3_user, s3_password)
        
        return cred
    
