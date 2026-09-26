from telebot import types

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

def get_gdz_submenu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for i in range(1,10,2):
        btn = types.KeyboardButton(f"{str(i)} Класс")
        btn_2 = types.KeyboardButton(f"{str(i+1)} Класс")
        markup.add(btn, btn_2)

    btn_11 = types.KeyboardButton(f"11 Класс")   
    back = types.KeyboardButton("Вернуться назад")
    markup.add(btn_11,back)

    return markup

function_list = [btn_1, btn_2,btn_3,btn_4,btn_5,btn_6,btn_7,btn_8,btn_9,btn_10,btn_11]