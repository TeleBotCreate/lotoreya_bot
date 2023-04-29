from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

qancha_yechish = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("6000 so'm",callback_data='s6000'),
            InlineKeyboardButton("10 000 so'm",callback_data='s10000'),
        ],
        [
            InlineKeyboardButton("15 000 so'm",callback_data='s15000'),
            InlineKeyboardButton("20 000 so'm",callback_data='s20000'),
        ],
        [
            InlineKeyboardButton("👈 Orqaga qaytish",callback_data='orqaga')
        ]
    ]
)


buyumlar_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("1 ta 🏆 = 50 000 so'm",callback_data='kubog1'),
            InlineKeyboardButton("5 ta 🏆 = 250 000 so'm",callback_data='kubog5'),
        ],
        [
            InlineKeyboardButton("1 ta ⚽ = 3000 so'm",callback_data="ball1"),
            InlineKeyboardButton("5 ta ⚽ = 15 000 so'm",callback_data="ball5"),
        ],
        [
            InlineKeyboardButton("1 ta 💎 = 1500 so'm",callback_data='gems1'),
            InlineKeyboardButton("5 ta 💎 = 7500 so'm",callback_data='gems5'),
        ],
        [
            InlineKeyboardButton("🔙 Orqaga qaytish 👈", callback_data='orqaga')
        ]
    ]
)


