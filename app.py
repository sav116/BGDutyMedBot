import threading
import time

from aiogram import executor
import os

from loader import dp, DATA_DEV, DATA_SUP
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands


async def on_startup(dispatcher):
    # Устанавливаем дефолтные команды
    await set_default_commands(dispatcher)
    # Уведомляет про запуск
    await on_startup_notify(dispatcher)


def printer():
    # print configs
    print(f"DATA_DEV:\n{DATA_DEV}\n")
    print(f"DATA_SUP:\n{DATA_SUP}\n")


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
