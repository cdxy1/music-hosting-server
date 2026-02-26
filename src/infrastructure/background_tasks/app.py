from celery import Celery

from src.infrastructure.config.rabbitmq import RabbitMQConfig
from src.infrastructure.config.s3 import S3Config
from src.infrastructure.database.s3.database import S3Storage

broker = RabbitMQConfig()

celery_app = Celery("worker", broker=broker.broker_uri, backend=broker.celery_backend)
celery_app.autodiscover_tasks(["src.infrastructure.background_tasks.tasks"])

storage_config = S3Config()
storage = S3Storage(storage_config)
