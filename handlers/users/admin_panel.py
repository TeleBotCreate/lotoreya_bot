from aiogram.types import Message, CallbackQuery
from loader import dp, bot

from .functions import *
from states.games import Game,Latareya, AdminState
from keyboards.inline.knopick import boshlash, davom_etish
from keyboards.default.button import profile_button

ADMIN = 1173831936

@dp.message_handler(text="elon",user_id=ADMIN)
@dp.message_handler(text="elon",state=Game.all_states_names,user_id=ADMIN)
@dp.message_handler(text="elon",state=Latareya.all_states_names,user_id=ADMIN)
@dp.message_handler(text="elon",state=AdminState.all_states_names,user_id=ADMIN)
async def ElonXona(ms:Message):
    user = elon()
    reklama = ms.reply_to_message.text
    await ms.delete()
    for el in user:
        try:
            await bot.send_message(chat_id=el['_id'],text=reklama)
        except:
            pass
    await ms.answer("📜 E'lon tugadi")


@dp.message_handler(text="game start",state=Game.all_states_names,user_id=ADMIN)
@dp.message_handler(text="game start",state=Latareya.all_states_names,user_id=ADMIN)
async def AdminStartGame(ms:Message):
    xabar = "Rostanham o'yinni boshlaysizmi ❓"
    game_update('game_status','true',1)
    await ms.answer(xabar,reply_markup=boshlash)
    await AdminState.boshlandi.set()



@dp.callback_query_handler(text='start',state=AdminState.boshlandi,user_id=ADMIN)
@dp.callback_query_handler(text='again',state=AdminState.boshlandi,user_id=ADMIN)
async def BoshlandiXona(call:CallbackQuery):
    about = game_info()['count']
    raqam = int(about) + 1
    xabar = f"{raqam} - sovg'aga nima qo'yiladi "
    game_update('count',raqam,1)
    await call.message.answer(xabar)
    await call.message.delete()
    await AdminState.yutuq.set()


@dp.message_handler(state=AdminState.yutuq)
async def Yutuqxaon(ms:Message):
    msg = ms.text
    yutuq = msg.split(',')
    nimaligi = yutuq[0]
    nechtaligi = int(yutuq[1])
    omadli_raqam = random_user_number()
    omadli_user = user_number(omadli_raqam)['name']
    golib = f"🎉 Tabriklayman sizni {omadli_user.title()} 🎉\
        \n🎰 Sizning lotoreya raqamingiz omadli chiqadi\
        \n✅ Siz {nechtaligi} {nimaligi} yutib oldingiz"

    user = int(user_number(omadli_raqam)['_id'])
    update_db('loto','false',user)
    update_db('number',0,user)

    if nimaligi == "kumush":
        user_gems = int(select_user(user)['gems'])
        all_gems = user_gems + int(nechtaligi)
        update_db('gems', all_gems, user)
    elif nimaligi == 'pul':
        bor_puli = int(select_user(user)['monney'])
        update_db('monney',int(nechtaligi)+bor_puli,user)
    elif nimaligi == "koptog":
        bor_ball = int(select_user(user)['ball'])
        all_ball = bor_ball + int(nechtaligi)
        update_db('ball', all_ball, user)
    elif nimaligi == "kubog":
        bor_kubog = int(select_user(user)['kubog'])
        all_kubog = bor_kubog + int(nechtaligi)
        update_db('kubog', all_kubog, user)
    await ms.answer(f"🎉 Lotoreya raqami: {omadli_raqam}\
        \n✨ Raqam egasi: {omadli_user}\
        \n🎁 Yutuq: {nechtaligi} {nimaligi}", reply_markup=davom_etish)
    await bot.send_message(chat_id=user,text=golib)
    await AdminState.boshlandi.set()



@dp.callback_query_handler(text="stop",state=AdminState.boshlandi)
async def StopXona(call:CallbackQuery):
    await call.message.answer("Asosiy Menyu",reply_markup=profile_button)
    await call.message.delete()
    await Game.header.set()

@dp.callback_query_handler(text="otmena",state=AdminState.boshlandi, user_id=ADMIN)
async def OtmenaXona(call:CallbackQuery):
    await call.message.delete()
    await call.message.answer("Asosiy menyu da siz", reply_markup=profile_button)
    await Game.header.set()






