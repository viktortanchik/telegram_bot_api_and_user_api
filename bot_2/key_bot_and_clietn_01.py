# Добалена возможность при добавлении нового канала получать сразу количество пользователей

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.dispatcher.filters import Text

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


from enter_to_db import *
import sqlite3

#from client_01 import *

import sqlite3

import asyncio



con = sqlite3.connect('sqlite_python.db')
from telethon import functions


# TelegramClient

import time
from telethon import TelegramClient, sync, events
from telethon.tl.functions.channels import GetFullChannelRequest
from telethon.tl.types import PeerChannel


from enter_to_db import *
#################################################
async def start_client(delay):
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
    task1 = asyncio.create_task(client.start())
    await asyncio.sleep(delay)
    return await task1

# Взятие URL с DB и поиск текущего имени чата и запись имени чата в DB.
async def get_chat_current_name():
    con = sqlite3.connect('sqlite_python.db')
    db = sql_select_all(con)
    client=start_client(1)
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
async def getID():
    con = sqlite3.connect('sqlite_python.db')
    db = sql_select_all(con)
    lens=[]
    for i in db:
        #print(i[0])
        lens.append(i[0])
        #sql_select_id(con, i[1])
        #print(sql_select_id(con, i[1]))
    return lens

async def getURL():
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
async def get_all_users(delay,channel):
    print("get_all_users :",channel)

    #channel = 'https://t.me/zerno_agro_ua'
###############
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
    task1 = asyncio.create_task(client.start())
    await asyncio.sleep(delay)
    print("client Start")
    await task1
    task2 = asyncio.create_task(client.get_participants(str(channel)))

    ############################
    conusers=[]
    for u in await task2:
        # можно получить id ,first_name ,last_name ,username
        #print(u.id, u.first_name, u.last_name, u.username)
        conusers.append(u.id)

    #await task2
    print(len(conusers))
    return len(conusers)

#url = 'https://t.me/zerno_agro_ua'
#get_all_users(url)

# Запись количества пользователей чата в Базу

async def save_len_users(len_users,id,sets):
    if sets ==True:
        set = ("Current_number_of_users_in_channel")
    else:
        set=("number_of_users_at_the_moment_of_insertion_into_the_bot")

    set_name = (str(len_users))
    where = ('UID')
    where_name = str(id)

    sql_update(con,set,set_name,where,where_name)

# Автообновления параметров

async def Auto_updates_save_len_users():
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


###################################################################################################################################################

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Главное меню"]
    keyboard.add(*buttons)
    await message.reply("Привет!\nНапиши мне что-нибудь!", reply_markup=keyboard)


####################################################################################
# Главное меню
@dp.message_handler(Text(equals="Главное меню"))
async def with_puree(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Первая кнопка", "Вторая кнопка"]
    keyboard.add(*buttons)
    await message.reply("Выбрать режим", reply_markup=keyboard)


@dp.message_handler(Text(equals="Первая кнопка"))
async def with_puree(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["+ кнопка", "- кнопка", "Главное меню"]
    keyboard.add(*buttons)
    await message.reply("Выбрать режим", reply_markup=keyboard)

# Кнопка удаления канала
@dp.message_handler(Text(equals="- кнопка"))
async def with_puree(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Удалить канал", "Главное меню"]
    keyboard.add(*buttons)

    # Запись во временый файл
    @dp.message_handler()
    async def echo_message(msg: types.Message):
        print(msg.text)
        file = open("temp.txt", "w")
        file.write(msg.text)
        file.close()

    await message.reply("Укажите названия через @ или ur ", reply_markup=keyboard)

# подтверждения удаления канала
@dp.message_handler(Text(equals="Удалить канал"))
async def with_puree(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Главное меню"]
    keyboard.add(*buttons)
    f = open('temp.txt', 'r')
    con = sqlite3.connect('sqlite_python.db')
    fstr = ''.join(f.read())
    print(fstr)
    temp = (fstr,)
    sql_del(con,temp)
    print("Канал удален: ",temp)
    await message.reply("Выбрать режим", reply_markup=keyboard)

# Добавления канала
@dp.message_handler(Text(equals="+ кнопка"))
async def with_puree(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Сохранить", "Отмена", "Главное меню"]
    keyboard.add(*buttons)

    #Запись во временый файл
    @dp.message_handler()
    async def echo_message(msg: types.Message):
        print(msg.text)
        file = open("temp.txt", "w")
        file.write(msg.text)
        file.close()
    await message.reply("Укажите названия через @ или url  канала ", reply_markup=keyboard)

# Сохранения канала
@dp.message_handler(Text(equals="Сохранить"))
async def with_puree(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Главное меню"]
    keyboard.add(*buttons)
    print('NAME CHANNEL: ')
    f = open('temp.txt', 'r')
    con = sqlite3.connect('sqlite_python.db')
    fstr=''.join(f.read())
    print(fstr)
    temp=(fstr,)
    sql_insert_one(con,temp)
    print("temp",temp[0])
    task1 = asyncio.create_task(get_all_users(1,str(temp[0])))

    id = sql_select_id(con, temp)
    sets=False

    task2 = asyncio.create_task(save_len_users(await task1, id, sets))
    await task2


    await message.reply("Канал добавлен", reply_markup=keyboard)


####################################################################################
@dp.message_handler(Text(equals="Вторая кнопка"))
async def with_puree(message: types.Message):
    await message.reply("Выбрана Вторую кнопку!")


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Напиши мне что-нибудь, и я отпрпавлю этот текст тебе в ответ!")


# @dp.message_handler()
# async def echo_message(msg: types.Message):
#     print(msg.text)
#     await bot.send_message(msg.from_user.id, msg.text)


if __name__ == '__main__':
    executor.start_polling(dp)
