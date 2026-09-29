from telebot import types
from button import *

import math
import telebot

# {user_id: {"математика": [90, 85, 100]}}
maps = {}
user_state = {}



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


def get_back():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton("Вернуться назад"))
    return markup


def parse_grades(text):
    parts = text.replace(";", " ").replace(",", " ").split()
    grades = []
    for p in parts:
        p = p.strip()
        try:
            g = float(p) if "." in p else int(p)
        except:
            return []
        if 0 <= g <= 100:
            grades.append(g)
        else:
            return []
    return grades


def need_marks(total, count, target, max_mark=100):
    if count == 0:
        return 0
    if total / count >= target:
        return 0
    n = math.ceil((target * count - total) / (max_mark - target))
    if n < 0:
        return 0
    return n


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

    if chat_id in user_state:
        if text == "Вернуться назад":
            del user_state[chat_id]
            bot.send_message(chat_id, "Выбери:", reply_markup=get_main_menu())
            return
        if user_state[chat_id] == "жду предмет":
            subject = text.strip().lower()
            user_state[chat_id] = subject
            bot.send_message(chat_id, "Предмет: " + subject + "\nВведи через запятую оценки от 0 до 100 (например: 90, 85, 100):")
            return
        subject = user_state[chat_id]
        new_grades = parse_grades(text or "")
        if not new_grades:
            bot.send_message(chat_id, "Не понял. Введи только числа от 0 до 100 через запятую, например: 90, 85, 100")
            return
        # добавляем к уже сохранённым оценкам, а не перезаписываем
        grades = maps.setdefault(chat_id, {}).setdefault(subject, [])
        grades.extend(new_grades)
        total = sum(grades)
        count = len(grades)
        avg = total / count
        out = "Предмет: " + subject + "\nОценки: " + ", ".join(map(str, grades)) + "\nСредний балл: " + str(round(avg, 2)) + "\nВсего: " + str(count) + ", мин: " + str(min(grades)) + ", макс: " + str(max(grades)) + "\n"
        if avg >= 90:
            out = out + "Выходит отлично!"
        elif avg >= 75:
            out = out + "Выходит хорошо. До 90 нужно еще " + str(need_marks(total, count, 90)) + " соток."
        elif avg >= 50:
            out = out + "Выходит удовл. До 75 нужно еще " + str(need_marks(total, count, 75)) + " соток."
        else:
            out = out + "Выходит неуд. До 50 нужно еще " + str(need_marks(total, count, 50)) + " соток."
        del user_state[chat_id]
        bot.send_message(chat_id, out, reply_markup=get_main_menu())
        return

    if text == "⭐ Подсчет Оценок":
        user_state[chat_id] = "жду предмет"
        bot.send_message(chat_id, "Введи название предмета:", reply_markup=get_back())
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


    if text == "Вернуться назад":
        bot.send_message(chat_id,"Выбери:",reply_markup=get_main_menu())
        return
        
    for i in range(1, 12):
        number_class = f"{str(i)} Класс"

        if text == number_class:

            bot.send_message(chat_id,"Выбери предмет:",reply_markup=function_list[i - 1]())
            break
bot.remove_webhook()
bot.infinity_polling()
