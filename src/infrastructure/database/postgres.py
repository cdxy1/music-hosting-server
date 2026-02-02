from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_scoped_session,
    async_sessionmaker,
    create_async_engine,
)

from src.infrastructure.models.base import BaseOrmModel
from src.infrastructure.config.contract import IDatabaseConfig
from src.infrastructure.database.contract import IDatabase


class PostgresDatabase(IDatabase):
    def __init__(self, config: IDatabaseConfig):
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
        
    async def create_tables(self):
        async with self.engine.begin() as conn:
            await conn.run_sync(BaseOrmModel.metadata.create_all)
