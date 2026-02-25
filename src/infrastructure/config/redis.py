import os

from src.infrastructure.config.contract import IDatabaseConfig


class RedisConfig(IDatabaseConfig):
    @property
    def database_uri(self) -> str:
        cache_host = os.environ.get("REDIS_HOST")
        cache_port = os.environ.get("REDIS_PORT")
        
        return f"redis://{cache_host}:{cache_port}"

    @property
    def ttl_seconds(self):
        cache_seconds_ttl = os.environ.get("REDIS_SECONDS_TTL", 60)

        return int(cache_seconds_ttl)
