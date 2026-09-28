# Базовый образ: минимальный Python 3.11
FROM python:3.11-slim

# Рабочий каталог
WORKDIR /app

# Устанавливаем зависимость для работы с RabbitMQ
RUN pip install pika

# Копируем исходный код
COPY consumer.py .

# Команда запуска
CMD ["python", "consumer.py"]
