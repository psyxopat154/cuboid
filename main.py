import os
import time

from telegram.ext import Updater, MessageHandler, Filters
import logging
import sys

TOKEN = os.getenv('TOKEN')
PORT = int(os.environ.get('PORT', '8443'))
APP_NAME = os.getenv('APP_NAME')

# STATUES = {
#     1: 'Бендера',
#     2: 'Либеральная собака',
#     3: 'Провокатор',
#     4: 'Коментатор из тырнета',
#     5: 'Росиянин',
#     6: 'Настоящий патриот'
# }

STATUES = {
    1: 'Дырявый',
    2: 'Сосал на вписке',
    3: 'Билюбознательный',
    4: 'Дрочит на гейпорно',
    5: 'Засомневался',
    6: 'Альфа'
}

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    stream=sys.stdout,
    level=logging.INFO,
)


def check_cube(update, context):
    value = update.message.dice.value
    chat = update.effective_chat
    name = update.message.from_user.first_name
    message = f'{name} - {STATUES[value]}'
    context.bot.send_message(
        chat_id=chat.id,
        text=message,
    )
    logging.info(message)


def main():
    updater = Updater(token=TOKEN, use_context=True)
    updater.dispatcher.add_handler(MessageHandler(Filters.dice, check_cube))
    time.sleep(1.5)
    updater.start_webhook(
         listen="0.0.0.0",
         port=PORT,
         url_path=TOKEN,
         webhook_url=f"https://{APP_NAME}.herokuapp.com/{TOKEN}"
    )
    updater.idle()


if __name__ == '__main__':
    main()
