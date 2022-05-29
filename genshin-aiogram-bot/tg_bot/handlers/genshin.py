import logging

from aiogram import Dispatcher
from aiogram.types import Message

logger = logging.getLogger(__name__)

async def user_start(m: Message):
    await m.answer("Hello, user!")


def register_genshin(dp: Dispatcher):
    dp.register_message_handler(user_start, commands="test")
    logger.info("genshin handlers registered commands successfuly")