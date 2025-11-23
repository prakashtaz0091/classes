# **Python Assignment — Functions, \*args, and **kwargs\*\*

You have learned how functions work, how to use `*args`, `**kwargs`, and how to create a simple student management system.

Now, complete the following tasks.
Write each program separately.

---

### **Task 1: Sum Using `*args`**

Write a function called `total_sum()` that accepts any amount of numbers using `*args` and prints the total.

**Example Output:**

```
total_sum(5,10,2,3)
Output: 20
```

---

### **Task 2: Display User Profile Using `**kwargs`\*\*

Write a function called `show_profile()` that takes any user information using `**kwargs` and prints it in this format:

```
name => Ram
age => 22
city => Pokhara
```

You can call it like:

```python
show_profile(name="Ram", age=22, city="Pokhara")
```

---

### **Task 3: Create a Contact Book**

Create a program with the following menu:

```
1. Add Contact
2. Show Contacts
3. Remove Contact
Q. Quit
```

Each contact must store:

- name
- phone
- email

Use a list of dictionaries to store the data — similar to the student program you learned in class.

---

### **Task 4: Count Students Based on Age**

Using the student list program from class:

- Ask the user: `"Enter age:"`
- Then print how many students are older than that age.

**Example:**

```
Enter age: 18
Output: 4 students are older than 18.
```

---

### **Task 5: Update Student Data (NEW FEATURE)**

Add a new option to your student program:

```
4. Update Student Data
```

**When updating:**

- Ask for the student name
- If found, ask whether they want to update `"name"` or `"age"`
- Update the dictionary value

Example:

```
Enter student name to update: Ram
What do you want to update?
1. Name
2. Age
Enter choice: 2
Enter new age: 21
Student updated successfully!
```

---

---

### Bonus Task (Optional)

Add a feature to prevent adding duplicate student names.

---
