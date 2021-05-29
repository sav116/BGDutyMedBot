from aiogram import executor

#from . .func.worker import update_docs
from BGDutyMedBot.func.worker import update_docs
from BGDutyMedBot import loader
#import middlewares, filters, handlers
from BGDutyMedBot.utils import notify_admins
from BGDutyMedBot.utils.set_bot_commands import set_default_commands
import threading

async def on_startup(dispatcher):
    # Устанавливаем дефолтные команды
    await set_default_commands(dispatcher)

    # Уведомляет про запуск
    await notify_admins.on_startup_notify(dispatcher)


if __name__ == '__main__':
    _update_doc = threading.Thread(target=update_docs)
    _update_doc.start()
    executor.start_polling(loader.dp, on_startup=on_startup)
