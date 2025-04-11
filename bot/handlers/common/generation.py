from io import BytesIO
import asyncio
import requests

from aiogram.types import BufferedInputFile, CallbackQuery, Message
from aiogram import Router, F

from generation_api.txt2img import txt2img_generate

from bot.models import PromptVariable, User

router = Router()


async def update_progress(message: Message):
    previous_text = None
    while True:
        try:
            r = requests.get("http://127.0.0.1:7860/sdapi/v1/progress").json()
            progress = int(r['progress'] * 100)
            bar = "█" * (progress // 10) + "░" * (10 - progress // 10)
            new_text = f"🧪 Генерація: [{bar}] {progress}%"
            if new_text != previous_text:
                await message.edit_text(new_text)
                previous_text = new_text
            if progress >= 100:
                break
            await asyncio.sleep(1)

        except Exception as e:
            print(f"[Прогресс] Ошибка: {e}")
            break


@router.callback_query(F.data.startswith('generation'))
async def generation(message: Message, user: User):
    if isinstance(message, Message):
        prompt_variables_dict = {"prompt": message.text}
    else:
        await message.edit_text('Starting generation...')

        data = message.data.split(':')
        prompt_variable = await PromptVariable.objects.aget(id=data[1])

        prompt_variables_dict = {
            "prompt": prompt_variable.prompt,
            'batch_size': prompt_variable.batch_size,
            'width': prompt_variable.width,
            'height': prompt_variable.height,
            'enable_hr': prompt_variable.enable_hr,
            'hr_checkpoint_name': prompt_variable.hr_checkpoint_name
        }

    progress_msg = await message.answer("🚀 Начинаю генерацию изображения...")

    _ = asyncio.create_task(update_progress(progress_msg))

    images = await txt2img_generate(prompt_variables_dict)

    for i in range(len(images)):
        img = images[i]
        file_name = f"{i + 1}-image.png"
        img_bytes = BytesIO()
        img.save(img_bytes, "PNG")
        file = BufferedInputFile(img_bytes.getvalue(), file_name)

        await message.answer_document(file)
