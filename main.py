import telebot
import key
from telebot import types

bot = telebot.TeleBot(key.token)


@bot.message_handler(commands=["start"])
def keyboard_start(message):
    startKBoard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    Raspisanya = types.KeyboardButton(text="Расписание уроков")
    startKBoard.add(Raspisanya)
    bot.send_message(message.chat.id, "Доброе утро!", reply_markup=startKBoard)


@bot.message_handler(func=lambda m: m.text == 'Расписание уроков')
def echo_all(message):
    startKBoard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    PP1 = types.KeyboardButton(text="Понедельник")
    PP2 = types.KeyboardButton(text="Вторник")
    PP3 = types.KeyboardButton(text="Среда")
    PP4 = types.KeyboardButton(text="Четверг")
    PP5 = types.KeyboardButton(text="Пятница")
    PP6 = types.KeyboardButton(text="Закончить смотреть расписание")
    startKBoard.add(PP1, PP2, PP3, PP4, PP5, PP6)
    bot.send_message(message.chat.id, "На какой день вы бы хотели увидеть расписание", reply_markup=startKBoard)


@bot.message_handler(func=lambda m: m.text == 'Понедельник')
def mes(message):
    startKboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    bot.send_message(message.chat.id,"Алгебра \n Геометрия \n Русский язык \n Русский язык \n Физика \n Физика \n Информатика", reply_markup=startKboard)
@bot.message_handler(func=lambda m: m.text == 'Вторник')
def nes(message):
    startKboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    bot.send_message(message.chat.id,"Химия \n Литература \n Английский язык \n Информатика \n Биология \n География", reply_markup=startKboard)
@bot.message_handler(func=lambda m: m.text == 'Среда')
def res(message):
    startKboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    bot.send_message(message.chat.id,"Геометрия \n Геометрия \n Английский язык \n Информатика \n История \n История", reply_markup=startKboard)
@bot.message_handler(func=lambda m: m.text == 'Четверг')
def ses(message):
    startKboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    bot.send_message(message.chat.id, "История \n Обществознание \n Физика \n Алгебра \n Физкультура \n Физкультура", reply_markup=startKboard)
@bot.message_handler(func=lambda m: m.text == 'Пятница')
def ges(message):
    startKboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    bot.send_message(message.chat.id, "Физика \n Физика \n Литература \n Обществознание \n Геометрия \n Алгебра", reply_markup=startKboard)
@bot.message_handler(func=lambda m: m.text == 'Закончить смотреть расписание')
def chert(message):
    startKboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    Raspisanya = types.KeyboardButton(text="Расписание уроков")
    startKboard.add(Raspisanya)
    bot.send_message(message.chat.id,"Вы закончили смотреть распиание,удачной учёбы", reply_markup=startKboard)
bot.polling()


