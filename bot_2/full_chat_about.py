from telethon import functions


# TelegramClient

import sqlite3
import time
from telethon import TelegramClient, sync, events
from telethon.tl.functions.channels import GetFullChannelRequest
from telethon.tl.types import PeerChannel
from telethon import utils

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
full = client(functions.channels.GetFullChannelRequest(channel))
#print(full)
full_channel = full.full_chat
channel_full_info = client(GetFullChannelRequest(channel=channel))
#print(channel_full_info.full_chat.about)


#print(channel_full_info.full_chat.id)



chat_id =channel_full_info.full_chat.id
chanPeer=PeerChannel(channel_id=chat_id)
channel_entity=client.get_entity(chanPeer)
print(channel_entity.photo.photo_id) 
#photo=ChatPhoto(photo_id=5226605750896408378,
#print(channel_entity.title)

