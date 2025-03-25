import asyncio

from aiogram import Bot, Dispatcher
from django.conf import settings
from django.core.management.base import BaseCommand

from bot import logger


async def on_startup(bot: Bot):
    from bot.commands import set_default_commands, set_admin_commands

    await set_default_commands(bot)
    for admin in settings.ADMINS:
        await set_admin_commands(bot, admin)

    await bot.send_message(chat_id=settings.MY_ID, text="Bot started")
    logger.info("Bot started")


async def on_shutdown(bot: Bot):
    await bot.send_message(chat_id=settings.MY_ID, text="Bot finished")
    logger.info("Bot finished")


def setup_main_middleware(dp: Dispatcher):
    from bot.middlewares import UserMiddleware, LoggingMiddleware

    dp.update.middleware(UserMiddleware())
    dp.update.middleware(LoggingMiddleware())


class Command(BaseCommand):
    help = 'Starts bot'

    def handle(self, *args, **options):
        from bot.generate_session import bot, dp
        from bot.handlers import main_router

        dp.include_router(main_router)
        setup_main_middleware(dp)

        dp.startup.register(on_startup)
        dp.shutdown.register(on_shutdown)
        asyncio.run(dp.start_polling(bot))
