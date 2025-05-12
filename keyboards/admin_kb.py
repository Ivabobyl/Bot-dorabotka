
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def main_menu():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Список пользователей")],
            [KeyboardButton(text="Изменить курс"), KeyboardButton(text="Сделки")]
        ],
        resize_keyboard=True
    )
