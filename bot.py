import telebot

TOKEN = '9073801530:AAGsS9i8mVVxsgNP4K37It-586z-WqxWdAo'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def send_link(message):
    query = message.text
    response = f"आपको '{query}' के लिए यह लिंक मिला: https://example.com/search?q={query}"
    bot.reply_to(message, response)
bot.deletewebhook()
bot.infinity_polling()
