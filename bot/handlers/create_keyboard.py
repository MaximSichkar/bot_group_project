import uuid

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def create_main_keyboard(variable_id: uuid.uuid4):
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Моделі", callback_data=f'models:{variable_id}')],
        [InlineKeyboardButton(text="Інші конфігурації", callback_data=f'options:{variable_id}')],
        [InlineKeyboardButton(text="Показати промпт", callback_data=f'show_prompt:{variable_id}')],
        [InlineKeyboardButton(text="Почати генерацію", callback_data=f'generation:{variable_id}')]
    ], one_time_keyboard=True)


def create_options_keyboard(variable_id: uuid.uuid4):
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Кількість картинок", callback_data=f'batch_size:{variable_id}')],
        [InlineKeyboardButton(text="Ширина картинки", callback_data=f'width:{variable_id}')],
        [InlineKeyboardButton(text="Висота картинки", callback_data=f'height:{variable_id}')],
        [InlineKeyboardButton(text="Увімкнути Hires Fix (рекомендовано)", callback_data=f'inclusion_hr:{variable_id}')],
        [InlineKeyboardButton(text="Повернутися", callback_data=f'back_to_options:{variable_id}')]
    ], one_time_keyboard=True)


def create_choose_model_keyboard(variable_id: uuid.uuid4):
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Level4XL", callback_data=f'level4XL.safetensors:{variable_id}')],
        [InlineKeyboardButton(text="grapefruit", callback_data=f'grapefruit.safetensors:{variable_id}')],
        [InlineKeyboardButton(text="calicomix", callback_data=f'calicomix.safetensors:{variable_id}')]
    ], one_time_keyboard=True)


def create_picture_number_keyboard(variable_id: uuid.uuid4):
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="1", callback_data=f'1p:{variable_id}')],
        [InlineKeyboardButton(text="2", callback_data=f'2p:{variable_id}')],
        [InlineKeyboardButton(text="3", callback_data=f'3p:{variable_id}')],
        [InlineKeyboardButton(text="4", callback_data=f'4p:{variable_id}')]
    ], one_time_keyboard=True)


def create_picture_width_keyboard(variable_id: uuid):
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="360", callback_data=f'360w:{variable_id}')],
        [InlineKeyboardButton(text="480", callback_data=f'480w:{variable_id}')],
        [InlineKeyboardButton(text="800", callback_data=f'800w:{variable_id}')]
    ], one_time_keyboard=True)


def create_picture_height_keyboard(variable_id: uuid):
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="360", callback_data=f'360h:{variable_id}')],
        [InlineKeyboardButton(text="480", callback_data=f'480h:{variable_id}')],
        [InlineKeyboardButton(text="800", callback_data=f'800h:{variable_id}')]
    ], one_time_keyboard=True)


def create_enable_hires_fix_keyboard(variable_id: uuid):
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Disable", callback_data=f'0i:{variable_id}')],
        [InlineKeyboardButton(text="Enable", callback_data=f'1i:{variable_id}')]
    ], one_time_keyboard=True)


def create_show_prompt_keyboard(variable_id: uuid):
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Повернутися", callback_data=f'back_to_options_prompt:{variable_id}')]
    ], one_time_keyboard=True)
