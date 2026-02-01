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
        self._session = self._create_session(
            self._engine,
        )

    def _create_engine(self, uri: str) -> AsyncEngine:
        return create_async_engine(uri)

    def _create_session(self, engine: AsyncEngine) -> AsyncSession:
        return async_scoped_session(
            async_sessionmaker(
                engine,
                autoflush=False,
                expire_on_commit=False,
            )
        )

    async def get_session(self) -> AsyncGenerator[AsyncSession, None]:
        async with self._session() as session:
            yield session
