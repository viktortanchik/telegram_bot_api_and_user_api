# TelegramClient

import sqlite3
import time
from telethon import TelegramClient, sync, events
from telethon.tl.functions.channels import GetFullChannelRequest

#################################################

# подключения
x = 1
db = sqlite3.connect('Account.db')
cur = db.cursor()
cur.execute(f"SELECT PHONE FROM Account WHERE ID = '{x}'")
time.sleep(0.4)
Phone = str(cur.fetchone()[0])
print("Входим в аккаунт: " + Phone, ' Номер ',x)
cur.execute(f"SELECT API_ID FROM Account WHERE ID = '{x}'")
time.sleep(0.4)
api_id = str(cur.fetchone()[0])
cur.execute(f"SELECT API_HASH FROM Account WHERE ID = '{x}'")
time.sleep(0.4)
api_hash = str(cur.fetchone()[0])
session = str("anon" + str(x))
client = TelegramClient(session, api_id, api_hash)
client.start()

channel = '@Pipl_test_chat'
# Отправка сообщения
#print('работа с ' + channel)
#client.send_message(channel, 'Start BOT')

# @client.on(events.NewMessage)
# async def my_event_handler(event):
#     print(event.raw_text)  # все новые сообщения
#     sender_id = event.sender_id  # Получаем ID Юзера
#     print(sender_id)
#


############################# BOT ##############################
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.dispatcher.filters import Text

from config import TOKEN
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Первая кнопка", "Вторая кнопка"]
    keyboard.add(*buttons)
    await message.reply("Привет!\nНапиши мне что-нибудь!", reply_markup=keyboard)

@dp.message_handler(Text(equals="Первая кнопка"))
async def with_puree(message: types.Message):
    await client.send_message(channel, 'TEST BOT Первая кнопка')
    ch = client.get_entity("@Pipl_test_chat")
    # ch_full = client(GetFullChannelRequest(channel=ch))
    # await ch_full.full_chat.about
    await message.reply("Выбрана Первая кнопка!")











#client.run_until_disconnected()
if __name__ == '__main__':
    #client.run_until_disconnected()
    executor.start_polling(dp)