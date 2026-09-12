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

    elif text == "1 Класс":
        bot.send_message(chat_id, "Выбери предмет:", reply_markup=btn_1())
    elif text == "2 Класс":
        bot.send_message(chat_id, "Выбери предмет:", reply_markup=btn_2())
    elif text == "3 Класс":
        bot.send_message(chat_id, "Выбери предмет:", reply_markup=btn_3())
    elif text == "4 Класс":
        bot.send_message(chat_id, "Выбери предмет:", reply_markup=btn_4())
    elif text == "5 Класс":
        bot.send_message(chat_id, "Выбери предмет:", reply_markup=btn_5())
    elif text == "6 Класс":
        bot.send_message(chat_id, "Выбери предмет:", reply_markup=btn_6())
    elif text == "7 Класс":
        bot.send_message(chat_id, "Выбери предмет:", reply_markup=btn_7())
    elif text == "8 Класс":
        bot.send_message(chat_id, "Выбери предмет:", reply_markup=btn_8())
    elif text == "9 Класс":
        bot.send_message(chat_id, "Выбери предмет:", reply_markup=btn_9())
    elif text == "10 Класс":
        bot.send_message(chat_id, "Выбери предмет:", reply_markup=btn_10())
    elif text == "11 Класс":
        bot.send_message(chat_id, "Выбери предмет:", reply_markup=btn_11())

    elif text == "Вернуться назад":
        bot.send_message(chat_id, "Выбери:", reply_markup=get_main_menu())



def get_gdz_submenu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_1 = types.KeyboardButton("1 Класс")
    btn_2 = types.KeyboardButton("2 Класс")
    btn_3 = types.KeyboardButton("3 Класс")
    btn_4 = types.KeyboardButton("4 Класс")
    btn_5 = types.KeyboardButton("5 Класс")
    btn_6 = types.KeyboardButton("6 Класс")
    btn_7 = types.KeyboardButton("7 Класс")
    btn_8 = types.KeyboardButton("8 Класс")
    btn_9 = types.KeyboardButton("9 Класс")
    btn_10 = types.KeyboardButton("10 Класс")
    btn_11 = types.KeyboardButton("11 Класс")
    back = types.KeyboardButton("Вернуться назад")

    markup.add(btn_1, btn_2)
    markup.add(btn_3, btn_4)
    markup.add(btn_5, btn_6)
    markup.add(btn_7, btn_8)
    markup.add(btn_9, btn_10)
    markup.add(btn_11,back)

    return markup

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

def btn_1():
    #markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup = types.InlineKeyboardMarkup()
    matem = types.InlineKeyboardButton("Математика",url="https://resh.skysmart.ru/1-klass/matematika/moro-1222?ysclid=mty9kc0imf317229549")
    rus = types.InlineKeyboardButton("Русский язык", url="https://resh.skysmart.ru/1-klass/russkij-yazyk/krylova-629")
    liter = types.InlineKeyboardButton("Литература", url="https://budu5.com/gdz/view/143")
    okr = types.InlineKeyboardButton("Окружающий мир", url="https://budu5.com/gdz/view/90")
    markup.add(matem, rus)
    markup.add(liter, okr)

    return markup

def btn_2():
    markup = types.InlineKeyboardMarkup()
    matem = types.InlineKeyboardButton("Математика",url="https://budu5.com/gdz/view/110")
    rus = types.InlineKeyboardButton("Русский язык", url="https://budu5.com/gdz/view/19")
    liter = types.InlineKeyboardButton("Литература", url="https://budu5.com/gdz/view/150")
    okr = types.InlineKeyboardButton("Окружающий мир", url="https://budu5.com/gdz/view/97")
    angl = types.InlineKeyboardButton("Английский язык",url="https://budu5.com/gdz/view/214")
    markup.add(matem, rus)
    markup.add(liter, okr)
    markup.add(angl)

    return markup

def btn_3():
    markup = types.InlineKeyboardMarkup()
    matem = types.InlineKeyboardButton("Математика",url="https://reshak.ru/tag/3klass_math.html")
    rus = types.InlineKeyboardButton("Русский язык", url="https://reshak.ru/tag/3klass_rus.html")
    liter = types.InlineKeyboardButton("Литература", url="https://reshak.ru/tag/3klass_chtenie.html")
    okr = types.InlineKeyboardButton("Окружающий мир", url="https://reshak.ru/tag/3klass_mir.html")
    angl = types.InlineKeyboardButton("Английский язык",url="https://reshak.ru/tag/3klass_eng.html")
    markup.add(matem, rus)
    markup.add(liter, okr)
    markup.add(angl,)

    return markup

