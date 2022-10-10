import os
import random
import time

from telegram.ext import Updater, MessageHandler, Filters
import logging
import sys

from values import VALUES
import statistic

SLEEP = 3
TOKEN = os.getenv('TOKEN')
PORT = int(os.environ.get('PORT', '8443'))
APP_NAME = os.getenv('APP_NAME')


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    stream=sys.stdout,
    level=logging.INFO,
)


def stats(chat):
    if chat.id not in statistic.CHATS:
        statistic.CHATS.append(chat.id)
        statistic.TOTAL_CHATS += 1
        logging.info(f'Добавлен новый чат. Всего {statistic.TOTAL_CHATS} чатов')
    else:
        logging.info(f'Всего чатов {statistic.TOTAL_CHATS} чатов')
        return None


def check_cube(update, context):
    time.sleep(SLEEP)
    value = update.message.dice.value
    chat = update.effective_chat
    name = update.message.from_user.first_name
    status = random.choice(VALUES[value])
    message = f'{name} - {status}'
    context.bot.send_message(
        chat_id=chat.id,
        text=message,
    )
    stats(chat)
    logging.info(f'{chat.id} - {name} - {status}')


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
