import sqlite3


def create_table_user():
    connection = sqlite3.connect("./data_access/user_db.db")
    cursor = connection.cursor()
    cursor.execute("create table if not exists users (id integer primary key  autoincrement, username text unique , password text, nickname text unique , locked integer)")
    connection.commit()
    connection.close()


def save_user(username,password,nickname,locked_status):
    connection = sqlite3.connect("./data_access/user_db.db")
    cursor = connection.cursor()
    cursor.execute("insert into users (username , password , nickname , locked) values(?,?,?,?)",
                   [username,password,nickname,locked_status])
    connection.commit()
    connection.close()

def find_user_by_username(username):
    connection = sqlite3.connect("./data_access/user_db.db")
    cursor = connection.cursor()
    cursor.execute("select * from users where username = ?", [username])
    result = cursor.fetchone()
    connection.close()
    return result


def find_all():
    connection = sqlite3.connect("./data_access/user_db.db")
    cursor = connection.cursor()
    users_list = cursor.execute("select * from users").fetchall()
    connection.close()
    return users_list