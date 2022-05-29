from genshin import Client

from tg_bot.config import load_config

def get_client():
    config = load_config("../bot.ini")
    client = Client()
    client.set_cookies(ltoken=config.genshin.ltoken, ltuid=config.genshin.ltuid)





