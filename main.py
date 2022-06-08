import telebot
import const


token = const.TOKEN
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет ✌️, дотсупные команды: \n/dan, \n/lily")


@bot.message_handler(commands=['dan'])
def start_message(message):
    bot.send_message(
    message.chat.id, "Привет ✌️, а кто такой Даник?, это король режима Metro!")

@bot.message_handler(commands=['lily'])
def start_message(message):
    bot.send_message(
    message.chat.id, "Привет ✌️, а кто такой Лилия?, это самая обаятельная девушка в мире!")


bot.infinity_polling()
