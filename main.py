from telebot import types
from button import *

import telebot

maps = {'user':{
    "математик":[5,5,5,5,4,3,4,5,5]
}}



bot = telebot.TeleBot('6700021409:AAH2TBRCtcIvtoQ4Bl73hNsTQIlNbOEDImo')


def get_main_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)


    btn_games = types.KeyboardButton("⭐ Подсчет Оценок")
    btn_schedule = types.KeyboardButton("📅 Расписание")
    btn_homework = types.KeyboardButton("📚 Домашка")
    btn_events = types.KeyboardButton("🎉 События")
    btn_gdz = types.KeyboardButton("📖 ГДЗ")

    markup.add(btn_games, btn_schedule)
    markup.add(btn_homework, btn_events)
    markup.add(btn_gdz)
    return markup


@bot.message_handler(commands=["start"])
def send_welcome(message):
    text = ("<-✧ ▬◻▬ ▬◻▬ ✦✧✦ ▬◻▬ ▬◻▬ ✧ ->\n"
        "Привет! Я твой бот для учёбы!\n"
        "Выбери пункт в меню, чтобы начать.\n"
        "<-✧ ▬◻▬ ▬◻▬ ✦✧✦ ▬◻▬ ▬◻▬ ✧ ->"
    )
    bot.send_message(message.chat.id, text, reply_markup=get_main_menu())




'''
Просто заметки 
    if text == "⭐ Подсчет Оценок":
        bot.send_message(chat_id, "Скоро...")
    elif text == "📅 Расписание":
        bot.send_message(chat_id, "Скоро...")
    elif text == "📚 Домашка":
        bot.send_message(chat_id, "Скоро...")
    elif text == "🎉 События":
        bot.send_message(chat_id, "Скоро...")
    elif text =="📖 ГДЗ":
        bot.send_message(
            message.chat.id,
            "Выбери класс:",
            reply_markup=get_gdz_submenu()
        )
'''
@bot.message_handler(func=lambda m: True)
def handle_all_messages(message):
    text = message.text
    chat_id = message.chat.id


    if text == "⭐ Подсчет Оценок":
        bot.send_message(chat_id, "Скоро...")
    elif text == "📅 Расписание":
        bot.send_message(chat_id, "Скоро...")
    elif text == "📚 Домашка":
        bot.send_message(chat_id, "Скоро...")
    elif text == "🎉 События":
        bot.send_message(chat_id, "Скоро...")

    elif text == "📖 ГДЗ":
        bot.send_message(chat_id, "Выбери класс:", reply_markup=get_gdz_submenu())
        
    if text == "Вернуться назад":
        bot.send_message(chat_id, "Выбери:", reply_markup=get_main_menu())
    else:
        for i in range(1,12):
            number_class = f'{str(i)} Класс'
            if text == number_class:
                bot.send_message(chat_id, "Выбери предмет:", reply_markup=function_list[i-1]())
                break





''' Каждый предмет если что внимание не обращайте
    1: ["Математика", "Русский язык", "Литература", "Окружающий мир"],
    2: ["Математика", "Русский язык", "Литература", "Окружающий мир","Английский язык"],
    3: ["Математика", "Русский язык", "Литература", "Окружающий мир","Английский язык"],
    4: ["Математика", "Русский язык", "Литература", "Окружающий мир","Английский язык"],
    5: ["Математика", "Русский язык", "Литература", "Английский язык", "История", "География", "Биология"],
    6: ["Математика", "Русский язык", "Литература", "Английский язык", "История", "География", "Биология",],
    7: ["Алгебра", "Геометрия", "Русский язык", "Литература", "Английский язык", "История","География", "Биология", "Физика", "Информатика"],
    8: ["Алгебра", "Геометрия", "Русский язык", "Литература", "Английский язык", "История","География", "Биология", "Физика", "Химия", "Информатика"],
    9: ["Алгебра", "Геометрия", "Русский язык", "Литература", "Английский язык", "История","География", "Биология", "Физика", "Химия", "Информатика"],
    10: ["Алгебра", "Геометрия", "Русский язык", "Литература", "Английский язык", "История","География", "Биология", "Физика", "Химия", "Информатика"],
    11: ["Алгебра", "Геометрия", "Русский язык", "Литература", "Английский язык", "История","География", "Биология", "Физика", "Химия", "Информатика"],
'''


@bot.message_handler(func=lambda message: True)
def handle_menu_click(message):
    text = message.text
    chat_id = message.chat.id
    
    if text == "1 Класс":
        bot.send_message(
            chat_id,
            "Выбери предмет:",
            reply_markup=btn_1(),
        )
    elif text == "2 Класс":
        bot.send_message(
            chat_id,
            "Выбери предмет:",
            reply_markup=btn_2(),
        )
    elif text == "3 Класс":
        bot.send_message(
            chat_id,
            "Выбери предмет:",
            reply_markup=btn_3(),
        )
    elif text == "4 Класс":
        bot.send_message(
            chat_id,
            "Выбери предмет:",
            reply_markup=btn_4(),
        )
    elif text == "5 Класс":
        bot.send_message(
            chat_id,
            "Выбери предмет:",
            reply_markup=btn_5(),
        )
    elif text == "6 Класс":
        bot.send_message(
            chat_id,
            "Выбери предмет:",
            reply_markup=btn_6(),
        )
    elif text == "7 Класс":
        bot.send_message(
            chat_id,
            "Выбери предмет:",
            reply_markup=btn_7(),
        )
    elif text == "8 Класс":
        bot.send_message(
            chat_id,
            "Выбери предмет:",
            reply_markup=btn_8(),
        )
    elif text == "9 Класс":
        bot.send_message(
            chat_id,
            "Выбери предмет:",
            reply_markup=btn_9(),
        )
    elif text == "10 Класс":
        bot.send_message(
            chat_id,
            "Выбери предмет:",
            reply_markup=btn_10(),
        )
    elif text == "11 Класс":
        bot.send_message(
            chat_id,
            "Выбери предмет:",
            reply_markup=btn_11(),
        )


bot.infinity_polling()