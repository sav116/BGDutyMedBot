from aiogram import types
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import ReplyKeyboardRemove, CallbackQuery
import datetime, pprint

from func.base import working_day
from func.when import get_when
from keyboards.inline.choice_buttons import menu, google_dev_keyboard, google_sup_keyboard, google_time_keyboard
from loader import dp


@dp.message_handler(Command("menu"))
async def show_menu(message: types.Message):
    await message.answer("Выберите команду из меню ниже:", reply_markup=menu)

@dp.callback_query_handler(text='when')
async def when(call: CallbackQuery):
    answer = get_when(call['from']['username'])
    #answer = get_when('RomanRudnyh')
    if answer is None:
        await call.answer('Вы не дежурите в этом месяце')
    else:
        await call.message.answer(text=answer)

@dp.callback_query_handler(text='who_now')
async def who_duty(call: CallbackQuery):
    if working_day():
        await call.answer(cache_time=60)
        await call.message.answer('В рабочее время смотри ответственного за распределение неотложек внутри команды в этом файле.',reply_markup=google_time_keyboard)
    else:
        await call.message.answer(text="В нерабочее время функция еще не реализована")

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