# from typing import Any
from contextlib import asynccontextmanager

from src.application.unit_of_work.contract import IUnitOfWork
from src.infrastructure.database.contract import IDatabase


class UnitOfWork(IUnitOfWork):
    def __init__(self, database: IDatabase):
        self._database = database

    @asynccontextmanager
    async def __call__(self):
        try:
            session = self._database.create_session()
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
        finally:
            await session.close()
