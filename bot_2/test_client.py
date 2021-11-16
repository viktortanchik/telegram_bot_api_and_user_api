# TelegramClient
from telethon import functions
from telethon import utils
from telethon import TelegramClient, sync, events
from telethon.tl.functions.channels import GetFullChannelRequest
from telethon.tl.types import PeerChannel
import time


import sqlite3
from enter_to_db import *
con = sqlite3.connect('sqlite_python.db')
x = 2
db = sqlite3.connect('Account.db')
cur = db.cursor()
cur.execute(f"SELECT PHONE FROM Account WHERE ID = '{x}'")
time.sleep(0.4)
Phone = str(cur.fetchone()[0])
print("Enter your account: " + Phone, ' Number ', x)
cur.execute(f"SELECT API_ID FROM Account WHERE ID = '{x}'")
time.sleep(0.4)
api_id = str(cur.fetchone()[0])
cur.execute(f"SELECT API_HASH FROM Account WHERE ID = '{x}'")
time.sleep(0.4)
api_hash = str(cur.fetchone()[0])
session = str("anon" + str(x))
client = TelegramClient(session, api_id, api_hash)
client.start()
############################################### Работа с чатом ###############################################

def chanelname(url):
    channel = url#'@Pipl_test_chat'
    full = client(functions.channels.GetFullChannelRequest(channel))
    # print(full)
    full_channel = full.full_chat
    channel_full_info = client(GetFullChannelRequest(channel=channel))
    chat_id = channel_full_info.full_chat.id
    chanPeer = PeerChannel(channel_id=chat_id)
    channel_entity = client.get_entity(chanPeer)
    #print(channel_entity.photo.photo_id)
    print(channel_entity.title)
    return channel_entity.title

def chanelidphoto(url):
    channel = url  # '@Pipl_test_chat'
    full = client(functions.channels.GetFullChannelRequest(channel))
    # print(full)
    full_channel = full.full_chat
    channel_full_info = client(GetFullChannelRequest(channel=channel))
    chat_id = channel_full_info.full_chat.id
    chanPeer = PeerChannel(channel_id=chat_id)
    channel_entity = client.get_entity(chanPeer)
    #print(channel_entity.photo.photo_id)
    #print(channel_entity.title)
    return channel_entity.photo.photo_id

def lenchanel(url):
    #print(stats.stringify())
    lens = client.get_participants(str(url))
    conusers=[]
    i=0
    for u in lens:
        # можно получить id ,first_name ,last_name ,username
        #print(u.id, u.first_name, u.last_name, u.username)
        conusers.append(u.id)
        i+=1
    print("Количество пользователей ",len(conusers))
    return i #len(conusers)
# url ='https://t.me/zernomart'
# print(lenchanel(url))
############################################### Работа с базой ###############################################

def geturls():
    con = sqlite3.connect('sqlite_python.db')
    db = sql_select_all(con)
    urls=[]
    for i in db:
        #print(i[2])
        urls.append(i[1])
    return urls

def get_id_in_url_db(url):
    return sql_select_id(con, url)

def save_name_chat(name_cha,id,):
    set=("previous_channel_names")
    set_name = (str(name_cha))
    where = ('UID')
    where_name = str(id)
    print("save_name_chat !!!")
    sql_update(con,set,set_name,where,where_name)

#url='@Pipl_test_chat'

def save_photo_chat(name_cha,id,):
    set=("picture_changed")
    set_name = (str(name_cha))
    where = ('UID')
    where_name = str(id)
    print("save_photo_chat !!!")
    sql_update(con,set,set_name,where,where_name)

def save_photo_chat_how_many(name_cha,id,):
    set=("How_many_times")
    set_name = (str(name_cha))
    where = ('UID')
    where_name = str(id)
    print("save_photo_chat !!!")
    sql_update(con,set,set_name,where,where_name)

# Current_number_of_users_in_channel
def save_current_number_of_users_in_channel(name_cha,id,):
    set = ("Current_number_of_users_in_channel")
    set_name = (str(name_cha))
    where = ('UID')
    where_name = str(id)
    print("Current_number !!!")
    sql_update(con, set, set_name, where, where_name)

admin="@viktortanchik"
while True:
    print("##################### START ###########################")
    urlls = geturls()
    for url in urlls:
        print("url >> ",url)
        # берем url и получаем текущее имя чата
        name_chat_now = chanelname(url)
        print("name_chat_now >> ",name_chat_now)
        # получаем id с базы по url
        id_cat_in_db = get_id_in_url_db(url)
        print("id_cat_in_db >> ",id_cat_in_db)
        # получаем имя с базы
        name_chat_in_db = sql_select_previous_channel_names(con,str(id_cat_in_db))
        print("name_chat_in_db >> ",name_chat_in_db)
        # сравниваем значения с базой и текущим
        if str(name_chat_in_db) != str(name_chat_now):
            print("Имя чата изменилось")
            mess = str(name_chat_in_db)+ " change name to: "+ str(name_chat_now)
            client.send_message(admin, mess)
            save_name_chat(name_chat_now, id_cat_in_db)
        # Получаем текущие значение id photo
        id_photo_now = chanelidphoto(url)
        # Получаем  значение id photo с DB
        id_photo_db = sql_select_picture_changed(con,str(id_cat_in_db))
        # Проверяем значения
        if str(id_photo_now) != str(id_photo_db):
            print("Изображения  чата изменилось")
            # сохраняем значения id в базе
            save_photo_chat(id_photo_now, id_cat_in_db)
            # получаем значения сколько раз менялось изображения и меням его
            how_many = sql_select_How_many_times(con,str(id_cat_in_db))
            print("how_many >> ", how_many)
            if how_many==None:
                how_many = 0
            how_many = int(how_many)
            how_many += 1
            save_photo_chat_how_many(how_many,id_cat_in_db)
            mess =  str(name_chat_now) +' change his picture' + str(how_many) +" many times"
            # отправляем сообщения
            client.send_message(admin, mess)
        # Получаем текущие количество пользователей чата
        chat_len = lenchanel(url)
        # Получаем  количество пользователей чата c DB
        chat_len_db = sql_select_Current_number_of_users_in_channel(con,str(id_cat_in_db))

        if str(chat_len) != str(chat_len_db):
            print("Количество участников  чата изменилось")
            mess =  str(name_chat_now) + " Change his number of chat participants has changed from "+str(chat_len_db) + " to " + str(chat_len)
            # отправляем сообщения
            client.send_message(admin, mess)
            save_current_number_of_users_in_channel(chat_len,str(id_cat_in_db))
    time.sleep(60)