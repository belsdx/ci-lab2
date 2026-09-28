"""Producer для распределённой системы RabbitMQ (задание 2.3).

Публикует сообщения в очередь 'task_queue'. Каждое сообщение также
сохраняется в bind-mount хранилище /var/data (для демонстрации связанной
точки монтирования).
"""

import os
import time
import pika

DATA_DIR = "/var/data"
HOST = os.environ.get("RABBITMQ_HOST", "rabbitmq")


def main():
    os.makedirs(DATA_DIR, exist_ok=True)
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=HOST, connection_attempts=10, retry_delay=3)
    )
    channel = connection.channel()
    channel.queue_declare(queue="task_queue", durable=True)

    i = 0
    while True:
        message = f"message-{i} @ {time.strftime('%H:%M:%S')}"
        channel.basic_publish(
            exchange="",
            routing_key="task_queue",
            body=message,
            properties=pika.BasicProperties(delivery_mode=2),
        )
        # Запись отправленного сообщения в bind-mount хранилище
        with open(os.path.join(DATA_DIR, "producer.log"), "a", encoding="utf-8") as fh:
            fh.write(message + "\n")
        print(f" [x] Sent {message}", flush=True)
        i += 1
        time.sleep(3)


if __name__ == "__main__":
    main()
