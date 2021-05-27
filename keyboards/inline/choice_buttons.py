from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

menu = InlineKeyboardMarkup(row_width=2,
                            inline_keyboard=[
                                [
                                    InlineKeyboardButton(
                                        text="Когда я дежурный",
                                        callback_data="when"
                                    )
                                ],
                                    InlineKeyboardButton(
                                        text="Кто сейчас дежурный",
                                        callback_data="who_now"
                                ),
                                    InlineKeyboardButton(
                                        text="График разработчиков",
                                        callback_data="google_dev"
                                    ),
                                    InlineKeyboardButton(
                                        text="Грфик 1 линия",
                                        callback_data="google_support"
                                    ),
                                    InlineKeyboardButton(
                                        text="Отмена",
                                        callback_data="cancel"
                                    )
                            ])