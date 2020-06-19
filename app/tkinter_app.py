import tkinter as tk
from tkinter import ttk

from school_project.app.sql_commands import student_login, student_logout


class MainApplication:
    """ Set up the Tkinter GUI window."""

    def __init__(self, parent):
        self.parent = parent
        self.set_window_config()
        self.create_entry_widgets()
        self.create_button_widgets()
        self.create_label_widgets()
        self.create_list_widgets()

    def set_window_config(self):
        """ Configuration settings for the Tkinter window."""

        self.parent.title("Hawksnest - Login/Logout")
        self.parent.columnconfigure([0, 1], minsize=50)
        self.parent.columnconfigure(2, minsize=200)
        self.parent.rowconfigure(0, minsize=100, weight=1)
        self.parent.bind("<Return>", StudentLogging.log_student)

    def create_entry_widgets(self):
        """ Create any needed Entry widgets."""

        self.entry_student_id = ttk.Entry()
        self.entry_student_id.grid(row=0, column=0, padx=5, pady=5, sticky="n")
        self.entry_student_id.focus()

    def create_button_widgets(self):
        """ Create any needed Button widgets."""

        self.btn_submit = ttk.Button(text="Submit", command=StudentLogging.log_student)
        self.btn_submit.grid(row=0, column=1, padx=5, pady=5, sticky="n")

    def create_label_widgets(self):
        """ Create any needed Label widgets."""

        self.lbl_frm_active_students = ttk.Labelframe(self.parent, text="Active Students: ", relief=tk.SUNKEN)
        self.lbl_frm_active_students.grid(row=0, column=2, sticky="n")
        self.lbl_active_students = ttk.Label(self.lbl_frm_active_students)
        self.lbl_active_students.grid()

    def create_list_widgets(self):
        """ Create any needed List widgets."""

        self.list_active_students = tk.Listbox(self.lbl_frm_active_students, height=20)


class StudentLogging:
    """ Logic dealing with logging students into and out of the system.

    :param active_students: List containing students that are signed into the system.
    """

    active_students = []

    @classmethod
    def log_student(cls, event):
        """ Logs students into and out of the system."""

        entry = app.entry_student_id.get()
        cls._is_student_logged_in(entry)
        students = "\n".join(cls.active_students)
        app.lbl_active_students["text"] = students
        app.entry_student_id.delete(0, tk.END)

    @classmethod
    def _is_student_logged_in(cls, student):
        """ Check to see if student is currently signed into the system."""

        # TODO: Clean up this method, it's doing too much.
        if student not in cls.active_students:
            cls.active_students.append(student)
            student_login(student)
        else:
            cls.active_students.remove(student)
            student_logout(student)


if __name__ == "__main__":
    root = tk.Tk()
    app = MainApplication(root)
    root.mainloop()
