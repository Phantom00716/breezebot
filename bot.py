
import telebot
import os
from flask import Flask, request
from telebot import types

TOKEN = os.getenv("TELEGRAM_TOKEN")
bot = telebot.TeleBot(TOKEN)

app = Flask(__name__)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("🛏 Размещение", "🍽 Меню", "💵 Прейскурант цен")
    markup.row("📞 Контакты")
    bot.send_message(message.chat.id, "Добро пожаловать в Бриз! Выберите нужный раздел👇", reply_markup=markup)

@bot.message_handler(func=lambda m: m.text == "🍽 Меню")
def show_menu(message):
    with open("menu.jpg", "rb") as photo:
        bot.send_photo(message.chat.id, photo, caption="🧾 Меню кафе\nОбслуживание: 15%")

@bot.message_handler(func=lambda m: m.text == "💵 Прейскурант цен")
def show_prices(message):
    with open("prices.jpg", "rb") as photo:
        bot.send_photo(message.chat.id, photo, caption="💵 Летние цены 2025 (май – август)")

@bot.message_handler(func=lambda m: m.text == "📞 Контакты")
def show_contacts(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(
        types.InlineKeyboardButton("Позвонить", url="tel:+998994449959"),
        types.InlineKeyboardButton("Написать в Telegram", url="https://t.me/breeztashmore")
    )
    bot.send_message(
        message.chat.id,
        "📱 Администратор:\n+998 99 444 99 59",
        reply_markup=markup
    )

@app.route('/', methods=['POST'])
def webhook():
    json_str = request.get_data().decode('UTF-8')
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return '!', 200

if __name__ == '__main__':
    bot.remove_webhook()
    bot.set_webhook(url='https://breezebot-vrsm.onrender.com')  # Замени на точную ссылку из Render
    app.run(host='0.0.0.0', port=10000)
