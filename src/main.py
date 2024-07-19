import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
import os
from dotenv import load_dotenv
import random

load_dotenv()
TOKEN = os.getenv("TOKEN_TELEGRAM_BOT")

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Hola Soy ChronuxNix, es un placer. Dime para que soy bueno. :3")
async def info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id,text="Soy un bot creado por Dylan Marcano, estoy en desarrollo en conjunto con Astro pero en la plataforma de discord, somos del mismo creador, espero podamos brindarte mucha ayuda. :3 ")

if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()
    
    start_handler = CommandHandler('start', start)
    info_handler = CommandHandler('info',info)
    application.add_handler(start_handler)
    application.add_handler(info_handler)
    
    application.run_polling()
