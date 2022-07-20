import telebot
import const
from telebot import types

# 5586627418:AAErB1NfsiR2GYytkEzm00yja9AyFbpB1oQ
token = const.TOKEN
bot = telebot.TeleBot(token)


@ bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bot.send_message(
        message.chat.id, text="Привет, {0.first_name}! Задавай мне вопросы и я отвечу!".format(message.from_user))


@bot.message_handler(regexp="Сколько стоит открыть ИП?")
def send_cost(message):
    mess = "Открыть ИП в Грузии стоит YXZ долларов."
    bot.reply_to(message, mess)


@bot.message_handler(regexp="Как зовут вашего руководителя?")
def send_cost(message):
    mess = "Giorgi Bezhitashvili"
    bot.reply_to(message, mess)


@bot.message_handler(regexp="Сколько стоит открыть ООО?")
def send_cost(message):
    mess = "Отркыть ООО в Грузии стоит YXZ долларов."
    bot.reply_to(message, mess)


if __name__ == '__main__':
    bot.infinity_polling()
