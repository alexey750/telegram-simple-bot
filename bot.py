import os
import telebot
from openai import OpenAI

bot = telebot.TeleBot(os.environ.get("BOT_TOKEN"))
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "🤖 Умный бот с GPT готов!\nСпрашивай анекдоты, советы, что угодно!")

@bot.message_handler(func=lambda message: True)
def smart_reply(message):
    print(f"📨 Получено: {message.text}")  # Отладка в логи
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": message.text[:100]}]  # 100 символов макс
        )
        answer = response.choices[0].message.content[:400]  # 400 символов макс
        bot.reply_to(message, answer)
        print(f"✅ GPT ответил")  # Отладка
    except Exception as e:
        print(f"❌ Ошибка GPT: {e}")  # В логи Railway
        bot.reply_to(message, f"🤖 GPT устал 😴\nОшибка: {str(e)[:100]}\nПопробуй позже!")

print("🚀 Умный GPT бот запущен!")
bot.polling()
