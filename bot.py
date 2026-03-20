import os
import telebot
from openai import OpenAI

# Токены
bot = telebot.TeleBot(os.environ.get("BOT_TOKEN"))
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я умный бот с GPT 😎\nСпрашивай что угодно!")

@bot.message_handler(func=lambda message: True)
def smart_reply(message):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": message.text}]
        )
        answer = response.choices[0].message.content
        bot.reply_to(message, answer)
    except Exception as e:
        bot.reply_to(message, f"Ошибка GPT: {e}\n(попробуй позже)")

print("Умный бот запущен...")
bot.polling()
