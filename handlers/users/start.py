from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher import FSMContext

from states.account_state import Register
from keyboards.default.button import phone_knopic,profile_button
from states.games import Game
from loader import dp
from .functions import register, check,select_user


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message, state:FSMContext):
    userid = message.from_user.id
    skt = check(userid)
    if skt:
        about = select_user(int(userid))
        loto = about['loto']
        if loto == 'true':
            msg = f"Salom {about['name']}\nSiznign lotoreya raqamingiz: {about['number']}"
            await message.answer(msg,reply_markup=profile_button)
            await Game.header.set()
        else:
            await message.answer(f"Salom {message.from_user.full_name}\
                \n/home ustiga bosing va botdan foydalaning")
            await Game.header.set()
        await state.update_data(user_id=userid)
    else:
        await message.answer(f"Salom {message.from_user.full_name}\
            \nIltimos ismingizni kiriting")
        await Register.name.set()


@dp.message_handler(state=Register.name)
async def NameGet(ms:types.Message, state:FSMContext):
    name = ms.text
    await state.update_data(ism=name)
    await ms.answer("📞 Telefon nomer kiriting yoki tugma ustiga bosing",reply_markup=phone_knopic)
    await Register.phone.set()


@dp.message_handler(content_types='contact',state=Register.phone)
@dp.message_handler(state=Register.phone)
async def PhoneGet(ms:types.Message, state:FSMContext):
    data = await state.get_data()
    uid = ms.from_user.id
    name = data.get('ism')
    if ms.contact:
        phone = ms.contact.phone_number
    else:
        phone = ms.text
    register(uid,name,phone)
    await ms.answer("Ro'yxatdan o'tish muvofaqiyatli tugadi\
        \n/home ustiga bosing va botdan foydalaning")
    await state.update_data(user_id=uid)
    await Game.header.set()



