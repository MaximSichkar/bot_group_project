from aiogram.types import CallbackQuery
from aiogram import Router, F

from bot.handlers.create_keyboard import create_main_keyboard

router = Router()

@router.callback_query(F.data.startswith('back_to_options'))
async def show_options(callback: CallbackQuery):
    await callback.message.edit_text(
        "Choose options:",
    reply_markup=create_main_keyboard(callback.data.split(':')[1]))
