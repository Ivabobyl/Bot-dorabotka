
from aiogram import Router, types
from aiogram.types import Message
from keyboards import user_kb

router = Router()

@router.message(lambda m: m.text == "Профиль")
async def profile(message: Message):
    await message.answer("Ваш профиль:
Скоро тут будет информация.")
