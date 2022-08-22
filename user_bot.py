from pyrogram import Client, filters
from time import sleep
from config.config import API_ID_TG, API_HASH_TG
from os import path
from random import choice

import res.user_bot_globals as USER_GLOBALS

APP_TELEGRAM = Client("my_account", API_ID_TG, API_HASH_TG)

@APP_TELEGRAM.on_message(filters.command('love', prefixes='.') & filters.me)
def love(_, message):
    for i in range(15):
        message.edit(USER_GLOBALS.LOVE_CLOUD_SMALL)
        sleep(0.25)
        message.edit(USER_GLOBALS.LOVE_CLOUD_A_LOT)

    message.edit(USER_GLOBALS.LOVE_YOU_TEXT)
    sleep(1)
    message.edit('Спасибо тебе. Ты самый лучший человек в моей жизни) 🤍')

@APP_TELEGRAM.on_message(filters.command('quote', prefixes='.') & filters.me)
def quote(_, message):
    try:
        if path.exists('res/quotes.txt'):
            with open('res/quotes.txt', mode='r', encoding='utf-8') as file:
                random_quote = choice(file.readlines())
            message.edit(str(random_quote))
    except:
        TypeError('Path res/quotes.txt not exists')

if __name__ == '__main__':
    APP_TELEGRAM.run()