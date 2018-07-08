# -*- coding: utf-8 -*-
# Example code for telegrambot.py module
from telegram.ext import CommandHandler, MessageHandler, Filters
from django_telegrambot.apps import DjangoTelegramBot
import requests, json
from datetime import date, timedelta
import datetime

import logging
logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.

def turnos(bot, update, **args):
    if len(args['args']) == 1:
        try:
            date_arg = datetime.datetime.strptime(args['args'][0], '%d-%m-%Y').date()
            date_today = datetime.datetime.now().date()
            if str(date_arg) >= str(date_today): 
                string_response = "Los turnos disponibles son: "
                response = requests.get("http://localhost:8000/appointments/turnos/?date="+str(date_arg))
                times = json.loads(response.text)
                if len(times) > 0:
                    for element in times:
                        string_response = string_response + element['time'] + '. '
                else:
                    string_response = "No hay turnos disponibles para la fecha ingresada."
                bot.sendMessage(update.message.chat_id, text=string_response)
            else:
                bot.sendMessage(update.message.chat_id, text="La fecha ingresada es anterior a la fecha actual.")
        except ValueError:
            bot.sendMessage(update.message.chat_id, text="El formato ingresado no es válido. Debe ser DD-MM-AAAA.")
    else:
        bot.sendMessage(update.message.chat_id, text="La cantidad de parámetros pasados es inválida (debe ser 1).")

def reservar(bot, update, **args):
    if len(args['args']) == 3:
        try: 
            dni_arg = int(args['args'][0])
            if dni_arg >= 500000:   
                try:
                    date_arg = datetime.datetime.strptime(args['args'][1], '%d-%m-%Y').date()
                    date_today = datetime.datetime.now()
                    if str(date_arg) >= str(date_today.date()):
                        try:
                            time_arg = datetime.datetime.strptime(args['args'][2], '%H:%M').time()
                            if ((str(time_arg) >= "08:00") and (str(time_arg) < "19:31")):
                                if ((str(date_arg) == str(date_today)) and (str(time_arg) >= str(date_today.time()))) or ((str(date_arg) != str(date_today))):
                                    if time_arg.minute > 0 and time_arg.minute < 30:
                                        time_arg = str(time_arg.hour)+":30"
                                    elif time_arg.minute > 30:
                                        time_arg = str(time_arg.hour + 1)+":00"
                                    response = requests.post("http://localhost:8000/appointments/turnos/?dni="+str(dni_arg)+"&date="+str(date_arg)+"&time="+str(time_arg))
                                    bot.sendMessage(update.message.chat_id, text=json.loads(response.text))
                                else:
                                    bot.sendMessage(update.message.chat_id, text="La hora ingresada es anterior a la hora actual.")
                            else:
                                bot.sendMessage(update.message.chat_id, text="El consultorio atiende entre 08:00 y 20:00 de corrido. Es decir, primer turno disponible podría ser 08:00, y el último 19:30 (consultar turnos disponibles para asegurarse).")
                        except ValueError:
                            bot.sendMessage(update.message.chat_id, text="El formato ingresado para la hora no es válido. Debe ser HH:MM.")
                    else:
                        bot.sendMessage(update.message.chat_id, text="La fecha ingresada es anterior a la fecha actual.")
                except ValueError:
                    bot.sendMessage(update.message.chat_id, text="El formato ingresado para la fecha no es válido. Debe ser DD-MM-AAAA.")
            else:
                bot.sendMessage(update.message.chat_id, text="El DNI debe ser mayor a 500000.")
        except ValueError:
            bot.sendMessage(update.message.chat_id, text="El DNI ingresado debe ser un número.")
    else:
        bot.sendMessage(update.message.chat_id, text="La cantidad de parámetros pasados es inválida (deben ser 3).")


def echo(bot, update):
    bot.sendMessage(update.message.chat_id, text=update.message.text)

def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))

def main():
    logger.info("Loading handlers for telegram bot")
    
    # Default dispatcher (this is related to the first bot in settings.TELEGRAM_BOT_TOKENS)
    dp = DjangoTelegramBot.dispatcher
    # To get Dispatcher related to a specific bot
    # dp = DjangoTelegramBot.getDispatcher('BOT_n_token')     #get by bot token
    # dp = DjangoTelegramBot.getDispatcher('BOT_n_username')  #get by bot username
    
    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("turnos", turnos, pass_args=True))
    dp.add_handler(CommandHandler("reservar", reservar, pass_args=True))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler([Filters.text], echo))

    # log all errors
    dp.add_error_handler(error)
