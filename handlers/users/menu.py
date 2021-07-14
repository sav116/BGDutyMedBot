import sys

from aiogram import types
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import ReplyKeyboardRemove, CallbackQuery

from data.config import ADMINS
from func.base import working_day_sup, working_day_dev, vladivostoc_time_sup, day_off, day_off_dev
from func.when import get_when
from func.who import who_duty_sup_weekday, who_duty_sup_dayoff, who_duty_dev
from keyboards.inline.choice_buttons import menu, google_dev_keyboard, google_sup_keyboard, google_time_keyboard_sup, google_time_keyboard_dev
from loader import dp
import os


@dp.message_handler(Command("menu"))
async def show_menu(message: types.Message):
    await message.answer("Выберите команду из меню ниже:", reply_markup=menu)


<<<<<<< HEAD
@dp.message_handler(Command("update"))
async def close(message: types.Message):
    os.system('supervisorctl restart telebot')

=======
# @dp.message_handler(Command("update"))
# async def update():
#     await sys.exit()
>>>>>>> 80fad2f571092d1f9eb6d734345c74fd15bd7619

@dp.callback_query_handler(text='who_now_sup')
async def who_duty(call: CallbackQuery):
    if day_off():
        answer = who_duty_sup_dayoff()
        await call.message.answer(text=answer)
    elif working_day_sup():
        await call.answer(cache_time=60)
        await call.message.answer(
            'В рабочее время смотри ответственного за распределение неотложек внутри команды в этом файле.',
            reply_markup=google_time_keyboard_sup)
    elif vladivostoc_time_sup():
        await call.answer(cache_time=60)
        await call.message.answer(text="Нет дежурных. Рабочее время Владивостока")
    else:
        answer = who_duty_sup_weekday()
        await call.message.answer(text=answer)


@dp.callback_query_handler(text='who_now_dev')
async def who_duty(call: CallbackQuery):
    if working_day_dev():
        await call.answer(cache_time=60)
        await call.message.answer(
            'В рабочее время смотри ответственного за распределение неотложек внутри команды в этом файле.',
            reply_markup=google_time_keyboard_dev)
    elif day_off_dev():
        await call.answer(cache_time=60)
        await call.message.answer(text="Выходные дни у 3 линии дежурств нет")
    else:
        answer = who_duty_dev()
        await call.message.answer(text=answer)


@dp.callback_query_handler(text='when')
async def when(call: CallbackQuery):
    answer = get_when(call['from']['username'])
    #answer = get_when('proff9vad')
    if answer is None:
        await call.answer('Ваши дежурства не найдены')
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
