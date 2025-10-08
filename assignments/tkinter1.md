# 🎓 Tkinter Practice Assignments — Student Registration Project

You already learned how to create a **Student Registration Form** using `tkinter`, `ttk`, and `csv`.

Now, let’s improve it step by step!  
Each task builds on the example you saw in class.

---

## 🧩 Assignment 1 — Add More Fields

### 🎯 Goal:

Add extra input fields and store them in the same CSV file.

### 📝 Task:

Add the following new fields:

- `Email`
- `Phone Number`

### 💡 Hint:

You’ll need:

- Two new `StringVar()` variables.
- Two new `Label` and `Entry` widgets.
- Include them in `save_data()` and `writer.writerow()`.

### ✅ Example Code:

```python
email_var = tk.StringVar()
phone_var = tk.StringVar()

tk.Label(root, text="Email:", font=("Arial", 10)).grid(row=7, column=0, padx=10, pady=10, sticky="w")
tk.Entry(root, textvariable=email_var, width=25).grid(row=7, column=1)

tk.Label(root, text="Phone:", font=("Arial", 10)).grid(row=8, column=0, padx=10, pady=10, sticky="w")
tk.Entry(root, textvariable=phone_var, width=25).grid(row=8, column=1)

# In save_data()
email = email_var.get().strip()
phone = phone_var.get().strip()

if not (email and phone):
    messagebox.showerror("Error", "All fields are required!")
    return

writer.writerow([name, age, address, gender, class_, email, phone])
```

---

## 🧩 Assignment 2 — Validate Email and Phone

### 🎯 Goal:

Add simple input validation for new fields.

### 📝 Task:

- Check if email contains `@` and `.`
- Check if phone has **exactly 10 digits**

### ✅ Example Code:

```python
if "@" not in email or "." not in email:
    messagebox.showerror("Error", "Invalid email format!")
    return

if not phone.isdigit() or len(phone) != 10:
    messagebox.showerror("Error", "Phone must be 10 digits!")
    return
```

---

## 🧩 Assignment 3 — Display Registered Students

### 🎯 Goal:

Add a **button** that opens a new window showing all saved records.

### 📝 Task:

- Read data from `students.csv`
- Show in a simple `Treeview` table

### ✅ Example Code:

```python
def show_students():
    try:
        with open("students.csv", "r") as file:
            reader = csv.reader(file)
            data = list(reader)
    except FileNotFoundError:
        messagebox.showerror("Error", "No student records found!")
        return

    win = tk.Toplevel(root)
    win.title("Registered Students")
    win.geometry("600x300")

    tree = ttk.Treeview(win, columns=("Name","Age","Address","Gender","Class","Email","Phone"), show="headings")
    for col in ("Name","Age","Address","Gender","Class","Email","Phone"):
        tree.heading(col, text=col)
        tree.column(col, width=80)
    tree.pack(fill="both", expand=True)

    for row in data:
        tree.insert("", tk.END, values=row)

# Add button below Register button
tk.Button(root, text="Show Students", command=show_students, bg="#2196F3", fg="white", width=15).grid(row=9, column=1, pady=5)
```

---

## 🧩 Assignment 4 — Clear All Records

### 🎯 Goal:

Add a **“Clear All Records”** button that empties the CSV file (with confirmation).

### ✅ Example Code:

```python
def clear_records():
    confirm = messagebox.askyesno("Confirm", "Are you sure you want to delete all student records?")
    if confirm:
        open("students.csv", "w").close()
        messagebox.showinfo("Cleared", "All records deleted successfully!")

tk.Button(root, text="Clear Records", command=clear_records, bg="#f44336", fg="white", width=15).grid(row=10, column=1, pady=5)
```

---

## 🧩 Assignment 5 — Auto Generate Student ID

### 🎯 Goal:

Automatically assign a unique ID to each student (e.g., S001, S002, ...).

### 📝 Hint:

- Count existing rows in `students.csv`
- Generate ID using that count + 1

### ✅ Example Code:

```python
def generate_id():
    try:
        with open("students.csv", "r") as file:
            return f"S{len(list(csv.reader(file))) + 1:03d}"
    except FileNotFoundError:
        return "S001"

# In save_data():
student_id = generate_id()
writer.writerow([student_id, name, age, address, gender, class_, email, phone])
```

### 💬 Note:

Don’t just copy the code — try changing labels, fonts, order, or logic slightly.
Your goal is to understand how `Tkinter` widgets, variables, and functions work together.

---
