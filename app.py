import os
from flask import Flask, request
from telegram import Update, Bot
from telegram.ext import Dispatcher, CommandHandler, CallbackContext

app = Flask(__name__)

TOKEN = os.getenv("BOT_TOKEN") or "PASTE_YOUR_BOT_TOKEN_HERE"
bot = Bot(token=TOKEN)
dispatcher = Dispatcher(bot, None, workers=0, use_context=True)

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Webhook bot is running!")

dispatcher.add_handler(CommandHandler("start", start))

@app.route(f"/webhook/{TOKEN}", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return "OK", 200

@app.route("/")
def home():
    return "Bot is alive!", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
