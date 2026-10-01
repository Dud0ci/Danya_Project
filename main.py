from telebot import types
from button import *

import math
import telebot
from datetime import date

# {user_id: {"математика": [90, 85, 100]}}
maps = {}
user_state = {}
# {user_id: {"понедельник": ["математика", "физика"]}}
schedules = {}
DAYS = ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье"]
# {user_id: [{"предмет": "математика", "задание": "№ 125, 126"}]}
homeworks = {}
# {user_id: [{"дата": date(2026, 10, 5), "текст": "контрольная по физике"}]}
events = {}



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


def get_schedule_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton("Понедельник"), types.KeyboardButton("Вторник"))
    markup.add(types.KeyboardButton("Среда"), types.KeyboardButton("Четверг"))
    markup.add(types.KeyboardButton("Пятница"), types.KeyboardButton("Суббота"))
    markup.add(types.KeyboardButton("Воскресенье"), types.KeyboardButton("Вся неделя"))
    markup.add(types.KeyboardButton("Ввести расписание"), types.KeyboardButton("Очистить"))
    markup.add(types.KeyboardButton("Вернуться назад"))
    return markup


def format_day(day, lessons):
    if not lessons:
        return day.capitalize() + ": пока пусто"
    lines = [day.capitalize() + ":"]
    for i, l in enumerate(lessons):
        lines.append(str(i + 1) + ". " + l)
    return "\n".join(lines)


def format_week(chat_id):
    sched = schedules.get(chat_id, {})
    parts = []
    for d in DAYS:
        parts.append(format_day(d, sched.get(d, [])))
    return "\n\n".join(parts)


def get_homework_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton("Добавить задание"), types.KeyboardButton("Все задания"))
    markup.add(types.KeyboardButton("Задание выполнено"), types.KeyboardButton("Удалить все задания"))
    markup.add(types.KeyboardButton("Вернуться назад"))
    return markup


def get_events_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton("Добавить событие"), types.KeyboardButton("Все события"))
    markup.add(types.KeyboardButton("Удалить событие"), types.KeyboardButton("Удалить все события"))
    markup.add(types.KeyboardButton("Вернуться назад"))
    return markup


def format_homeworks(chat_id):
    hw = homeworks.get(chat_id, [])
    if not hw:
        return "Домашних заданий нет 🎉"
    lines = ["Домашка:"]
    for i, h in enumerate(hw):
        lines.append(str(i + 1) + ". " + h["предмет"].capitalize() + ": " + h["задание"])
    return "\n".join(lines)


def parse_date(text):
    # принимает ДД.ММ или ДД.ММ.ГГГГ
    parts = text.strip().replace("/", ".").replace("-", ".").split(".")
    try:
        day = int(parts[0])
        month = int(parts[1])
        year = int(parts[2]) if len(parts) > 2 else date.today().year
        if year < 100:
            year += 2000
        d = date(year, month, day)
    except:
        return None
    # если год не указан и дата уже прошла — значит следующий год
    if len(parts) == 2 and d < date.today():
        d = date(year + 1, month, day)
    return d


