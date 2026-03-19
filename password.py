import tkinter as tk

def check():
    p = entry.get()
    strength = "Weak"

    if len(p) >= 8:
        strength = "Moderate"
    if any(c.isdigit() for c in p) and any(not c.isalnum() for c in p):
        strength = "Strong"

    result.set(strength)

root = tk.Tk()

entry = tk.Entry(root, show="*")
entry.pack()

tk.Button(root, text="Check Strength", command=check).pack()

result = tk.StringVar()
tk.Label(root, textvariable=result).pack()

root.mainloop()
