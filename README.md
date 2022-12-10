# pythonProject1

[Ru] БОТ, ВЕДУЩИЙ TELEGRAM-КАНАЛ С АНЕКДОТАМИ

## Описание

Бот получает список анекдотов из файла и каждый час постит в канал один из этих анекдотов.

## Требования

* Установить внешние зависимости
* $ pip install -r requirements.txt
* Создать свой канал в Telegram, добавить в подписчики канала нашего бота и назначить его администратором канала с
  правом публиковать сообщения.
* Создать файл с анекдотами fun.txt и размесить в папке со скриптом бота.
* Создать файл config.py, в котором будут храниться токен для доступа к боту и адрес телеграм-канала (начинается с @) в
  виде

```python
token = "1234567890:ASDFGHH..."
channel = '@topjokes...'
```

## Где взять токен?

* https://xakep.ru/2021/11/28/python-telegram-bots/

## Подключаем модули

```python
import telebot
import time
from config import token, channel
```

## Примеры использования

#### Загружаем список шуток

Указываем название текстового файла с шутками, 'r' - чтение текста, кодировку текта 'UTF-8'

```python
f = open('fun.txt', 'r', encoding='UTF-8')
jokes = f.read().split('\n')
f.close()
```

#### Выставляем время начала работы бота "morning" и окончания "night", чтобы сообщения не будили по ночам

```python
work_bot_fl = True
while work_bot_fl:
    current_date_time = datetime.datetime.now()
    now = current_date_time.time()  # текущее время
    morning = datetime.time(7, 3, 0)  # время начала работы бота
    night = datetime.time(23, 45, 0)  # время окончания работы бота
```

#### Посылаются случайные шутки через случайные периоды времени в диапазоне от 1 минуты до 4 часов

```python
 if morning < now < night:  # если день
    # таймер работы бота (от 1 минуты до 4 часов)
    bot.send_message(CHANNEL_NAME, random.choice(jokes))
    time.sleep(random.randint(60, 14400))
```
