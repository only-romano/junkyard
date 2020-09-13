# Стандартная библиотека
import pickle
from copy import deepcopy
from datetime import datetime
import requests
# Внешние пакеты
import telebot
from telebot import types
# Локальные модули бота
import nonsense_buttons as NB
# Config
try:
    from config import pickle_file, bot_name, bot_token, bad_file_replacer
except ImportError:
    pickle_file = "db.pickle"
    bot_name = "💬  TopKEK bot  💬\n\n"  # Отметка сообщений от бота
    bot_token = ""
    bad_file_replacer = 'static/empty.png' 

# Bot
bot = telebot.TeleBot(token=bot_token)

# Users
try:
    with open(pickle_file, 'rb') as file:
        users = pickle.load(file)
except Exception:
    # Если БД не существует
    users = {}


# Разметка
def get_markup(buttons, line_index=None, button_index=None, conflict=None):
    """
    Создаёт объект разметки, изменяет статус "Выбрано" (✓) кнопок,
    добавляет линии кнопок в объект разметки. Возвращает объект разметки.

    args:
        buttons: список линий разметки, содержащие список кнопок в линии
        ~ [опционально] для изменения статуса "Выбрано" (✓):
        ~ line_index: индекс линии разметки с нажатой кнопкой
        ~ button_index: индекс нажатой кнопки в её линии разметки
        ~ conflict: список конфликтующих кнопок
    returns:
        markup: объект разметки types.InlineKeyboardMarkup
    """
    markup = types.InlineKeyboardMarkup(row_width=3)  # макс.кнопок в ряду
    # если требуется изменить статусы "Выбрано" (✓) у кнопок
    if line_index is not None:
        # изменение статуса (✓) у нажатой кнопки
        bt = buttons[line_index][button_index][0]  # bt as button_text
        bt = bt[2:-2] if bt.startswith("✓") else "✓ " + bt + " ✓"
        buttons[line_index][button_index][0] = bt
        # если есть конфликтующие кнопки (возможен единственный выбор)
        if conflict:
            # перебор конфликтующих кнопок
            for option in conflict:
                # проверка и обнуление статуса (✓) конфликтующей кнопки
                cb = buttons[option[0]][option[1]]  # cb as conflict_button
                if cb[0].startswith("✓"):
                    cb[0] = cb[0][2:-2]
    # перебор списка линий разметки
    for line in buttons:
        # создание списка кнопок types.InlineKeyboardButton
        line = [types.InlineKeyboardButton(text=sb[0], callback_data=sb[1])
                for sb in line]  # sb as single_button
        # добавление линии разметки с правильным форматом кнопок
        markup.add(*line)
    # возвращаем объект разметки types.InlineKeyboardMarkup
    return markup


def edit_settings(message, pressed_button=False, options=None):
    """
    Обрабатывает нажатие кнопки "Настройки" и изменение настроек

    args:
        message: объект сообщения настроек с разметкой
        pressed_button: флаг нажатия кнопки выбора опции в настройках
        ~ [опционально] при изменении настроек:
        ~ options: список параметров для создания разметки
    """
    if pressed_button:  # именения в настройках
        # преобразование объекта разметки (из объекта сообщения) в список
        buttons_object = message.json['reply_markup']['inline_keyboard']
        buttons_list = process_buttons(buttons_object)
        # создание разметки настроек из списка
        markup = get_markup(buttons_list, *options)
    else:  # нажатие кнопки "Настройки" в главном меню
        # создание копии разметки по умолчанию
        buttons_list = deepcopy(NB.settings_buttons)
        # создание разметки с расстановкой статусов "Выбрано" (✓)
        markup = get_markup(set_checkmarks(message.chat.id, buttons_list))
    # текст отправляемого ботом сообщения (перед разметкой)
    text = f"{bot_name}Заполни информацию о себе и подбери себе партнёра"
    # редактирование сообщения
    bot.edit_message_text(chat_id=message.chat.id,
        message_id=message.message_id, text=text, reply_markup=markup)


def process_buttons(buttons_object):
    # Преобразует объект кнопок в список кнопок
    return [list(map(lambda button: [button['text'], button['callback_data']],
        line)) for line in buttons_object]


def set_checkmarks(chat_id, buttons):
    """
    Визуализация статуса "Выбрано" кнопок (✓)

    args:
        chat_id: идентификатор чата
        buttons: cписок разметки кнопок
    returns:
        buttons: список разметки кнопок со статусами "Выбрано" (✓)
    """
    # mark helper
    def create_mark(line_index, button_index):
        # Добавляет статус "Выбрано" (✓) кнопке с указанными индексами
        bt = buttons[line_index][button_index][0]  # bt as button text
        if not bt.startswith("✓"):
            buttons[line_index][button_index][0] = "✓ "+ bt + " ✓"
    # Проверки выбранных настроек пользователя и запуск create_mark для них
    if chat_id in users:
        if users[chat_id]["sex"]:
            create_mark(1, int(users[chat_id]["sex"])-1)
        if users[chat_id]["age"]:
            create_mark(3, int(users[chat_id]["age"])-1)
        if users[chat_id]["p_sex"]:
            for i in users[chat_id]["p_sex"]:
                create_mark(5, int(i)-1)
        if users[chat_id]["p_age"]:
            for i in users[chat_id]["p_age"]:
                create_mark(7, int(i)-1)
    # возвращаем список разметки кнопок со статусами "Выбрано" (✓)
    return buttons


