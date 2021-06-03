from aiogram import types
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import ReplyKeyboardRemove, CallbackQuery

from func.base import working_day_sup, working_day_dev, vladivostoc_time_sup
from func.when import get_when
from func.who import who_duty_sup
from keyboards.inline.choice_buttons import menu, google_dev_keyboard, google_sup_keyboard, google_time_keyboard
from loader import dp


@dp.message_handler(Command("menu"))
async def show_menu(message: types.Message):
    await message.answer("Выберите команду из меню ниже:", reply_markup=menu)

@dp.callback_query_handler(text='who_now_sup')
async def who_duty(call: CallbackQuery):
    if working_day_sup():
        await call.answer(cache_time=60)
        await call.message.answer('В рабочее время смотри ответственного за распределение неотложек внутри команды в этом файле.',reply_markup=google_time_keyboard)
    elif vladivostoc_time_sup():
        await call.answer(cache_time=60)
        await call.message.answer(text="Нет дежурных. Рабочее время Владивостока")
    else:
        # answer = who_duty_dev()
        answer = who_duty_sup()
        await call.message.answer(text=answer)

@dp.callback_query_handler(text='who_now_dev')
async def who_duty(call: CallbackQuery):
    if working_day_dev():
        await call.answer(cache_time=60)
        await call.message.answer('В рабочее время смотри ответственного за распределение неотложек внутри команды в этом файле.',reply_markup=google_time_keyboard)
    else:
        # answer =
        await call.message.answer(text="В нерабочее время функция еще не реализована")

@dp.callback_query_handler(text='when')
async def when(call: CallbackQuery):
    answer = get_when(call['from']['username'])
    #answer = get_when('abyanov')
    if answer is None:
        await call.answer('Вы не дежурите в этом месяце')
    else:
        await call.message.answer(text=answer)

@dp.callback_query_handler(text='cancel')
async def cancel(call: CallbackQuery):
    await call.message.edit_reply_markup()

@dp.callback_query_handler(text='google_dev')
async def cancel(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer('Вы выбрали график дежурств разработчиков', reply_markup=google_dev_keyboard)

@dp.callback_query_handler(text='google_sup')
async def cancel(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer('Вы выбрали график дежурств 1 линии', reply_markup=google_sup_keyboard)