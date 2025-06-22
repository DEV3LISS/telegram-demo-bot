from aiogram import Bot, Dispatcher, types, executor
import os

API_TOKEN = os.getenv("BOT_TOKEN") or "PASTE_YOUR_TOKEN"
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler()
async def echo(msg: types.Message):
    await msg.answer(msg.text)

if __name__ == "__main__":
    executor.start_polling(dp)
