1️⃣ Basic intro to `tkinter`
2️⃣ Common components/widgets
3️⃣ Event handling
4️⃣ Layout management
5️⃣ Practical example — **Student Registration Form** that saves to a CSV file

---

## 🧩 1. Introduction to Tkinter

**Tkinter** is Python’s **built-in GUI (Graphical User Interface)** library.
It lets you make windows, buttons, textboxes, labels, etc., easily — no external installation needed.

```python
import tkinter as tk

root = tk.Tk()         # Create the main window
root.title("My First App")
root.geometry("400x300")  # Width x Height

root.mainloop()        # Keeps window running
```

> 💡 `mainloop()` keeps listening for user events (clicks, typing, etc.)

---

## 🧱 2. Common Tkinter Components (Widgets)

Let’s learn the **most-used widgets** for basic forms.

| Widget        | Purpose                 | Example                                                             |
| ------------- | ----------------------- | ------------------------------------------------------------------- |
| `Label`       | Display static text     | `tk.Label(root, text="Name")`                                       |
| `Entry`       | Single-line input       | `tk.Entry(root)`                                                    |
| `Text`        | Multi-line input        | `tk.Text(root, height=4, width=30)`                                 |
| `Button`      | Trigger actions         | `tk.Button(root, text="Submit", command=save_data)`                 |
| `Radiobutton` | Select one option       | `tk.Radiobutton(root, text="Male", value="M", variable=gender_var)` |
| `Checkbutton` | True/False option       | `tk.Checkbutton(root, text="I Agree", variable=agree_var)`          |
| `Combobox`    | Dropdown list           | from `ttk` module → `ttk.Combobox(root, values=["BCA", "BBA"])`     |
| `Frame`       | Group elements together | `tk.Frame(root)`                                                    |
| `LabelFrame`  | Frame with a title      | `tk.LabelFrame(root, text="Personal Info")`                         |

---

## 🧮 3. Layout Managers

Tkinter has **three layout systems** to position widgets inside the window:

| Manager    | Description                                | Example                       |
| ---------- | ------------------------------------------ | ----------------------------- |
| `.pack()`  | Simple stacking (top, bottom, left, right) | `label.pack()`                |
| `.grid()`  | Table-like layout using rows and columns   | `entry.grid(row=0, column=1)` |
| `.place()` | Absolute positioning (x, y)                | `button.place(x=20, y=50)`    |

> 💡 Use `.grid()` for forms — it keeps things neat and aligned.

---

## ⚡ 4. Event Handling (Connecting Button to Action)

You can make buttons **do something** when clicked using the `command` parameter:

```python
def greet():
    print("Hello, " + name_entry.get())

tk.Button(root, text="Greet", command=greet).pack()
```

> `.get()` fetches the text from input fields (`Entry`, `Combobox`, etc.)
> `.delete(0, tk.END)` clears an entry box.

---

## 🧾 5. Practical Example — Student Registration Form

Here’s a full working mini-project you can run and test:

### 📘 Example Code

```python
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
age_var = tk.StringVar()
gender_var = tk.StringVar()
course_var = tk.StringVar()

# -------------------------------
# Save function
# -------------------------------
def save_data():
    name = name_var.get().strip()
    age = age_var.get().strip()
    gender = gender_var.get()
    course = course_var.get()

    if not (name and age and gender and course):
        messagebox.showerror("Error", "All fields are required!")
        return

    # Save data to CSV file
    with open("students.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, age, gender, course])

    messagebox.showinfo("Success", "Student registered successfully!")

    # Clear fields
    name_var.set("")
    age_var.set("")
    gender_var.set("")
    course_var.set("")

# -------------------------------
# UI Layout using grid()
# -------------------------------

# Labels and Entries
tk.Label(root, text="Full Name:", font=("Arial", 10)).grid(row=0, column=0, padx=10, pady=10, sticky="w")
tk.Entry(root, textvariable=name_var, width=25).grid(row=0, column=1)

tk.Label(root, text="Age:", font=("Arial", 10)).grid(row=1, column=0, padx=10, pady=10, sticky="w")
tk.Entry(root, textvariable=age_var, width=25).grid(row=1, column=1)

tk.Label(root, text="Gender:", font=("Arial", 10)).grid(row=2, column=0, padx=10, pady=10, sticky="w")

tk.Radiobutton(root, text="Male", value="Male", variable=gender_var).grid(row=2, column=1, sticky="w")
tk.Radiobutton(root, text="Female", value="Female", variable=gender_var).grid(row=3, column=1, sticky="w")

tk.Label(root, text="Course:", font=("Arial", 10)).grid(row=4, column=0, padx=10, pady=10, sticky="w")

course_combo = ttk.Combobox(root, textvariable=course_var, values=["BCA", "BBA", "BSc", "BIT"], state="readonly", width=22)
course_combo.grid(row=4, column=1)
course_combo.set("Select Course")

# Submit button
tk.Button(root, text="Register", command=save_data, bg="#4CAF50", fg="white", width=15).grid(row=5, column=1, pady=20)

root.mainloop()
```

---

### 🗂️ Output: CSV File Example (`students.csv`)

| Name       | Age | Gender | Course |
| ---------- | --- | ------ | ------ |
| Ram Sharma | 20  | Male   | BCA    |
| Sita Rai   | 21  | Female | BBA    |

---
