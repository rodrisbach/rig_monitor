import json, logging, sys
from rig import Rig
from apscheduler.schedulers.background import BackgroundScheduler
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update

def main():

    try:
        jsonfile = open("../config/config.json")
    except OSError:
        print("OS error occurred trying to open config file")
        sys.exit(1)
    except FileNotFoundError:
        print("Config file not found. Aborting")
        sys.exit(1)
    else:
        with jsonfile:
            config = json.load(jsonfile)

#    logging.basicConfig(level=logging.INFO,filename=config["log_path"], filemode='w',format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
#    logging.getLogger('apscheduler').setLevel(logging.INFO)
    token = config["telegram_token"]
    updater = Updater(token=token, use_context=True)
    scheduler = BackgroundScheduler()
    scheduler.start()
    rig = Rig(config["rig_url"],config["rig_password"],config["min_hashrate"],config["wallet_address"],config["coin"],config["flexpool_api"])
#    scheduler.add_job(rig.verify_status,'interval', seconds=10, args=(updater))
    updater.dispatcher.add_handler(CommandHandler('start',start))
#    updater.dispatcher.add_handler(CommandHandler('status', status))
    updater.dispatcher.add_handler(CommandHandler('status', lambda rig:status(rig)))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))
    # Start the bot
    updater.start_polling()
    # Run until the user stop the bot
    updater.idle()


def start(update: Update, context: CallbackContext):
    keyboard = [
        [
            InlineKeyboardButton("status", callback_data="status"),
            InlineKeyboardButton("restart", callback_data="restart"),
            InlineKeyboardButton("shutdown", callback_data="shutdown"),
            InlineKeyboardButton("config", callback_data="config"),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Please choose:', reply_markup=reply_markup)

def status(update: Update, context: CallbackContext, rig):
    message = rig.get_status()
    update.message.reply_text(f'{message}')

def button(update: Update, context: CallbackContext):
    with open("config.json") as jsonfile:
        config = json.load(jsonfile)
    query = update.callback_query
    query.answer()
    if query.data == str("status"):
        get_status(config["rig_url"], update)

if __name__ == "__main__":
    main()
