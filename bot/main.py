import asyncio
import os

from aiogram import Bot, Dispatcher, Router, types
from aiogram.filters import Command
from dotenv import load_dotenv

load_dotenv()

TG_TOKEN = os.getenv("TELEGRAM_TOKEN")

bot = Bot(token=TG_TOKEN)
dp = Dispatcher()
router = Router()

@router.message(Command('start'))
async def start_handler(message: types.Message):
    await message.answer("Привет!")
    
@router.message(Command("gift"))
async def handle_gift_command(message: types.Message):
    await message.answer("Скоро буду давать кнопки для выбора подарка!")
    
dp.include_router(router)

async def main():
    await dp.start_polling(bot)
    
if __name__ == "__main__":
    asyncio.run(main())