# Запись в БД
def update_db(chat_id, key, value):
    """
    Проверка наличия пользователя в БД, запись пользователя в БД,
    проверка отличия передаваемого значения от имеющегося,
    запись в БД нового значения

    args:
        chat_id: идентификатор чата
        key: ключ записи
        value: значение, которое записывается
    returns:
        флаг (bool) о статусе перезаписи
    """
    if chat_id not in users:
        # создание новой записи пользователя в БД
        users[chat_id] = deepcopy(NB.user_default)
    old_value = users[chat_id][key]  # Старое значение ключа
    if old_value != value:
        # Перезапись ключа
        if old_value and key in ["p_sex", "p_age"]:
            value = get_complex_value(old_value, value)
        users[chat_id][key] = value
        return write_to_db()
    return False


def write_to_db():
    """
    Запись в базу данных объекта users

    returns:
        bool - статус успеха перезаписи
    """
    try:
        with open(pickle_file, "wb") as file:
            pickle.dump(users, file)
        return True
    except Exception:
        return False


def get_complex_value(old_value, new_value):
    # Обновление составного значения для полей p_sex или p_age
    if new_value in old_value:
        return "".join(filter(lambda a: a != new_value, list(old_value)))
    else:
        return "".join(sorted(old_value + new_value))


def get_params(key):
    # Параметры для изменения настроек профиля
    keys = {
        "user_male": ("sex", "1", 1, 0, [[1,1]]),
        "user_female": ("sex", "2", 1, 1, [[1,0]]),
        "user_age_1822": ("age", "1", 3, 0, [[3,1], [3,2]]),
        "user_age_2329": ("age", "2", 3, 1, [[3,0], [3,2]]),
        "user_age_30": ("age", "3", 3, 2, [[3,0], [3,1]]),
        "pref_male": ("p_sex", "1", 5, 0, None),
        "pref_female": ("p_sex", "2", 5, 1, None),
        "pref_1822": ("p_age", "1", 7, 0, None),
        "pref_2329": ("p_age", "2", 7, 1, None),
        "pref_30": ("p_age", "3", 7, 2, None),
    }
    return keys.get(key, None)


def check_profile(chat_id):
    # Проверка заполненности профиля пользователя
    return (chat_id in users and
        users[chat_id]["sex"] and
        users[chat_id]["age"] and
        users[chat_id]["p_sex"] and
        users[chat_id]["p_age"] and
        users[chat_id]["partner"] is None)


def get_post_buttons(sender_id, sex, age):
    # Кнопка ответа на объявления пользователей
    sex_values = ["👨", "👩"]
    age_values = ["18-22", "23-29", "30+"]
    sex, age = int(sex)-1, int(age)-1
    text = f"Ответить    {sex_values[sex]} {age_values[age]}"
    callback_data = f"private_{sender_id}"
    # Жалоба на пользователя
    button_bad = ["Жалоба   🚫", "complain_msg"]
    return [[text, callback_data], button_bad]


def filtered_users(sender, sender_id):
    # Возвращает фильтрованный список пользователей, которым будет показано
    # объявление
    return [user for user in users if
                user != sender_id and
                check_profile(user) and
                users[user]["sex"] in sender["p_sex"] and
                users[user]["age"] in sender["p_age"] and
                sender["sex"] in users[user]["p_sex"] and
                sender["age"] in users[user]["p_age"]]

def get_file(file):
    file_path = bot.get_file(file).file_path
    link = f'https://api.telegram.org/file/bot{bot_token}/{file_path}'
    try:
        file = requests.get(link).content
    except Exception:
        file = open(bad_file_replacer, "rb")
    return file

def get_reply_message(content_type, message):
    if content_type == "text":
        reply = message.text.replace("eval","еvаl").replace("exec","ехес")
    elif content_type == "sticker":
        reply = get_file(message.sticker.file_id)
    return reply

def broadcast_post(content_type, sender, chat_id, reply, markup):
    broadcast_to = filtered_users(sender, chat_id)
    if content_type == "text":
        for user in broadcast_to:
            bot.send_message(user, reply, reply_markup=markup)
    elif content_type == "sticker":
        for user in broadcast_to:
            bot.send_sticker(user, reply, reply_markup=markup)

# HANDLERS
@bot.message_handler(commands=["start"])
def send_welcome(message):
    # Команда /start
    chat_id = message.chat.id
    text = f"{bot_name}Дороу! Чего делать будем?"
    markup = get_markup(NB.main_buttons)
    sti = open('static/welcome.webp', 'rb')
    bot.send_sticker(chat_id, sti)
    bot.send_message(chat_id, text, reply_markup=markup)


