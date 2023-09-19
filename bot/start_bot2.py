# import psycopg2
import sqlite3
from folder_to_ignore.tg_token import ENGLISH_TOKEN_BOT


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

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
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




def start_bot():
    # updater = Updater("6510017854:AAEswtD4P00Mx80Q53ylqxr_bldY2FNr4Nk")
    application = Application.builder().token(ENGLISH_TOKEN_BOT).build()

    # dispatcher = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_name)],
            AGE: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_age)],
        },
        fallbacks=[],
    )

# /////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////


    # conv_handler1 = ConversationHandler(
    #     entry_points=[CommandHandler('notification', notification)],
    #     states={
    #         DATE: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_date)],
    #         TIME: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_time)],
    #     },
    #     fallbacks=[],
    # )

    # conv_handler2 = ConversationHandler(
    #     entry_points=[MessageHandler(filters.Regex('^/notification$'), notification)],
    #     states={
    #         DATE: [MessageHandler(filters.Regex('^\d{4}-\d{2}-\d{2}$'), set_date)],
    #         TIME: [MessageHandler(filters.Regex('^\d{2}:\d{2}$'), set_time)],
    #         CONFIRM: [MessageHandler(filters.Regex('^(да|нет)$'), confirm)],
    #     },
    #     fallbacks=[MessageHandler(filters.Regex('^/cancel$'), cancel)],
    # )

    # conv_handler2 = ConversationHandler(
    #     entry_points=[MessageHandler(filters.Regex('/notification'), notification)],
    #     states={
    #         SET_INTERVAL: [MessageHandler(filters.TEXT & ~filters.COMMAND, set_interval)],
    #     },
    #     fallbacks=[]
    # )

    # conv_handler2 = ConversationHandler(
    #     entry_points=[MessageHandler(filters.Regex('/notification'), notification)],
    #     states={
    #         SET_INTERVAL: [MessageHandler(filters.TEXT & ~filters.COMMAND, set_interval)],
    #     },
    #     fallbacks=[]
    # )


# /////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////

    # conv_handler3 = ConversationHandler(
    #     entry_points=[MessageHandler(filters.Regex('^/new_phrase$'), new_phrase)],
    #     states={

    #     },
    #     fallbacks=[],
    # )

    # conv_handler4 = ConversationHandler(
    #     entry_points=[MessageHandler(filters.Regex('^/buy_premium$'), buy_premium)],
    #     states={

    #     },
    #     fallbacks=[],
    # )

    application.add_handler(conv_handler)
    # application.add_handler(conv_handler1)
    # application.add_handler(conv_handler2)
    # application.add_handler(conv_handler3)
    # application.add_handler(conv_handler4)
    application.run_polling(allowed_updates=Update.ALL_TYPES)
    # updater.start_polling()
    # updater.idle()

