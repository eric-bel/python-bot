import telebot
import const
from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


token = const.TOKEN
bot = telebot.TeleBot(token)


def gen_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(InlineKeyboardButton("Основной чат IT Georgia", url="https://t.me/itgeorgia"),
               InlineKeyboardButton("Резюме и вакансии",
                                    url="https://t.me/cvjobge"),
               InlineKeyboardButton(
                   "Открытие и ведение ИП в Грузии", url="https://t.me/ipgeorgia"),
               InlineKeyboardButton(
                   "Список чатов по направлениям ИТ в Грузии", url="https://t.me/itgeorgia/16041"),
               InlineKeyboardButton(
                   "Анонсы мероприятий и новости ИТ комьюнити", url="https://t.me/itgeorgianews"),
               )
    markup.row_width = 3
    markup.add(InlineKeyboardButton("Frontend Georgia", url="https://t.me/frontge"),
               InlineKeyboardButton(
                   "Backend Georgia", url="https://t.me/backendge"))
    markup.row_width = 1
    markup.add(InlineKeyboardButton(
        "ИТ и Психология", url="https://t.me/icyberpsy"))
    return markup


@ bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bot.send_message(
        message.chat.id, text="Привет, {0.first_name}! Я справочный бот для ИТ комьюнити в Грузии. У меня ты можешь получить информацию разного рода.".format(message.from_user), reply_markup=gen_markup())


@ bot.message_handler(commands=['help'])
def start(message):
    bot.send_message(
        message.chat.id, text="Доступнеые команды: \n/start - начало работы с ботом \n/help - помощь \n/about - о боте")


@ bot.message_handler(commands=['about'])
def start(message):
    bot.send_message(
        message.chat.id, text="Меня разработал основатель беларуского ИТ комьюнити в Грузии @object_relations. У меня пока не широкий функционал и я пока умею только оказывать информационную помощь. Возможно, со временем, мои функции расширятся.")


# @ bot.message_handler(content_types=['text'])
# def func(message):
#     if(message.text == "👋 Поздороваться"):
#         bot.send_message(
#             message.chat.id, text="Привеет.. Спасибо что читаешь статью!)")
#     elif(message.text == "❓ Задать вопрос"):
#         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#         btn1 = types.KeyboardButton("Как меня зовут?")
#         btn2 = types.KeyboardButton("Что я могу?")
#         back = types.KeyboardButton("Вернуться в главное меню")
#         markup.add(btn1, btn2, back)
#         bot.send_message(
#             message.chat.id, text="Задай мне вопрос", reply_markup=markup)

#     elif(message.text == "Как меня зовут?"):
#         bot.send_message(message.chat.id, "У меня нет имени..")

#     elif message.text == "Что я могу?":
#         bot.send_message(message.chat.id, text="Поздороваться с читателями")

#     elif (message.text == "Вернуться в главное меню"):
#         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#         button1 = types.KeyboardButton("👋 Поздороваться")
#         button2 = types.KeyboardButton("❓ Задать вопрос")
#         markup.add(button1, button2)
#         bot.send_message(
#             message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
#     else:
#         bot.send_message(
#             message.chat.id, text="Команда не найдена. Попробуйте другие команды или напишите рекомендации и отзывы разработчику @object_relations.")


bot.infinity_polling()
