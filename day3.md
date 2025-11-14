# **📘 Python Notes – Control Flow Statements**

Control flow statements help Python decide:

1. **What to do**
2. **When to do it**
3. **How many times to do it**

There are two main parts:

- **A. Conditional Statements**
- **B. Looping Statements**

---

# **A. Conditional Statements**

Conditional statements let your program choose between different actions based on conditions.

---

# **1. `if` Statement**

Used when you want to run a block of code **only if** a condition is true.

### **Syntax**

```python
if condition:
    statement(s)
```

### **Example**

```python
x = 10
if x > 5:
    print("x is greater than 5")
```

---

# 🌟 **IMPORTANT: Understanding Indentation in Python**

This is the first time you see a “space at the beginning of a line”.
Python uses **indentation** to define blocks of code.

### **What is indentation?**

Indentation means adding **spaces or a tab** before a line of code.

Usually:

- **4 spaces** (most recommended), or
- **1 Tab** (your editor converts it to spaces)

### **Why is indentation needed?**

In languages like C, C++, or Java, blocks are written using `{ }`.

But in Python:

👉 **Indentation decides which statements belong inside a block.**
(No `{ }`, no `end`, no `begin` — just indentation.)

Whenever you see a line ending with `:`,
the next line MUST be indented.

### **Example with labeled indentation**

```python
if x > 5:        # No indentation here
    print("Yes") # This line is indented → inside the if block
```

### **Example (wrong)**

```python
if x > 5:
print("Yes")   # ❌ Error: missing indentation
```

### **Example (correct)**

```python
if x > 5:
    print("Yes")   # ✔ Proper indentation
```

📌 **Indentation is one of the most important rules to learn in Python.**

---

# **2. `if-else` Statement**

### **Syntax**

```python
if condition:
    statements
else:
    statements
```

### **Example**

```python
age = 17
if age >= 18:
    print("You can vote.")
else:
    print("You cannot vote.")
```

---

# **3. `if-elif-else` Statement**

### **Syntax**

```python
if condition1:
    block1
elif condition2:
    block2
else:
    block3
```

### **Example**

```python
marks = 72

if marks >= 90:
    print("A+ Grade")
elif marks >= 75:
    print("A Grade")
elif marks >= 60:
    print("B Grade")
else:
    print("C Grade")
```

---

# **B. Looping Statements**

Loops help you repeat actions.

Python provides two main loops:

1. **for loop**
2. **while loop**

---

# **1. `for-in` Loop**

A `for` loop goes through items one by one.

---

## **A. For Loop With Strings**

### **Example**

```python
text = "Hello"

for ch in text:
    print(ch)
```

### Output:

```
H
e
l
l
o
```

---

## **B. For Loop With `range()`**

`range()` generates numbers. Useful when you want to run a loop a fixed number of times.

### **Basic Example**

```python
for i in range(5):
    print(i)
```

### Output

```
0
1
2
3
4
```

### **range() Variations**

#### 1. range(stop)

```python
for i in range(5):
    print(i)
```

#### 2. range(start, stop)

```python
for i in range(2, 6):
    print(i)
```

Output: 2, 3, 4, 5

#### 3. range(start, stop, step)

```python
for i in range(1, 10, 2):
    print(i)
```

Output: 1, 3, 5, 7, 9

---

# **2. `while` Loop**

Runs as long as the condition is true.

### Example

```python
i = 1
while i <= 5:
    print(i)
    i += 1
```

---

# **3. `break` and `continue`**

## **A. `break`**

Exits the loop immediately.

### Example

```python
for i in range(10):
    if i == 5:
        break
    print(i)
```

---

## **B. `continue`**

Skips the current iteration and moves to the next.

### Example

```python
for i in range(5):
    if i == 2:
        continue
    print(i)
```

---

# **📌 Extra Note**

You have now learned:

- Conditional statements
- Indentation
- For-loops with strings and range()
- While loops
- break & continue

In future lessons, you will learn how loops work with **data structures**, such as:

- Lists
- Tuples
- Dictionaries
- Sets

These make loops even more powerful and useful for real programs.

---
