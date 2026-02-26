import os

from src.infrastructure.config.contract import IDatabaseConfig


class PostgresConfig(IDatabaseConfig):
    @property
    def database_uri(self) -> str:
        db_host = os.environ.get("DB_HOST")
        db_port = os.environ.get("DB_PORT")
        db_user = os.environ.get("DB_USER")
        db_password = os.environ.get("DB_PASSWORD")
        db_name = os.environ.get("DB_NAME")
        
        return f"postgresql+asyncpg://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

    @property
    def sync_database_uri(self) -> str:
        db_host = os.environ.get("DB_HOST")
        db_port = os.environ.get("DB_PORT")
        db_user = os.environ.get("DB_USER")
        db_password = os.environ.get("DB_PASSWORD")
        db_name = os.environ.get("DB_NAME")
        
        return f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"      
