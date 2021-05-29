from aiogram import types

from ...loader import dp


@dp.message_handler(content_types=types.ContentType.NEW_CHAT_MEMBERS)
async def new_member(message: types.Message):
    await message.reply(f"Привет, {message.new_chat_members[0].full_name}!")
