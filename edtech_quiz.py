import csv
import tkinter as tk
from tkinter import messagebox


def save_name(filename, name):
    header = ["name"]

    try:
        with open(filename, "x", newline='', encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(header)
    except FileExistsError:
        pass

    with open(filename, "a", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([name])

def submit_name():

    name = name_var.get().strip()
  
    save_name("names.csv", name)
    root.destroy()

root = tk.Tk()
root.title("EdTech Name Collector")

name_var = tk.StringVar()

tk.Label(root, text="Enter your name:").pack()
tk.Entry(root, textvariable=name_var).pack()

tk.Button(root, text="Submit", command=submit_name).pack(pady=10)

root.mainloop()
