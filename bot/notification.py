

# /////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////



# class NotificationBot:
#     def __init__(self, bot_token):
#         self.updater = Updater(token=bot_token, use_context=True)
#         self.bot = Bot(token=bot_token)
#         self.interval = None
#         self.chat_id = None

#     def start(self, update: Update, context):
#         context.bot.send_message(chat_id=update.effective_chat.id, text="Введите интервал уведомлений в секундах.")
        
#     def set_interval(self, update: Update, context):
#         try:
#             self.interval = int(update.message.text)
#             self.chat_id = update.effective_chat.id
#             context.bot.send_message(chat_id=self.chat_id, text=f"Установлен интервал уведомлений: {self.interval} секунд.")
#         except ValueError:
#             context.bot.send_message(chat_id=update.effective_chat.id, text="Пожалуйста, введите число.")

#     def send_notification(self):
#         if self.interval and self.chat_id:
#             while True:
#                 self.bot.send_message(chat_id=self.chat_id, text="Уведомление!")
#                 time.sleep(self.interval)

#     def run(self):
#         dispatcher = self.updater.dispatcher
#         start_handler = CommandHandler('start', self.start)
#         dispatcher.add_handler(start_handler)
        
#         interval_handler = MessageHandler(Filters.text & (~Filters.command), self.set_interval)
#         dispatcher.add_handler(interval_handler)

#         self.updater.start_polling()


# /////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////


# async def notification(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
#     await update.message.reply_text(f'Typing date notification: ')
#     return DATE
    

# async def get_date(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
#     user = update.message.from_user

#     await update.message.reply_text(f"Отлично! Typing time study:")
#     return TIME

# # Обработчик возраста пользователя
# async def get_time(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
#     user = update.message.from_user
#     try:
#         age = int(update.message.text)
#         context.user_data['age'] = age
#         # Сохраняем данные в базу данных SQLite
#         conn = sqlite3.connect('user_data.db')
#         cursor = conn.cursor()
#         cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")
#         cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", (context.user_data['name'], age))
#         conn.commit()
#         conn.close()

#         await update.message.reply_text(f"Спасибо, {context.user_data['name']}! Ваш возраст ({age}) был сохранен в базе данных.")
#         return ConversationHandler.END
#     except ValueError:
#         await update.message.reply_text("Пожалуйста, введите корректный время (6:00)):")
#         return TIME
    

# async def phrase(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     await update.message.reply_text(f'New phrase for you: ')


# /////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////


# Глобальная переменная для хранения интервала (в секундах)
# interval = None

# # Состояния диалога
# SET_INTERVAL = 0


# async def notification(update: Update, context: CallbackContext) -> int:
#     await update.message.reply_text("Привет! Введите интервал (в секундах), с которым вы хотите получать уведомления:")
#     return SET_INTERVAL

# async def set_interval(update: Update, context: CallbackContext) -> int:
#     global interval
#     try:
#         interval = int(update.message.text)
#         if interval <= 0:
#             await update.message.reply_text("Интервал должен быть положительным числом. Пожалуйста, введите интервал снова:")
#             return SET_INTERVAL
#         else:
#             await update.message.reply_text(f"Интервал установлен на {interval} секунд. Теперь я буду отправлять вам уведомления с этим интервалом.")
#             context.job_queue.run_repeating(send_notification, interval=interval, first=0, context=update.message.chat_id)
#             return ConversationHandler.END
#     except ValueError:
#         await update.message.reply_text("Некорректный формат интервала. Пожалуйста, введите интервал снова (в секундах):")
#         return SET_INTERVAL
    

# async def send_notification(context: CallbackContext):
#     context.bot.send_message(context.job.context, "Это ваше уведомление!")


# /////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////

# # Обработчик ввода даты
# async def set_date(update: Update, context: CallbackContext) -> int:
#     context.user_data['date'] = update.message.text
#     await update.message.reply_text("Теперь введите время (в формате ЧЧ:ММ):")
#     return TIME

# # Обработчик ввода времени
# async def set_time(update: Update, context: CallbackContext) -> int:
#     context.user_data['time'] = update.message.text
#     await update.message.reply_text(f"Уведомление установлено на {context.user_data['date']} в {context.user_data['time']}. Подтвердите (Да/Нет):")
#     return CONFIRM

# # Обработчик подтверждения уведомления
# async def confirm(update: Update, context: CallbackContext) -> int:
#     user = update.message.from_user

#     if update.message.text.lower() == "да":
#         # Сохраняем уведомление в базе данных SQLite
#         conn = sqlite3.connect('user_data.db')
#         cursor = conn.cursor()
#         # cursor.execute("CREATE TABLE IF NOT EXISTS notifications (id INTEGER PRIMARY KEY, user_id INTEGER, date TEXT, time TEXT)")
#         cursor.execute("INSERT INTO notifications (user_id, date, time) VALUES (?, ?, ?)", (user.id, context.user_data['date'], context.user_data['time']))
#         conn.commit()
#         conn.close()

#         await update.message.reply_text("Уведомление сохранено.")
#     else:
#         await update.message.reply_text("Уведомление не сохранено.")

#     # Сбрасываем состояние диалога
#     context.user_data.clear()
#     return ConversationHandler.END

# # Функция отмены диалога
# async def cancel(update: Update, context: CallbackContext) -> int:
#     await update.message.reply_text("Диалог отменен.")
#     context.user_data.clear()
#     return ConversationHandler.END


# /////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////


