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

#### Посылаются случайные шутки через случайные периоды времени

```python
fl = 'start'
while fl == 'start':
    bot.send_message(CHANNEL_NAME, random.choice(jokes))
    time.sleep(random.randint(60, 3600))
```
