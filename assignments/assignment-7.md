# Assignment – File Handling (Text File & CSV File)

---

## **Part 1: Text File (7 Questions)**

1. Write a program to create a text file `notes.txt` and write your name into it.
   _Hint: Use `open("notes.txt", "w")` and `file.write()`._

2. Append a new line `"I am learning Python"` to `notes.txt`.
   _Hint: Use `"a"` mode._

3. Read and display the content of `notes.txt`.
   _Hint: Use `"r"` mode and `file.read()`._

4. Write a program to store 5 student names into `students.txt`, each on a new line.

5. Read `students.txt` and display all student names with serial numbers.
   _Hint: Use `for line in file` and `enumerate`._

6. Count how many lines (students) are inside `students.txt`.
   _Hint: Use `len(file.readlines())`._

7. Write a program that asks user input continuously and saves every input into `log.txt` until user types `"exit"`.

---

## **Part 2: CSV File (7 Questions)**

📌 **Note**: CSV files are like text files, but values are separated by commas. Python has a built-in `csv` module to handle them easily.

8. Create a CSV file `students.csv` with columns: `id, name, age`. Insert one record into it.
   _Hint: Use `csv.writer` with `"w"` mode._

9. Append another student record into `students.csv`.
   _Hint: Use `"a"` mode so data is not erased._

10. Read and display all student records from `students.csv`.
    _Hint: Use `csv.reader` in `"r"` mode._

11. Write a program to store 3 product details (`id, name, price`) into `products.csv`.

12. Read `products.csv` and display all products in a tabular format.
    _Hint: Loop through rows and print._

13. Count total number of records (rows) inside `students.csv`.

14. Write a program that asks user input (`id, name, age`) and saves it as a new row in `students.csv`.

---

## **Part 3: Menu-Driven Program Examples (CSV)**

Here we practice real simulations, where data is saved permanently in a CSV file.

---

### **1: Employee Management (Add, View, Exit)**

- Functions you can make:

  - `add_employee()` → Takes input and writes to `employees.csv`
  - `show_employees()` → Reads and prints all employees
  - `show_menu()` → Displays menu options

- Main program runs in a loop:

  - 1 → Add employee
  - 2 → Show employees
  - 3 → Exit

---

## **Part 4: How Update & Delete Works in CSV**

- A CSV file is like a text file.
- You **cannot directly change one row inside it**. Instead:

  1. Read all rows into a list.
  2. Modify the row (update or delete).
  3. Write all rows back into the CSV file (overwrite).

---

### **Example: Update a Student’s Age**

Steps:

1. Read all rows from `students.csv`.
2. Loop through each row, if `id` matches → change the `age`.
3. Write all rows back to the file.

```python
import csv

def update_student(student_id, new_age):
    rows = []
    with open("students.csv", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] == student_id:
                row[2] = new_age  # update age
            rows.append(row)
    with open("students.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(rows)

update_student("1", "22")
```

---

### **Example: Delete a Student**

Steps:

1. Read all rows.
2. Skip the row that matches `id`.
3. Write the remaining rows back.

```python
import csv

def delete_student(student_id):
    rows = []
    with open("students.csv", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] != student_id:  # skip row to delete
                rows.append(row)
    with open("students.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(rows)

delete_student("1")
```
