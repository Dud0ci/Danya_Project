import time
import math
import telebot
from telebot import types

bot = telebot.TeleBot("8624090640:AAFMEIbit3V34rNzz2AXKfcjhAzBuAhP-_U")

maps = {}
user_state = {}

def get_main_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    markup.add(types.KeyboardButton("⭐ подсчет оценок"), types.KeyboardButton("📅 расписание"))
    markup.add(types.KeyboardButton("📚 домашка"), types.KeyboardButton("🎉 события"))
    markup.add(types.KeyboardButton("📖 гдз"))
    return markup

def get_gdz_submenu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton("1 класс"), types.KeyboardButton("2 класс"))
    markup.add(types.KeyboardButton("3 класс"), types.KeyboardButton("4 класс"))
    markup.add(types.KeyboardButton("5 класс"), types.KeyboardButton("6 класс"))
    markup.add(types.KeyboardButton("7 класс"), types.KeyboardButton("8 класс"))
    markup.add(types.KeyboardButton("9 класс"), types.KeyboardButton("10 класс"))
    markup.add(types.KeyboardButton("11 класс"), types.KeyboardButton("вернуться назад"))
    return markup

def get_back():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton("вернуться назад"))
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

def btn_1():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("математика", url="https://resh.skysmart.ru/1-klass/matematika/moro-1222?ysclid=mty9kc0imf317229549"), types.InlineKeyboardButton("русский язык", url="https://resh.skysmart.ru/1-klass/russkij-yazyk/krylova-629"))
    markup.add(types.InlineKeyboardButton("литература", url="https://budu5.com/gdz/view/143"), types.InlineKeyboardButton("окружающий мир", url="https://budu5.com/gdz/view/90"))
    return markup

def btn_2():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("математика", url="https://budu5.com/gdz/view/110"), types.InlineKeyboardButton("русский язык", url="https://budu5.com/gdz/view/19"))
    markup.add(types.InlineKeyboardButton("литература", url="https://budu5.com/gdz/view/150"), types.InlineKeyboardButton("окружающий мир", url="https://budu5.com/gdz/view/97"))
    markup.add(types.InlineKeyboardButton("английский язык", url="https://budu5.com/gdz/view/214"))
    return markup

def btn_3():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("математика", url="https://reshak.ru/tag/3klass_math.html"), types.InlineKeyboardButton("русский язык", url="https://reshak.ru/tag/3klass_rus.html"))
    markup.add(types.InlineKeyboardButton("литература", url="https://reshak.ru/tag/3klass_chtenie.html"), types.InlineKeyboardButton("окружающий мир", url="https://reshak.ru/tag/3klass_mir.html"))
    markup.add(types.InlineKeyboardButton("английский язык", url="https://reshak.ru/tag/3klass_eng.html"))
    return markup

def btn_4():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("математика", url="https://reshak.ru/tag/4klass_math.html"), types.InlineKeyboardButton("русский язык", url="https://reshak.ru/tag/4klass_rus.html"))
    markup.add(types.InlineKeyboardButton("литература", url="https://reshak.ru/tag/4klass_chtenie.html"), types.InlineKeyboardButton("окружающий мир", url="https://reshak.ru/tag/4klass_mir.html"))
    markup.add(types.InlineKeyboardButton("английский язык", url="https://reshak.ru/tag/4klass_eng.html"))
    return markup

def btn_5():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("математика", url="https://reshak.ru/tag/5klass_math.html"), types.InlineKeyboardButton("русский язык", url="https://reshak.ru/tag/5klass_rus.html"))
    markup.add(types.InlineKeyboardButton("литература", url="https://reshak.ru/tag/5klass_chtenie.html"), types.InlineKeyboardButton("история", url="https://reshak.ru/tag/5klass_istoria.html"))
    markup.add(types.InlineKeyboardButton("география", url="https://reshak.ru/tag/5klass_geograph.html"), types.InlineKeyboardButton("биология", url="https://reshak.ru/tag/5klass_bio.html"))
    markup.add(types.InlineKeyboardButton("английский язык", url="https://reshak.ru/tag/5klass_eng.html"))
    return markup

def btn_6():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("математика", url="https://reshak.ru/tag/6klass_math.html"), types.InlineKeyboardButton("русский язык", url="https://reshak.ru/tag/6klass_rus.html"))
    markup.add(types.InlineKeyboardButton("литература", url="https://reshak.ru/tag/6klass_chtenie.html"), types.InlineKeyboardButton("история", url="https://reshak.ru/tag/6klass_istoria.html"))
    markup.add(types.InlineKeyboardButton("география", url="https://reshak.ru/tag/6klass_geograph.html"), types.InlineKeyboardButton("биология", url="https://reshak.ru/tag/6klass_bio.html"))
    markup.add(types.InlineKeyboardButton("английский язык", url="https://reshak.ru/tag/6klass_eng.html"))
    return markup

