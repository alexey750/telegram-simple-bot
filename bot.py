@bot.message_handler(func=lambda message: True)
def smart_reply(message):
    print(f"📨 Сообщение: {message.text}")  # В логи Railway
    
    # Проверка ключей
    openai_key = os.environ.get("OPENAI_API_KEY")
    if not openai_key:
        bot.reply_to(message, "❌ OPENAI_API_KEY не задан!")
        return
    
    try:
        import openai
        print("✅ openai импортирована")
        
        client = OpenAI(api_key=openai_key)
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": message.text}]
        )
        answer = response.choices[0].message.content
        bot.reply_to(message, answer)
        print("✅ GPT ответил")
        
    except ImportError:
        bot.reply_to(message, "❌ Нет библиотеки openai (проверь requirements.txt)")
    except Exception as e:
        bot.reply_to(message, f"❌ GPT ошибка: {str(e)}")
        print(f"❌ Ошибка: {e}")
