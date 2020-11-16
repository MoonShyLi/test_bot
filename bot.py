import logging
from datetime import datetime 
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import settings

logging.basicConfig(filename="bot.log", level=logging.INFO)

a = ["Alex", "Nat", "Bob", "Cat"] #test
#print(a);


def greet_user(update, context):
#	print(update)
	print("Start bot")
	update.message.reply_text('Say hello to Mother Russia')

def talk_to_me (update, context):
	text = update.message.text
	print(text)
	update.message.reply_text(text)

def main():
	mybot = Updater(settings.API_KEY, use_context=True)

	dp = mybot.dispatcher
	dp.add_handler(CommandHandler(a, greet_user))
	dp.add_handler(MessageHandler(Filters.text, talk_to_me))
	
	time_start = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
	logging.info(f"the bot has started {time_start}")
	mybot.start_polling()
	mybot.idle()

if __name__ == "__main__":
	main()
