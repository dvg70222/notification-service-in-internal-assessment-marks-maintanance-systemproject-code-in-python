
import tkinter as tk
from tkinter import messagebox
from login_module import check_login
from marks_module import add_student, get_students
from email_module import send_email
from database_module import connect_db

def main_gui():
    connect_db()
    root = tk.Tk()
    root.title("Internal Assessment System")

    # Login Frame
    login_frame = tk.Frame(root)
    tk.Label(login_frame, text="Username").grid(row=0, column=0)
    tk.Label(login_frame, text="Password").grid(row=1, column=0)
    username = tk.Entry(login_frame)
    password = tk.Entry(login_frame, show='*')
    username.grid(row=0, column=1)
    password.grid(row=1, column=1)

    def login_action():
        if check_login(username.get(), password.get()):
            login_frame.pack_forget()
            dashboard()
        else:
            messagebox.showerror("Error", "Invalid login")

    tk.Button(login_frame, text="Login", command=login_action).grid(row=2, column=0, columnspan=2)
    login_frame.pack()

    def dashboard():
        dashboard_frame = tk.Frame(root)
        tk.Label(dashboard_frame, text="Student Name").grid(row=0, column=0)
        tk.Label(dashboard_frame, text="Email").grid(row=1, column=0)
        tk.Label(dashboard_frame, text="Marks").grid(row=2, column=0)
        name = tk.Entry(dashboard_frame)
        email = tk.Entry(dashboard_frame)
        marks = tk.Entry(dashboard_frame)
        name.grid(row=0, column=1)
        email.grid(row=1, column=1)
        marks.grid(row=2, column=1)

        def save_student():
            add_student(name.get(), email.get(), int(marks.get()))
            messagebox.showinfo("Saved", "Student added")

        def notify():
            for student in get_students():
                send_email(
                    student[2],
                    "Internal Marks Notification",
                    f"Hi {student[1]}, your marks are {student[3]}",
                    "universitydvg@gmail.com",
                    "uvzq qoux floq cwpz"
                )
            messagebox.showinfo("Sent", "Emails sent to all students")

        tk.Button(dashboard_frame, text="Add Student", command=save_student).grid(row=3, column=0)
        tk.Button(dashboard_frame, text="Send Email", command=notify).grid(row=3, column=1)
        dashboard_frame.pack()

    root.mainloop()

if __name__ == "__main__":
    main_gui()
