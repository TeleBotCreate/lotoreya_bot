import asyncio
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery
from loader import dp, bot

from .functions import select_user, game_info
from states.games import Game, Latareya
from keyboards.inline.knopick import inline_news, bekor_qilish, orqaga,boshqalar
from keyboards.default.button import profile_button
ADMIN = 1173831936


@dp.message_handler(commands='home',state=Game.header)
async def ProfileSet(ms:Message, state:FSMContext):
    date = await state.get_data()
    userid = int(date.get('user_id'))
    about = select_user(userid)
    loto = about['loto']
    if loto == 'true':
        xabar = f"Asosiy menyu\
            \nSiznign lotoreya raqamingiz: {about['number']}"
        await ms.answer(xabar,reply_markup=profile_button)
    else:
        batafsil = f"Salom 👋 <b>{about['name'].title()}</b>\
            \n🤖 Bu bot orqali lotoreya o'yinlari bo'lib o'tadi \
            \n🤑 Siz ham o'yinda qatnashib omadingizni sinab ko'ring"
        await ms.answer(batafsil,reply_markup=profile_button)
    await Game.header.set()


@dp.message_handler(text="🛒 Hisobim",state=Game.header)
async def HisobimXona(ms:Message, state:FSMContext):
    data = await state.get_data()
    user_id = int(data.get('user_id'))
    info = select_user(user_id)
    about = f"💰   <b>Sizning hisobingiz</b>\n\
        \n💸 Pullar: {info['monney']} so'm\
        \n💎 Kumushlar: {info['gems']} ta"
    await ms.answer(about,reply_markup=profile_button)


@dp.message_handler(text="🛠 Boshqalar...",state=Game.header)
async def BoshqalarXona(ms:Message):
    await ms.answer(f"Qo'shimcha sahifa\nID : <code>{ms.from_user.id}</code>",reply_markup=boshqalar)
    await Game.boshqas.set()






@dp.callback_query_handler(text="news",state=Game.boshqas)
async def YangilikNews(call:CallbackQuery):
    yangilik = game_info()['news']
    await call.message.answer(yangilik, reply_markup=inline_news)
    await call.message.delete()
    await Game.yangiliklar.set()

@dp.callback_query_handler(text='bask',state=Game.yangiliklar)
async def BavkXona(call:CallbackQuery, state:FSMContext):
    await call.message.delete()
    data = await state.get_data()
    userid = int(data.get('user_id'))
    about = select_user(userid)
    lotos = about['loto']
    if lotos == 'true':
        xabar = f"Asosiy menyuda siz\nLotoreya raqamingiz: {about['number']}"
    else:
        xabar = "Asosiy menyuda siz\nLatareya sotib oling va o'yinlarda ishtirok eting"
    await call.message.answer(xabar,reply_markup=profile_button)
    await Game.header.set()


@dp.callback_query_handler(text="quiz",state=Game.yangiliklar)
async def SavolXona(call:CallbackQuery):
    await call.message.answer("👤 Savolingizni yozib qoldirishingiz mumkin ",reply_markup=bekor_qilish)
    await call.message.delete()
    await Game.savollar.set()

@dp.message_handler(state=Game.savollar)
async def BootXone(ms:Message):
    savol = ms.text
    quiz = f"Savoll\n\n<b>{savol}</b>\n{ms.from_user.full_name} ---> dan"
    await bot.send_message(chat_id=1173831936,text=quiz)
    await ms.answer("Savolingiz qabul qilindi ✅",reply_markup=profile_button)
    await Game.header.set()


@dp.callback_query_handler(text="bekor", state=Game.savollar)
async def BekorXoan(call:CallbackQuery):
    yangilik = game_info()['news']
    await call.message.answer(yangilik, reply_markup=inline_news)
    await call.message.delete()
    await Game.yangiliklar.set()




@dp.callback_query_handler(text="status",state=Game.boshqas)
async def StatusHome(call:CallbackQuery, state:FSMContext):
    data = await state.get_data()
    userid = int(data.get("user_id"))
    about = select_user(userid)
    lot_num = int(about['number'])
    if lot_num:
        xabar = f"👍 Lotoreya: {lot_num} --> active\n✅ O'yinda qatnasha olasiz"
    else:
        xabar = "Sizda lotoreya yo'q ❌\nLotoreya sotib oling va o'yinda qatnashing 👈 "
    balo = await call.message.answer(xabar)
    await asyncio.sleep(5)
    await balo.delete()


@dp.callback_query_handler(text="asosiy",state=Game.boshqas)
async def AsosiyMEnyu(call:CallbackQuery):
    await call.message.answer("⚙ Asosiy menyu",reply_markup=profile_button)
    await call.message.delete()
    await Game.header.set()








@dp.message_handler(text="👇 O'yinga kirish",state=Game.header)
async def KirishXona(ms:Message, state:FSMContext):
    info = game_info()['game_status']
    data = await state.get_data()
    userid = int(data.get('user_id'))
    if info == 'true':
        about = select_user(userid)
        user_number = about['number']
        xabar = f"✅ O'yin boshlangan 👍\n\
            \nO'yinda yozish mumkin\
            \nChiqish uchun \"Quit\" deb yozing"
        await ms.answer(xabar,reply_markup=orqaga)
        await Latareya.uyin_holati.set()
    else:
        msg = "Hozir o'yin to'xtatilgan\nO'yin Boshlansa sizga botdan xabar keladi"
        await ms.answer(msg)

@dp.message_handler(state=Latareya.uyin_holati)
async def AllChats(ms:Message):
    xabar = ms.text
    stops = ['Quit','quit']
    if xabar in stops:
        message = "Asosiy menyu da siz"
        await ms.answer(message,reply_markup=profile_button)
        await Game.header.set()
    else:
        user = ms.from_user.full_name
        about = f"<b>{xabar}</b>\n\n{user} --> dan"
        await bot.send_message(chat_id=ADMIN,text=about)

@dp.callback_query_handler(text="orqaga", state=Latareya.uyin_holati)
async def OrqagaXonas(call:CallbackQuery):
    await call.message.answer("Asosiy menyu da siz",reply_markup=profile_button)
    await call.message.delete()
    await Game.header.set()

