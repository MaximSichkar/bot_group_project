from aiogram import Router

from .batch_size import router as batch_size_router
from .choose_model import router as choose_model_router
from .forbidden_message import router as forbidden_message_router
from .generation import router as generation_router
from .hr_fix_statement import router as hr_fix_statement_router
from .other_options import router as other_options_router
from .picture_height import router as picture_height_router
from .picture_width import router as picture_width_router
from .show_prompt import router as show_prompt_router
from .text_message import router as text_message_router
from .back_to_options import router as back_to_options_router

router = Router()

router.include_routers(
    forbidden_message_router,
    generation_router,
    other_options_router,
    batch_size_router,
    picture_width_router,
    picture_height_router,
    hr_fix_statement_router,
    choose_model_router,
    show_prompt_router,
    text_message_router,
    back_to_options_router
)
