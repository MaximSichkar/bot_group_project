from aiogram import Router

from .common import router as common_router
from .admin import router as admin_router
from .default import router as default_router

main_router = Router()
main_router.include_routers(
    common_router,
    admin_router,
    default_router
)
