import os
import telebot
from openai import OpenAI

# 1. ОПРЕДЕЛЯЕМ bot ПЕРВЫМ
bot = telebot.TeleBot(os.environ["BOT_TOKEN"])
client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

print("🚀 GPT Бот запущен!")

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "🤖 GPT-бот готов!\nНапиши 'анекдот' или вопрос!")

@bot.message_handler(func=lambda message: True)
def gpt_reply(message):
    print(f"Сообщение: {message.text}")  # В логи
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": message.text}]
        )
        answer = response.choices[0].message.content
        bot.reply_to(message, answer[:1000])  # Макс 1000 символов
    except Exception as e:
        print(f"Ошибка: {e}")
        bot.reply_to(message, f"GPT ошибка: {str(e)}")

bot.polling(none_stop=True)
