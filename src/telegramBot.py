import json
from apscheduler.schedulers.background import BackgroundScheduler
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from aux_functions import verify_status
import logging

def main():

    with open("config.json") as jsonfile:
        config = json.load(jsonfile)
    logging.basicConfig()
    logging.getLogger('apscheduler').setLevel(logging.DEBUG)
    token = config["telegram_token"]
    updater = Updater(token=token, use_context=True)
    scheduler = BackgroundScheduler()
    scheduler.start()
    scheduler.add_job(verify_status,'interval', seconds=20, args=(updater,config["rig_url"],float(config["min_hashrate"]),float(config["raw_hashrate"])))
    updater.dispatcher.add_handler(CommandHandler('start',start))
#    updater.dispatcher.add_handler(CallbackQueryHandler(button))
    # Start the bot
    updater.start_polling()
    # Run until the user stop the bot
    updater.idle()


def start(update, context):
    update.message.reply_text('Hi Rodri, I\'m here to help you')

#def button(update, context):
#    query = update.callback_query
#    query.answer()
#    if query.data == str("BTC"):
#        price = get_price('bitcoin')
#    if query.data == str("ETH"):
#        price = get_price('ethereum')
#    query.edit_message_text(text=f"The current price of {query.data} is {price}U$D")

if __name__ == "__main__":
    main()
