from aiogram.dispatcher.filters.state import StatesGroup, State

class Game(StatesGroup):
    header = State()
    boshqas = State()
    hisob_tuldir = State()
    yangiliklar = State()
    savollar = State()
    update_user = State()
    pul_pilus = State()
     
class Latareya(StatesGroup):
    asosiy = State()
    random_kirish = State()
    tanlab_ol = State()
    uyin_holati = State()

class AdminState(StatesGroup):
    boshlandi = State()
    yutuq = State()
    winner = State()
    news_add = State()

class PulYech(StatesGroup):
    bosh_holat = State()
    yech6 = State()
    yech10 = State()
    yech15 = State()
    yech20 = State()

class Buyumlar(StatesGroup):
    asosiy = State()
    

