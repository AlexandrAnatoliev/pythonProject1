# pythonProject1

# БОТ, ВЕДУЩИЙ TELEGRAM-КАНАЛ С АНЕКДОТАМИ
# Бот получает список анекдотов из файла и случайные шутки через случайные периоды времени постит в канал.
# Для этого нам нужно создать свой канал в Telegram,
# добавить в подписчики канала нашего бота и назначить его администратором канала с правом публиковать сообщения.
# Файл с анекдотами должен лежать в папке data рядом со скриптом бота.

import telebot
import random
import time
# from config import token, channel

# убрать токен и канал
# token = "5969843689:AAFskKqCFHbh5pIHCkTQFPyStOVMRJl2G20"
channel = '@topmostjokes'
# тестовый токен
token = "5943261012:AAENwlcynSTVsyFMUSFIX9CVde_73XwNy-Q"

# Создаем бота
bot = telebot.TeleBot(token)

# Адрес телеграм-канала, начинается с @
CHANNEL_NAME = channel

# Загружаем список шуток
f = open('fun.txt', 'r', encoding='UTF-8')
jokes = f.read().split('\n')
f.close()

fl_go = 'go'
# проверяем включение программы
bot.send_message(CHANNEL_NAME, random.choice(jokes))
while fl_go == 'go':
    # таймер работы бота
    time.sleep(random.randint(60, 3600))
    fl = 'start'

# посылаются случайные шутки через случайные периоды времени
    if fl == 'start':
        bot.send_message(CHANNEL_NAME, random.choice(jokes))
        fl = 'stop'
