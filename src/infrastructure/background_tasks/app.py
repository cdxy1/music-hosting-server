from celery import Celery

from src.infrastructure.config.rabbitmq import RabbitMQConfig

broker = RabbitMQConfig()

app = Celery("worker", broker=broker.broker_uri, backend=broker.celery_backend)
