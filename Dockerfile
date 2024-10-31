# Используем официальный образ Python
FROM python:3.10-slim

# Устанавливаем необходимые системные зависимости
RUN apt-get update && \
    apt-get install -y gcc libpq-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файл зависимостей
COPY requirements.txt .  

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем все файлы приложения
COPY . .

# Указываем переменные окружения для Django
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=blog_api.settings  

# Команда для запуска приложения
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
