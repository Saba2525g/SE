from balebale import Bot, Dispatcher
import llmf

BALE_TOKEN = "204146131:Zu-2bP5euoi4prIS2xmsplNzAYLXUx_eDzA"

bot = Bot(BALE_TOKEN)
dp = Dispatcher(bot)

@dp.message()
def handle(message):
    if not message.text:
        message.answer("Please send text only.")
        return

    try:
        reply = llmf.chat(message.text)
        message.answer(str(reply))
    except Exception as e:
        message.answer(f"AI error: {e}")

if __name__ == "__main__":
    print("Bot started...")
    bot.start_polling(dp)