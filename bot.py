import telebot
from telebot import types
from flask import Flask, request

bot = telebot.TeleBot("7076217052:AAHQyKdKEwdd5qwMtNvu3dWAq_78eHbzn9Y")
bot.set_webhook(url="https://breezebot-vrsm.onrender.com")

app = Flask(__name__)

# Главное меню
@bot.message_handler(commands=["start"])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("📋 Меню", "💰 Прейскурант цен", "📞 Контакты", "🏠 Размещение")
    bot.send_message(message.chat.id, "Добро пожаловать в 'Бриз'! Выберите нужный раздел:", reply_markup=markup)

# Меню кафе
@bot.message_handler(func=lambda m: m.text == "📋 Меню")
def show_menu(message):
    with open("menu.jpg", "rb") as photo:
        bot.send_photo(message.chat.id, photo, caption="🧾 Меню кафе\nОбслуживание: 15%")

# Прейскурант
@bot.message_handler(func=lambda m: m.text == "💰 Прейскурант цен")
def show_prices(message):
    with open("prices.jpg", "rb") as photo:
        bot.send_photo(message.chat.id, photo, caption="📌 Летние цены 2025 (май – август)")

# Контакты (текст с активными ссылками)
@bot.message_handler(func=lambda m: m.text == "📞 Контакты")
def show_contacts(message):
    text = (
        "📞 *Контакты*\n"
        "📱 *Администратор:*\n"
        "`+998 99 444 99 59`\n\n"
        "📲 [Позвонить](tel:+998994449959)\n"
        "💬 [Написать в Telegram](https://t.me/breeztashmore)"
    )
    bot.send_message(message.chat.id, text, parse_mode="Markdown")

# Размещение — выбор
@bot.message_handler(func=lambda m: m.text == "🏠 Размещение")
def show_accommodation(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("🏡 Коттеджи", "🛏 Стандартные номера")
    markup.add("🌅 Топчаны")
    markup.add("🔙 Назад в меню")
    bot.send_message(message.chat.id, "Выберите тип размещения:", reply_markup=markup)

# Назад в главное меню
@bot.message_handler(func=lambda m: m.text == "🔙 Назад в меню")
def back_to_main_menu(message):
    send_welcome(message)

# Назад к размещению
@bot.message_handler(func=lambda m: m.text == "🔙 Назад к размещению")
def back_to_accommodation(message):
    show_accommodation(message)

# --- Коттеджи ---
@bot.message_handler(func=lambda m: m.text == "🏡 Коттеджи")
def show_cottages(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("2-местный коттедж", "4-местный коттедж", "5-местный коттедж")
    markup.add("🔙 Назад к размещению")
    bot.send_message(message.chat.id, "Выберите тип коттеджа:", reply_markup=markup)

@bot.message_handler(func=lambda m: m.text == "2-местный коттедж")
def cottage_2(message):
    bot.send_message(message.chat.id, "🏡 2-местный коттедж:\n— Уютный номер\n— Доступ к бассейну\n— Цена: 500 000 сум/сутки")

@bot.message_handler(func=lambda m: m.text == "4-местный коттедж")
def cottage_4(message):
    bot.send_message(message.chat.id, "🏡 4-местный коттедж:\n— Просторный домик\n— Доступ к бассейну\n— Цена: 700 000 сум/сутки")

@bot.message_handler(func=lambda m: m.text == "5-местный коттедж")
def cottage_5(message):
    bot.send_message(message.chat.id, "🏡 5-местный коттедж:\n— Для большой компании\n— Доступ к бассейну\n— Цена: 800 000 сум/сутки")

# --- Стандартные номера ---
@bot.message_handler(func=lambda m: m.text == "🛏 Стандартные номера")
def show_standard_rooms(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("2-местный номер", "4-местный номер")
    markup.add("🔙 Назад к размещению")
    bot.send_message(message.chat.id, "Выберите тип номера:", reply_markup=markup)

@bot.message_handler(func=lambda m: m.text == "2-местный номер")
def standard_2(message):
    bot.send_message(message.chat.id, "🛏 2-местный номер:\n— Удобная мебель\n— Кондиционер\n— Доступ к бассейну\n— Цена: 300 000 сум/сутки")

@bot.message_handler(func=lambda m: m.text == "4-местный номер")
def standard_4(message):
    bot.send_message(message.chat.id, "🛏 4-местный номер:\n— Идеально для семьи\n— Кондиционер, холодильник\n— Доступ к бассейну\n— Цена: 500 000 сум/сутки")

# --- Топчаны ---
@bot.message_handler(func=lambda m: m.text == "🌅 Топчаны")
def show_topchans(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("🏖 Топчан с бассейном", "🪵 Простой топчан")
    markup.add("🔙 Назад к размещению")
    bot.send_message(message.chat.id, "Выберите тип топчана:", reply_markup=markup)

@bot.message_handler(func=lambda m: m.text == "🏖 Топчан с бассейном")
def topchan_with_pool(message):
    bot.send_message(message.chat.id, "🏖 Топчан с бассейном:\n— Рядом с водой\n— Доступ к бассейну\n— Столик включен\n— Цена: 150 000 сум/день")

@bot.message_handler(func=lambda m: m.text == "🪵 Простой топчан")
def topchan_simple(message):
    bot.send_message(message.chat.id, "🪵 Простой топчан:\n— Тень и столик\n— Без доступа к бассейну\n— Цена: 100 000 сум/день")

# Вебхук для Render
@app.route('/', methods=['POST'])
def webhook():
    json_str = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return 'ok', 200

# Запуск Flask-сервера
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
