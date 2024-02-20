import os
import telegram
from dotenv import load_dotenv


load_dotenv()
bot = telegram.Bot(token=os.getenv('TELEGRAM_BOT_TOKEN'))
bot.send_message(text="Hi! I'm a bot", chat_id=os.getenv('CHAT_ID'))
