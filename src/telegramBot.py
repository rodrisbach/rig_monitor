import json
from apscheduler.schedulers.background import BackgroundScheduler
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from aux_functions import verify_status, get_status
import logging

def main():

    with open("../config/config.json") as jsonfile:
        config = json.load(jsonfile)
    logging.basicConfig(level=logging.INFO,filename=config["log_path"], filemode='w',format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
    logging.getLogger('apscheduler').setLevel(logging.INFO)
    token = config["telegram_token"]
    updater = Updater(token=token, use_context=True)
    scheduler = BackgroundScheduler()
    scheduler.start()

    #scheduler.add_job(verify_status,'interval', seconds=10, args=(config["rig_url"],float(config["min_hashrate"]),float(config["raw_hashrate"]),updater))
    updater.dispatcher.add_handler(CommandHandler('start',start))
    updater.dispatcher.add_handler(CommandHandler('status',status))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))
    # Start the bot
    updater.start_polling()
    # Run until the user stop the bot
    updater.idle()


def start(update, context):
    keyboard = [
        [
            InlineKeyboardButton("status", callback_data="status"),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Please choose:', reply_markup=reply_markup)

def status(update, context):
    with open("config.json") as jsonfile:
        config = json.load(jsonfile)
    get_status(config["rig_url"],update)

def button(update, context):
    with open("config.json") as jsonfile:
        config = json.load(jsonfile)
    query = update.callback_query
    query.answer()
    if query.data == str("status"):
        get_status(config["rig_url"], update)

if __name__ == "__main__":
    main()
