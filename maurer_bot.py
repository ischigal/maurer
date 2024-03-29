import telegram  # make sure that python-telegram-bot 12 or newer is installed 
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import threading

key = open("botkey.txt").readlines()[0].strip()
DEVID = int(open("botkey.txt").readlines()[1].strip()) 


# Enable logging #TODO how does this work and what does it do?
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
	"""Send a message when the command /start is issued."""
	update.message.reply_text('Hi!') 

def help(update, context):
	"""Send a message when the command /help is issued."""
	
	update.message.reply_text('HELP')

def error(update, context):
	"""Log Errors caused by Updates."""
	logger.warning('Update "%s" caused error "%s"', update, context.error)
	#TODO find out how this works

def main():
	"""Start the bot."""
	# Create the Updater and pass it your bot's token.
	# Make sure to set use_context=True to use the new context based callbacks
	# Post version 12 this will no longer be necessary
	updater = Updater(key, use_context=True)

	# Get the dispatcher to register handlers
	dp = updater.dispatcher

	# on different commands - answer in Telegram
	dp.add_handler(CommandHandler("start", start))
	dp.add_handler(CommandHandler("help", help))
	
	# on noncommand - send help info:
	dp.add_handler(MessageHandler(Filters.text, help))  #does not trigger on typos in commands e.g. /tomorow

	# log all errors
	dp.add_error_handler(error)

	# Start the Bot
	updater.start_polling()

	# Run the bot until you press Ctrl-C or the process receives SIGINT,
	# SIGTERM or SIGABRT. This should be used most of the time, since
	# start_polling() is non-blocking and will stop the bot gracefully.
	updater.idle()

if __name__ == '__main__':
	main()
