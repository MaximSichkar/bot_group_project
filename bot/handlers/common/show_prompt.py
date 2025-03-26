from aiogram.types import CallbackQuery
from aiogram import Router, F

from bot.handlers.create_keyboard import create_show_prompt_keyboard

from bot.models import PromptVariable, User

router = Router()


@router.callback_query(F.data.startswith('show_prompt'))
async def choose_model_create(callback: CallbackQuery):
    data = callback.data.split(':')
    prompt_variable = await PromptVariable.objects.aget(id=data[1])

    await callback.message.edit_text(
        "Ваш промпт наведено нижче:\n"
        f"{prompt_variable.prompt}", reply_markup=create_show_prompt_keyboard(data[1]))
