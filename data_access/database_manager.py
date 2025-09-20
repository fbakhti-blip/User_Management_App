import sqlite3


def create_table_user():
    connection = sqlite3.connect("./data_access/user_db.db")
    cursor = connection.cursor()
    cursor.execute("create table if not exists users (id integer primary key  autoincrement, username text, password text, nickname text, locked integer)")
    connection.commit()
    connection.close()


def save_user(username,password,nickname,locked_status):
    connection = sqlite3.connect("./data_access/user_db.db")
    cursor = connection.cursor()
    cursor.execute("insert into users (username , password , nickname , locked) values(?,?,?,?)",
                   [username,password,nickname,locked_status])
    connection.commit()
    connection.close()

