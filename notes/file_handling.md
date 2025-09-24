File handling in Python is all about working with files — creating, reading, writing, and closing them. Python makes this process straightforward with built-in functions. Here’s a breakdown:

---

## 1. Opening a File

You use the built-in `open()` function:

```python
file = open("example.txt", "mode")
```

### Common modes:

- `"r"` → Read (default). File must exist.
- `"w"` → Write. Creates new file or overwrites existing.
- `"a"` → Append. Adds to end of file if it exists.
- `"x"` → Create. Fails if file already exists.
- `"b"` → Binary mode (e.g., `"rb"`, `"wb"`).
- `"t"` → Text mode (default).

Example:

```python
f = open("data.txt", "r")  # open in read mode
```

---

## 2. Reading a File

There are several ways to read:

```python
f = open("data.txt", "r")

print(f.read())        # read entire file
print(f.read(10))      # read first 10 characters
print(f.readline())    # read one line
print(f.readlines())   # read all lines into a list

f.close()
```

---

## 3. Writing to a File

```python
f = open("data.txt", "w")  # overwrite mode
f.write("Hello, Python!\n")
f.write("File handling is easy.")
f.close()
```

Appending instead of overwriting:

```python
f = open("data.txt", "a")
f.write("\nThis line is added at the end.")
f.close()
```

---

## 4. Using `with` Statement (Best Practice)

The `with` statement automatically closes the file for you:

```python
with open("data.txt", "r") as f:
    content = f.read()
    print(content)
```

---

## 5. Working with Binary Files

For images, audio, etc.:

```python
with open("image.jpg", "rb") as f:
    data = f.read()
```

---

## 6. Checking File Existence

```python
import os

if os.path.exists("data.txt"):
    print("File exists")
else:
    print("File does not exist")
```

---

✅ **In summary**:

- Use `open()` with the right mode.
- Use `read()`, `readline()`, or `readlines()` to read.
- Use `write()` or `writelines()` to write.
- Always close the file, or better — use `with`.

---

## 🔹 What is a CSV File?

- **CSV** stands for **Comma-Separated Values**.
- It’s a simple text file where data is stored in **rows and columns**, separated by commas (or sometimes tabs/semicolons).
- Example:

```
Name, Age, City
Alice, 25, New York
Bob, 30, London
Charlie, 28, Sydney
```

---

## 🔹 Handling CSV Files in Python

Python has a built-in module: **`csv`**.

---

### 1. Reading a CSV File

```python
import csv

with open("people.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)   # each row is a list
```

**Output:**

```
['Name', 'Age', 'City']
['Alice', '25', 'New York']
['Bob', '30', 'London']
['Charlie', '28', 'Sydney']
```

---

### 2. Writing to a CSV File

```python
import csv

data = [
    ["Name", "Age", "City"],
    ["Alice", 25, "New York"],
    ["Bob", 30, "London"],
    ["Charlie", 28, "Sydney"]
]

with open("people.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)   # write multiple rows
```

---

### 3. Using `DictReader` and `DictWriter`

Works with dictionaries instead of lists.

```python
import csv

# Writing with DictWriter
with open("people.csv", "w", newline="") as file:
    fieldnames = ["Name", "Age", "City"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()  # writes column names
    writer.writerow({"Name": "Alice", "Age": 25, "City": "New York"})
    writer.writerow({"Name": "Bob", "Age": 30, "City": "London"})

# Reading with DictReader
with open("people.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)   # each row is an OrderedDict
```

**Output:**

```
{'Name': 'Alice', 'Age': '25', 'City': 'New York'}
{'Name': 'Bob', 'Age': '30', 'City': 'London'}
```

---

### 4. Handling Different Delimiters

Not all CSVs use commas — some use semicolons (`;`) or tabs (`\t`):

```python
import csv

with open("data.tsv", "r") as file:   # tab-separated file
    reader = csv.reader(file, delimiter="\t")
    for row in reader:
        print(row)
```

---

✅ **In summary:**

- Use `csv.reader()` to **read CSV** as lists.
- Use `csv.writer()` to **write CSV** from lists.
- Use `DictReader` / `DictWriter` for **dictionary-based handling**.
- Always use `newline=""` when writing (prevents blank lines on Windows).

---