def btn_4():
    markup = types.InlineKeyboardMarkup()
    matem = types.InlineKeyboardButton("Математика", url="https://reshak.ru/tag/4klass_math.html")
    rus = types.InlineKeyboardButton("Русский язык", url="https://reshak.ru/tag/4klass_rus.html")
    liter = types.InlineKeyboardButton("Литература", url="https://reshak.ru/tag/4klass_chtenie.html")
    okr = types.InlineKeyboardButton("Окружающий мир", url="https://reshak.ru/tag/4klass_mir.html")
    angl = types.InlineKeyboardButton("Английский язык", url="https://reshak.ru/tag/4klass_eng.html")
    markup.add(matem, rus)
    markup.add(liter, okr)
    markup.add(angl)

    return markup

def btn_5():
    markup = types.InlineKeyboardMarkup()
    matem = types.InlineKeyboardButton("Математика", url="https://reshak.ru/tag/5klass_math.html")
    rus = types.InlineKeyboardButton("Русский язык", url="https://reshak.ru/tag/5klass_rus.html")
    liter = types.InlineKeyboardButton("Литература", url="https://reshak.ru/tag/5klass_chtenie.html")
    angl = types.InlineKeyboardButton("Английский язык", url="https://reshak.ru/tag/5klass_eng.html")
    ist = types.InlineKeyboardButton("История", url="https://reshak.ru/tag/5klass_istoria.html")
    geogr = types.InlineKeyboardButton("География", url="https://reshak.ru/tag/5klass_geograph.html")
    biolog = types.InlineKeyboardButton("Биология", url="https://reshak.ru/tag/5klass_bio.html")
    markup.add(matem, rus)
    markup.add(liter, ist)
    markup.add(geogr, biolog)
    markup.add(angl)

    return markup

def btn_6():
    markup = types.InlineKeyboardMarkup()
    matem = types.InlineKeyboardButton("Математика", url="https://reshak.ru/tag/6klass_math.html")
    rus = types.InlineKeyboardButton("Русский язык", url="https://reshak.ru/tag/6klass_rus.html")
    liter = types.InlineKeyboardButton("Литература", url="https://reshak.ru/tag/6klass_chtenie.html")
    angl = types.InlineKeyboardButton("Английский язык", url="https://reshak.ru/tag/6klass_eng.html")
    ist = types.InlineKeyboardButton("История", url="https://reshak.ru/tag/6klass_istoria.html")
    geogr = types.InlineKeyboardButton("География", url="https://reshak.ru/tag/6klass_geograph.html")
    biolog = types.InlineKeyboardButton("Биология", url="https://reshak.ru/tag/6klass_bio.html")
    markup.add(matem, rus)
    markup.add(liter, ist)
    markup.add(geogr, biolog)
    markup.add(angl)

    return markup

def btn_7():
    markup = types.InlineKeyboardMarkup()
    rus = types.InlineKeyboardButton("Русский язык", url="https://reshak.ru/tag/7klass_rus.html")
    liter = types.InlineKeyboardButton("Литература", url="https://reshak.ru/tag/7klass_chtenie.html")
    angl = types.InlineKeyboardButton("Английский язык", url="https://reshak.ru/tag/7klass_eng.html")
    ist = types.InlineKeyboardButton("История", url="https://reshak.ru/tag/7klass_istoria.html")
    geogr = types.InlineKeyboardButton("География", url="https://reshak.ru/tag/7klass_geograph.html")
    biolog = types.InlineKeyboardButton("Биология", url="https://reshak.ru/tag/7klass_bio.html")
    alg = types.InlineKeyboardButton("Алгебра", url="https://reshak.ru/tag/7klass_alg.html")
    fizika = types.InlineKeyboardButton("Физика",url="https://reshak.ru/tag/7klass_fiz.html")
    geo = types.InlineKeyboardButton("Геометрия",url="https://reshak.ru/tag/7klass_geo.html")
    markup.add(alg, rus)
    markup.add(liter, ist)
    markup.add(geogr, biolog)
    markup.add(angl, fizika)
    markup.add(geo)
    return markup

def btn_8():
    markup = types.InlineKeyboardMarkup()
    rus = types.InlineKeyboardButton("Русский язык", url="https://reshak.ru/tag/8klass_rus.html")
    liter = types.InlineKeyboardButton("Литература", url="https://reshak.ru/tag/8klass_chtenie.html")
    angl = types.InlineKeyboardButton("Английский язык", url="https://reshak.ru/tag/8klass_eng.html")
    ist = types.InlineKeyboardButton("История", url="https://reshak.ru/tag/8klass_istoria.html")
    geogr = types.InlineKeyboardButton("География", url="https://reshak.ru/tag/8klass_geograph.html")
    biolog = types.InlineKeyboardButton("Биология", url="https://reshak.ru/tag/8klass_bio.html")
    alg = types.InlineKeyboardButton("Алгебра", url="https://reshak.ru/tag/8klass_alg.html")
    fizika = types.InlineKeyboardButton("Физика",url="https://reshak.ru/tag/8klass_fiz.html")
    geo = types.InlineKeyboardButton("Геометрия",url="https://reshak.ru/tag/8klass_geo.html")
    ximia = types.InlineKeyboardButton("Химия", url="https://reshak.ru/tag/8klass_him.html")
    markup.add(alg, rus)
    markup.add(liter, ist)
    markup.add(geogr, biolog)
    markup.add(angl, fizika)
    markup.add(geo, ximia)
    return markup

