import configparser
from dataclasses import dataclass


@dataclass
class TelegramBot:
    token: str


@dataclass
class GenshinAPI:
    ltuid: str
    ltoken: str
    login: str
    password: str


@dataclass
class Config:
    tg_bot: TelegramBot
    genshin: GenshinAPI


def cast_bool(value: str) -> bool:
    if not value:
        return False
    return value.lower() in ("true", "t", "1", "yes")


def load_config(path: str):
    config = configparser.ConfigParser()
    config.read(path)

    tg_bot = config["tg_bot"]

    return Config(
        tg_bot=TelegramBot(
            token=tg_bot["token"],
        ),
        genshin=GenshinAPI(**config["genshin"]))
