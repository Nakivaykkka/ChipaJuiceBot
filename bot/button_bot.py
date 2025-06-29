from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from bot.collections_gift import COLLECTIONS


def get_navigations_buttons(page: int, total_pages: int):
    prev_page = (page - 1) % total_pages
    next_page = (page + 1) % total_pages
    return [
        InlineKeyboardButton(text="⬅️ Назад", callback_data=f"page_{prev_page}"),
        InlineKeyboardButton(text="🏠 В начало", callback_data="page_0"),
        InlineKeyboardButton(text="➡️ Вперёд", callback_data=f"page_{next_page}")
    ]   
    

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_collections_keyboard(page: int = 0, per_page: int = 9):
    all_collections = list(COLLECTIONS.items())
    total_pages = (len(all_collections) + per_page - 1) // per_page
    start = page * per_page
    end = start + per_page
    page_collections = all_collections[start:end]

    keyboard = []

    row = []
    for i, (title, slug) in enumerate(page_collections, 1):
        row.append(InlineKeyboardButton(text=title, callback_data=f"col_{slug}"))
        if i % 3 == 0:
            keyboard.append(row)
            row = []
    if row:
        keyboard.append(row)

    total_pages = (len(COLLECTIONS) + per_page - 1) // per_page
    nav_row = get_navigations_buttons(page, total_pages)
    keyboard.append(nav_row)

   
    return InlineKeyboardMarkup(inline_keyboard=keyboard)

