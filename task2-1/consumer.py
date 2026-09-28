"""Упражнение 2.1 — Consumer для CloudAMQP (RabbitMQ для аналитика).

Читает одно сообщение из очереди 'hello' через облачный брокер CloudAMQP.
Параметры подключения берутся из переменной окружения CLOUDAMQP_URL.
"""

import os
import pika

url = os.environ.get("CLOUDAMQP_URL")
if not url:
    raise SystemExit("Установите переменную окружения CLOUDAMQP_URL")

params = pika.URLParameters(url)
params.heartbeat = 30

connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue="hello")

method, properties, body = channel.basic_get(queue="hello", auto_ack=True)
if method:
    print(f" [x] Received {body.decode()}")
else:
    print(" [x] Queue is empty")

connection.close()
