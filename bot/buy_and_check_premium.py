import sqlite3

from telegram import Update
from telegram.ext import (
    CommandHandler,
    CallbackContext,
)

async def buy_and_check_premium(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    user_name = update.message.from_user.username

    conn = sqlite3.connect('user_data.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE user_id=?", (user_id,))
    existing_user = cursor.fetchone()

    if existing_user:
        cursor.execute("UPDATE users SET premium=1 WHERE user_id=?", (user_id,))
        conn.commit()
        conn.close()
        await update.message.reply_text(f"Поздравляем, {user_name}! Вы приобрели премиум.")
    else:
        cursor.execute("INSERT INTO users (user_id, username, premium) VALUES (?, ?, ?)", (user_id, user_name, 1))
        conn.commit()
        conn.close()
        await update.message.reply_text(f"Поздравляем, {user_name}! Вы приобрели премиум.")


        