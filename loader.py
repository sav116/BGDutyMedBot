from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from data import config
from func.base import _download_docs

bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

GOOGLE_DEV, GOOGLE_SUP, DATA_DEV, DATA_SUP, GOOGLE_DEV_SHEET_CUR_MONTH, GOOGLE_DEV_SHEET_NEXT_MONTH, GOOGLE_SUP_SHEET_CUR_MONTH, GOOGLE_SUP_SHEET_NEXT_MONTH = _download_docs()