def format_events(chat_id):
    ev = events.get(chat_id, [])
    if not ev:
        return "Событий пока нет."
    today = date.today()
    lines = ["События:"]
    for i, e in enumerate(ev):
        left = (e["дата"] - today).days
        if left == 0:
            when = "сегодня!"
        elif left == 1:
            when = "завтра"
        elif left > 0:
            when = "через " + str(left) + " дн."
        else:
            when = "прошло"
        lines.append(str(i + 1) + ". " + e["дата"].strftime("%d.%m.%Y") + " — " + e["текст"] + " (" + when + ")")
    return "\n".join(lines)


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
        state = user_state[chat_id]
        if state == "ввод дня":
            day = (text or "").strip().lower()
            if day in DAYS:
                user_state[chat_id] = "ввод уроков:" + day
                bot.send_message(chat_id, day.capitalize() + ": введи уроки через запятую или с новой строки. Пример: математика, русский язык, физика. Для пустого дня отправь: пусто", reply_markup=get_back())
            else:
                bot.send_message(chat_id, "Выбери день кнопками.", reply_markup=get_schedule_menu())
            return
        if state.startswith("ввод уроков:"):
            day = state.split(":", 1)[1]
            if (text or "").strip().lower() in ("пусто", "нет", "-", "выходной"):
                lessons = []
            else:
                lessons = [s.strip() for s in (text or "").replace("\n", ",").split(",") if s.strip()]
                if not lessons:
                    bot.send_message(chat_id, "Не понял. Введи уроки через запятую.")
                    return
            schedules.setdefault(chat_id, {})[day] = lessons
            del user_state[chat_id]
            bot.send_message(chat_id, format_day(day, lessons), reply_markup=get_schedule_menu())
            return
        if state == "дз предмет":
            subject = (text or "").strip().lower()
            if not subject:
                bot.send_message(chat_id, "Введи название предмета.")
                return
            user_state[chat_id] = "дз задание:" + subject
            bot.send_message(chat_id, "Предмет: " + subject + "\nТеперь напиши, что задали:", reply_markup=get_back())
            return
        if state.startswith("дз задание:"):
            subject = state.split(":", 1)[1]
            task = (text or "").strip()
            if not task:
                bot.send_message(chat_id, "Напиши задание текстом.")
                return
            homeworks.setdefault(chat_id, []).append({"предмет": subject, "задание": task})
            del user_state[chat_id]
            bot.send_message(chat_id, "Записал!\n\n" + format_homeworks(chat_id), reply_markup=get_homework_menu())
            return
        if state == "дз выполнено":
            hw = homeworks.get(chat_id, [])
            try:
                n = int((text or "").strip())
            except:
                n = 0
            if not 1 <= n <= len(hw):
                bot.send_message(chat_id, "Введи номер задания из списка (от 1 до " + str(len(hw)) + ").")
                return
            done = hw.pop(n - 1)
            del user_state[chat_id]
            bot.send_message(chat_id, "Молодец! Выполнено: " + done["предмет"].capitalize() + " — " + done["задание"] + "\n\n" + format_homeworks(chat_id), reply_markup=get_homework_menu())
            return
        if state == "событие дата":
            d = parse_date(text or "")
            if d is None:
                bot.send_message(chat_id, "Не понял дату. Введи в формате ДД.ММ, например: 05.10")
                return
            user_state[chat_id] = "событие текст:" + d.isoformat()
            bot.send_message(chat_id, "Дата: " + d.strftime("%d.%m.%Y") + "\nЧто за событие?", reply_markup=get_back())
            return
        if state.startswith("событие текст:"):
            d = date.fromisoformat(state.split(":", 1)[1])
            what = (text or "").strip()
            if not what:
                bot.send_message(chat_id, "Напиши, что за событие.")
                return
            ev = events.setdefault(chat_id, [])
            ev.append({"дата": d, "текст": what})
            ev.sort(key=lambda e: e["дата"])
            del user_state[chat_id]
            bot.send_message(chat_id, "Добавил!\n\n" + format_events(chat_id), reply_markup=get_events_menu())
            return
        if state == "событие удалить":
            ev = events.get(chat_id, [])
            try:
                n = int((text or "").strip())
            except:
                n = 0
            if not 1 <= n <= len(ev):
                bot.send_message(chat_id, "Введи номер события из списка (от 1 до " + str(len(ev)) + ").")
                return
            ev.pop(n - 1)
            del user_state[chat_id]
            bot.send_message(chat_id, "Удалил.\n\n" + format_events(chat_id), reply_markup=get_events_menu())
            return
        if state == "жду предмет":
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
        bot.send_message(chat_id, "Выбери день или нажми «Ввести расписание»:", reply_markup=get_schedule_menu())
    elif text == "Ввести расписание":
        user_state[chat_id] = "ввод дня"
        bot.send_message(chat_id, "На какой день ввести? Выбери кнопкой.", reply_markup=get_schedule_menu())
    elif text == "Очистить":
        schedules[chat_id] = {}
        bot.send_message(chat_id, "Расписание очищено.", reply_markup=get_schedule_menu())
    elif text == "Вся неделя":
        bot.send_message(chat_id, format_week(chat_id), reply_markup=get_schedule_menu())
    elif (text or "").lower() in DAYS:
        day = text.lower()
        bot.send_message(chat_id, format_day(day, schedules.get(chat_id, {}).get(day, [])), reply_markup=get_schedule_menu())
    elif text == "📚 Домашка":
        bot.send_message(chat_id, format_homeworks(chat_id), reply_markup=get_homework_menu())
    elif text == "Добавить задание":
        user_state[chat_id] = "дз предмет"
        bot.send_message(chat_id, "По какому предмету задание?", reply_markup=get_back())
    elif text == "Все задания":
        bot.send_message(chat_id, format_homeworks(chat_id), reply_markup=get_homework_menu())
    elif text == "Задание выполнено":
        if not homeworks.get(chat_id):
            bot.send_message(chat_id, "Домашних заданий нет 🎉", reply_markup=get_homework_menu())
        else:
            user_state[chat_id] = "дз выполнено"
            bot.send_message(chat_id, format_homeworks(chat_id) + "\n\nВведи номер выполненного задания:", reply_markup=get_back())
    elif text == "Удалить все задания":
        homeworks[chat_id] = []
        bot.send_message(chat_id, "Все задания удалены.", reply_markup=get_homework_menu())
    elif text == "🎉 События":
        bot.send_message(chat_id, format_events(chat_id), reply_markup=get_events_menu())
    elif text == "Добавить событие":
        user_state[chat_id] = "событие дата"
        bot.send_message(chat_id, "Введи дату в формате ДД.ММ (например: 05.10):", reply_markup=get_back())
    elif text == "Все события":
        bot.send_message(chat_id, format_events(chat_id), reply_markup=get_events_menu())
    elif text == "Удалить событие":
        if not events.get(chat_id):
            bot.send_message(chat_id, "Событий пока нет.", reply_markup=get_events_menu())
        else:
            user_state[chat_id] = "событие удалить"
            bot.send_message(chat_id, format_events(chat_id) + "\n\nВведи номер события, которое удалить:", reply_markup=get_back())
    elif text == "Удалить все события":
        events[chat_id] = []
        bot.send_message(chat_id, "Все события удалены.", reply_markup=get_events_menu())

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
