import telebot
from telebot import types

bot = telebot.TeleBot("7076217052:AAHQyKdKEwdd5qwMtNvu3dWAq_78eHbzn9Y")

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["📋 Меню", "📊 Прейскурант цен", "📞 Контакты"]
    markup.add(*[types.KeyboardButton(btn) for btn in buttons])
    bot.send_message(message.chat.id, "Добро пожаловать в Бриз 🌊", reply_markup=markup)

@bot.message_handler(func=lambda m: m.text == "📋 Меню")
def show_menu(message):
    with open("menu.jpg", "rb") as photo:
        bot.send_photo(message.chat.id, photo, caption="🧾 Меню кафе\nОбслуживание: 15%")

@bot.message_handler(func=lambda m: m.text == "📊 Прейскурант цен")
def show_prices(message):
    with open("prices.jpg", "rb") as photo:
        bot.send_photo(message.chat.id, photo, caption="📊 Летние цены 2025 (май – август)")

@bot.message_handler(func=lambda m: m.text == "📞 Контакты")
def show_contacts(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(
        types.InlineKeyboardButton("📞 Позвонить", url="tel:+998994449959"),
        types.InlineKeyboardButton("💬 Написать в Telegram", url="https://t.me/breeztashmore")
    )
    bot.send_message(message.chat.id, "📞 Администратор: +998 99 444 99 59", reply_markup=markup)

bot.polling(none_stop=True)
