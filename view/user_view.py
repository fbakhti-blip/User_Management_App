from tkinter import *
import tkinter.messagebox as msg

# TODO making sure database path is always found! ;-(((
# import sys
# sys.path.append("C:\\Users\farzi\Downloads\User_Management_App")

from tools.validation import *
from data_access.database_manager import user_list, save_user


def save_click():
    try:
        username_validator(username.get())
        password_validator(password.get())
        nickname_validator(nickname.get())
        username_repeat_validator(username.get())
        nickname_repeat_validator(nickname.get())
        save_user(username.get(),password.get(),nickname.get(),locked_status.get())
        msg.showinfo("Save", "User saved")
        username.set("")
        password.set("")
        nickname.set("")
    except Exception as e:
        msg.showerror("Error", f"{e}")


window = Tk()

window.title("User Profile")
window.geometry("270x300")

# Username
username = StringVar()
Label(window, text="Username:").place(x=20, y=20)
Entry(window, textvariable=username, bd=5).place(x=100, y=20)

# Password
password = StringVar()
Label(window, text="Password:").place(x=20, y=60)
Entry(window, show="*", textvariable=password, bd=5).place(x=100, y=60)

# Nickname
nickname = StringVar()
Label(window, text="Nickname:").place(x=20, y=100)
Entry(window, textvariable=nickname, bd=5).place(x=100, y=100)


# Locked
locked_status = BooleanVar()
Label(window, text="Locked").place(x=20, y=200)
Checkbutton(window, variable=locked_status).place(x=100, y=200)


Button(window, text="Save", width=15, command=save_click).place(x=70, y=240)

window.mainloop()
