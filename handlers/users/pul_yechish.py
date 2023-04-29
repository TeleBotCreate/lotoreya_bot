import asyncio
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext
from loader import dp, bot

from keyboards.inline.knopick import boshqalar
from keyboards.inline.pull import qancha_yechish
from states.games import *
from .functions import select_user, update_db


@dp.callback_query_handler(text="yechish",state=Game.boshqas)
async def YechishXona(call:CallbackQuery, state:FSMContext):
    data = await state.get_data()
    userid = int(data.get("user_id"))
    user_puli = select_user(userid)['monney']
    xabar = f"💰 Qancha pul yechasiz ❓\
        \n💳 Hisobingizda: {user_puli} so'm bor"
    await call.message.answer(xabar, reply_markup=qancha_yechish)
    await call.message.delete()
    await PulYech.bosh_holat.set()


@dp.callback_query_handler(text="orqaga",state=PulYech.bosh_holat)
async def OrKhaxona(call:CallbackQuery):
    await call.message.answer("Qo'shimcha sahifa",reply_markup=boshqalar)
    await call.message.delete()
    await Game.boshqas.set()






@dp.callback_query_handler(text="s6000",state=PulYech.bosh_holat)
async def S6000sum(call:CallbackQuery, state:FSMContext):
    data = await state.get_data()
    userid = int(data.get("user_id"))
    about = select_user(userid)
    pull = int(about['monney'])
    
    if pull >= 6000:
        await call.message.delete()
        xabar = "Karta raqam yoki telefon nomer kiriting\
            \nPul kiritilgan nomerga tushadi ✅"
        await call.message.answer(xabar)
        await PulYech.yech6.set()
    else:
        balo = await call.message.answer("❌ Sizning hisobingizda mablag' yetarli emas")
        await asyncio.sleep(3)
        await balo.delete()


@dp.callback_query_handler(text="s10000",state=PulYech.bosh_holat)
async def S6000sum(call:CallbackQuery, state:FSMContext):
    data = await state.get_data()
    userid = int(data.get("user_id"))
    about = select_user(userid)
    pull = int(about['monney'])
    
    if pull >= 10000:
        await call.message.delete()
        xabar = "Karta raqam yoki telefon nomer kiriting\
            \nPul kiritilgan nomerga tushadi ✅"
        await call.message.answer(xabar)
        await PulYech.yech10.set()
    else:
        balo = await call.message.answer("❌ Sizning hisobingizda mablag' yetarli emas")
        await asyncio.sleep(3)
        await balo.delete()


@dp.callback_query_handler(text="s15000",state=PulYech.bosh_holat)
async def S6000sum(call:CallbackQuery, state:FSMContext):
    data = await state.get_data()
    userid = int(data.get("user_id"))
    about = select_user(userid)
    pull = int(about['monney'])
    
    if pull >= 15000:
        await call.message.delete()
        xabar = "Karta raqam yoki telefon nomer kiriting\
            \nPul kiritilgan nomerga tushadi ✅"
        await call.message.answer(xabar)
        await PulYech.yech15.set()
    else:
        balo = await call.message.answer("❌ Sizning hisobingizda mablag' yetarli emas")
        await asyncio.sleep(3)
        await balo.delete()


@dp.callback_query_handler(text="s20000",state=PulYech.bosh_holat)
async def S6000sum(call:CallbackQuery, state:FSMContext):
    data = await state.get_data()
    userid = int(data.get("user_id"))
    about = select_user(userid)
    pull = int(about['monney'])
    
    if pull >= 20000:
        await call.message.delete()
        xabar = "Karta raqam yoki telefon nomer kiriting\
            \nPul kiritilgan nomerga tushadi ✅"
        await call.message.answer(xabar)
        await PulYech.yech20.set()
    else:
        balo = await call.message.answer("❌ Sizning hisobingizda mablag' yetarli emas")
        await asyncio.sleep(3)
        await balo.delete()
