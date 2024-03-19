from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from mainNobu import *
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from mainNobu import *

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hola {update.effective_user.first_name}!')

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = update.message.text
    await update.message.reply_text(text)
    
# Crear la aplicación y configurar los manejadores de comandos y mensajes


# hay que utilizar el markdown para que se vea bonito en telegram
async def obtener_info(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Obteniendo tareas... ⏳")
    print("Obteniendo tareas... ⏳")
    tareas = main()  # Suponiendo que esto devuelve una lista de tareas
    await update.message.reply_text("Tareas obtenidas. 🎉")
    print("Tareas obtenidas. 🎉")

    for tarea in tareas:
        # Construir el mensaje sin Markdown
        mensaje_tarea = f"""
🆔 ID: {tarea["idTarea"]}
{"-"*30}
⏹️ Evento: {tarea["titulo"]}
📆 Fecha: {tarea["fecha_entrega"]}
⏳ Días restantes: {tarea["dias_restantes"]}, Horas restantes: {tarea["horas_restantes"]}, Minutos restantes: {tarea["minutos_restantes"]}, Segundos restantes: {tarea["segundos_restantes"]}
📝 DESCRIPCION:
{"-"*30}
{tarea["descripcion"]}
{"-"*30}
📚 Materia: {tarea["materia"]}
ESTADO: {tarea["estado"]}
                        """
        # Enviar el mensaje sin especificar parse_mode
        await update.message.reply_text(mensaje_tarea)





app = ApplicationBuilder().token("7072827563:AAHCfNu3q8x810V6H5BHk3xS96_4XZwQGFA").build()

# Comandos de uso

app.add_handler(CommandHandler("obtener_tareas", obtener_info))


# Manejador de mensajes de texto, que hace eco del mensaje
#app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

app.run_polling()
