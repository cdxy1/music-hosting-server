# from typing import Any
from contextlib import asynccontextmanager

from src.application.unit_of_work.contract import IUnitOfWork
from src.infrastructure.database.contract import IDatabase


class UnitOfWork(IUnitOfWork):
    def __init__(self, database: IDatabase):
        self._database = database

    # async def __aenter__(self):
    #     self._session = self._database.create_session()

    #     return self

    # async def __aexit__(self,
    #                     exc_type: type[BaseException] | None,
    #                     exc_val: BaseException | None,
    #                     exc_tb: Any,
    #                     ):
    #     if exc_type is not None:
    #         await self.rollback()

    #     if self._session is not None:
    #         await self._session.close()
    #         self._session = None

    # async def commit(self):
    #     self._session.commit()

    # async def rollback(self):
    #     self._session.rollback()

    @asynccontextmanager
    async def __call__(self):
        try:
            session = self._database.create_session()
            yield session
            session.commit()
        except Exception:
            session.rollback()
        finally:
            session.close()
