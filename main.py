import os
import random
import time

from telegram.ext import Updater, MessageHandler, Filters
import logging
import sys

from values import VALUES

SLEEP = 3
TOKEN = os.getenv('TOKEN')
PORT = int(os.environ.get('PORT', '8443'))
APP_NAME = os.getenv('APP_NAME')


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    stream=sys.stdout,
    level=logging.INFO,
)


def check_cube(update, context):
    time.sleep(SLEEP)
    value = 10*update.message.dice.value
    ext = value + random.randrange(1, 9)
    chat = update.effective_chat
    name = update.message.from_user.first_name
    message = f'{name} - {VALUES[ext]}'
    context.bot.send_message(
        chat_id=chat.id,
        text=message,
    )
    logging.info(message)


def main():
    updater = Updater(token=TOKEN, use_context=True)
    updater.dispatcher.add_handler(MessageHandler(Filters.dice, check_cube))
    updater.start_webhook(
         listen="0.0.0.0",
         port=PORT,
         url_path=TOKEN,
         webhook_url=f"https://{APP_NAME}.herokuapp.com/{TOKEN}"
    )
    updater.idle()


if __name__ == '__main__':
    main()
