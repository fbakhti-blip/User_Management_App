import re
import sqlite3
from data_access.database_manager import *

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
    if find_user_by_username(username):
        raise ValueError("Username Already Taken !!!")
    else:
        return username


def nickname_repeat_validator(nickname):

    for usr in users_list:
        if  nickname == usr[3]:
            raise ValueError("Nickname Already Taken !!!")
        else:
            return nickname