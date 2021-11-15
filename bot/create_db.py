import sqlite3

db = sqlite3.connect('Account.db')
cur = db.cursor()
    # Создаем таблицу
cur.execute("""CREATE TABLE IF NOT EXISTS Account (
    ID INTEGER PRIMARY KEY,
    PHONE TEXT,
    PASS TEXT,
    API_ID TEXT,
    API_HASH TEXT,
    ACTIVITY TEXT,
    LITECOIN TEXT
)""")
db.commit()
Phone = "+380****"
password = "****"
Api_id = "****"
Api_hash = "****"
Activity = "ON"

cur.execute(f"SELECT PHONE FROM Account WHERE PHONE = '{Phone}'")
if cur.fetchone() is None:
    cur.execute("""INSERT INTO Account(PHONE, PASS, API_ID, API_HASH, ACTIVITY) VALUES (?,?,?,?,?);""", (Phone, password, Api_id, Api_hash, Activity))
    db.commit()
    print("Registered!")
    for value in cur.execute("SELECT * FROM Account"):
        print(value)