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



async def buy_premium(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    user_name = update.message.from_user.username

    conn = sqlite3.connect('user_data.db')
    cursor = conn.cursor()

    # Проверяем, есть ли пользователь в базе данных
    cursor.execute("SELECT * FROM users WHERE user_id=?", (user_id,))
    existing_user = cursor.fetchone()

    if existing_user:
        # Если пользователь уже есть, обновляем его статус премиума
        cursor.execute("UPDATE users SET premium=1 WHERE user_id=?", (user_id,))
        conn.commit()
        conn.close()
        await update.message.reply_text(f"Поздравляем, {user_name}! Вы приобрели премиум.")
    else:
        # Если пользователя нет в базе данных, добавляем его
        cursor.execute("INSERT INTO users (user_id, username, premium) VALUES (?, ?, ?)", (user_id, user_name, 1))
        conn.commit()
        conn.close()
        await update.message.reply_text(f"Поздравляем, {user_name}! Вы приобрели премиум.")



# ///////////////////////////////////////////////////////////////////////////////////////

# from flask import Flask, request
# import stripe

# app = Flask(__name__)

# @app.route('/stripe-webhook', methods=['POST'])
# def stripe_webhook():
#     payload = request.data
#     event = None

#     try:
#         event = stripe.Event.construct_from(
#             payload, stripe.api_key, stripe_webhook_secret
#         )
#     except ValueError as e:
#         return str(e), 400

#     if event.type == "payment_intent.succeeded":
#         payment_intent = event.data.object
#         user_id = payment_intent.metadata.get("user_id")

#         # Add the user to the premium database
#         add_user_to_premium_database(user_id)

#     return "", 200

# import sqlite3

# def add_user_to_premium_database(user_id):
#     conn = sqlite3.connect('premium_users.db')
#     cursor = conn.cursor()

#     cursor.execute("INSERT INTO premium_users (user_id) VALUES (?)", (user_id,))
#     conn.commit()
#     conn.close()


# def check_premium(update: Update, context: CallbackContext):
#     user_id = update.message.from_user.id
#     if is_user_premium(user_id):
#         update.message.reply_text("You are a premium user!")
#     else:
#         update.message.reply_text("You are not a premium user.")
        

# def is_user_premium(user_id):
#     conn = sqlite3.connect('premium_users.db')
#     cursor = conn.cursor()

#     cursor.execute("SELECT user_id FROM premium_users WHERE user_id = ?", (user_id,))
#     result = cursor.fetchone()

#     conn.close()

#     return result is not None

# ///////////////////////////////////////////////////////////////////////////////////////