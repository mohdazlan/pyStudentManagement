import tkinter as tk
from tkinter import *
import pymssql
from tkinter import messagebox
def login():
    username = username_entry.get()
    password = password_entry.get()

    try:
        #Connection to the SQL Server
        conn = pymssql.connect(server='Z4P5-NB003', user='sa', password='p@ssw0rd',database='sekolah')

        cursor = conn.cursor()

        query=f"SELECT * FROM login WHERE username = '{username}' AND password ='{password}'"

        cursor.execute(query)

        row = cursor.fetchone()

        if row:
            messagebox.showinfo("Login Successful", "Welcome, User!")
        else:
            messagebox.showwarning("Login failed", "Invalid Username or Password!")

        cursor.close()
        conn.close()
    except Exception as e:
        messagebox.showerror("Error", str(e))

def click_here():
    print("Hello World")

window = tk.Tk()
window.title("Login window")

username_label = tk.Label(window,text="Username")
username_label.grid(row=1, column=0,padx=10,pady=5)

username_entry = tk.Entry(window)
username_entry.grid(row=1, column=1,padx=10,pady=5)


password_label = tk.Label(window,text="Password")
password_label.grid(row=2, column=0,padx=10,pady=5)

password_entry = tk.Entry(window)
password_entry.grid(row=2, column=1,padx=10,pady=5)

login_button = tk.Button(window,text="Login",command=login)
login_button.grid(row=3, column=1,padx=10,pady=5)

window.mainloop()

