# pythonProject1

# БОТ, ВЕДУЩИЙ TELEGRAM-КАНАЛ С АНЕКДОТАМИ
# Бот получает список анекдотов из файла и случайные шутки через случайные периоды времени постит в канал.
# Для этого нам нужно создать свой канал в Telegram,
# добавить в подписчики канала нашего бота и назначить его администратором канала с правом публиковать сообщения.
# Файл с анекдотами должен лежать в папке data рядом со скриптом бота.

# $ pip install schedule - установить внешние зависимости

import telebot
import random
import time
import datetime
import schedule
from multiprocessing import Process

from config import token, channel

# Создаем бота
bot = telebot.TeleBot(token)

# Адрес телеграм-канала, начинается с @
CHANNEL_NAME = channel

# Загружаем список шуток
f = open('fun.txt', 'r', encoding='UTF-8')
jokes = f.read().split('\n\n')
f.close()

# Загружаем список утренних приветствий
m = open('morning_text.txt', 'r', encoding='UTF-8')
good_morning = m.read().split('\n\n')
m.close()

# Загружаем список вечерних пожеланий
n = open('nigth_text.txt', 'r', encoding='UTF-8')
good_night = n.read().split('\n\n')
n.close()


def wish_morning():
    """
    Посылает случайную фразу из списка good_morning в канал CHANNEL_NAME
    :return:
    """
    bot.send_message(CHANNEL_NAME, random.choice(good_morning))


def wish_evening():
    """
    Посылает случайную фразу из списка good_night в канал CHANNEL_NAME
    :return:
    """
    bot.send_message(CHANNEL_NAME, random.choice(good_night))


def first_process():
    """
    Каждое утро "7:08" и каждый вечер "23:49" посылать сообщение в чат.
    :return:
    """
    schedule.every().day.at("07:08").do(wish_morning)
    # каждый вечер посылать сообщение в чат
    schedule.every().day.at("23:49").do(wish_evening)
    while True:
        schedule.run_pending()
        time.sleep(1)


def second_process():
    """
    Посылаем случайный анекдот в чат.
    :return:
    """
    work_bot_fl = True
    while work_bot_fl:
        current_date_time = datetime.datetime.now()
        now = current_date_time.time()  # текущее время
        morning = datetime.time(7, 32, 0)  # время начала работы бота
        night = datetime.time(23, 45, 0)  # время окончания работы бота

        if morning < now < night:  # если день
            # таймер работы бота (от 1 до 3 часов)
            bot.send_message(CHANNEL_NAME, random.choice(jokes))
            time.sleep(random.randint(3600, 10800))


if __name__ == '__main__':
    # Запускаем два процесса параллельно
    p1 = Process(target=first_process, daemon=True)
    p2 = Process(target=second_process, daemon=True)
    p1.start()
    p2.start()
    p1.join()
    p2.join()
