### Practice Exercises - List Data Structure

**1. Build a Contact List**

Write a program that starts with an empty list:

```python
contacts = []
```

Ask the user to enter names repeatedly.

* Add each name to the list using `append()`.
* Stop when the user enters `"stop"`.
* After stopping, print all contacts using a `for` loop.
* Capitalize each name when displaying it.

---

**2. Classroom Attendance**

Create a program to take attendance.

* Start with an empty list called `present_students`.
* Ask for a student's name.
* Keep asking until the teacher enters `"done"`.
* Add each student's name to the list.
* Finally, print:

```text
-------- Attendance --------
Ayan
Hari
John

Total students: 3
```

**Challenge:** Research how Python's `len()` function works with lists and use it to display the total number of students. ([Google for Developers][2])

---

**3. Understand Before You Code 🔎**

Do some research and answer these questions **in your own words**:

1. What is a Python list?
2. Why do we use `[]` when creating a list?
3. What does `append()` do?
4. What is the difference between:

   ```python
   students = []
   ```

   and

   ```python
   students = ["Ayan", "Hari"]
   ```
5. What happens if we use `append()` on an empty list?

Then write a small program demonstrating your answers.

---

**4. `while` vs `for` — Research Challenge 🔎**

Research the difference between a **`for` loop** and a **`while` loop** in Python.

Then answer:

* When is a `for` loop useful?
* When is a `while` loop useful?
* Why did we use `while` to collect participant names?
* Why did we use `for` to display the participants?
* What would happen if we replaced the `while` loop in today's program with a `for` loop?

Finally, create a small example showing **one situation where you would choose `for` and one where you would choose `while`**.

---

**5. Modify Today's Program**

Take today's participant program and improve it.

Requirements:

* If the user enters `"stop"`, the program should stop.
* Otherwise, add the name to the list.
* When finished, display all names with `.capitalize()`.
* Display the total number of participants.
* Research and use **one new list feature/method** that you have not learned yet.

**Important:** Don't just copy an example. Find out what the new method does, explain it in **1–2 sentences**, and then use it in your program.
