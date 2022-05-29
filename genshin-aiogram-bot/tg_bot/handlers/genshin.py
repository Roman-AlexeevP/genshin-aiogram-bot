import logging

from aiogram import Dispatcher
from aiogram.types import Message


logger = logging.getLogger(__name__)

# write commands handlers here


def register_genshin(dp: Dispatcher):
    # dp.register_message_handler()
    # register commands here
    logger.info("genshin handlers registered commands successfuly")