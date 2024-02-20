import os
import telegram
from dotenv import load_dotenv


def uploading_photo(telegram_bot_token, chat_id):
    bot = telegram.Bot(token=telegram_bot_token)
    bot.send_document(chat_id=chat_id, document=open('C:/Users/user/Desktop/API-lesson4/nasa_epic/epic_1.png', 'rb'))


if __name__ == '__main__':
    load_dotenv()
    telegram_bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
    chat_id = os.getenv('CHAT_ID')
    uploading_photo(telegram_bot_token, chat_id)
