from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.dispatcher.filters import Text

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

import datetime

from enter_to_db import *
import sqlite3

from client_01 import *

import sqlite3

import asyncio



con = sqlite3.connect('sqlite_python.db')



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
    #print("len_users : ", await get_all_users(str(temp[0])))

    #await get_all_users(str(temp[0]))
    # id = sql_select_id(con, temp)
    # sets=False
    # save_len_users(len_users, id, sets)
    # start = datetime.datetime.now()
    # loop = asyncio.get_event_loop()
    #loop.run(get_all_users(str(temp[0])))
    #exec_time = (datetime.datetime.now() - start).seconds
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
