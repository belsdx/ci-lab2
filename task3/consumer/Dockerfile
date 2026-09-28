# Базовый образ: минимальный Python 3.11
FROM python:3.11-slim

# Рабочий каталог
WORKDIR /app

# Устанавливаем клиент Kafka
RUN pip install kafka-python

# Копируем исходный код
COPY consumer.py .

# Команда запуска
CMD ["python", "consumer.py"]
