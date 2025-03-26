from aiogram.types import Message
from aiogram import Router, F
from aiogram.enums.content_type import ContentType

router = Router()


@router.message(F.content_type != ContentType.TEXT)
async def cringe_receive(message: Message):
    await message.answer('This message is prohibited, discard it immediately')
    await message.answer('Nothing will be committed...')
