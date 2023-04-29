from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

olish_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("🎲 Tasotifiy son",callback_data='random'),
            InlineKeyboardButton("🔍 Tanlab olish",callback_data='tanlab'),
        ],
        [
            InlineKeyboardButton("👈 Orqaga",callback_data='back')
        ]
        
    ]
)

orqaga = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("👈 orqaga qaytish",callback_data='orqaga')
        ]
    ]
)

bosh_menyu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("📃 Batafsil malumot",callback_data='help')
        ],
        [
            InlineKeyboardButton("🔙 Orqaga Qaytish 🔙", callback_data='nazat')
        ]
    ]
)

inline_news = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("📝 Savollar berish",callback_data='quiz'),
            InlineKeyboardButton("🔙 Orqaga",callback_data='bask')
        ]
    ]
)

bekor_qilish = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton("⛔ Bekor qilish", callback_data='bekor')
    ]]
)

boshlash = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton("O'yinni boshlash ✅",callback_data='start')
    ],[InlineKeyboardButton("Bekor qilish ❌", callback_data='otmena')]]
)

davom_etish = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("Yana aniqlash",callback_data='again')
        ],
        [
            InlineKeyboardButton("Bekor qilish",callback_data='stop')
        ]
    ]
)

boshqalar = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("🗞 Yangiliklar",callback_data='news'),
            InlineKeyboardButton("📊 Holat",callback_data='status'),
        ],
        [
            InlineKeyboardButton("💰 Pul Yechish",callback_data='yechish'),
            InlineKeyboardButton("👜 Buyumlar",callback_data='buyum')
        ],
        [
            InlineKeyboardButton("👈 Asosiy menyu",callback_data='asosiy')
        ]
    ]
)

