import logging
import os
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from dotenv import load_dotenv

# Logger sozlamalari
logging.basicConfig(level=logging.INFO)

# .env faylidan TOKEN va ADMIN_ID ni yuklash
load_dotenv()
TOKEN = os.getenv("TOKEN")
ADMIN_ID = os.getenv("ADMIN_ID")

# Bot va Dispatcher
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# /start komandasi
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Salom! Apelsin Cargo botiga xush kelibsiz!")

# Botni ishga tushirish
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
