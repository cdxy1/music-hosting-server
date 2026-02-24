from typing import Callable

from src.application.repository.contract import IRepository
from src.application.unit_of_work.contract import IUnitOfWork
from src.application.cache.contract import ICacheWrapper


class BaseUsecase:
    def __init__(self, repo: IRepository, uow_factory: Callable[[], IUnitOfWork], cache: ICacheWrapper):
        self.repo = repo
        self.uow_factory = uow_factory
        self.cache = cache
