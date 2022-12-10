# pythonProject1

# БОТ, ВЕДУЩИЙ TELEGRAM-КАНАЛ С АНЕКДОТАМИ
# Бот получает список анекдотов из файла и случайные шутки через случайные периоды времени постит в канал.
# Для этого нам нужно создать свой канал в Telegram,
# добавить в подписчики канала нашего бота и назначить его администратором канала с правом публиковать сообщения.
# Файл с анекдотами должен лежать в папке data рядом со скриптом бота.

import telebot
import random
import time
import datetime

from config import token, channel

# Создаем бота
bot = telebot.TeleBot(token)

# Адрес телеграм-канала, начинается с @
CHANNEL_NAME = channel

# Загружаем список шуток
f = open('fun.txt', 'r', encoding='UTF-8')
jokes = f.read().split('\n')
f.close()

work_bot_fl = True
while work_bot_fl:
    current_date_time = datetime.datetime.now()
    now = current_date_time.time()  # текущее время
    morning = datetime.time(7, 3, 0)  # время начала работы бота
    night = datetime.time(23, 45, 0)  # время окончания работы бота

    if morning < now < night:  # если день
        # таймер работы бота (от 1 минуты до 4 часов)
        bot.send_message(CHANNEL_NAME, random.choice(jokes))
        time.sleep(random.randint(60, 14400))
