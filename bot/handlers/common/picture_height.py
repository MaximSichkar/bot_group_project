from aiogram.types import CallbackQuery
from aiogram import Router, F

from bot.handlers.create_keyboard import create_picture_height_keyboard, create_options_keyboard

from bot.models import PromptVariable, User

router = Router()


@router.callback_query(F.data.startswith('height'))
async def height_create(callback: CallbackQuery):
    await callback.message.edit_text(
        "Choose height:",
        reply_markup=create_picture_height_keyboard(callback.data.split(':')[1]))


@router.callback_query(F.data.regexp(r'^\d+h:.*'))
async def height_of_pictures(callback: CallbackQuery, user: User):
    data = callback.data.split(':')
    prompt_variable = await PromptVariable.objects.aget(id=data[1])

    height = data[0][:-1]

    prompt_variable.height = int(height)

    await prompt_variable.asave()

    await callback.message.edit_text("Виберіть висоту:", reply_markup=create_options_keyboard(data[1]))
