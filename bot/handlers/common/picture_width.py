from aiogram.types import CallbackQuery
from aiogram import Router, F

from bot.handlers.create_keyboard import create_picture_width_keyboard, create_options_keyboard

from bot.models import PromptVariable, User

router = Router()


@router.callback_query(F.data.startswith('width'))
async def width_create(callback: CallbackQuery):
    await callback.message.edit_text(
        "Choose width:",
        reply_markup=create_picture_width_keyboard(callback.data.split(':')[1]))


@router.callback_query(F.data.regexp(r'^\d+w:.*'))
async def width_of_pictures(callback: CallbackQuery, user: User):
    data = callback.data.split(':')
    prompt_variable = await PromptVariable.objects.aget(id=data[1])

    width = data[0][:-1]

    prompt_variable.width = int(width)

    await prompt_variable.asave()

    await callback.message.edit_text("Виберіть ширину:", reply_markup=create_options_keyboard(data[1]))
