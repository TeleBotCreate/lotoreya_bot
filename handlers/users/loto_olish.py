import asyncio
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery
from loader import dp

from .functions import (select_user,update_db,
                        random_son,number_yes_or_no,
                        game_update,game_info)
from states.games import Game,Latareya
from keyboards.inline.knopick import olish_button,orqaga
from keyboards.default.button import profile_button



@dp.message_handler(text="🎲 Lotoreya olish",state=Game.header)
async def HisobimXona(ms:Message,state:FSMContext):
    data = await state.get_data()
    userid = int(data.get('user_id'))
    status = select_user(userid)['loto']
    loto_status = game_info()['loto_status']
    if loto_status == "true":
        if status == 'true':
            await ms.answer("✅ Sizda allaqachan lotoreya mavjut")
        else:
            xabar = "Qanday usulda lotoreya olasiz ❓"
            await ms.answer(xabar, reply_markup=olish_button)
            await Latareya.asosiy.set()
    else:
        balo = await ms.answer("❌ Lotoreyalar hali sotuvga qo'yilmagan")
        await asyncio.sleep(3)
        await balo.delete()

@dp.callback_query_handler(text="back",state=Latareya.asosiy)
async def OrqaXona(call:CallbackQuery):
    xabar = "Asosiy menyu "
    await call.message.answer(xabar,reply_markup=profile_button)
    await call.message.delete()
    await Game.header.set()


## Random orqali olish uchun cod 👇
## Random orqali olish uchun cod  👇
@dp.callback_query_handler(text="random",state=Latareya.asosiy)
async def RandomLoto(call:CallbackQuery, state:FSMContext):
    data = await state.get_data()
    userid = int(data.get("user_id"))
    user_about = select_user(userid)
    pull = int(user_about['monney'])
    loto_narxi = 5000

    if pull >= loto_narxi:
        await call.message.delete()
        qolgan_pul = pull - loto_narxi
        olganlar = int(game_info()['olganlar']) + 1
        update_db('monney',qolgan_pul,userid)
        game_update('olganlar',olganlar,1)
        tasodif = random_son()
        xabar = f"Sizning lotoreya raqamingiz: <b>{tasodif}</b>"
        update_db('loto','true',userid)
        update_db('number',tasodif,userid)
        await call.message.answer(xabar,reply_markup=orqaga)
        await Latareya.random_kirish.set()
    else:
        balo = await call.message.answer(f"Kechirasiz sizning pulingiz yetrali emas 😔 \
            \nPulingiz <b>{loto_narxi-pull} so'm</b> kamlik qilyapti")
        await asyncio.sleep(5)
        await balo.delete()

@dp.callback_query_handler(text="orqaga",state=Latareya.random_kirish)
async def orqagaXonasi(call:CallbackQuery,state:FSMContext):
    await call.message.delete()
    data = await state.get_data()
    userid = data.get("user_id")
    loto_number = select_user(int(userid))['number']
    xabar = f"Asosiy menyu\nSizning <b>latareya raqam</b>ingiz: {loto_number}"
    await call.message.answer(xabar, reply_markup=profile_button)
    await Game.header.set()



## Tanlab olish uchun cod 👇
## Tanlab olish uchun cod  👇

@dp.callback_query_handler(text="tanlab",state=Latareya.asosiy)
async def TanlabOlish(call:CallbackQuery):
    xabar = "Qaysi raqamni olasiz ❓\nOlmoqchi bo'lgan raqamingizni kiriting"
    await call.message.answer(xabar)
    await call.message.delete()
    await Latareya.tanlab_ol.set()

@dp.message_handler(state=Latareya.tanlab_ol)
async def TanlaKirit(ms:Message, state:FSMContext):
    data = await state.get_data()
    userid = int(data.get('user_id'))
    about = select_user(userid)
    loto_narxi = 5000
    pull = int(about['monney'])
    if len(ms.text) < 4:
        try:
            if pull >= loto_narxi:
                number = int(ms.text)
                tekshirish = number_yes_or_no(ms.text)
                if tekshirish == 'bor':
                    await ms.answer("Bu raqam allaqachon olib bo'lingan\
                        \nBoshqa raqam kiriting",reply_markup=orqaga)
                else:
                    olganlar = int(game_info()['olganlar']) + 1
                    game_update('olganlar',olganlar,1)
                    update_db('monney',pull-loto_narxi,userid)
                    update_db('number',ms.text,userid)
                    update_db('loto','true',userid)
                    xabar = f"Lotoreya sotib olindi\nSizning raqamingiz: {ms.text}"
                    await ms.answer(xabar,reply_markup=profile_button)
                    await Game.header.set()
            else:
                await ms.answer("Sizning pulingiz yetarli emas\
                    \nLotoreya narxi 5000 so'm",reply_markup=olish_button)
                await Latareya.asosiy.set()
        except:
            await ms.answer("1 dan 299 ga butun son kiriting")
    else:
        await ms.answer("Iltimos 3 xonali son tanlang ")     



