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
x = 6
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
client.connect()


#https://t.me/joinchat/JxjBZVYL-1g2NTVi
#https://t.me/joinchat/-hHsK5t8fatmYTQ0
# https://t.me/joinchat/0miZIt7WAYcwM2Y0
from telethon.tl.functions.messages import ImportChatInviteRequest
#updates =  client(ImportChatInviteRequest("8qK8C3bzmwNkNDRk"))


from telethon.tl.functions.channels import GetFullChannelRequest
channel_connect = client.get_entity("https://t.me/joinchat/PfJvl_6nZQcwOTk0")
channel_full_info = client(GetFullChannelRequest(channel=channel_connect))
print(channel_full_info)
client.send_message("https://t.me/joinchat/0miZIt7WAYcwM2Y0", "TEST_bot")