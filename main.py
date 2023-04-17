import constants as keys
from telegram.ext import *
import responses as R

print("Bot started...")


def start_command(update, context):
    update.message.reply_text("Hello Welcome to Smart Bot!\nType /help to know more about me!")


def help_command(update, context):
    update.message.reply_text("Enter 'orderfood' to order food\nEnter 'menu' to see the menu\nEnter 'time' to see the time\nEnter 'address \n [your address]' to update your address\nEnter 'who are you' to know more about me!")


def handle_message(update, context):
    text = str(update.message.text).lower()
    if text == "orderfood":
        update.message.reply_text(R.orderp())
    elif text == "menu":
        update.message.reply_text(R.menu())
    # elif text == "name":
    #     update.message.reply_text(R.name(text))
    elif "address" in text:
        update.message.reply_text(R.address(text.splitlines()[1]))
    elif "order" in text:
        update.message.reply_text(R.order(text.splitlines()[1:]))
    else:
        response = R.sample_responses(text)
        update.message.reply_text(response)


def error(update, context):
    print(f"Update {update} caused error {context.error}")


def main():
    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("start", help_command))

    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()

main()
