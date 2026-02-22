import os

class RabbitMQConfig:
    @property
    def broker_uri(self):
        broker_host = os.environ.get("RABBITMQ_HOST")
        broker_port = os.environ.get("RABBITMQ_PORT")
        broker_user = os.environ.get("RABBITMQ_USER")
        broker_password = os.environ.get("RABBITMQ_PASSWORD")
        broker_vhost = os.environ.get("RABBITMQ_VHOST")
        
        return f"amqp://{broker_user}:{broker_password}@{broker_host}:{broker_port}/{broker_vhost}"
    
    @property
    def celery_backend(self):
        return "rpc://"
