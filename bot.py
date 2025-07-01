
import telebot
from telebot import types

TOKEN = "вставь_сюда_свой_токен"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["🏡 Размещение", "🍽 Меню", "💰 Прейскурант цен", "📞 Контакты"]
    markup.add(*buttons)
    bot.send_message(message.chat.id, "Добро пожаловать в зону отдыха «Бриз»! Выберите раздел:", reply_markup=markup)

@bot.message_handler(func=lambda m: m.text == "🏡 Размещение")
def show_accommodation(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(
        types.InlineKeyboardButton("Коттеджи", callback_data="cottages"),
        types.InlineKeyboardButton("Стандартные номера", callback_data="rooms"),
        types.InlineKeyboardButton("Топчаны", callback_data="tapchans"),
        types.InlineKeyboardButton("Столики", callback_data="tables"),
        types.InlineKeyboardButton("Сауна", callback_data="sauna")
    )
    bot.send_message(message.chat.id, "Выберите тип размещения:", reply_markup=markup)

@bot.message_handler(func=lambda m: m.text == "🍽 Меню")
def show_menu(message):
    with open("menu.jpg", "rb") as photo:
        bot.send_photo(message.chat.id, photo, caption="🧾 Меню кафе Обслуживание: 15%")

@bot.message_handler(func=lambda m: m.text == "💰 Прейскурант цен")
def show_prices(message):
    with open("prices.jpg", "rb") as photo:
        bot.send_photo(message.chat.id, photo, caption="💰 Летние цены 2025 (май – август)")

@bot.message_handler(func=lambda m: m.text == "📞 Контакты")
def show_contacts(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(
        types.InlineKeyboardButton("Позвонить", url="tel:+998994449959"),
        types.InlineKeyboardButton("Написать в Telegram", url="https://t.me/breeztashmore")
    )
    bot.send_message(
        message.chat.id,
        "📱 Администратор:
+998 99 444 99 59",
        reply_markup=markup
    )

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    data = call.data
    messages = {
        "cottages": "🏡 Коттеджи:

▪️ 2-местный — 850 000 сум
▪️ 4-местный — 1 100 000 сум
▪️ 5-местный — 1 900 000 сум

⏱ Заезд/выезд в 10:00
🏊 Доступ к бассейну
🍳 Казан и мангал
🧺 Можно приносить продукты

Фото: https://t.me/breezuzb/525?single",
        "rooms": "🛏 Стандартные номера:

▪️ 2-местный — 650 000 сум
▪️ 4-местный — 900 000 сум

⏱ Заезд/выезд в 10:00
🏊 Доступ к бассейну
🍳 Казан и мангал
🧺 Можно приносить продукты

Фото: https://t.me/breezuzb/533",
        "tapchans": "🏖 Топчаны:

▪️ С бассейном — 500 000 сум
▪️ Без бассейна — 350 000 сум

🕒 09:00 – 19:00
🍳 Казан и мангал
🧺 Можно приносить продукты

Фото: https://t.me/breezuzb/788",
        "tables": "🍽 Столики:

▪️ 250 000 сум

🕒 09:00 – 19:00
🍳 Казан и мангал
🧺 Можно приносить продукты

Фото: https://t.me/breezuzb/791",
        "sauna": "♨️ Сауна:

▪️ 300 000 сум / час
👥 До 6 человек

Фото: https://t.me/BreezTashMoreUzbekistan/32955"
    }
    if data in messages:
        bot.send_message(call.message.chat.id, messages[data])

bot.infinity_polling()
