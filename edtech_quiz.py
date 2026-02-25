import csv # for permanent storage functionality
import tkinter as tk # for GUI
from tkinter import messagebox # for pop-up information boxes

def load_questions(filename):
    with open(filename, newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))

def save_results(filename, name, school, answers):
    header = ["name", "school"] + [f"Q{i+1}" for i in range(len(answers))]

    try:
        with open(filename, "x", newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(header)
    except FileExistsError:
        pass

    with open(filename, "a", newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([name, school] + answers)

def start_quiz():
    name = name_var.get().strip()
    school = school_var.get().strip()

    if name == "" or school == "":
        messagebox.showwarning("Missing info", "Please enter your name and school.")
        return

    show_question(0, [])

def show_question(question_number, answers_so_far):
    for widget in root.winfo_children():
        widget.destroy()

    question = questions[question_number]

    tk.Label(root,text=f"Question {question_number + 1}: {question['question']}",wraplength=1000,justify="left").pack(anchor="w")

    choice_var.set("")

    for option in ["a", "b", "c", "d"]:
        text = f"{option.upper()}: {question[option]}"
        tk.Radiobutton(root,text=text,variable=choice_var,value=option,wraplength=950,justify="left").pack(anchor="w")

    tk.Button(
        root,
        text="Next",
        command=lambda: next_question(question_number, answers_so_far)
    ).pack(pady=10)

def next_question(question_number, answers_so_far):
    selected = choice_var.get()

    if selected == "":
        messagebox.showwarning("No answer", "Please select an answer.")
        return

    new_answers = answers_so_far + [selected]

    if question_number + 1 < len(questions):
        show_question(question_number + 1, new_answers)
    else:
        finish_quiz(new_answers)

def finish_quiz(all_answers):
    save_results("results.csv", name_var.get(), school_var.get(), all_answers)
    messagebox.showinfo("Done", "Your answers have been saved.")
    root.destroy()

if __name__ == "__main__":
    questions = load_questions("questions.csv")

    root = tk.Tk()
    root.title("EdTech Quiz")
    root.geometry("1000x350") 
    root.configure(bg="#FFFFFF") 

    root.option_add("*Background", "#FFFFFF")
    root.option_add("*Foreground", "#B60000")
    root.option_add("*Font", "Sans-Serif 16")

    name_var = tk.StringVar()
    school_var = tk.StringVar()
    choice_var = tk.StringVar()

    tk.Label(root,text="Welcome to the EdTech Quiz!\n\nPlease enter your name and school below, then click the Start Quiz button.\nYou will then be asked six questions, select one answer per question and confirm by clicking Next. ",wraplength=950,justify="center").pack(pady=20)

    tk.Label(root, text="Enter your name:").pack()
    tk.Entry(root, textvariable=name_var).pack()

    tk.Label(root, text="Enter your school:").pack()
    tk.Entry(root, textvariable=school_var).pack()

    tk.Button(root, text="Start Quiz", command=start_quiz).pack(pady=10)

    root.mainloop()
