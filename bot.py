import telebot
from telebot import types

# Токен бота
TOKEN = '7076217052:AAHQyKdKEwdd5qwMtNvu3dWAq_78eHbzn9Y'
bot = telebot.TeleBot(TOKEN)

# Главное меню
def main_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("🏡 Размещение", "🍽 Меню")
    markup.row("💰 Прейскурант цен", "📸 Фото")
    markup.row("📞 Контакты")
    return markup

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "🌟 Добро пожаловать в зону отдыха Бриз!\n🌊 Выберите нужный раздел ниже:", reply_markup=main_menu())

@bot.message_handler(func=lambda message: True)
def menu_handler(message):
    if message.text == "🏡 Размещение":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Коттеджи", callback_data='cottages'))
        markup.add(types.InlineKeyboardButton("Стандартные номера", callback_data='rooms'))
        markup.add(types.InlineKeyboardButton("Топчаны", callback_data='topchan'))
        markup.add(types.InlineKeyboardButton("Столики", callback_data='tables'))
        markup.add(types.InlineKeyboardButton("Сауна", callback_data='sauna'))
        bot.send_message(message.chat.id, "🏡 Выберите тип размещения:", reply_markup=markup)

    elif message.text == "🍽 Меню":
        photo = open("menu.jpg", "rb")
        bot.send_photo(message.chat.id, photo, caption="🍽 Меню кафе.\n📌 Все цены указаны на изображении.\n☝️ Обслуживание: 15%")
        photo.close()

    elif message.text == "💰 Прейскурант цен":
        photo = open("prices.jpg", "rb")
        bot.send_photo(message.chat.id, photo, caption="💰 Летние цены 2025 (май – август)")
        photo.close()

    elif message.text == "📸 Фото":
        bot.send_message(message.chat.id, "📸 Фото по разделам доступны в нашем Instagram/канале")

    elif message.text == "📞 Контакты":
        bot.send_message(
            message.chat.id,
            "📞 Связаться с нами:\n📱 +998 99 444 99 59\n🔗 Telegram: @breeztashmore",
            reply_markup=types.InlineKeyboardMarkup().add(
                types.InlineKeyboardButton("📞 Позвонить", url="tel:+998994449959"),
                types.InlineKeyboardButton("💬 Написать в Telegram", url="https://t.me/breeztashmore")
            )
        )

# Обработчик инлайн-кнопок (заглушка)
@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    text = "🌊 Здесь будет информация о "
    if call.data == 'cottages':
        text += "коттеджах"
    elif call.data == 'rooms':
        text += "номерах"
    elif call.data == 'topchan':
        text += "топчанах"
    elif call.data == 'tables':
        text += "столиках"
    elif call.data == 'sauna':
        text += "сауне"
    bot.answer_callback_query(call.id)
    bot.send_message(call.message.chat.id, text)

# Запуск бота
print("Bot is running...")
bot.polling(none_stop=True)
