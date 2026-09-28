"""RabbitMQ Tutorial 2 — Work Queues (new_task).

Публикует задачу в очередь 'task_queue'. Передайте текст сообщения
как аргумент командной строки.
"""

import sys
import pika

message = " ".join(sys.argv[1:]) or "Hello World!"

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()

channel.queue_declare(queue="task_queue", durable=True)

channel.basic_publish(
    exchange="",
    routing_key="task_queue",
    body=message,
    properties=pika.BasicProperties(delivery_mode=2),  # сообщение durable
)
print(f" [x] Sent {message}")

connection.close()
