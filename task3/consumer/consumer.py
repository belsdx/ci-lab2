"""Consumer для Apache Kafka (задание 3).

Читает сообщения из топика 'test-topic' и выводит их на экран.
"""

import os
import json
from kafka import KafkaConsumer

BOOTSTRAP = os.environ.get("KAFKA_BOOTSTRAP", "kafka:29092")
TOPIC = os.environ.get("KAFKA_TOPIC", "test-topic")
GROUP = os.environ.get("KAFKA_GROUP", "my-group")


def main():
    consumer = KafkaConsumer(
        TOPIC,
        bootstrap_servers=BOOTSTRAP,
        group_id=GROUP,
        auto_offset_reset="earliest",
        value_deserializer=lambda v: json.loads(v.decode("utf-8")),
    )
    print(f" [*] Subscribed to '{TOPIC}' (group '{GROUP}')")
    for message in consumer:
        print(f" [x] Received {message.value}", flush=True)


if __name__ == "__main__":
    main()
