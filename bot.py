import os
import telebot
import google.generativeai as genai
from flask import Flask
from threading import Thread

# --- अपनी API Keys यहाँ डालें ---
TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN", "अपना_TELEGRAM_BOT_TOKEN_यहाँ_डालें")
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "अपनी_GEMINI_API_KEY_यहाँ_डालें")

bot = telebot.TeleBot(TELEGRAM_TOKEN)
client = genai.Client(api_key=GEMINI_API_KEY)

# Render पर ज़िंदा रखने के लिए
app = Flask('')
@app.route('/')
def home():
    return "बॉट चालू है!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "नमस्ते! मैं आपका लिंक और चैट बॉट हूँ। जो चाहिए, बेझिझक माँगें।")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_text = message.text
    bot.send_chat_action(message.chat.id, 'typing')
    
    prompt = f"""
    तुम एक सीधे और सटीक जवाब देने वाले असिस्टेंट हो।
    नियम:
    1. अगर यूजर सामान्य बात करे, तो छोटा जवाब दो।
    2. अगर यूजर किसी वेबसाइट, ऐप या गेम का लिंक माँगे, तो बिना कोई फालतू बात किए सिर्फ उसका सीधा और सही लिंक दो।
    
    यूजर का मैसेज: {user_text}
    """
    
    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
        )
        bot.reply_to(message, response.text)
    except Exception as e:
        bot.reply_to(message, "एरर आ रहा है, बाद में कोशिश करें।")
        print(f"Error: {e}")

if __name__ == "__main__":
    keep_alive()
    bot.infinity_polling()
    
