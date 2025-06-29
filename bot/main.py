import asyncio
import logging
import os

from aiogram import (
    Bot, Dispatcher,
    F, Router, types
)
from aiogram.exceptions import TelegramBadRequest
from aiogram.filters import Command
from dotenv import load_dotenv

from bot.button_bot import get_collections_keyboard
from bot.collections_gift import COLLECTIONS
from parsers.parser_gift import get_gift_offers_parser

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

load_dotenv()

TG_TOKEN = os.getenv("TELEGRAM_TOKEN")

bot = Bot(token=TG_TOKEN)
dp = Dispatcher()
router = Router()

@router.message(Command('start'))
async def start_handler(message: types.Message):
    keyboard = get_collections_keyboard(page=0)
    await message.answer("Выбери категорию подарков: 👇🏻", reply_markup=keyboard)
    
@router.message(Command("gift"))
async def handle_gift_command(message: types.Message):
    await message.answer("Скоро буду давать кнопки для выбора подарка!")
    
@router.callback_query(F.data.startswith("page_"))
async def paginate_collections_handler(callback_query: types.CallbackQuery):
    page_str = callback_query.data.split("_")[1]
    page = int(page_str)
    keyboard = get_collections_keyboard(page=page)
    try:
        await callback_query.message.edit_reply_markup(reply_markup=keyboard)
    except TelegramBadRequest as e:
        if "message is not modified" not in str(e):
            raise
    try:
        await callback_query.answer()
    except TelegramBadRequest:
        pass

@router.callback_query(F.data.startswith("col_"))
async def collection_chosen_handler(callback_query: types.CallbackQuery):
    slug = callback_query.data.replace("col_", "")
    offers = await get_gift_offers_parser(slug)
    if offers:
        collection_name = next((name for name, slug_val in COLLECTIONS.items() if slug_val == slug), slug)
        result = f"🎁 <b>{collection_name}</b>:\n\n"
        for offer in offers:
            result += f"💎 <b>{offer['price']} TON</b> — <a href=\"{offer['url']}\">Ссылка</a>\n"
        await callback_query.message.answer(result, parse_mode="HTML", disable_web_page_preview=True)
    else:
        await callback_query.message.answer("Нет доступных лотов для этой коллекции.")
    keyboard = get_collections_keyboard(page=0)  
    await callback_query.message.answer("👇 Выбери другую категорию или листай меню:", reply_markup=keyboard)
    
dp.include_router(router)

async def main():
    await dp.start_polling(bot)
    
if __name__ == "__main__":
    asyncio.run(main())