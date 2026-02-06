from src.infrastructure.database.contract import IDatabase
from src.infrastructure.unit_of_work.unit_of_work_impl import UnitOfWork

class UnitOfWorkSingletonFactory:
    _instance = None
    _initialized = False
    
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self, database: IDatabase = None):
        if self._initialized:
            return
        self.database = database
        self._initialized = True
    
    def create_uow_instance(self):
        return UnitOfWork(self.database)

