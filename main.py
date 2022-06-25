# from email import message
import asyncio
import telebot
import const
from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.async_telebot import AsyncTeleBot


token = const.TOKEN
# bot = telebot.TeleBot(token)
bot = AsyncTeleBot(token=token)


async def update_listener(messages):
    for message in messages:
        if message.text == '/start':
            await bot.send_message(message.chat.id, 'Hello!')

bot.set_update_listener(update_listener)


def gen_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(InlineKeyboardButton("Основной чат IT Georgia", url="https://t.me/itgeorgia"),
               InlineKeyboardButton(
                   "Анонсы мероприятий и новости ИТ комьюнити", url="https://t.me/itgeorgianews"),
               InlineKeyboardButton("Резюме и вакансии",
                                    url="https://t.me/cvjobge"),
               InlineKeyboardButton(
                   "Открытие и ведение ИП в Грузии", url="https://t.me/ipgeorgia"),
               InlineKeyboardButton(
                   "Список чатов по направлениям ИТ в Грузии", callback_data="list_chats"),
               )
    markup.row_width = 2
    markup.add(InlineKeyboardButton("ИТ и Психология", callback_data="cyberpsy"),
               InlineKeyboardButton("Для HR и рекрутеров", callback_data="hr"))
    return markup


def list_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(
        InlineKeyboardButton("IT CV&Vacancy Georgia",
                             url="https://t.me/cvjobge"),
        InlineKeyboardButton("Frontend", url="https://t.me/frontge"),
        InlineKeyboardButton("Backend", url="https://t.me/backendge"),
        InlineKeyboardButton("Mobile dev", url="https://t.me/mobdevge"),
        InlineKeyboardButton("Design", url="https://t.me/designge"),
        InlineKeyboardButton("РМ + PdM + BA", url="https://t.me/itpmge"),
        InlineKeyboardButton(
            "Sales/продажи", url="https://t.me/itsalesgeorgia"),
        InlineKeyboardButton("Marketing", url="https://t.me/marketingeorgia"),
        InlineKeyboardButton("Python", url="https://t.me/georgiapython"),
        InlineKeyboardButton("Ruby", url="https://t.me/rubydevcom"),
        InlineKeyboardButton("QA", url="https://t.me/+u11UXTsveJkwOTAy"),)
    return markup


@bot.callback_query_handler(func=lambda call: True)
async def callback_inline(call):
    if call.message:
        if call.data == "hr":
            mess = "В основном чате @itgeorgia запрещено публиковать вакансии. \nДля этого есть ряд дочерних и партнёрских чатов:"
            await bot.send_message(call.message.chat.id, mess,
                             reply_markup=list_markup())
        elif call.data == "cyberpsy":
            mess = "Всех, кто интересуется ИТ и психологией, приглашаю подписаться на канал https://t.me/icyberpsy, также у канала есть чат для обсуждений https://t.me/icyberpsy_chat. Этот канал не относится к беларускому ИТ комьюнити в Грузии, Это просто на правах рекламы ))"
            await bot.send_message(call.message.chat.id, mess)
        elif call.data == "list_chats":
            mess = "Список чатов по направлениям ИТ в Грузии"
            await bot.send_message(call.message.chat.id, mess,
                                   reply_markup=list_markup())


@bot.message_handler(regexp="Vacancy")
async def send_text(message):
    mess = "В этом чате запрещено публиковать вакансии. \nДля этого есть ряд дочерних и партнёрских чатов:"
    bot.send_message(message.chat.id, mess, reply_markup=list_markup())


@bot.message_handler(regexp="Вакансия")
async def send_text(message):
    mess = "В этом чате запрещено публиковать вакансии. \nДля этого есть ряд дочерних и партнёрских чатов:"
    await bot.send_message(message.chat.id, mess, reply_markup=list_markup())


@ bot.message_handler(commands=['start'])
async def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    await bot.send_message(
        message.chat.id, text="Привет, {0.first_name}! Я справочный бот для ИТ комьюнити в Грузии. У меня ты можешь получить информацию разного рода.".format(message.from_user), reply_markup=gen_markup())


@ bot.message_handler(commands=['help'])
async def help(message):
    await bot.send_message(
        message.chat.id, text="Доступнеые команды: \n/start - начало работы с ботом \n/help - помощь \n/about - о боте")


@ bot.message_handler(commands=['hr'])
async def hr(message):
    mess = "В этом чате запрещено публиковать вакансии. \nДля этого есть ряд дочерних и партнёрских чатов:"
    await bot.send_message(message.chat.id, mess, reply_markup=list_markup())


@ bot.message_handler(commands=['about'])
async def about(message):
    await bot.send_message(
        message.chat.id, text="У меня пока не широкий функционал и я пока предоставляю только справочную информацию. Возможно, со временем, мои функции расширятся.")


# @ bot.message_handler()
# def send_welcome(message):
#     bot.send_message(
#         message.chat.id, "Команда не найдена. Попробуйте ввести /help")

asyncio.run(bot.polling())
# bot.infinity_polling()
