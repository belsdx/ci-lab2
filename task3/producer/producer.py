"""Producer для Apache Kafka (задание 3).

Публикует сообщения в топик 'test-topic'. Работает в режиме KRaft
(без ZooKeeper) через брокер kafka:29092.
"""

import os
import time
import json
from kafka import KafkaProducer

BOOTSTRAP = os.environ.get("KAFKA_BOOTSTRAP", "kafka:29092")
TOPIC = os.environ.get("KAFKA_TOPIC", "test-topic")


def main():
    producer = KafkaProducer(
        bootstrap_servers=BOOTSTRAP,
        value_serializer=lambda v: json.dumps(v).encode("utf-8"),
    )
    i = 0
    while True:
        message = {"id": i, "value": f"event-{i}", "ts": time.time()}
        producer.send(TOPIC, value=message)
        print(f" [x] Sent {message}", flush=True)
        producer.flush()
        i += 1
        time.sleep(3)


if __name__ == "__main__":
    main()
