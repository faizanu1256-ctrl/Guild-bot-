import telebot

TOKEN = 'YOUR_BOT_TOKEN_HERE'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def send_link(message):
    query = message.text
    response = f"आपको '{query}' के लिए यह लिंक मिला: https://example.com/search?q={query}"
    bot.reply_to(message, response)

bot.infinity_polling()
