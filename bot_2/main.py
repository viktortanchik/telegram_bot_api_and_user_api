#SmartPip_moderator_bot
# 2024277284:AAGis5LiCFGpD81TtNA64CkUqvezEegU6pw
# 2024277284 id bot
#https://t.me/Pipl_test_chat
import sqlite3
import time
from telethon import TelegramClient, sync, events
from telethon import TelegramClient, events, utils

###############################################
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

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
id_bot = 2024277284


@client.on(events.NewMessage())
async def handler_all(event):
    chat_id = event.chat_id  # ID чата

    sender_id = event.sender_id  # Получаем ID Юзера
    msg_id = event.id  # Получаем ID сообщения

    sender = await event.get_sender()  # получаем имя юзера
    name = utils.get_display_name(sender)  # Имя Юзера

    chat_from = event.chat if event.chat else (await event.get_chat())  # получаем имя группы
    chat_title = utils.get_display_name(chat_from)  # получаем имя группы
    print(f"ID: {chat_id} {chat_title} >>  (ID: {sender_id})  {name} - (ID: {msg_id}) {event.text}")


#
# @client.on(events.NewMessage)
# async def my_event_handler(event):
#     print(event)  # все новые сообщения
#     sender_id = event.sender_id  # Получаем ID Юзера
#     print(sender_id)
#
#     if 'hello' in event.raw_text:
#         await event.reply('hi!')
#         await client.send_message(channel, 'TEST BOT')
#
#






if __name__ == '__main__':
    #client.start()
    client.run_until_disconnected()
    executor.start_polling(dp)