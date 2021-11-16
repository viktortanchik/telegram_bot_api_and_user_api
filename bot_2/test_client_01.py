#https://t.me/channkt
from telethon.sync import TelegramClient, events
from telethon import functions
from telethon import utils
import time
from telethon import TelegramClient, sync, events
from telethon.tl.functions.channels import GetFullChannelRequest
from telethon.tl.types import PeerChannel
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch,ChannelParticipantsBots,ChannelParticipant
from time import sleep

import sqlite3
import asyncio

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

client.connect()

#channel_name="https://t.me/viktortanchikchannel"
channel_name="https://t.me/Pipl_test_chat"
channel_connect = client.get_entity(channel_name)
channel_full_info = client(GetFullChannelRequest(channel=channel_connect))
#print(channel_full_info.full_chat.participants_count)
print(channel_full_info.chats[0].photo)
photo =channel_full_info.chats[0].photo
if str(photo) == "ChatPhotoEmpty()":
    print("photo None")
else:
    print("photo OK")
    print(channel_full_info.chats[0].photo.photo_id)

#print(channel_full_info.chats[0].photo)
#print(channel_full_info.chats[0].photo.photo_id) # photo_id
#print(channel_full_info.chats[0].title)# name