def btn_9():
    markup = types.InlineKeyboardMarkup()
    rus = types.InlineKeyboardButton("Русский язык", url="https://reshak.ru/tag/9klass_rus.html")
    liter = types.InlineKeyboardButton("Литература", url="https://reshak.ru/tag/9klass_chtenie.html")
    angl = types.InlineKeyboardButton("Английский язык", url="https://reshak.ru/tag/9klass_eng.html")
    ist = types.InlineKeyboardButton("История", url="https://reshak.ru/tag/9klass_istoria.html")
    geogr = types.InlineKeyboardButton("География", url="https://reshak.ru/tag/9klass_geograph.html")
    biolog = types.InlineKeyboardButton("Биология", url="https://reshak.ru/tag/9klass_bio.html")
    alg = types.InlineKeyboardButton("Алгебра", url="https://reshak.ru/tag/9klass_alg.html")
    fizika = types.InlineKeyboardButton("Физика",url="https://reshak.ru/tag/9klass_fiz.html")
    geo = types.InlineKeyboardButton("Геометрия",url="https://reshak.ru/tag/9klass_geo.html")
    ximia = types.InlineKeyboardButton("Химия",url="https://reshak.ru/tag/9klass_him.html")
    markup.add(alg, rus)
    markup.add(liter, ist)
    markup.add(geogr, biolog)
    markup.add(angl, fizika)
    markup.add(geo, ximia)
    return markup

def btn_10():
    markup = types.InlineKeyboardMarkup()
    rus = types.InlineKeyboardButton("Русский язык", url="https://reshak.ru/tag/10klass_rus.html")
    liter = types.InlineKeyboardButton("Литература", url="https://reshak.ru/tag/10klass_chtenie.html")
    angl = types.InlineKeyboardButton("Английский язык", url="https://reshak.ru/tag/10klass_eng.html")
    ist = types.InlineKeyboardButton("История", url="https://reshak.ru/tag/10klass_istoria.html")
    geogr = types.InlineKeyboardButton("География", url="https://reshak.ru/tag/10klass_geograph.html")
    biolog = types.InlineKeyboardButton("Биология", url="https://reshak.ru/tag/10klass_bio.html")
    alg = types.InlineKeyboardButton("Алгебра", url="https://reshak.ru/tag/10klass_alg.html")
    fizika = types.InlineKeyboardButton("Физика",url="https://reshak.ru/tag/10klass_fiz.html")
    geo = types.InlineKeyboardButton("Геометрия",url="https://reshak.ru/tag/10klass_geo.html")
    ximia = types.InlineKeyboardButton("Химия",url="https://reshak.ru/tag/10klass_him.html")
    markup.add(liter, ist)
    markup.add(geogr, biolog)
    markup.add(angl, fizika)
    markup.add(geo, ximia)
    markup.add(rus,alg)
    return markup

def btn_11():
    markup = types.InlineKeyboardMarkup()
    rus = types.InlineKeyboardButton("Русский язык", url="https://reshak.ru/tag/11klass_rus.html")
    liter = types.InlineKeyboardButton("Литература", url="https://reshak.ru/tag/11klass_chtenie.html")
    angl = types.InlineKeyboardButton("Английский язык", url="https://reshak.ru/tag/11klass_eng.html")
    ist = types.InlineKeyboardButton("История", url="https://reshak.ru/tag/11klass_istoria.html")
    geogr = types.InlineKeyboardButton("География", url="https://reshak.ru/tag/11klass_geograph.html")
    biolog = types.InlineKeyboardButton("Биология", url="https://reshak.ru/tag/11klass_bio.html")
    alg = types.InlineKeyboardButton("Алгебра", url="https://reshak.ru/tag/11klass_alg.html")
    fizika = types.InlineKeyboardButton("Физика",url="https://reshak.ru/tag/11klass_fiz.html")
    geo = types.InlineKeyboardButton("Геометрия",url="https://reshak.ru/tag/11klass_geo.html")
    ximia = types.InlineKeyboardButton("Химия",url="https://reshak.ru/tag/11klass_him.html")
    markup.add(alg, rus)
    markup.add(liter, ist)
    markup.add(geogr, biolog)
    markup.add(angl, fizika)
    markup.add(geo, ximia)
    return markup

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
