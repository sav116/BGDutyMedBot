from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
        KeyboardButton(text="Когда я дежурю"),
        KeyboardButton(text="Кто сейчас дежурный"),
        ],
    ],
    resize_keyboard=True
)