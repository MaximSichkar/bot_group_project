from aiogram.types import CallbackQuery
from aiogram import Router, F

from bot.handlers.create_keyboard import create_choose_model_keyboard, create_options_keyboard

from bot.models import PromptVariable, User

router = Router()


@router.callback_query(F.data.startswith('models'))
async def choose_model_create(callback: CallbackQuery):
    await callback.message.edit_text(
        "Choose model to generate:",
        reply_markup=create_choose_model_keyboard(callback.data.split(':')[1]))


@router.callback_query(F.data.startswith('grapefruit') | F.data.startswith('calicomix') | F.data.startswith('level4XL'))
async def model_of_pictures(callback: CallbackQuery, user: User):
    data = callback.data.split(':')
    prompt_variable = await PromptVariable.objects.aget(id=data[1])

    model = data[0]

    prompt_variable.hr_checkpoint_name = str(model)

    await prompt_variable.asave()

    await callback.message.edit_text("Choose options:", reply_markup=create_options_keyboard(data[1]))
