from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeChat
from .CommandNames import *

commands = [
    BotCommand(command=f"/admin_command", description="description"),
]


async def set_admin_commands(bot: Bot, admin_id: int):
    from .default import commands as default_commands
    await bot.set_my_commands(default_commands + commands, scope=BotCommandScopeChat(chat_id=admin_id))
