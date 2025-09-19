import sqlite3

# from view.user_view import username, nickname

connection = sqlite3.connect("user_db.db")
cursor = connection.cursor()
tables_list = cursor.execute(
  "select name from sqlite_master where type='table' and name='users'").fetchall()

print(tables_list)

if tables_list == []:
    cursor.execute(
        "create table users (id integer primary key  autoincrement, username text, password text, nickname text, locked integer)")

cursor.execute("insert into users (username , password , nickname , locked) values ('Farzin' , 'asghkl' , 'fzbk' , 1)")
cursor.execute("insert into users (username , password , nickname , locked) values ('Fashin' , 'askl' , 'fZbk' , 0)")
cursor.execute("insert into users (username , password , nickname , locked) values ('Ali' , 'sabat' , 'Alidj' , 1)")
connection.commit()
connection.close()

username = input("Enter username: ")
nickname = input("Enter nickname: ")

connection = sqlite3.connect("user_db.db")
cursor = connection.cursor()
user_list = cursor.execute("select * from users").fetchall()
for usr in user_list:
    if username == usr[1]:
        raise ValueError("Username Already Taken !!!")
    elif nickname == usr[3]:
        raise ValueError("Nickname Already Taken !!!")
    else:
        print(username, nickname)
        break

# connection = sqlite3.connect("user_db.db")
# cursor = connection.cursor()
# cursor.execute("insert into users (username , password , nickname , locked) values (Farzin,asghkl,fzbk,1)")
# connection.commit()
# connection.close()