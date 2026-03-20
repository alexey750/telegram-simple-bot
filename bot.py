import os
import telebot

bot = telebot.TeleBot(os.environ.get("BOT_TOKEN"))

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я очень простой бот :)")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"Ты написал: {message.text}")

print("Бот запущен локально...")
bot.polling()
