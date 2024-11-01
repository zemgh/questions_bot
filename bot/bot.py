import os

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

load_dotenv()
API_TOKEN = os.getenv('TELEGRAM_API_TOKEN')

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot=bot)