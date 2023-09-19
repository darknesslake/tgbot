# import psycopg2
import sqlite3


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



async def new_phrase(update: Update, context: CallbackContext) -> None:
    conn = sqlite3.connect('phrases.db')
    cursor = conn.cursor()

    # Выбираем случайную фразу из базы данных
    # cursor.execute("CREATE TABLE IF NOT EXISTS phrases (id INTEGER PRIMARY KEY, phrase TEXT)")
    cursor.execute("SELECT phrase FROM phrases ORDER BY RANDOM() LIMIT 1")
    result = cursor.fetchone()

    if result:
        phrase = result[0]
        await update.message.reply_text(phrase)
    else:
        await update.message.reply_text("В базе данных нет фраз.")

    conn.close()
