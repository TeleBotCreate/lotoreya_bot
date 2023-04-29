from pymongo import MongoClient
import random as r

cluster = MongoClient('mongodb://localhost:27017')
table = cluster['lotoreya']

admin_uchun = table['malumotnoma']
collection_user = table['users']

def admin():
    news = "Latareya olganlar soni 70 taga yetsa o'yinni boshlaymiz\
        \nO'yin boshlanishidan oldin xabar beriladi"
    about = {'_id':1, 'count':0, 'summa':0,'olganlar':0,'game_status':'false', 'loto_status':'false', 'news':news}
    admin_uchun.insert_one(about)

def game_info():
    about = admin_uchun.find_one({'_id':1})
    return about

def game_update(nimani,nimaga, uid):
    son = admin_uchun.update_one({'_id':uid},{'$set':{f"{nimani}":f"{nimaga}"}})
    return "true"

def random_user_number():
    user = collection_user.find()
    all_number = []
    try:
        for us in user:
            if us['loto'] == 'true':
                all_number.append(us['number'])
        return r.choice(all_number)
    except:
        return "random_user_number funksiyada xato mavjut"

def elon():
    user = collection_user.find()
    return user

def game_over():
    admin_uchun.update_one({'_id':1},{'$set':{"count":0}})
    admin_uchun.update_one({'_id':1},{'$set':{"olganlar":0}})
    admin_uchun.update_one({'_id':1},{'$set':{"game_status":'false'}})
    
    user = collection_user.find()
    for us in user:
        if us['loto'] == 'true':
            collection_user.update_one({'_id':us['_id']},{'$set':{'loto':'false'}})
            collection_user.update_one({'_id':us['_id']},{'$set':{'number':'0'}})
    return True





def register(uid, name, phone):
    info = {'_id':uid, 'name':name, 'phone':phone, 'monney':0, 'gems':0, 'kubog':0, 'ball':0,'loto':'false', 'number':0}
    collection_user.insert_one(info)

def check(uid):
    result = collection_user.find_one({'_id':uid})
    if result:
        return True
    else:
        return False

def select_user(idn):
    about = collection_user.find_one({'_id':idn})
    return about

def user_number(number):
    bitta = collection_user.find_one({'number':number})
    if bitta:
        return bitta
    else:
        return "Malumot topilmadi"

def update_db(nimani, nimaga, uid):
    """Bazaga o'zgartirish kiritish uchun yasalgan funksiya"""
    son = collection_user.update_one({'_id':uid},{'$set':{f"{nimani}":f"{nimaga}"}})
    return "true"

def random_son():
    b = 999
    son = r.randint(1,b)
    status = False
    count = 0
    while status==False:
        holat = collection_user.find_one({'number':son})
        if count == b:
            status = True
            return "Kechirasiz lotoreyalar tugagan 😔"
        if holat:
            count += 1
            continue
        else:
            status = True
            return son

def number_yes_or_no(number):
    user = collection_user.find_one({'number':number})
    if user:
        return "bor"
    else:
        return "yo'q"







def oyindagilar():
    user = collection_user.find()
    for x in user:
        if x['loto'] == 'true':
            print(x['name'])











