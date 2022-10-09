import os
from telegram.ext import Updater, MessageHandler, Filters
import logging
import sys

TOKEN = '5687710657:AAE1F5rCmWWllLF_ALq-ccJg9qqohhseQqQ'
PORT = int(os.environ.get('PORT', '8443'))
APP_URL = 'cubeoid'

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
    name = update.message.chat.first_name
    context.bot.send_message(
        chat_id=chat.id,
        text=f'{name} - {STATUES[value]}',
    )


def main():
    updater = Updater(token=TOKEN, use_context=True)
    updater.dispatcher.add_handler(MessageHandler(Filters.dice, check_cube))
    updater.start_webhook(
        listen="0.0.0.0",
        port=PORT,
        url_path=TOKEN,
        webhook_url=f"https://{APP_URL}.herokuapp.com/{TOKEN}"
    )
    updater.idle()


if __name__ == '__main__':
    main()

