"""Упражнение 2.1 — Producer для CloudAMQP (RabbitMQ для аналитика).

Публикует сообщения в очередь 'hello' через облачный брокер CloudAMQP.
Параметры подключения берутся из переменной окружения CLOUDAMQP_URL.
"""

import os
import json
import time
import pika

# AMQP URL вида amqps://user:password@host/vhost (из CloudAMQP)
url = os.environ.get("CLOUDAMQP_URL")
if not url:
    raise SystemExit("Установите переменную окружения CLOUDAMQP_URL")

params = pika.URLParameters(url)
params.heartbeat = 30  # keep-alive для облачного соединения

connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue="hello")

# Публикуем JSON-сообщение (пример из статьи)
message = {
    "event": "order.created",
    "order_id": 12345,
    "amount": 99.95,
    "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
}
body = json.dumps(message, ensure_ascii=False)

channel.basic_publish(exchange="", routing_key="hello", body=body)
print(f" [x] Sent {body}")

connection.close()
