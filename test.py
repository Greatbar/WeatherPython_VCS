import telebot
import time
import logging
import const
import requests
import json
from pprint import pprint
from pyowm.owm import OWM
from pyowm.utils.config import get_default_config

config_dict = get_default_config()
config_dict['language'] = 'ru'
owm = OWM('a3cf06415e6a17d1b39450e3aaadb2e9', config_dict)
bot = telebot.TeleBot('1856711707:AAFH3BirZu3v7_m2l5OUWnAhDJKMJmAF4MQ')


@bot.message_handler(content_types=['text'])
def send_message(message):
    if message.text.lower() == "/start" or message.text.lower() == "/help":
        bot.send_message(message.from_user.id,
                         "Здравтсвуйте, напишите название города, в котором хотите узнать погоду." + "\n")
    else:
        try:

            url = const.URL.format(token=const.TOKEN, method=const.UPDATE_METH)
            content = requests.get(url).text
            data = json.loads(content)
            pprint(data)

            mgr = owm.weather_manager()
            observation = mgr.weather_at_place(message.text)  # Берем название города из сообщения
            weather = observation.weather
            temperature = weather.temperature('celsius')["temp"]
            temperature = round(temperature)
            # Формируется ответ для логов
            print(time.ctime(), "User id: ", message.from_user.id)
            print(time.ctime(), "Message: ", message.text.title(), temperature, weather.detailed_status)
            # Формируемтся и выводится ответ для чата
            answer = "В городе " + message.text.title() + " сейчас " + weather.detailed_status + "." + "\n"
            answer += "Температура около: " + str(temperature) + "\n"
            bot.send_message(message.chat.id, answer)  # Ответить сообщением

        except Exception:
            answer = "Город не найден.\n"
            print(time.ctime(), "User id:", message.from_user.id)
            print(time.ctime(), "Message:", message.text.title())
            logging.error('Failed.', exc_info=True)
            bot.send_message(message.chat.id, answer)  # Ответить сообщением


# Запускаем бота
bot.polling(none_stop=True)
