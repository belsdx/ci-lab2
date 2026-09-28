# Лабораторная работа №2 — Задание 2, упражнение 2.2

Асинхронная коммуникация на основе брокера сообщений RabbitMQ.

## Запуск RabbitMQ в Docker

```bash
docker compose up -d
```

Веб-интерфейс администрирования: http://localhost:15672
(логин/пароль: guest / guest).

## Установка зависимостей (на хост-системе)

```bash
pip install pika
```

## Урок 1 — Hello World

```bash
python lesson1_send.py      # в одном терминале
python lesson1_receive.py   # в другом терминале
```

## Урок 2 — Work Queues

```bash
python lesson2_new_task.py "First message...."   # несколько раз
python lesson2_worker.py                          # можно запустить несколько воркеров
```

## Урок 3 — Publish/Subscribe

```bash
python lesson3_emit_log.py "info: hello"
python lesson3_receive_logs.py   # можно запустить несколько подписчиков
```

## Примечание

Код уроков выполняется локально на хост-системе (контейнер для кода
не создаётся — по условию задания). RabbitMQ работает в контейнере.
