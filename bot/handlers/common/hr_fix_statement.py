from aiogram.types import CallbackQuery
from aiogram import Router, F

from bot.handlers.create_keyboard import create_enable_hires_fix_keyboard, create_options_keyboard

from bot.models import PromptVariable, User

router = Router()


@router.callback_query(F.data.startswith('inclusion_hr'))
async def hr_create(callback: CallbackQuery):
    await callback.message.edit_text(
        "Choose statement:",
        reply_markup=create_enable_hires_fix_keyboard(callback.data.split(':')[1]))


@router.callback_query(F.data.regexp(r'^\d+i:.*'))
async def hr_of_pictures(callback: CallbackQuery, user: User):
    data = callback.data.split(':')
    prompt_variable = await PromptVariable.objects.aget(id=data[1])

    if data[0][:-1] == 0:
        hr = False
    else:
        hr = True

    prompt_variable.enable_hr = bool(hr)

    await prompt_variable.asave()

    await callback.message.edit_text("Choose options:", reply_markup=create_options_keyboard(data[1]))
