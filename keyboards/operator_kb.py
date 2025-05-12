
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def main_menu():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Активные заявки")],
            [KeyboardButton(text="Подтвердить"), KeyboardButton(text="Завершить сделку")]
        ],
        resize_keyboard=True
    )
