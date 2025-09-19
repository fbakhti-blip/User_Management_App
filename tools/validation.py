import re
import sqlite3

def username_validator(username):
    if re.match(r"^[a-zA-Z\d]{10,20}$", username):
        return username
    else:
        raise ValueError("Invalid Username !!!" , "فقط 10 تا 20 کاراکتر حروف و اعداد")


def password_validator(password):
    if re.match(r"^[a-zA-Z\d$@#]{8,14}$", password):
        return password
    else:
        raise ValueError("Invalid Password !!!" , "فقط 8 تا 14 کاراکتر بدون فاصله")


def nickname_validator(nickname):
    if re.match(r"^[a-zA-Z\s\d]{3,30}$", nickname):
        return nickname
    else:
        raise ValueError("Invalid Nickname !!!" , "فقط 3 تا 30 کاراکتر حروف و اعداد و فاصله")


def username_repeat_validator(username):
    connection = sqlite3.connect("User_Management_App.data_access.user_db.db")
    cursor = connection.cursor()
    users_list = cursor.execute("select * from users").fetchall()
    connection.close()
    for usr in users_list:
        if  username == usr[1]:
            raise ValueError("Username Already Taken !!!")
        else:
            return username


def nickname_repeat_validator(nickname):
    connection = sqlite3.connect("User_Management_App.data_access.user_db.db")
    cursor = connection.cursor()
    users_list = cursor.execute("select * from users").fetchall()
    connection.close()
    for usr in users_list:
        if  nickname == usr[3]:
            raise ValueError("Nickname Already Taken !!!")
        else:
            return nickname