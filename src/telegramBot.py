from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from price import get_price
import os

def main():
    TOKEN = os.getenv('TOKEN')
    updater = Updater(token=TOKEN, use_context=True)
    updater.dispatcher.add_handler(CommandHandler('start',start))
    updater.dispatcher.add_handler(CommandHandler('price',price))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))
    # Start the bot
    updater.start_polling()
    # Run until the user stop the bot
    updater.idle()

def price(update, context):
    keyboard = [
        [
            InlineKeyboardButton("BTC", callback_data="BTC"),
            InlineKeyboardButton("ETH", callback_data="ETH"),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Please choose:', reply_markup=reply_markup)


def start(update, context):
    update.message.reply_text('Hi Rodri, I\'m here to help you')

def button(update, context):
    query = update.callback_query
    query.answer()
    if query.data == str("BTC"):
        price = get_price('bitcoin')
    if query.data == str("ETH"):
        price = get_price('ethereum')
    query.edit_message_text(text=f"The current price of {query.data} is {price}U$D")

if __name__ == "__main__":
    main()
