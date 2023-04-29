from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

profile_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('🎲 Lotoreya olish'),
            KeyboardButton("💰 Hisob to'ldirish"),
        ],
        [
            KeyboardButton('🛒 Hisobim'),
            KeyboardButton("🛠 Boshqalar..."),
        ],
        [
            KeyboardButton("👇 O'yinga kirish")
        ]
    ],
    resize_keyboard=True,one_time_keyboard=True
)


phone_knopic = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("📞 Telefon raqam yuborish",request_contact=True)
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)
