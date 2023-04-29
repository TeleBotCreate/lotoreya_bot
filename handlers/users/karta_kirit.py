import asyncio
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext
from loader import dp, bot

from keyboards.inline.knopick import boshqalar
from keyboards.inline.pull import qancha_yechish
from states.games import *
from .functions import select_user, update_db

ADMIN = 1173831936



@dp.message_handler(state=PulYech.yech6)
async def Yech6Xona(ms:Message, state:FSMContext):
    data = await state.get_data()
    userid = int(data.get("user_id"))
    about = select_user(userid)
    user_puli = int(about['monney'])
    jami = user_puli - 6000
    update_db('monney',jami,userid)
    karta = ms.text
    username = about['name']
    uid = about['_id']
    xabar = "Pul yechish bo'yicha so'rov qabul qilindi ✅\
        \n24 soat ichida <b>kiritilgan raqamga</b> pul tushadi"
    admin_xabar = f"💰 PUL YECHISH SO'ROVI 💰\n\
        \n👤 User : {username}\
        \n💡 ID : {uid}\
        \n💸 Summa : 6000 so'm\
        \n💳 Karta : {karta}"
    await bot.send_message(chat_id=ADMIN, text=admin_xabar)
    await ms.answer(xabar,reply_markup=boshqalar)
    await Game.boshqas.set()

@dp.message_handler(state=PulYech.yech10)
async def Yech6Xona(ms:Message, state:FSMContext):
    data = await state.get_data()
    userid = int(data.get("user_id"))
    about = select_user(userid)
    user_puli = int(about['monney'])
    jami = user_puli - 10000
    update_db('monney',jami,userid)
    karta = ms.text
    username = about['name']
    uid = about['_id']
    xabar = "Pul yechish bo'yicha so'rov qabul qilindi ✅\
        \n24 soat ichida <b>kiritilgan raqamga</b> pul tushadi"
    admin_xabar = f"💰 PUL YECHISH SO'ROVI 💰\n\
        \n👤 User : {username}\
        \n💡 ID : {uid}\
        \n💸 Summa : 10 000 so'm\
        \n💳 Karta : {karta}"
    await bot.send_message(chat_id=ADMIN, text=admin_xabar)
    await ms.answer(xabar,reply_markup=boshqalar)
    await Game.boshqas.set()


@dp.message_handler(state=PulYech.yech15)
async def Yech6Xona(ms:Message, state:FSMContext):
    data = await state.get_data()
    userid = int(data.get("user_id"))
    about = select_user(userid)
    user_puli = int(about['monney'])
    jami = user_puli - 15000
    update_db('monney',jami,userid)
    karta = ms.text
    username = about['name']
    uid = about['_id']
    xabar = "Pul yechish bo'yicha so'rov qabul qilindi ✅\
        \n24 soat ichida <b>kiritilgan raqamga</b> pul tushadi"
    admin_xabar = f"💰 PUL YECHISH SO'ROVI 💰\n\
        \n👤 User : {username}\
        \n💡 ID : {uid}\
        \n💸 Summa : 15 000 so'm\
        \n💳 Karta : {karta}"
    await bot.send_message(chat_id=ADMIN, text=admin_xabar)
    await ms.answer(xabar,reply_markup=boshqalar)
    await Game.boshqas.set()



@dp.message_handler(state=PulYech.yech20)
async def Yech6Xona(ms:Message, state:FSMContext):
    data = await state.get_data()
    userid = int(data.get("user_id"))
    about = select_user(userid)
    user_puli = int(about['monney'])
    jami = user_puli - 20000
    update_db('monney',jami,userid)
    karta = ms.text
    username = about['name']
    uid = about['_id']
    xabar = "Pul yechish bo'yicha so'rov qabul qilindi ✅\
        \n24 soat ichida <b>kiritilgan raqamga</b> pul tushadi"
    admin_xabar = f"💰 PUL YECHISH SO'ROVI 💰\n\
        \n👤 User : {username}\
        \n💡 ID : {uid}\
        \n💸 Summa : 20 000 so'm\
        \n💳 Karta : {karta}"
    await bot.send_message(chat_id=ADMIN, text=admin_xabar)
    await ms.answer(xabar,reply_markup=boshqalar)
    await Game.boshqas.set()