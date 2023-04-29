from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp
from states.games import *


@dp.message_handler(CommandHelp())
@dp.message_handler(CommandHelp(),state=Game.all_states_names)
@dp.message_handler(CommandHelp(),state=AdminState.all_states_names)
@dp.message_handler(CommandHelp(),state=PulYech.all_states_names)
async def bot_help(message: types.Message):
    text = ("Buyruqlar: ",
            "/start - Botni ishga tushirish",
            "/help - Yordam",
            f"💡 ID - <code>{message.from_user.id}</code>",
            "Admin - https://t.me/jake1309")
    
    await message.answer("\n".join(text),disable_web_page_preview=True)