@bot.message_handler(commands=["end"])
def end_private(message):
    # Команда /end
    text = (f"{bot_name}!  Диалог завершён. Опубликуйте новое объявление" +
        " или ждите ответа на прошлое  !")
    sender_id = message.chat.id
    receiver_id = users[sender_id]["partner"]
    if receiver_id:
        for user in [sender_id, receiver_id]:
            users[user]["partner"] = None
            bot.send_message(user, text)
        write_to_db()
    else:
        text = f"{bot_name}!  Вы не в приватном диалоге  !"
        bot.send_message(sender_id, text)

@bot.message_handler(content_types=["text", "sticker"])
def any_msg(message):
    # Текстовые сообщения
    chat_id = message.chat.id
    if check_profile(chat_id):
        # можно будет перенести в nonsense_buttons.py разметку кнопки
        ct = message.content_type  # ct as content_type
        button_post = ["Опубликовать объявление   \u2709", f"post_msg_{ct}"]
        markup = get_markup([[button_post]])
        send_distributed_msg(message, chat_id, markup)
    elif users[chat_id]["partner"]:
        send_distributed_msg(message, users[chat_id]["partner"])
    else:
        text = f"{bot_name}Перед публикацией необходимо заполнить профиль"

def send_distributed_msg(message, chat_id, markup=None):
    content_type = message.content_type
    partner_id = users[chat_id]["partner"] or chat_id
    message_id = message.message_id
    if content_type == "text":
        bot.send_message(chat_id, message.text, reply_markup=markup)
    elif content_type == "sticker":
        if markup:
            sticker = get_file(message.sticker.file_id)
            bot.send_sticker(chat_id, sticker, reply_markup=markup)
        else:
            bot.forward_message(chat_id, partner_id, message_id)

# @bot.message_handler(content_types=["text"])
# def any_msg(message):
#     # Текстовые сообщения
#     chat_id = message.chat.id
#     print(users)
#     if check_profile(chat_id):
#         # можно будет перенести в nonsense_buttons.py разметку кнопки
#         button_post = ["Опубликовать объявление   \u2709", "post_msg"]
#         markup = get_markup([[button_post]])
#         bot.send_message(chat_id, message.text, reply_markup=markup)
#     elif users[chat_id]["partner"]:
#         bot.send_message(users[chat_id]["partner"], message.text)
#     else:
#         text = f"{bot_name}Перед публикацией необходимо заполнить профиль"
#         markup = get_markup(NB.main_buttons)
#         bot.send_message(chat_id, text, reply_markup=markup)


@bot.callback_query_handler(func=lambda call:True)
def callback_inline(call):
    chat_id = call.message.chat.id

    # Главное меню
    if call.data == "mainmenu":
        text = f"{bot_name}Главное меню"
        markup = get_markup(NB.main_buttons)
        bot.edit_message_text(chat_id=chat_id, text=text, reply_markup=markup,
            message_id=call.message.message_id)

    # Не реализовано
    elif call.data == "main_search_button":
        bot.send_message(chat_id, '❗Тут должен быть поиск')
    elif call.data == "main_porn_button":
        bot.send_message(chat_id, '❗Тут будет прон')

    # Настройки
    elif call.data == "main_settings_button":
        edit_settings(call.message)

    # Изменение настроек
    elif call.data.startswith(("user_", "pref_")):
        key, value, line_index, button_index, conflict = get_params(call.data)
        if update_db(chat_id, key, value):
            options = [line_index, button_index, conflict]
            edit_settings(call.message, True, options)

    # Публикация объявления
    elif call.data.startswith("post_msg_"):
        # Таймаут между публикациями
        msg_timeout = 60
        _s = users[chat_id]  # s as sender
        now_msg_time = int(datetime.timestamp(datetime.utcnow()))
        last_msg_time = _s["msg_time"]
        if not last_msg_time or now_msg_time - last_msg_time > msg_timeout:
            post_buttons = get_post_buttons(chat_id, _s["sex"], _s["age"])
            markup = get_markup([post_buttons])
            content_type = call.data[9:]
            reply = get_reply_message(content_type, call.message)
            broadcast_post(content_type, _s, chat_id, reply, markup)
            # сообщение для отправителя
            text = f"{bot_name}! Ваше объявление опубликовано, ждите ответа !"
            bot.send_message(chat_id, text)
            update_db(chat_id, "msg_time", now_msg_time)
        else:
            # прошлая публикация была менее минуты назад
            text = (f"{bot_name}Пожалуйста подождите 1 минуту перед тем," +
                " как опубликовывать новое объявление")
            bot.answer_callback_query(callback_query_id=call.id,
                show_alert=True, text=text)

    # Приват
    elif call.data.startswith("private_"):
        receiver_id = int(call.data[8:])
        text = f"{bot_name}!  Собеседник подключен, диалог начался  !"
        # обновление БД
        users[chat_id]["partner"] = receiver_id
        users[receiver_id]["partner"] = chat_id
        # сообщения от бота для пользователей
        bot.send_message(chat_id, text)
        bot.send_message(receiver_id, text)
        write_to_db()


if __name__ == "__main__":
    # запуск бота
    bot.polling(none_stop=True)
