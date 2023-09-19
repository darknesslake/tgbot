import logging
from typing import Dict

import time
import re

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update, Bot
from telegram.ext import (
    Application,
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    CallbackContext,
    filters,
    Updater,
    Job,
)

# import psycopg2
import sqlite3

from bot.start_bot import start_bot
from bot.new_phrases import new_phrase
from bot.buy_premium import buy_premium
from bot.buy_and_check_premium import buy_and_check_premium

from folder_to_ignore.tg_token import ENGLISH_TOKEN_BOT



# Главная функция
def main() -> None:
    application = Application.builder().token(ENGLISH_TOKEN_BOT).build()

    conv_handler = CommandHandler('start', start_bot)
    conv_handler2 = CommandHandler('new_phrase', new_phrase)
    conv_handler3 = CommandHandler('buy_premium', buy_premium)
    

    application.add_handler(conv_handler)
    application.add_handler(conv_handler2)
    application.add_handler(conv_handler3)


    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()