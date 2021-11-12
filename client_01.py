from telethon import functions


# TelegramClient

import sqlite3
import time
from telethon import TelegramClient, sync, events
from telethon.tl.functions.channels import GetFullChannelRequest
from telethon.tl.types import PeerChannel


from enter_to_db import *
#################################################

# подключения
def start ():
    x = 1
    db = sqlite3.connect('Account.db')
    cur = db.cursor()
    cur.execute(f"SELECT PHONE FROM Account WHERE ID = '{x}'")
    time.sleep(0.4)
    Phone = str(cur.fetchone()[0])
    print("Входим в аккаунт: " + Phone, ' Номер ', x)
    cur.execute(f"SELECT API_ID FROM Account WHERE ID = '{x}'")
    time.sleep(0.4)
    api_id = str(cur.fetchone()[0])
    cur.execute(f"SELECT API_HASH FROM Account WHERE ID = '{x}'")
    time.sleep(0.4)
    api_hash = str(cur.fetchone()[0])
    session = str("anon" + str(x))
    client = TelegramClient(session, api_id, api_hash)
    client.start()
    return  client.start()





# Взятие URL с DB и поиск текущего имени чата и запись имени чата в DB.
def get_chat_current_name():
    con = sqlite3.connect('sqlite_python.db')
    db = sql_select_all(con)
    #print(db)
    for i in db:
        print(i[1])
        time.sleep(1)
        channel = i[1]
        full = client(functions.channels.GetFullChannelRequest(channel))
        full_channel = full.full_chat
        channel_full_info = client(GetFullChannelRequest(channel=channel))
        #print(channel_full_info.full_chat.about)
        #print(full_channel.migrated_from_chat_id)
        chat_id = channel_full_info.full_chat.id
        chanPeer = PeerChannel(channel_id=chat_id)
        channel_entity = client.get_entity(chanPeer)
        print(channel_entity.title)
        # Запись в базу сначала получаем id а потом по id записываем имя чата
        print(sql_select_id(con,i[1]))
        set = ("original_channel_name")
        set_name = (channel_entity.title)
        where = ('UID')
        where_name = sql_select_id(con,i[1])
        sql_update(con,set,set_name,where,where_name)


# получения  списка ID для автообнавления
def getID():
    con = sqlite3.connect('sqlite_python.db')
    db = sql_select_all(con)
    lens=[]
    for i in db:
        #print(i[0])
        lens.append(i[0])
        #sql_select_id(con, i[1])
        #print(sql_select_id(con, i[1]))
    return lens

def getURL():
    con = sqlite3.connect('sqlite_python.db')
    db = sql_select_all(con)
    lens=[]
    for i in db:
        #print(i[0])
        lens.append(i[1])
        #sql_select_id(con, i[1])
        #print(sql_select_id(con, i[1]))
    return lens

#print(getURL())

# Получить всех пользователей чата
def get_all_users(channel):
    client=start()
    print("get_all_users :",channel)
    #channel = 'https://t.me/zerno_agro_ua'
    conusers=[]
    for u in client.get_participants(str(channel)):
        # можно получить id ,first_name ,last_name ,username
        #print(u.id, u.first_name, u.last_name, u.username)
        conusers.append(u.id)
    return len(conusers)
#url = 'https://t.me/zerno_agro_ua'
#get_all_users(url)

# Запись количества пользователей чата в Базу

def save_len_users(len_users,id,sets):
    if sets ==True:
        set = ("Current_number_of_users_in_channel")
    else:
        set=("number_of_users_at_the_moment_of_insertion_into_the_bot")

    set_name = (str(len_users))
    where = ('UID')
    where_name = str(id)

    sql_update(con,set,set_name,where,where_name)

# Автообновления параметров

def Auto_updates_save_len_users():
    urls = getURL()
    for url in urls:
        print(url)
        time.sleep(1)
        #print(get_all_users(url))
        lenuser =get_all_users(url)
        print(sql_select_id(con,url))
        id = sql_select_id(con,url)
        sets=True
        save_len_users(lenuser,id,sets)

#Auto_updates_save_len_users()





# channel = '@Pipl_test_chat'
# full = client(functions.channels.GetFullChannelRequest(channel))
# full_channel = full.full_chat
# channel_full_info = client(GetFullChannelRequest(channel=channel))
# #print(channel_full_info.full_chat.about)
# #print(full_channel.migrated_from_chat_id)