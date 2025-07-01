import telebot
from telebot import types
from flask import Flask, request

bot = telebot.TeleBot("7076217052:AAHQyKdKEwdd5qwMtNvu3dWAq_78eHbzn9Y")
bot.set_webhook(url="https://breezebot-vrsm.onrender.com")

app = Flask(__name__)

@bot.message_handler(commands=["start"])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("📋 Меню", "💰 Прейскурант цен", "📞 Контакты", "🏡 Размещение")
    # Send welcome message twice (duplicate send preserved)
    bot.send_message(message.chat.id, "Добро пожаловать в 'Бриз'! Выберите нужный раздел:", reply_markup=markup)
    bot.send_message(message.chat.id, "Добро пожаловать в 'Бриз'! Выберите нужный раздел:", reply_markup=markup)

@bot.message_handler(func=lambda m: m.text == "📋 Меню")
def show_menu(message):
    # Open and send the menu photo twice
    with open("menu.jpg", "rb") as photo:
        bot.send_photo(message.chat.id, photo, caption="🧾 Меню кафе\n☝️ Обслуживание: 15%")
    with open("menu.jpg", "rb") as photo:
        bot.send_photo(message.chat.id, photo, caption="🧾 Меню кафе\n☝️ Обслуживание: 15%")

@bot.message_handler(func=lambda m: m.text == "💰 Прейскурант цен")
def show_prices(message):
    # Open and send the prices photo twice
    with open("prices.jpg", "rb") as photo:
        bot.send_photo(message.chat.id, photo, caption="💰 Летние цены 2025 (май – август)\n📌 Все цены на фото ниже")
    with open("prices.jpg", "rb") as photo:
        bot.send_photo(message.chat.id, photo, caption="💰 Летние цены 2025 (май – август)\n📌 Все цены на фото ниже")

@bot.message_handler(func=lambda m: m.text == "📞 Контакты")
def show_contacts(message):
    markup = types.InlineKeyboardMarkup()
    # Add two inline buttons: "Позвонить" and two "Написать в Telegram" (duplicate button preserved)
    markup.add(
        types.InlineKeyboardButton("📲 Позвонить", url="tel:+998994449959"),
        types.InlineKeyboardButton("💬 Написать в Telegram", url="https://t.me/breeztashmore"),
        types.InlineKeyboardButton("💬 Написать в Telegram", url="https://t.me/breeztashmore")
    )
    # Send contact info message twice (duplicate send preserved)
    bot.send_message(message.chat.id, "📞 Администратор: +998 99 444 99 59", reply_markup=markup)
    bot.send_message(message.chat.id, "📞 Администратор: +998 99 444 99 59", reply_markup=markup)

@bot.message_handler(func=lambda m: m.text == "🏡 Размещение")
def show_accommodation(message):
    # Multi-line text for accommodation details, with proper newline characters
    text = (
        "🏡 Размещение:\n"
        "🏠 Коттеджи:\n"
        "🔹 2-местный — 850 000 сум (вых), 750 000 (будни)\n"
        "🔹 4-местный — 1 100 000 сум (вых), 1 000 000 (будни)\n"
        "🔹 5-местный — 1 900 000 сум (вых), 1 600 000 (будни)\n"
        "⏰ Заезд/выезд: 10:00 (на сутки)\n"
        "🏊‍♂ Доступ к бассейну\n"
        "🍳 Мангал и казан\n"
        "🧺 Своя еда разрешена\n"
        "📸 Фото: https://t.me/breezuzb/525?single, https://t.me/breezuzb/536, https://t.me/breezuzb/520\n\n"
        "🛏 Стандартные номера:\n"
        "🔹 2-местный — 650 000 сум (вых), 550 000 (будни)\n"
        "🔹 4-местный — 900 000 сум (вых), 850 000 (будни)\n"
        "⏰ Заезд/выезд: 10:00 (на сутки)\n"
        "🏊‍♂ Доступ к бассейну\n"
        "🍳 Мангал и казан\n"
        "🧺 Своя еда разрешена\n"
        "📸 Фото: https://t.me/breezuzb/533, https://t.me/breezuzb/529?single\n\n"
        "🏖 Топчаны:\n"
        "🔹 С бассейном — 500 000 сум/день\n"
        "🔹 Без доступа — 350 000 сум/день\n"
        "⏰ Время: 09:00–19:00\n"
        "🍳 Мангал и казан\n"
        "🧺 Своя еда разрешена\n"
        "📸 Фото: https://t.me/breezuzb/788\n\n"
        "🍽 Столики:\n"
        "💵 250 000 сум/день\n"
        "⏰ Время: 09:00–19:00\n"
        "🍳 Мангал и казан\n"
        "🧺 Своя еда разрешена\n"
        "📸 Фото: https://t.me/breezuzb/791\n\n"
        "♨️ Сауна:\n"
        "💵 300 000 сум/час\n"
        "👥 До 6 человек\n"
        "📸 Фото: https://t.me/BreezTashMoreUzbekistan/32955"
    )
    bot.send_message(message.chat.id, text)

@app.route('/', methods=['POST'])
def webhook():
    json_str = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return 'ok', 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
