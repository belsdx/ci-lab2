# Лабораторная работа №2 — Задание 2, упражнение 2.3

Распределённая система из трёх контейнеров: RabbitMQ + Producer + Consumer.
Каждое приложение использует связанную точку монтирования (bind mount) как
хранилище.

## Архитектура

```
Producer ──publish──> RabbitMQ ──consume──> Consumer
   │                     │                      │
   └─ bind mount ── data-producer      data-consumer ── bind mount ──┘
```

## Запуск

```bash
docker compose up --build
```

- Интерфейс администрирования: http://localhost:15672 (guest/guest)
- Producer публикует сообщения в очередь `task_queue` каждые 3 секунды и
  пишет их в `data-producer/producer.log`.
- Consumer читает очередь и пишет сообщения в `data-consumer/consumer.log`.

## Демонстрация консольных утилит

```bash
# Список очередей
docker exec rabbitmq_local rabbitmqctl list_queues

# Список соединений
docker exec rabbitmq_local rabbitmqctl list_connections

# Через rabbitmqadmin (нужен плагин management)
docker exec rabbitmq_local rabbitmqadmin list queues
docker exec rabbitmq_local rabbitmqadmin list exchanges
docker exec rabbitmq_local rabbitmqadmin get queue=task_queue
```

## Локальный ИИ-агент (из задания 6 лабораторной работы 1)

При работе с кодом и конфигурационными файлами используется локальный
ИИ-агент, развёрнутый в инфраструктуре (см. compose-файл лабораторной работы 1,
задание 6). Агент помогает генерировать и проверять код producer/consumer,
Dockerfile и compose.yaml. Пример применения — генерация и ревью приведённых
выше файлов, проверка синтаксиса и корректности конфигурации.

> Замечание: конфигурация ИИ-агента добавляется в compose.yaml этой работы
> в соответствии с заданием 6 ЛР1 (образ и параметры подключаются по аналогии
> с остальными сервисами).
