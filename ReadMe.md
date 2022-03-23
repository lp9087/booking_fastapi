Для миграции через Alembic:
1. ```alembic init migrations```
2. ```alembic revision --autogenerate -m "First"```
3. ```alembic upgrade head```