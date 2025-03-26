from aiogram.types import CallbackQuery
from aiogram import Router, F

from bot.handlers.create_keyboard import create_picture_number_keyboard, create_options_keyboard

from bot.models import PromptVariable, User

router = Router()


@router.callback_query(F.data.startswith('batch_size'))
async def batch_size(callback: CallbackQuery):
    await callback.message.edit_text(
        "Number of pictures:",
        reply_markup=create_picture_number_keyboard(callback.data.split(':')[1]))


@router.callback_query(F.data.regexp(r'^\d+p:.*'))
async def number_of_pictures(callback: CallbackQuery):
    data = callback.data.split(':')
    prompt_variable = await PromptVariable.objects.aget(id=data[1])

    picture_num = data[0][:-1]

    prompt_variable.batch_size = int(picture_num)

    await prompt_variable.asave()

    await callback.message.edit_text("Choose options:", reply_markup=create_options_keyboard(data[1]))
