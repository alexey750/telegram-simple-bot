@bot.message_handler(func=lambda message: True)
def smart_reply(message):
    bot.reply_to(message, f"Получил: {message.text}\nGPT скоро заработает!")
