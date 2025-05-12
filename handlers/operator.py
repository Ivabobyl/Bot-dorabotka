
from aiogram import Router, types
from aiogram.types import Message
from keyboards import operator_kb

router = Router()

@router.message(lambda m: m.text == "Оператор")
async def operator_panel(message: Message):
    await message.answer("Панель оператора активна.", reply_markup=operator_kb.main_menu())
