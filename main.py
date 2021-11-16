#SmartPip_moderator_bot
# 2024277284:AAGis5LiCFGpD81TtNA64CkUqvezEegU6pw
# 2024277284 id bot
#https://t.me/Pipl_test_chat
import sqlite3
import time
from telethon import TelegramClient, sync, events
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
client.connect()

from telethon.tl.functions.channels import JoinChannelRequest

# from telethon.tl.functions.messages import ImportChatInviteRequest
# updates =  client(ImportChatInviteRequest("-hHsK5t8fatmYTQ0"))

from datetime import datetime
curent_time = datetime.now().time()


#client.send_message('@viktortanchik', "TEST TIME")


if __name__ == '__main__':
    client.start()
    client.run_until_disconnected()
    executor.start_polling(dp)