from telethon.sync import TelegramClient, events
from telethon import functions
from telethon import utils
import time
from telethon import TelegramClient, sync, events
from telethon.tl.functions.channels import GetFullChannelRequest
from telethon.tl.types import PeerChannel
import sqlite3

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

from telethon.tl.types import PeerUser, PeerChat, PeerChannel


async def main():
    peer = await client.get_input_entity('https://t.me/channkt')
    print(peer)
    my_channel = await client.get_entity(PeerChannel(1557420008))
    print(my_channel)

client.loop.run_until_complete(main())

# @client.on(events.NewMessage())
# async def handler_all(event):
#     chat_from = event.chat if event.chat else (await event.get_chat())  # telegram MAY not send the chat enity
#     chat_title = utils.get_display_name(chat_from)
#     print(chat_title)
    # chat_id = event.chat_id  # ID чата
    #
    # sender_id = event.sender_id  # Получаем ID Юзера
    # msg_id = event.id  # Получаем ID сообщения
    #
    # sender = await event.get_sender()  # получаем имя юзера
    # name = utils.get_display_name(sender)  # Имя Юзера
    #
    # chat_from = event.chat if event.chat else (await event.get_chat())  # получаем имя группы
    # chat_title = utils.get_display_name(chat_from)  # получаем имя группы chat_from
    # #print(chat_title)
    # print(f"ID: {chat_id} {chat_title} >>  (ID: {sender_id})  {name} - (ID: {msg_id}) {event.text}")
    #

client.run_until_disconnected()



