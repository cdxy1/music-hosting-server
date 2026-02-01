from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_scoped_session,
    async_sessionmaker,
    create_async_engine,
)

from src.infrastructure.config.settings import DatabaseConfig
from src.infrastructure.database.contract import IDatabase


class PostgresDatabase(IDatabase):
    def __init__(self, config: DatabaseConfig):
        self._engine = self._create_engine(config.database_uri)

    def _create_engine(self, uri: str) -> AsyncEngine:
        return create_async_engine(uri)

    def create_session(self) -> AsyncSession:
        return async_scoped_session(
            async_sessionmaker(
                self.engine,
                autoflush=False,
                expire_on_commit=False,
            )
        )
