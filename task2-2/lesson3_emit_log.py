"""RabbitMQ Tutorial 3 — Publish/Subscribe (emit_log).

Публикует сообщение в обменник 'logs' (тип fanout). Передайте текст
сообщения как аргумент командной строки.
"""

import sys
import pika

message = " ".join(sys.argv[1:]) or "info: Hello World!"

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()

channel.exchange_declare(exchange="logs", exchange_type="fanout")

channel.basic_publish(exchange="logs", routing_key="", body=message)
print(f" [x] Sent {message}")

connection.close()
