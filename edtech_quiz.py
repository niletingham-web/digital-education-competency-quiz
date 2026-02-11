import csv
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("EdTech Quiz")

name_var = tk.StringVar()

tk.Label(root, text="Enter your name:").pack()
tk.Entry(root, textvariable=name_var).pack()

tk.Button(root, text="Submit").pack(pady=10)

root.mainloop()
