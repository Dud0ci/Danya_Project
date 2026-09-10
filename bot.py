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

    else:
        bot.send_message(chat_id, "Нажми на кнопку в меню!")

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
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    matem = types.KeyboardButton("Математика")
    rus = types.KeyboardButton("Русский язык")
    liter = types.KeyboardButton("Литература")
    okr = types.KeyboardButton("Окружающий мир")
    back = types.KeyboardButton("Вернуться назад")
    markup.add(matem, rus)
    markup.add(liter, okr)
    markup.add(back)

    return markup

def btn_2():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    angl = types.KeyboardButton("Английский язык")
    matem = types.KeyboardButton("Математика")
    rus = types.KeyboardButton("Русский язык")
    liter = types.KeyboardButton("Литература")
    okr = types.KeyboardButton("Окружающий мир")
    back = types.KeyboardButton("Вернуться назад")

    markup.add(matem, rus)
    markup.add(liter, okr)
    markup.add(angl,back)

    return markup

def btn_3():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    angl = types.KeyboardButton("Английский язык")
    matem = types.KeyboardButton("Математика")
    rus = types.KeyboardButton("Русский язык")
    liter = types.KeyboardButton("Литература")
    okr = types.KeyboardButton("Окружающий мир")
    back = types.KeyboardButton("Вернуться назад")
    markup.add(matem, rus)
    markup.add(liter, okr)
    markup.add(angl,back)

    return markup

def btn_4():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    angl = types.KeyboardButton("Английский язык")
    matem = types.KeyboardButton("Математика")
    rus = types.KeyboardButton("Русский язык")
    liter = types.KeyboardButton("Литература")
    okr = types.KeyboardButton("Окружающий мир")
    back = types.KeyboardButton("Вернуться назад")
    markup.add(matem, rus)
    markup.add(liter, okr)
    markup.add(angl,back)

    return markup

def btn_5():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    angl = types.KeyboardButton("Английский язык")
    matem = types.KeyboardButton("Математика")
    rus = types.KeyboardButton("Русский язык")
    liter = types.KeyboardButton("Литература")
    ist = types.KeyboardButton("История")
    geogr = types.KeyboardButton("География")
    biolog = types.KeyboardButton("Биология")
    back = types.KeyboardButton("Вернуться назад")
    markup.add(matem, rus)
    markup.add(liter, ist)
    markup.add(geogr, biolog)
    markup.add(angl, back)

    return markup

def btn_6():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    angl = types.KeyboardButton("Английский язык")
    matem = types.KeyboardButton("Математика")
    rus = types.KeyboardButton("Русский язык")
    liter = types.KeyboardButton("Литература")
    ist = types.KeyboardButton("История")
    geogr = types.KeyboardButton("География")
    biolog = types.KeyboardButton("Биология")
    back = types.KeyboardButton("Вернуться назад")
    markup.add(matem, rus)
    markup.add(liter, ist)
    markup.add(geogr, biolog)
    markup.add(angl, back)

    return markup

def btn_7():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    angl = types.KeyboardButton("Английский язык")
    alg = types.KeyboardButton("Алгебра")
    geo = types.KeyboardButton("Геометрия")
    rus = types.KeyboardButton("Русский язык")
    liter = types.KeyboardButton("Литература")
    ist = types.KeyboardButton("История")
    geogr = types.KeyboardButton("География")
    biolog = types.KeyboardButton("Биология")
    fizika = types.KeyboardButton("Физика")
    back = types.KeyboardButton("Вернуться назад")
    markup.add(alg, rus)
    markup.add(liter, ist)
    markup.add(geogr, biolog)
    markup.add(angl, fizika)
    markup.add(geo, back)
    return markup

def btn_8():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    angl = types.KeyboardButton("Английский язык")
    alg = types.KeyboardButton("Алгебра")
    geo = types.KeyboardButton("Геометрия")
    rus = types.KeyboardButton("Русский язык")
    liter = types.KeyboardButton("Литература")
    ist = types.KeyboardButton("История")
    geogr = types.KeyboardButton("География")
    biolog = types.KeyboardButton("Биология")
    fizika = types.KeyboardButton("Физика")
    ximia = types.KeyboardButton("Химия")
    back = types.KeyboardButton("Вернуться назад")
    markup.add(alg, rus)
    markup.add(liter, ist)
    markup.add(geogr, biolog)
    markup.add(angl, fizika)
    markup.add(geo, ximia)
    markup.add(back)
    return markup

def btn_9():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    angl = types.KeyboardButton("Английский язык")
    alg = types.KeyboardButton("Алгебра")
    geo = types.KeyboardButton("Геометрия")
    rus = types.KeyboardButton("Русский язык")
    liter = types.KeyboardButton("Литература")
    ist = types.KeyboardButton("История")
    geogr = types.KeyboardButton("География")
    biolog = types.KeyboardButton("Биология")
    fizika = types.KeyboardButton("Физика")
    ximia = types.KeyboardButton("Химия")
    back = types.KeyboardButton("Вернуться назад")
    markup.add(alg, rus)
    markup.add(liter, ist)
    markup.add(geogr, biolog)
    markup.add(angl, fizika)
    markup.add(geo, ximia)
    markup.add(back)
    return markup

def btn_10():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    angl = types.KeyboardButton("Английский язык")
    alg = types.KeyboardButton("Алгебра")
    geo = types.KeyboardButton("Геометрия")
    rus = types.KeyboardButton("Русский язык")
    liter = types.KeyboardButton("Литература")
    ist = types.KeyboardButton("История")
    geogr = types.KeyboardButton("География")
    biolog = types.KeyboardButton("Биология")
    fizika = types.KeyboardButton("Физика")
    ximia = types.KeyboardButton("Химия")
    back = types.KeyboardButton("Вернуться назад")
    markup.add(alg, rus)
    markup.add(liter, ist)
    markup.add(geogr, biolog)
    markup.add(angl, fizika)
    markup.add(geo, ximia)
    markup.add(back)
    return markup

def btn_11():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    angl = types.KeyboardButton("Английский язык")
    alg = types.KeyboardButton("Алгебра")
    geo = types.KeyboardButton("Геометрия")
    rus = types.KeyboardButton("Русский язык")
    liter = types.KeyboardButton("Литература")
    ist = types.KeyboardButton("История")
    geogr = types.KeyboardButton("География")
    biolog = types.KeyboardButton("Биология")
    fizika = types.KeyboardButton("Физика")
    ximia = types.KeyboardButton("Химия")
    back = types.KeyboardButton("Вернуться назад")
    markup.add(alg, rus)
    markup.add(liter, ist)
    markup.add(geogr, biolog)
    markup.add(angl, fizika)
    markup.add(geo, ximia)
    markup.add(back)
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
