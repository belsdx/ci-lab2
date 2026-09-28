# Лабораторная работа №2 — Задание 2, упражнение 2.1

Изучение статьи «RabbitMQ для аналитика: практический ликбез» и работа с
облачным сервисом CloudAMQP.

## Ход выполнения

1. Зарегистрирована учётная запись на https://www.cloudamqp.com (план
   «Little Lemur» — бесплатный).
2. Создан инстанс RabbitMQ `belsdx` (region AP-East-1, Hong Kong), получен
   AMQP URL вида `amqps://user:password@host/vhost` (host: gerbil).
3. Реализован пример из статьи (производитель + потребитель) с
   использованием библиотеки `pika` на Python (файлы `producer.py`,
   `consumer.py`).
4. Сообщения публиковались и принимались через облачный брокер — проверено:
   producer отправил JSON-сообщение, consumer успешно его прочитал из очереди
   `hello`.

## Запуск

```powershell
# Windows (PowerShell)
$env:CLOUDAMQP_URL = "amqps://<user>:<password>@gerbil.rmq.cloudamqp.com/opggltdn"
python producer.py    # публикация сообщения
python consumer.py    # чтение сообщения
```

> AMQP URL хранится в переменной окружения и не публикуется в репозитории.

## Фрагменты JSON

Пример ответа REST API CloudAMQP со списком инстансов (`/api/instances`):

```json
[
  {
    "name": "my-first-rabbit",
    "plan": "lemur",
    "region": "amazon-web-services::us-east-1",
    "url": "amqps://xyzabcde:L3mUr-P4ss@mouse.rmq2.cloudamqp.com/xyzabcde",
    "apikey": "a1b2c3d4e5f6a7b8c9d0e1f2",
    "vhost": "xyzabcde"
  }
]
```

Пример сообщения в формате JSON, публикуемого в очередь:

```json
{
  "event": "order.created",
  "order_id": 12345,
  "amount": 99.95,
  "timestamp": "2026-09-28T12:00:00Z"
}
```

## Результат выполнения (лог)

```
[x] Sent {"event": "order.created", "order_id": 12345, "amount": 99.95, "timestamp": "2026-09-28T13:27:24Z"}
[x] Received {"event": "order.created", "order_id": 12345, "amount": 99.95, "timestamp": "2026-09-28T13:27:24Z"}
```

Сообщение успешно прошло путь producer → CloudAMQP (брокер) → consumer.
