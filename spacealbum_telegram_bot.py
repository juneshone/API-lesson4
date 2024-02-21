import argparse
import os
import random
import telegram
import time
from dotenv import load_dotenv


def upload_selected_photo(bot_token, chat_id, filename):
    bot = telegram.Bot(token=bot_token)
    document = open(f'images/{filename}', 'rb')
    bot.send_document(chat_id=chat_id, document=document)


def upload_random_photo(bot_token, chat_id, interval):
    while True:
        for root, dirs, file in os.walk('images/'):
            filename = random.choice(file)
            bot = telegram.Bot(token=bot_token)
            document = open(f'images/{filename}', 'rb')
            bot.send_document(chat_id=chat_id, document=document)
            time.sleep(interval)


if __name__ == '__main__':
    load_dotenv()
    bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
    parser = argparse.ArgumentParser(
        description='Публикация фотографий в Telegram чате'
    )
    parser.add_argument("--chat_id", help='Cсылка на чат, например, @chatChat')
    parser.add_argument("--interval",
                        type=int,
                        default=14400,
                        help='Частота публикаций')
    parser.add_argument("--filename", help='Выбор определенной фотографии')
    args = parser.parse_args()
    if args.filename:
        upload_selected_photo(bot_token, args.chat_id, args.filename)
    else:
        interval = int(os.getenv('PUBLICATION_INTERVAL'))
        if not interval:
            interval = args.interval
        upload_random_photo(bot_token, args.chat_id, interval)
