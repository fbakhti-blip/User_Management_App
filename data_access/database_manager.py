import sqlite3


def create_table_user():
    connection = sqlite3.connect("User_Management_App.data_access.user_db.db")
    cursor = connection.cursor()
    tables_list = cursor.execute(
        "select name from sqlite_master where type='table' and name='users'").fetchall()
    if tables_list == []:
        cursor.execute("create table users (id integer primary key  autoincrement, username text, password text, nickname text, locked integer)")
    connection.commit()
    connection.close()


def save_user(username,password,nickname,locked_status):
    connection = sqlite3.connect("User_Management_App.data_access.user_db.db")
    cursor = connection.cursor()
    cursor.execute("insert into users (username , password , nickname , locked) values(?,?,?,?)",
                   [username,password,nickname,locked_status])
    connection.commit()
    connection.close()


connection = sqlite3.connect('user_db.db')
cursor = connection.cursor()
user_list = cursor.execute("select * from users").fetchall()
connection.close()
# print(user_list)