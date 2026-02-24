from datetime import timedelta
from typing import Optional

from redis import ConnectionError, Redis
from redis import asyncio as aioredis

from src.infrastructure.config.contract import IDatabaseConfig


class RedisCache:
    _connection = None
    
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self, config: IDatabaseConfig):
        self.config = config
        self._connection: Optional[Redis] = None

    async def connect(self):
        self._connection = await aioredis.from_url(self.config.database_uri, decode_responses=True)

    async def close(self):
        if self._connection:
            await self._connection.close()

    async def set(self, key: str, value: str, expire: timedelta):
        try:
            await self._connection.setex(key, expire, value)
        except ConnectionError:
            raise

    async def get(self, key) -> Optional[str]:
        try:
            return await self._connection.get(key)
        except ConnectionError:
            raise

    async def delete(self, key):
        try:
            await self._connection.delete(key)
        except ConnectionError:
            raise
