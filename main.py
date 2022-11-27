# pythonProject1

# БОТ, ВЕДУЩИЙ TELEGRAM-КАНАЛ С АНЕКДОТАМИ
# Бот получает список анекдотов из файла и каждый час постит в канал один из этих анекдотов.
# Для этого нам нужно создать свой канал в Telegram,
# добавить в подписчики канала нашего бота и назначить его администратором канала с правом публиковать сообщения.
# Файл с анекдотами должен лежать в папке data рядом со скриптом бота.

import telebot
import random
import time
from config import token, channel

# Создаем бота
bot = telebot.TeleBot(token)

# Адрес телеграм-канала, начинается с @
CHANNEL_NAME = channel

# Загружаем список шуток
f = open('fun.txt', 'r', encoding='UTF-8')
jokes = f.read().split('\n')
f.close()

# посылаются случайные шутки с периодом 30 секунд
bot.send_message(CHANNEL_NAME, random.choice(jokes))
time.sleep(30)
bot.send_message(CHANNEL_NAME, random.choice(jokes))

