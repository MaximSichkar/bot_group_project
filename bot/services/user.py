from bot.models import User
from aiogram import types
from bot.logger import logger


async def create_user(tele_user: types.User) -> User:
    user = User(user_id=tele_user.id,
                first_name=tele_user.first_name,
                last_name=tele_user.last_name,
                user_name=tele_user.username)
    await user.asave()

    logger.info(f"New user created with id: {user.user_id}")
    
    return user


async def get_user(user_id: int) -> User | None:
    try:
        user = await User.objects.aget(pk=user_id)
        return user
    except User.DoesNotExist as e:
        return None


async def get_or_create_user(tele_user: types.User) -> User:
    user = await get_user(tele_user.id)
    if user:
        return user
    return await create_user(tele_user)
