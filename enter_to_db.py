import sqlite3

con = sqlite3.connect('sqlite_python.db')


def sql_insert_all(con, entities):
    cursorObj = con.cursor()
    cursorObj.execute('INSERT INTO users VALUES( ?,?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', entities)
    con.commit()

def sql_insert_one(con, entitie):
    cursorObj = con.cursor()
    cursorObj.execute(
    'INSERT INTO users(url_channel) VALUES(?)', entitie)
    con.commit()


def sql_insert_something(con,name, entitie):
    cursorObj = con.cursor()
    names = 'INSERT INTO users('+str(name)+ ') VALUES(?)'
    cursorObj.execute(names, entitie)
    con.commit()



# Обновления любого значения
def sql_update(con,set,set_name,where,where_name):
    cursorObj = con.cursor()
    strs = 'UPDATE users SET '+str(set)+' = '+"'"+str(set_name)+"'"+' where '+str(where)  +' = '+str(where_name)
    #'UPDATE users SET original_channel_name = "Rogers" where UID = 2'
    print(strs)
    cursorObj.execute(strs)
    con.commit()

set = ("original_channel_name")
set_name = ('TEST_UPDATE')
where = ('UID')
where_name =2

#sql_update(con,set,set_name,where,where_name)


# поиск ID по URL
def sql_select_id(con,url):
    cursorObj = con.cursor()
    stre =''.join(url)
    query="SELECT * FROM users WHERE url_channel = "+ "'" +str(stre) + "'"  # +str(name)
    #print(query)
    cursorObj.execute(query)
    values = cursorObj.fetchone()
    return values[0]

#name ='https://t.me/AgroTerritoriya'
#print(sql_select_id(con,name))


# Получения всех значений с базы
def sql_select_all(con):
    cursorObj = con.cursor()
    #stre =''.join(previous_channel_names)
    query="SELECT * FROM users  "  # +str(name)
    #print(query)
    cursorObj.execute(query)
    values = cursorObj.fetchmany(-1)
    return values

#urls =sql_select_urls(con)
#print(urls[0][1])

def sql_del(con,name):
    cur = con.cursor()
    query = "DELETE FROM users WHERE original_channel_name =?"
    cur.execute(query,(name))
    con.commit()


entities = ['url_channel','original_channel_name', 'previous_channel_names', 'Date_of_submission_to_bot', 'Current_username',
            'Edited_usernames', 'picture_changed', 'How_many_times', 'Current_number_of_users_in_channel',
            'number_of_users_at_the_moment_of_insertion_into_the_bot', 'There_is_an_ad_inside']

entitie = ('url_channel')

#sql_select_name(con,entitie)
#sql_del(con,entitie)
#sql_select(con)
#sql_update(con)
#sql_insert_one(con,entitie)
#sql_insert_all(con, entities)