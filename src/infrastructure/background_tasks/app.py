from celery import Celery

from src.infrastructure.config.postgres import PostgresConfig
from src.infrastructure.config.rabbitmq import RabbitMQConfig
from src.infrastructure.config.s3 import S3Config
from src.infrastructure.database.postgres.database import PostgresDatabase
from src.infrastructure.database.s3.database import S3Storage
from src.infrastructure.unit_of_work.unit_of_work_factory import (
    UnitOfWorkSingletonFactory,
)

broker = RabbitMQConfig()

celery_app = Celery("worker", broker=broker.broker_uri, backend=broker.celery_backend)
celery_app.autodiscover_tasks(["src.infrastructure.background_tasks.tasks"])

config = S3Config()
storage = S3Storage(config)

database_config = PostgresConfig()
database = PostgresDatabase(database_config)
UnitOfWorkSingletonFactory(database)
