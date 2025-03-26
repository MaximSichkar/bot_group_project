from aiogram.types import Message, CallbackQuery
from aiogram import Router, F
from aiogram.enums.content_type import ContentType

from bot.handlers.common.generation import generation

from bot.handlers.create_keyboard import create_main_keyboard
from bot.models import PromptVariable, User

router = Router()


@router.message(F.content_type == ContentType.TEXT)
async def first_message(message: Message, user: User):
    variable = PromptVariable(
        user=user,
        prompt=message.text
    )
    await variable.asave()
    fake_callback = CallbackQuery(
        id='unique_fake_callback_id_987654',
        from_user=user,
        chat_instance=message.chat.id,
        data=f'generation:{variable}',
        message=message.text,
    )
    await generation(fake_callback)
#    await message.answer("Почніть генерацію..", reply_markup=create_main_keyboard(variable.id))
