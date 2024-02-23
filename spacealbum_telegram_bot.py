import argparse
import os
import random
import telegram
import time
from dotenv import load_dotenv


def upload_selected_photo(chat_id, filename):
    with open(f'images/{filename}', 'rb') as document:
        bot.send_document(chat_id=chat_id, document=document)


def upload_random_photo(chat_id, interval):
    while True:
        for root, dirs, file in os.walk('images/'):
            filename = random.choice(file)
            with open(f'images/{filename}', 'rb') as document:
                bot.send_document(chat_id=chat_id, document=document)
                time.sleep(interval)


if __name__ == '__main__':
    load_dotenv()
    bot = telegram.Bot(token=os.getenv('TELEGRAM_BOT_TOKEN'))
    parser = argparse.ArgumentParser(
        description='Публикация фотографий в Telegram чате'
    )
    parser.add_argument("--chat_id", required=True, help='Cсылка на чат, например, @chatChat')
    parser.add_argument("--interval",
                        type=int,
                        default=14400,
                        help='Частота публикаций')
    parser.add_argument("--filename", help='Выбор определенной фотографии')
    args = parser.parse_args()
    if args.filename:
        upload_selected_photo(args.chat_id, args.filename)
    else:
        interval = int(os.getenv('PUBLICATION_INTERVAL'))
        if not interval:
            interval = args.interval
        upload_random_photo(args.chat_id, interval)
