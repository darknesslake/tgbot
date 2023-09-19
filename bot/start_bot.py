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


NAME, AGE = range(2)

async def start_bot(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text("Привет! Давайте начнем. Пожалуйста, введите ваше имя:")
    return NAME

# Обработчик имени пользователя
async def get_name(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user = update.message.from_user

    context.user_data['name'] = update.message.text
    await update.message.reply_text(f"Отлично, {context.user_data['name']}! Теперь введите ваш возраст:")
    return AGE

# Обработчик возраста пользователя
async def get_age(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user = update.message.from_user
    try:
        age = int(update.message.text)
        context.user_data['age'] = age
        # Сохраняем данные в базу данных SQLite
        conn = sqlite3.connect('user_data.db')
        cursor = conn.cursor()
        # cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")
        cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", (context.user_data['name'], age))
        conn.commit()
        conn.close()

        await update.message.reply_text(f"Спасибо, {context.user_data['name']}! Ваш возраст ({age}) был сохранен в базе данных.")
        return ConversationHandler.END
    except ValueError:
        await update.message.reply_text("Пожалуйста, введите корректный возраст (целое число):")
        return AGE