def btn_7():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("алгебра", url="https://reshak.ru/tag/7klass_alg.html"), types.InlineKeyboardButton("геометрия", url="https://reshak.ru/tag/7klass_geo.html"))
    markup.add(types.InlineKeyboardButton("русский язык", url="https://reshak.ru/tag/7klass_rus.html"), types.InlineKeyboardButton("литература", url="https://reshak.ru/tag/7klass_chtenie.html"))
    markup.add(types.InlineKeyboardButton("история", url="https://reshak.ru/tag/7klass_istoria.html"), types.InlineKeyboardButton("география", url="https://reshak.ru/tag/7klass_geograph.html"))
    markup.add(types.InlineKeyboardButton("биология", url="https://reshak.ru/tag/7klass_bio.html"), types.InlineKeyboardButton("физика", url="https://reshak.ru/tag/7klass_fiz.html"))
    markup.add(types.InlineKeyboardButton("английский язык", url="https://reshak.ru/tag/7klass_eng.html"), types.InlineKeyboardButton("информатика", url="https://reshak.ru/tag/7klass_inf.html"))
    return markup

def btn_8():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("алгебра", url="https://reshak.ru/tag/8klass_alg.html"), types.InlineKeyboardButton("геометрия", url="https://reshak.ru/tag/8klass_geo.html"))
    markup.add(types.InlineKeyboardButton("русский язык", url="https://reshak.ru/tag/8klass_rus.html"), types.InlineKeyboardButton("литература", url="https://reshak.ru/tag/8klass_chtenie.html"))
    markup.add(types.InlineKeyboardButton("история", url="https://reshak.ru/tag/8klass_istoria.html"), types.InlineKeyboardButton("география", url="https://reshak.ru/tag/8klass_geograph.html"))
    markup.add(types.InlineKeyboardButton("биология", url="https://reshak.ru/tag/8klass_bio.html"), types.InlineKeyboardButton("физика", url="https://reshak.ru/tag/8klass_fiz.html"))
    markup.add(types.InlineKeyboardButton("химия", url="https://reshak.ru/tag/8klass_him.html"), types.InlineKeyboardButton("информатика", url="https://reshak.ru/tag/8klass_inf.html"))
    markup.add(types.InlineKeyboardButton("английский язык", url="https://reshak.ru/tag/8klass_eng.html"))
    return markup

def btn_9():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("алгебра", url="https://reshak.ru/tag/9klass_alg.html"), types.InlineKeyboardButton("геометрия", url="https://reshak.ru/tag/9klass_geo.html"))
    markup.add(types.InlineKeyboardButton("русский язык", url="https://reshak.ru/tag/9klass_rus.html"), types.InlineKeyboardButton("литература", url="https://reshak.ru/tag/9klass_chtenie.html"))
    markup.add(types.InlineKeyboardButton("история", url="https://reshak.ru/tag/9klass_istoria.html"), types.InlineKeyboardButton("география", url="https://reshak.ru/tag/9klass_geograph.html"))
    markup.add(types.InlineKeyboardButton("биология", url="https://reshak.ru/tag/9klass_bio.html"), types.InlineKeyboardButton("физика", url="https://reshak.ru/tag/9klass_fiz.html"))
    markup.add(types.InlineKeyboardButton("химия", url="https://reshak.ru/tag/9klass_him.html"), types.InlineKeyboardButton("информатика", url="https://reshak.ru/tag/9klass_inf.html"))
    markup.add(types.InlineKeyboardButton("английский язык", url="https://reshak.ru/tag/9klass_eng.html"))
    return markup

def btn_10():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("алгебра", url="https://reshak.ru/tag/10klass_alg.html"), types.InlineKeyboardButton("геометрия", url="https://reshak.ru/tag/10klass_geo.html"))
    markup.add(types.InlineKeyboardButton("русский язык", url="https://reshak.ru/tag/10klass_rus.html"), types.InlineKeyboardButton("литература", url="https://reshak.ru/tag/10klass_chtenie.html"))
    markup.add(types.InlineKeyboardButton("история", url="https://reshak.ru/tag/10klass_istoria.html"), types.InlineKeyboardButton("география", url="https://reshak.ru/tag/10klass_geograph.html"))
    markup.add(types.InlineKeyboardButton("биология", url="https://reshak.ru/tag/10klass_bio.html"), types.InlineKeyboardButton("физика", url="https://reshak.ru/tag/10klass_fiz.html"))
    markup.add(types.InlineKeyboardButton("химия", url="https://reshak.ru/tag/10klass_him.html"), types.InlineKeyboardButton("информатика", url="https://reshak.ru/tag/10klass_inf.html"))
    markup.add(types.InlineKeyboardButton("английский язык", url="https://reshak.ru/tag/10klass_eng.html"))
    return markup

