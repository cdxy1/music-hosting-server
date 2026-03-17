<div align="right">
  
[![No AI](https://custom-icon-badges.demolab.com/badge/No%20AI-2f2f2f?logo=non-ai&logoColor=white)](#)
<br>(даже для написания readme)
</div>

## Основные возможности:
- Управление авторами, жанрами, релизами и треками
- Загрузка и хранение аудио/изображений в объектное хранилище
- Кеширование
- Асинхронная обработка/загрузка через RabbitMQ

## Технологии

- **Backend**: Python 3.14, FastAPI, SQLAlchemy, Celery
- **База данных**: PostgreSQL
- **Кеш**: Redis
- **Хранилище файлов**: S3/MinIO
- **Брокер**: RabbitMQ
- **Контейнеризация**: Docker, Docker Compose
- **Линтер**: Ruff

## Установка и запуск

### Требования для запуска
- Docker и Docker Compose
- Для локального запуска Python 3.14 и UV

### Клонирование репозитория
```bash
git clone https://github.com/cdxy1/music-hosting-server.git
cd music-hosting-server
```

### Настройка окружения
   ```bash
   cp .env.example .env # Требуется вставить нужные переменные окружения
   ```

### Запуск с Docker Compose
```bash
docker-compose up --build # Или make up
```

## Структура проекта

```
src/
├── application/
├── domain/
├── infrastructure/
└── presentation/
```

## Лицензия

[Лицензия MIT](LICENSE)
