import os
from flask import Flask
from telegram.ext import Updater, CommandHandler

app = Flask(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")

def start(update, context):
    update.message.reply_text("Bot is running!")

updater = Updater(BOT_TOKEN, use_context=True)
dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start))

@app.route('/')
def index():
    return 'Bot is alive!'

if __name__ == '__main__':
    updater.start_polling()
    app.run(host='0.0.0.0', port=10000)
