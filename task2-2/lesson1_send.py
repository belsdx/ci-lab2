"""RabbitMQ Tutorial 1 — Hello World (producer).

Отправляет одно сообщение в очередь 'hello'.
"""

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()

channel.queue_declare(queue="hello")

channel.basic_publish(exchange="", routing_key="hello", body="Hello World!")
print(" [x] Sent 'Hello World!'")

connection.close()
