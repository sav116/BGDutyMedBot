from aiogram import types
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import ReplyKeyboardRemove

from keyboards.inline.choice_buttons import menu
from loader import dp

@dp.message_handler(Command("menu"))
async def show_menu(message: types.Message):
    await message.answer("Выберите команду из меню ниже", reply_markup=menu)

@dp.message_handler(Text(equals=["Когда я дежурю", "Кто сейчас дежурный"]))
async def get_command(message: types.Message):
    await message.answer(f"Вы выбрали: {message.text}", reply_markup=ReplyKeyboardRemove())

