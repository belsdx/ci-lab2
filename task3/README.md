# Лабораторная работа №2 — Задание 3

Асинхронная коммуникация на основе потоковой системы Apache Kafka
(режим KRaft, без ZooKeeper) с веб-интерфейсом AKHQ.

## Архитектура

```
Producer ──publish──> Kafka (KRaft) <── AKHQ (UI :8080)
                          ^
                          |
                       Consumer
```

## Запуск

```bash
docker compose up --build
```

- Kafka брокер: `localhost:9092` (внутри сети `kafka:29092`)
- AKHQ UI: http://localhost:8080
- Producer публикует сообщения в топик `test-topic`.
- Consumer читает из `test-topic` (группа `my-group`).

## Проверка

1. Откройте http://localhost:8080 — выберите подключение
   `docker-kafka-cluster`, увидите топик `test-topic` и поток сообщений.
2. В логах `docker compose logs producer consumer` видно публикацию и
   потребление сообщений.

## Статьи, изученные в ходе выполнения

- Обзор UI-инструментов для мониторинга и управления кластерами Kafka.
- Как запустить Apache Kafka с GUI на офисном ноутбуке и Windows.
- Настройка Kafka в Docker.
