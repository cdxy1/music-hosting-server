from src.infrastructure.database.contract import IDatabase
from src.infrastructure.unit_of_work.unit_of_work_impl import UnitOfWork


def uow_factory(database: IDatabase):
    def inner():
        return UnitOfWork(database)
    return inner
