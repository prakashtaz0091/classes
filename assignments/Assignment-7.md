# Assignment Questions

## **1. List Comprehension (Basics)**

1. Given the list

   ```python
   nums = [2, 5, 7, 10, 13]
   ```

   Create a new list containing the **cube** of each number using list comprehension.

2. From the list

   ```python
   nums = [3, 8, 12, 15, 18, 21]
   ```

   Create a new list that contains **only the numbers divisible by 3**.

3. Given

   ```python
   words = ["apple", "cat", "banana", "car", "dog"]
   ```

   Create a list that contains only the words **that do NOT start with 'c'**.

---

## **2. Dictionary Comprehension**

4. Given the dictionary

   ```python
   scores = {1: 55, 2: 80, 3: 40, 4: 90}
   ```

   Create a new dictionary containing **only the items where the score is above 60**.

5. Convert this dictionary into a reverse dictionary (swap key ↔ value)

   ```python
   colors = {
       1: "red",
       2: "blue",
       3: "green"
   }
   ```

---

## **3. Exception Handling**

6. Write a program that:

   - Takes a number from the user
   - Tries to convert it to an integer
   - If the user enters something invalid, print:
     `"Invalid input! Please enter a number."`

7. Write a program that:

   - Asks the user for two numbers
   - Tries to divide them
   - Handles:

     - `ValueError` → when input is not a number
     - `ZeroDivisionError` → when denominator is 0
     - `Exception` → any other error

   - Prints `"Division successful!"` inside the `else` block.

---

## **4. File Handling**

# **File Handling Examples (with Code)**

---

# **1. Writing to a File (`w` mode)**

✔ Creates the file if it doesn’t exist
✔ Overwrites the file if it already exists

### **Example 1: Write a single line**

```python
file = open("hello.txt", "w")
file.write("Hello students!")
file.close()
```

---

### **Example 2: Write multiple lines**

```python
file = open("fruits.txt", "w")
file.write("Apple\n")
file.write("Banana\n")
file.write("Mango\n")
file.close()
```

---

# **2. Reading from a File (`r` mode)**

✔ File must already exist
✔ Used to read data

### **Example 3: Read entire file**

```python
file = open("hello.txt", "r")
content = file.read()
print(content)
file.close()
```

---

### **Example 4: Read line by line**

```python
file = open("fruits.txt", "r")
for line in file:
    print(line.strip())  # strip() removes \n
file.close()
```

---

### **Example 5: Read all lines into a list**

```python
file = open("fruits.txt", "r")
lines = file.readlines()
print(lines)
file.close()
```

---

# **3. Appending to a File (`a` mode)**

✔ Adds new content at the end
✔ Does not delete previous data

### **Example 6: Append lines**

```python
file = open("fruits.txt", "a")
file.write("Orange\n")
file.close()
```

---

# **4. Using `with open()` (Best Practice)**

✔ Automatically closes the file
✔ Prevents mistakes like forgetting `close()`

### **Example 7: Writing with `with`**

```python
with open("city.txt", "w") as f:
    f.write("Mumbai\n")
    f.write("Delhi\n")
    f.write("Chennai\n")
```

---

### **Example 8: Reading with `with`**

```python
with open("city.txt", "r") as f:
    print(f.read())
```

---

# **5. Example: Reading Numbers & Doing Something with Them**

Assume **numbers.txt** contains:

```
10
20
30
40
50
```

### **Example 9: Read numbers and calculate sum**

```python
with open("numbers.txt", "r") as f:
    total = 0
    for line in f:
        total += int(line.strip())

print("Total =", total)
```

---

# **6. Example: Write User Input to a File**

### **Example 10: Ask the user for 3 names and save them**

```python
with open("names.txt", "w") as f:
    for i in range(3):
        name = input("Enter a name: ")
        f.write(name + "\n")
```

---

# **7. Example: Read a File Safely (with Exception Handling)**

### **Example 11: Handle file-not-found error**

```python
try:
    with open("unknown.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("File does not exist!")
```

---
