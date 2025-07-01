import telebot
from telebot import types
from flask import Flask, request

bot = telebot.TeleBot("7076217052:AAHQyKdKEwdd5qwMtNvu3dWAq_78eHbzn9Y")  # Вставь свой Telegram Bot Token
bot.set_webhook(url="https://breezebot-vrsm.onrender.com")  # Твоя ссылка Render

app = Flask(__name__)

@bot.message_handler(commands=["start"])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("📋 Меню", "💰 Прейскурант цен", "📞 Контакты", "🏠 Размещение")
    bot.send_message(message.chat.id, "Добро пожаловать в 'Бриз'! Выберите нужный раздел:", reply_markup=markup)

@bot.message_handler(func=lambda m: m.text == "📋 Меню")
def show_menu(message):
    with open("menu.jpg", "rb") as photo:
        bot.send_photo(message.chat.id, photo, caption="🧾 Меню кафе\nОбслуживание: 15%")

@bot.message_handler(func=lambda m: m.text == "💰 Прейскурант цен")
def show_prices(message):
    with open("prices.jpg", "rb") as photo:
        bot.send_photo(message.chat.id, photo, caption="📌 Летние цены 2025 (май – август)")

@bot.message_handler(func=lambda m: m.text == "📞 Контакты")
def show_contacts(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(
        types.InlineKeyboardButton("📞 Позвонить", url="tel:+998994449959"),
        types.InlineKeyboardButton("💬 Telegram", url="https://t.me/breeztashmore")
    )
    bot.send_message(message.chat.id, "📍 Администратор: +998 99 444 99 59", reply_markup=markup)

@bot.message_handler(func=lambda m: m.text == "🏠 Размещение")
def show_accommodation(message):
    text = (
        "🏡 Размещение:\n\n"
        "— Коттеджи:\n"
        "  • 3 четырёхместных\n"
        "  • 2 пятиместных\n"
        "  • 7 двухместных\n"
        "  ➕ Доступ к бассейну\n\n"
        "— Номера:\n"
        "  • 8 двухместных\n"
        "  • 4 четырёхместных\n"
        "  ➕ Доступ к бассейну\n\n"
        "— Топчаны у воды:\n"
        "  • Все с бассейном и столиками\n\n"
        "🧖‍♀️ Сауна: 300 000 сум/час (до 6 человек)"
    )
    bot.send_message(message.chat.id, text)

# Обработка вебхука
@app.route('/', methods=['POST'])
def webhook():
    json_str = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return 'ok', 200

# Запуск сервера
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
