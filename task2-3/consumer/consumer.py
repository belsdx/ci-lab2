"""Consumer для распределённой системы RabbitMQ (задание 2.3).

Читает сообщения из очереди 'task_queue' и сохраняет их в bind-mount
хранилище /var/data (связанная точка монтирования).
"""

import os
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

    def callback(ch, method, properties, body):
        message = body.decode()
        print(f" [x] Received {message}", flush=True)
        # Сохранение полученного сообщения в bind-mount хранилище
        with open(os.path.join(DATA_DIR, "consumer.log"), "a", encoding="utf-8") as fh:
            fh.write(message + "\n")
        ch.basic_ack(delivery_tag=method.delivery_tag)

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue="task_queue", on_message_callback=callback)

    print(" [*] Waiting for messages. To exit press CTRL+C")
    channel.start_consuming()


if __name__ == "__main__":
    main()
