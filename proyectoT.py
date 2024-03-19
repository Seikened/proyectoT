from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hola {update.effective_user.first_name}!')

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = update.message.text
    await update.message.reply_text(text)

app = ApplicationBuilder().token("7072827563:AAHCfNu3q8x810V6H5BHk3xS96_4XZwQGFA").build()

# Comando 'hello'
app.add_handler(CommandHandler("hello", hello))

# Manejador de mensajes de texto, que hace eco del mensaje
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

app.run_polling()
