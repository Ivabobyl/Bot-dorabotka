
from aiogram import Router, types
from aiogram.types import Message
from keyboards import admin_kb

router = Router()

@router.message(lambda m: m.text == "Админка")
async def admin_panel(message: Message):
    await message.answer("Добро пожаловать в админку.", reply_markup=admin_kb.main_menu())