def btn_11():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("алгебра", url="https://reshak.ru/tag/11klass_alg.html"), types.InlineKeyboardButton("геометрия", url="https://reshak.ru/tag/11klass_geo.html"))
    markup.add(types.InlineKeyboardButton("русский язык", url="https://reshak.ru/tag/11klass_rus.html"), types.InlineKeyboardButton("литература", url="https://reshak.ru/tag/11klass_chtenie.html"))
    markup.add(types.InlineKeyboardButton("история", url="https://reshak.ru/tag/11klass_istoria.html"), types.InlineKeyboardButton("география", url="https://reshak.ru/tag/11klass_geograph.html"))
    markup.add(types.InlineKeyboardButton("биология", url="https://reshak.ru/tag/11klass_bio.html"), types.InlineKeyboardButton("физика", url="https://reshak.ru/tag/11klass_fiz.html"))
    markup.add(types.InlineKeyboardButton("химия", url="https://reshak.ru/tag/11klass_him.html"), types.InlineKeyboardButton("информатика", url="https://reshak.ru/tag/11klass_inf.html"))
    markup.add(types.InlineKeyboardButton("английский язык", url="https://reshak.ru/tag/11klass_eng.html"))
    return markup

class_to_markup = {"1 класс": btn_1, "2 класс": btn_2, "3 класс": btn_3, "4 класс": btn_4, "5 класс": btn_5, "6 класс": btn_6, "7 класс": btn_7, "8 класс": btn_8, "9 класс": btn_9, "10 класс": btn_10, "11 класс": btn_11}

@bot.message_handler(commands=["start"])
def send_welcome(message):
    if message.chat.id in user_state:
        del user_state[message.chat.id]
    bot.send_message(message.chat.id, "привет! я твой бот для учёбы! выбери пункт в меню, чтобы начать.", reply_markup=get_main_menu())

@bot.message_handler(content_types=["text"])
def handle_all_messages(message):
    raw = (message.text or "").strip()
    text = raw.lower()
    chat_id = message.chat.id
    if not text:
        return
    if text.startswith("/"):
        return
    if text == "⭐ подсчет оценок":
        user_state[chat_id] = "жду предмет"
        bot.send_message(chat_id, "введи название предмета:", reply_markup=get_back())
        return
    if user_state.get(chat_id, "") == "жду предмет":
        if text == "вернуться назад":
            del user_state[chat_id]
            bot.send_message(chat_id, "выбери:", reply_markup=get_main_menu())
            return
        subject = text
        user_state[chat_id] = subject
        bot.send_message(chat_id, "предмет: " + subject + "\nвведи через запятую оценки от 0 до 100 (например: 90, 85, 100):")
        return
    if chat_id in user_state:
        subject = user_state[chat_id]
        if subject == "жду предмет":
            return
        if text == "вернуться назад":
            del user_state[chat_id]
            bot.send_message(chat_id, "выбери:", reply_markup=get_main_menu())
            return
        grades = parse_grades(raw)
        if not grades:
            bot.send_message(chat_id, "не понял. введи только числа от 0 до 100 через запятую, например: 90, 85, 100")
            return
        if chat_id not in maps:
            maps[chat_id] = {}
        maps[chat_id][subject] = grades
        total = sum(grades)
        count = len(grades)
        avg = total / count
        out = "предмет: " + subject + "\nоценки: " + ", ".join(map(str, grades)) + "\nсредний балл: " + str(round(avg, 2)) + "\nвсего: " + str(count) + ", мин: " + str(min(grades)) + ", макс: " + str(max(grades)) + "\n"
        if avg >= 90:
            out = out + "выходит отлично!"
        elif avg >= 75:
            out = out + "выходит хорошо. до 90 нужно еще " + str(need_marks(total, count, 90)) + " соток."
        elif avg >= 50:
            out = out + "выходит удовл. до 75 нужно еще " + str(need_marks(total, count, 75)) + " соток."
        else:
            out = out + "выходит неуд. до 50 нужно еще " + str(need_marks(total, count, 50)) + " соток."
        del user_state[chat_id]
        bot.send_message(chat_id, out, reply_markup=get_main_menu())
        return
    if text == "📅 расписание":
        bot.send_message(chat_id, "скоро...")
    elif text == "📚 домашка":
        bot.send_message(chat_id, "скоро...")
    elif text == "🎉 события":
        bot.send_message(chat_id, "скоро...")
    elif text == "📖 гдз":
        bot.send_message(chat_id, "выбери класс:", reply_markup=get_gdz_submenu())
    elif text in class_to_markup:
        bot.send_message(chat_id, "выбери предмет:", reply_markup=class_to_markup[text]())
    elif text == "вернуться назад":
        bot.send_message(chat_id, "выбери:", reply_markup=get_main_menu())

if __name__ == "__main__":
    while True:
        try:
            bot.infinity_polling(timeout=15, long_polling_timeout=30, skip_pending=True)
        except:
            print("polling error")
            time.sleep(5)
