import asyncio
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery
from loader import dp

from .functions import select_user,update_db,random_son,number_yes_or_no
from states.games import Game,Latareya
from keyboards.inline.knopick import olish_button,orqaga,bosh_menyu
from keyboards.default.button import profile_button


@dp.message_handler(text="💰 Hisob to'ldirish",state=Game.header)
async def HisobHona(ms:Message):
    xabar = "Hisobingizni quyidagi karta raqam orqali to'ldiring\
        \nPul tushgach screenshot qilib botga yuboring\
        \nKarta: <code>4073 4200 4157 2854</code>\n\
        \n<b>2 - usul</b>\nAdmin bilan bog'lanib hisobni to'ldiring\
        \nAdmin: https://t.me/jake1309"
    await ms.answer(xabar,reply_markup=bosh_menyu,disable_web_page_preview=True)
    await Game.hisob_tuldir.set()


@dp.callback_query_handler(text="help",state=Game.hisob_tuldir)
async def HisopHelp(call:CallbackQuery):
    xabar = "👉 Bu muhim o'qib chiqing 👇\n\nUshbu karta raqamga qancha pul tashlasangiz hisobingizga shuncha pul tushadi\n\
        \n📃 <b>Asosiysi pulni tashlab bo'lib rasmini(screenshot qilib) botga jo'nating</b> va qancha tashlaganingizni rasm ostiga yozib qoldiring\n\
        \n<b>Karta: <code>4073420041572854</code></b>\
        \nMurojat uchun: @Bot_creatorN1"
    await call.message.answer(xabar,reply_markup=bosh_menyu)
    await call.message.delete()

@dp.callback_query_handler(text="nazat",state=Game.hisob_tuldir)
async def NazatXona(call:CallbackQuery, state:FSMContext):
    date = await state.get_data()
    userid = int(date.get('user_id'))
    about = select_user(userid)
    loto = about['loto']
    if loto == 'true':
        xabar = f"Asosiy menyu\
            \nSiznign lotoreya raqamingiz: {about['number']}"
        await call.message.answer(xabar,reply_markup=profile_button)
    else:
        batafsil = f"Salom 👋 <b>{about['name'].title()}</b>\
            \n🤖 Bu bot orqali lotoreya o'yinlari bo'lib o'tadi \
            \n🤑 Siz ham o'yinda qatnashib omadingizni sinab ko'ring"
        await call.message.answer(batafsil,reply_markup=profile_button)
    await call.message.delete()
    await Game.header.set()


