import tkinter as tk
from tkinter import messagebox

def login():
    u = username.get()
    p = password.get()

    if not u or not p:
        messagebox.showwarning("Error", "Fields cannot be empty")
    elif u == "admin" and p == "1234":
        messagebox.showinfo("Success", "Login Successful")
    else:
        messagebox.showerror("Error", "Invalid Credentials")

root = tk.Tk()

username = tk.Entry(root)
username.pack()

password = tk.Entry(root, show="*")
password.pack()

tk.Button(root, text="Login", command=login).pack()

root.mainloop()
