from aiogram.types import  ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text="Tilni sozlash")
        ],
    ],
    resize_keyboard=True
)
