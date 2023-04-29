import asyncio
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext
from loader import dp, bot

from keyboards.inline.knopick import boshqalar
from keyboards.inline.pull import qancha_yechish,buyumlar_btn
from states.games import *
from .functions import select_user, update_db


@dp.callback_query_handler(text="buyum",state=Game.boshqas)
async def YechishXona(call:CallbackQuery, state:FSMContext):
    userid = call.from_user.id
    about = select_user(userid)
    kubog = about['kubog']
    ball = about['ball']
    kumush = about['gems']
    info = f"👜 <b>Sizning buyumlaringiz</b> 👇\n\
        \n🏆 Kubog : {kubog} ta\n⚽ Koptog : {ball} ta\n💎 Kumush : {kumush} ta\n\
        \n<b>Buyumlarni pullarga almashtiring</b>"
    await call.message.answer(info,reply_markup=buyumlar_btn)
    await call.message.delete()
    await Buyumlar.asosiy.set()


@dp.callback_query_handler(text="orqaga",state=Buyumlar.asosiy)
async def Orqagasd(call:CallbackQuery):
    await call.message.answer("Qo'shimcha sahifa",reply_markup=boshqalar)
    await call.message.delete()
    await Game.boshqas.set()


# Kubog uchun handler 👇
# Kubog uchun handler  👇
@dp.callback_query_handler(text="kubog1",state=Buyumlar.asosiy)
async def Kubog1Xoan(call:CallbackQuery):
    userid = call.from_user.id
    about = select_user(userid)
    user_puli = int(about['monney'])
    kubog = int(about['kubog'])

    if kubog >= 1:
        update_db('kubog',kubog-1,userid)
        update_db('monney',user_puli+50000,userid)
        xabar = f"🏆 Kubog sotildi. Sizda {kubog-1} ta kubog qoldi ✅"
        vabo = await call.message.answer(xabar)
        await asyncio.sleep(5)
        await vabo.delete()
    else:
        balo = await call.message.answer("❌ Sizda bironta <b>Kubog</b> yo'q 😔")
        await asyncio.sleep(3)
        await balo.delete()


@dp.callback_query_handler(text="kubog5",state=Buyumlar.asosiy)
async def Kubog5Xona(call:CallbackQuery):
    userid = call.from_user.id
    about = select_user(userid)
    user_puli = int(about['monney'])
    kubog = int(about['kubog'])

    if kubog >= 5:
        update_db('kubog',kubog-5,userid)
        update_db('monney',user_puli+250000,userid)
        xabar = f"🏆 Kubog sotildi. Sizda {kubog-5} ta kubog qoldi ✅"
        vabo = await call.message.answer(xabar)
        await asyncio.sleep(5)
        await vabo.delete()
    else:
        balo = await call.message.answer("❌ Sizning <b>Kubogingiz</b> kamlik qilyapti 😔")
        await asyncio.sleep(3)
        await balo.delete()


# Ball uchun handler 👇
# Ball uchun handler  👇
@dp.callback_query_handler(text="ball1",state=Buyumlar.asosiy)
async def Koptog1Xona(call:CallbackQuery):
    userid = call.from_user.id
    about = select_user(userid)
    user_puli = int(about['monney'])
    kubog = int(about['ball'])

    if kubog >= 1:
        update_db('ball', kubog-1, userid)
        update_db('monney', user_puli+3000, userid)
        xabar = f"⚽ Koptok sotildi. Sizda {kubog-1} ta koptok qoldi ✅"
        vabo = await call.message.answer(xabar)
        await asyncio.sleep(5)
        await vabo.delete()
    else:
        balo = await call.message.answer("❌ Sizda bironta <b>Koptok</b> yo'q 😔")
        await asyncio.sleep(3)
        await balo.delete()


@dp.callback_query_handler(text="ball5",state=Buyumlar.asosiy)
async def Koptog5Xona(call:CallbackQuery):
    userid = call.from_user.id
    about = select_user(userid)
    user_puli = int(about['monney'])
    kubog = int(about['ball'])

    if kubog >= 5:
        update_db('ball', kubog-5, userid)
        update_db('monney',user_puli+15000, userid)
        xabar = f"⚽ Koptok sotildi. Sizda {kubog-5} ta koptok qoldi ✅"
        vabo = await call.message.answer(xabar)
        await asyncio.sleep(5)
        await vabo.delete()
    else:
        balo = await call.message.answer("❌ Sizda <b>Koptok</b> kamlik qilyapti 😔")
        await asyncio.sleep(3)
        await balo.delete()



# Kumush uchun handler 👇
# Kumush uchun handler  👇
@dp.callback_query_handler(text="gems1",state=Buyumlar.asosiy)
async def Gems1Xona(call:CallbackQuery):
    userid = call.from_user.id
    about = select_user(userid)
    user_puli = int(about['monney'])
    kubog = int(about['gems'])

    if kubog >= 1:
        update_db('gems',kubog-1,userid)
        update_db('monney',user_puli+1500,userid)
        xabar = f"💎 Kumush sotildi. Sizda {kubog-1} ta kumush qoldi ✅"
        vabo = await call.message.answer(xabar)
        await asyncio.sleep(5)
        await vabo.delete()
    else:
        balo = await call.message.answer("❌ Sizda bironta <b>Kumush</b> yo'q 😔")
        await asyncio.sleep(3)
        await balo.delete()


@dp.callback_query_handler(text="gems5",state=Buyumlar.asosiy)
async def Gems1Xona(call:CallbackQuery):
    userid = call.from_user.id
    about = select_user(userid)
    user_puli = int(about['monney'])
    kubog = int(about['gems'])

    if kubog >= 5:
        update_db('gems',kubog-5,userid)
        update_db('monney',user_puli+7500,userid)
        xabar = f"💎 5 ta Kumush sotildi. Sizda {kubog-5} ta kumush qoldi ✅"
        vabo = await call.message.answer(xabar)
        await asyncio.sleep(5)
        await vabo.delete()
    else:
        balo = await call.message.answer("❌ Sizda <b>Kumushlar</b> kamlik qilyapti 😔")
        await asyncio.sleep(3)
        await balo.delete()

