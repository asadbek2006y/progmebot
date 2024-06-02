import telebot
from telebot import types

TOKEN = '6646775232:AAGeUgv7RXmue8YC55lrJGptdkZn3Rc0aH8'
bot = telebot.TeleBot(TOKEN)

# Google Form havolasi
google_form_link = "https://docs.google.com/forms/d/e/1FAIpQLScI5GSxWl7b8wNwEdERlSiTq6Zfok9Q0mO3ipXlZPct5LLzwQ/viewform?usp=sf_link"

@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Xush kelibsiz xabari
    welcome_text = ("Salom! PROGME ta'lim markazi botiga xush kelibsiz. 👋\n"
                    "Sizga qanday yordam bera olishim mumkin?\n\n"
                    "Quyidagi tugmalardan birini tanlang:")

    # Tugmalarni yaratish
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn_register = types.KeyboardButton('Ro\'yxatdan o\'tish')
    btn_about = types.KeyboardButton('Haqida')
    markup.add(btn_register, btn_about)

    # Xush kelibsiz xabarini yuborish
    bot.send_message(message.chat.id, welcome_text, reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text == 'Ro\'yxatdan o\'tish':
        markup = types.InlineKeyboardMarkup()
        btn = types.InlineKeyboardButton(text="Ro'yxatdan o'tish", url=google_form_link)
        markup.add(btn)
        bot.send_message(message.chat.id, "Ro'yxatdan o'tish uchun quyidagi tugmani bosing:", reply_markup=markup)
    elif message.text == 'Haqida':
        about_text = ("PROGME ta'lim markazi - bu innovatsion ta'lim markazi bo'lib, biz turli fanlar bo'yicha yuqori sifatli ta'lim xizmatlarini taqdim etamiz. 📚\n\n"
                      "Markazimiz quyidagi yo'nalishlarda kurslar taqdim etadi:\n"
                      "- Ingliz tili\n"
                      "- Matematika\n"
                      "- Kompyuter Savodxonligi\n"
                      "- Web Dasturlash\n\n"
                      "Asadbek Otabekov - PROGME ta'lim markazining asoschisi va bosh direktori. U o'zining ta'lim sohasidagi tajribasi va innovatsion yondashuvi bilan markazimizni yetaklaydi.\n\n"
                      "Kurslarimiz va boshqa xizmatlarimiz haqida ko'proq ma'lumot olish uchun rasmiy veb-saytimizga tashrif buyuring yoki biz bilan bog'laning.")
        bot.reply_to(message, about_text)
    else:
        bot.reply_to(message, "Iltimos, quyidagi tugmalardan birini tanlang: Ro'yxatdan o'tish yoki Haqida.")

bot.polling()
