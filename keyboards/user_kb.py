
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def main_menu():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Купить крипту"), KeyboardButton(text="Продать крипту")],
            [KeyboardButton(text="Профиль")]
        ],
        resize_keyboard=True
    )
