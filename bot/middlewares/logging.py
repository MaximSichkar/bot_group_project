from typing import Callable, Dict, Any, Awaitable
from aiogram import BaseMiddleware
from aiogram.types import TelegramObject

from bot.logger import logger


class LoggingMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any]
    ) -> Any:
        logger.info("Received {event} from {user_id}",
                    event=event.event_type,
                    user_id=event.event.from_user.id,
                    user=event.event.from_user)
        await handler(event, data)
