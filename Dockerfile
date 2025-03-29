FROM python:3.10.12

WORKDIR /app

# Установка Poetry
RUN pip install poetry==1.2.0

# Копируем файлы зависимостей
COPY pyproject.toml poetry.lock ./

# Устанавливаем зависимости (без виртуальной среды)
RUN poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi

# Копируем остальные файлы
COPY . .

# Команда для запуска
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]