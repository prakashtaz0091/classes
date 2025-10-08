import tkinter as tk
from tkinter import ttk, messagebox
import csv

# -------------------------------
# Main window setup
# -------------------------------
root = tk.Tk()
root.title("Student Registration Form")
root.geometry("400x400")
root.resizable(False, False)

# -------------------------------
# Variables to hold input data
# -------------------------------
name_var = tk.StringVar()
# age_var = tk.StringVar()
age_var = tk.IntVar()
address_var = tk.StringVar()
gender_var = tk.StringVar()
class_var = tk.StringVar()


# -------------------------------
# Save function
# -------------------------------
def save_data():
    name = name_var.get().strip()  # "   ram   "-> "ram"
    try:
        age = age_var.get()
        if age <= 0:
            raise ValueError("Age must be greater than 0")
    except ValueError:
        age_var.set("")
        messagebox.showerror("Error", "Age must be greater than 0")
        return
    except Exception:
        age_var.set("")
        messagebox.showerror("Error", "Age must be a number")
        return

    address = address_var.get().strip()
    gender = gender_var.get()
    class_ = class_var.get()

    if not (name and age and address and gender and class_):
        messagebox.showerror("Error", "All fields are required!")
        return

    # Save data to CSV file
    with open("students.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, age, address, gender, class_])

    messagebox.showinfo("Success", "Student registered successfully!")

    # Clear fields
    name_var.set("")
    age_var.set("")
    address_var.set("")
    gender_var.set("")
    class_var.set("")


# -------------------------------
# UI Layout using grid()
# -------------------------------

# Labels and Entries
tk.Label(root, text="Full Name:", font=("Arial", 10)).grid(
    row=0, column=0, padx=10, pady=10, sticky="w"
)
tk.Entry(root, textvariable=name_var, width=25).grid(row=0, column=1)

tk.Label(root, text="Age:", font=("Arial", 10)).grid(
    row=1, column=0, padx=10, pady=10, sticky="w"
)
tk.Entry(root, textvariable=age_var, width=25).grid(row=1, column=1)

tk.Label(root, text="Address:", font=("Arial", 10)).grid(
    row=2, column=0, padx=10, pady=10, sticky="w"
)
tk.Entry(root, textvariable=address_var, width=25).grid(row=2, column=1)


tk.Label(root, text="Gender:", font=("Arial", 10)).grid(
    row=3, column=0, padx=10, pady=10, sticky="w"
)

tk.Radiobutton(root, text="Male", value="Male", variable=gender_var).grid(
    row=3, column=1, sticky="w"
)
tk.Radiobutton(root, text="Female", value="Female", variable=gender_var).grid(
    row=4, column=1, sticky="w"
)
tk.Radiobutton(
    root, text="Rather not say", value="Rather not say", variable=gender_var
).grid(row=5, column=1, sticky="w")

tk.Label(root, text="Class:", font=("Arial", 10)).grid(
    row=6, column=0, padx=10, pady=10, sticky="w"
)

course_combo = ttk.Combobox(
    root,
    textvariable=class_var,
    values=["class 1", "class 2", "class 3", "class 4", "class 5", "class 6"],
    state="readonly",
    width=22,
)
course_combo.grid(row=6, column=1)
course_combo.set("Select class")


# Submit button
tk.Button(
    root, text="Register", command=save_data, bg="#4CAF50", fg="white", width=15
).grid(row=7, column=1, pady=20)

password = tk.Entry(root, show="*", width=15)
password.grid(row=8, column=1)


root.mainloop()
