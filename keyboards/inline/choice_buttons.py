from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

menu = InlineKeyboardMarkup(row_width=1,
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='Когда я дежурю',
                callback_data='when'
            )
        ],
        [
            InlineKeyboardButton(
                text='Кто сейчас дежурный',
                callback_data='who_now'
            )
        ],
        [
            InlineKeyboardButton(
                text='График разработчиков',
                callback_data='google_dev'
            )
        ],
        [
            InlineKeyboardButton(
                text='График 1 линия',
                callback_data='google_sup'
            )
        ],
        [
            InlineKeyboardButton(
                text='Отмена',
                callback_data='cancel'
            )
        ]
    ],
)

google_dev_keyboard = InlineKeyboardMarkup()
GOOGLE_DEV_LINK = "https://docs.google.com/spreadsheets/d/1_fJJ-1brnFaYjmwVouKnujxqlk_7yvN0l_vuMnTT8hM/edit#gid=614226428"
google_dev_link = InlineKeyboardButton(text='График тут', url=GOOGLE_DEV_LINK)
google_dev_keyboard.insert(google_dev_link)

google_sup_keyboard = InlineKeyboardMarkup()
GOOGLE_SUP_LINK = "https://docs.google.com/spreadsheets/d/1ow4emdGPrva66CP__TIc1IFGnLay-_ZSvL54fGOB1cY/edit#gid=614226428"
google_sup_link = InlineKeyboardButton(text='График тут', url=GOOGLE_SUP_LINK)
google_sup_keyboard.insert(google_sup_link)

google_time_keyboard = InlineKeyboardMarkup()
GOOGLE_WORK_LINK = "https://docs.google.com/spreadsheets/d/1EQVeV3LAqXPh7U24CBXmlpD9xt8n4B_nHMYDGgbs3HI/edit#gid=150891771"
google_work_link = InlineKeyboardButton(text='Файл тут', url=GOOGLE_WORK_LINK)
google_time_keyboard.insert(google_work_link)