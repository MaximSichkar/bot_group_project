from aiogram import Router
from aiogram.types import Message
from aiogram.filters.command import CommandStart


router = Router()


@router.message(CommandStart())
async def start(message: Message):
    await message.answer('Добрий день, це бот для генерації картинок Artois. Щоб почати генерувати картинки напишіть '
                         'слово, яке буде описувати, те що ви хочете згенерувати.\n'
                         'Наприклад: lake \n'
                         'Якщо ви хочете згенерувати використовуючи декілька "тагів", то треба відповідно написати їх '
                         'через кому: lake, Sunrise, clear sky \n'
                         'Нейронна мережа сприймає тільки англійську мову, тому на інші мови вона не буде давати гарні '
                         'картинки \n'
                         'Це все, дуже рекомендовано використовувати саме таги, а не прямим текстом писати запит.')
