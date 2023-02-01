import tkinter
from tkinter import messagebox


window = tkinter.Tk()
window.title("Login Form")
window.geometry('340x440')
window.configure(bg='#333333')


def login():
    username = "aimma"
    password = "12345"

    if username_entry.get()==username and password_entry.get()==password: 
       messagebox.showinfo(title="Login Success", message="You successfully logged in.")
    else: 
        messagebox.showinfo(title="Error", message="Invalid login.")

frame = tkinter.Frame(bg='#333333')

login_label = tkinter.Label(frame, text="Login Form", bg='#333333', fg='#FFFFFF', font=("Arial", 25))
username_label = tkinter.Label(frame, text="Username", bg='#333333',fg='#FFFFFF', font=("Arial", 16))
username_entry = tkinter.Entry(frame, font=("Arial", 25))
password_entry = tkinter.Entry(frame, show="*")
password_label = tkinter.Label(frame, text="Password", bg='#333333', fg='#FFFFFF', font=("Arial", 16))
login_button = tkinter.Button(frame, text="Login", bg='#333333', fg='#FFFFFF', font=("Arial", 16), command=login)

login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1, pady=30)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1, pady=30)
login_button.grid(row=3, column=0, columnspan=2, pady=30)

frame.pack()

window.mainloop()