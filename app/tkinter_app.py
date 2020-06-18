# TODO: Clean up the code with OOP

import tkinter as tk
from tkinter import ttk

from school_project.app.sql_commands import student_login, student_logout


active_students = []


def log_student(event):
    entry = entry_student_id.get()
    _is_student_logged_in(entry)
    students = "\n".join(active_students)
    lbl_active_students["text"] = students
    entry_student_id.delete(0, tk.END)


def _is_student_logged_in(student):
    if student not in active_students:
        active_students.append(student)
        student_login(student)
    else:
        active_students.remove(student)
        student_logout(student)


window = tk.Tk()
window.title("Hawksnest - Login/Logout")
window.columnconfigure([0, 1], minsize=50)
window.columnconfigure(2, minsize=200)
window.rowconfigure(0, minsize=100, weight=1)
window.bind("<Return>", log_student)

entry_student_id = ttk.Entry()
entry_student_id.grid(row=0, column=0, padx=5, pady=5, sticky="n")

btn_submit = ttk.Button(text="Submit", command=log_student)
btn_submit.grid(row=0, column=1, padx=5, pady=5, sticky="n")


lbl_frm_active_students = ttk.Labelframe(window, text="Active Students: ", relief=tk.SUNKEN)
lbl_frm_active_students.grid(row=0, column=2, sticky="n")

list_active_students = tk.Listbox(lbl_frm_active_students, height=20)

lbl_active_students = ttk.Label(lbl_frm_active_students)
lbl_active_students.grid()

entry_student_id.focus()

window.mainloop()
