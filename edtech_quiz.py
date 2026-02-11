import csv
import tkinter as tk
from tkinter import messagebox

def save_details(filename, name, school):
    header = ["name", "school"]

    try:
        with open(filename, "x", newline='', encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(header)
    except FileExistsError:
        pass

    with open(filename, "a", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([name, school])

def submit_details():
    name = name_var.get().strip()
    school = school_var.get().strip()

    if name == "" or school == "":
        messagebox.showwarning("Missing information", "Please enter both your name and school.")
        return

    save_details("user_details.csv", name, school)
    messagebox.showinfo("Saved", "Your details have been saved.")
    root.destroy()

root = tk.Tk()
root.title("EdTech Details Form")

name_var = tk.StringVar()
school_var = tk.StringVar()

tk.Label(root, text="Enter your name:").pack()
tk.Entry(root, textvariable=name_var).pack()

tk.Label(root, text="Enter your school:").pack()
tk.Entry(root, textvariable=school_var).pack()

tk.Button(root, text="Submit", command=submit_details).pack(pady=10)

root.mainloop()
