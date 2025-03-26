from io import BytesIO

from aiogram.enums import ContentType
from aiogram.types import BufferedInputFile, CallbackQuery, Message
from aiogram import Router, F

from generation_api.txt2img import txt2img_generate

from bot.models import PromptVariable, User

router = Router()


@router.message(F.content_type == ContentType.TEXT)
@router.callback_query(F.data.startswith('generation'))
async def generation(event: CallbackQuery | Message, user: User):
    if isinstance(event, Message):
        prompt_variables_dict = {"prompt": event.text}
    else:
        await event.message.edit_text('Starting generation...')

        data = event.data.split(':')
        prompt_variable = await PromptVariable.objects.aget(id=data[1])

        prompt_variables_dict = {
            "prompt": prompt_variable.prompt,
            'batch_size': prompt_variable.batch_size,
            'width': prompt_variable.width,
            'height': prompt_variable.height,
            'enable_hr': prompt_variable.enable_hr,
            'hr_checkpoint_name': prompt_variable.hr_checkpoint_name
        }

    images = await txt2img_generate(prompt_variables_dict)

    message = event if isinstance(event, Message) else event.message

    for i in range(len(images)):
        img = images[i]
        file_name = f"{i + 1}-image.png"
        img_bytes = BytesIO()
        img.save(img_bytes, "PNG")
        file = BufferedInputFile(img_bytes.getvalue(), file_name)

        await message.answer_document(file)
