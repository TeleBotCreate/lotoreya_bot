from aiogram.types import Message, CallbackQuery
from loader import dp, bot

from .functions import *
from states.games import Game,Latareya, AdminState
from keyboards.inline.knopick import boshlash, davom_etish
from keyboards.default.button import profile_button
from .functions import game_over

ADMIN = 1173831936


@dp.message_handler(text="game over",state=AdminState.all_states_names,user_id=ADMIN)
async def GameOverHome(ms:Message):
    game_over() # O'yinni tugatuvchi funksiya
    
    await ms.answer("❌ O'yin tugatildi ❌",reply_markup=profile_button)
    await Game.header.set()



@dp.message_handler(text="news add",state=Game.all_states_names,user_id=ADMIN)
@dp.message_handler(text="news add",state=Latareya.all_states_names,user_id=ADMIN)
@dp.message_handler(text="news add",state=AdminState.all_states_names,user_id=ADMIN)
async def NewsAddHome(ms:Message):
    await ms.answer("Yangilikni kiritishigin mumkin ✅")
    await AdminState.news_add.set()

@dp.message_handler(state=AdminState.news_add)
async def AddNewsOk(ms:Message):
    game_update('news',ms.text,1)
    await ms.answer("Yangilik o'zgartirildi",reply_markup=profile_button)
    await Game.header.set()




@dp.message_handler(text="loto true",state=AdminState.all_states_names,user_id=ADMIN)
@dp.message_handler(text="loto true",state=Game.all_states_names,user_id=ADMIN)
async def LotoTrueXona(ms:Message):
    game_update('loto_status','true',1)
    await ms.answer("✅ Lotoreyalar sotuvga qo'yildi")

@dp.message_handler(text="loto false",state=AdminState.all_states_names,user_id=ADMIN)
@dp.message_handler(text="loto false",state=Game.all_states_names,user_id=ADMIN)
async def LotoTrueXona(ms:Message):
    game_update('loto_status','false',1)
    await ms.answer("⛔ Lotoreyalar sotuvi cheklandi")



@dp.message_handler(text=':update',user_id=ADMIN)
@dp.message_handler(text=':update',state=Game.all_states_names,user_id=ADMIN)
@dp.message_handler(text=':update',state=AdminState.all_states_names,user_id=ADMIN)
async def UpdateUserome(ms:Message):
    await ms.answer("✅ Update qilish uchun ruxsat\n📃 Misol : nimani/nimaga/id")
    await Game.update_user.set()

@dp.message_handler(state=Game.update_user)
async def UpdateOkUser(ms:Message):
    try:
        all_update = ms.text.split('/')
        nimani = all_update[0]
        nimaga = all_update[1]
        uid = all_update[2]
        update_db(nimani, nimaga, uid)
        xabar = "✅ Bazaga ✅ o'zgartirish ✅ kiritildi ✅"
    except:
        xabar = "Xato ❌ malumotlar ❌ kiritildi ❌"
    await ms.answer(xabar,reply_markup=profile_button)
    await Game.header.set()



@dp.message_handler(text='+pul',user_id=ADMIN)
@dp.message_handler(text='+pul',state=Game.all_states_names,user_id=ADMIN)
@dp.message_handler(text='+pul',state=AdminState.all_states_names,user_id=ADMIN)
async def PulPilusXona(ms:Message):
    await ms.answer("Kimga qancha pul qo'shasiz ❓\
        \n💡 Misol : 5000/id")
    await Game.pul_pilus.set()

@dp.message_handler(state=Game.pul_pilus)
async def PulLLLL(ms:Message):
    try:
        about = ms.text.split('/')
        summa = int(about[0])
        uid = int(about[1])
        user_puli = int(select_user(uid)['monney'])
        update_db('monney', user_puli+summa, uid)
        await ms.answer("✅ Pul qo'shildi",reply_markup=profile_button)
        await Game.header.set()
    except:
        await ms.answer("❌ Xato yuzaga keldi",reply_markup=profile_button)
        await Game.header.set()



