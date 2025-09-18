import sqlite3

connection = sqlite3.connect("user_db.db")
cursor = connection.cursor()
tables_list = cursor.execute(
  "select name from sqlite_master where type='table' and name='users'").fetchall()

print(tables_list)

if tables_list == []:
    cursor.execute(
        "create table users (id integer primary key  autoincrement, username text, password text, nickname text, locked integer)")

connection.commit()
connection.close()


connection = sqlite3.connect("user_db.db")
cursor = connection.cursor()
cursor.execute("insert into users (username , password , nickname , locked) values(?,?,?,?)",
                   [username,password,nickname,locked_status])
connection.commit()
connection.close()