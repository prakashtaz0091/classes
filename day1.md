# **Python Notes for Beginners**

---

## 1. What is Software?

- **Software** is a collection of **programs** that tell a computer what to do and how to do it.
- It is the **set of instructions** that make hardware useful.

**Examples:**

- Microsoft Word – helps us create documents.
- Google Chrome – helps us browse the internet.
- Python – a software that helps us write and execute other programs.

---

## 2. What is a Program?

- A **program** is a **set of instructions** written in a **programming language** to perform a specific task.

**Example:**

```python
print("Hello, World!")
```

This small program instructs the computer to display the text “Hello, World!” on the screen. Small programs are combined to form **applications** and **softwares**.

---

## 3. Evolution of Programming Languages

Computers understand only **machine language (0s and 1s)**, which is very difficult for humans to use.
To make programming easier, languages evolved over time.

| Stage | Language Type            | Example             | Description                                                      |
| :---- | :----------------------- | :------------------ | :--------------------------------------------------------------- |
| 1     | **Machine Language**     | `10110000 01100001` | Written in binary (0s and 1s), hard for humans to understand.    |
| 2     | **Assembly Language**    | `MOV AL, 61h`       | Uses mnemonics (short codes), slightly easier but still complex. |
| 3     | **High-Level Languages** | `print("Hello")`    | Easy to read and write, closer to human language.                |

**Python** is a **high-level language**, meaning we can write simple, human-readable code.
Internally, Python is **built using C**, a lower-level language that communicates with hardware more directly.

---

## 4. Translators: Assembler, Compiler, and Interpreter

Computers only understand **machine code**, so we use **translators** to convert our source code into machine-readable form.

| Translator      | Converts                      | Commonly Used For                 | Example            |
| :-------------- | :---------------------------- | :-------------------------------- | :----------------- |
| **Assembler**   | Assembly → Machine Code       | Low-level programming             | Device drivers     |
| **Compiler**    | Entire program → Machine Code | Languages like C, C++             | GCC Compiler       |
| **Interpreter** | Line by line → Machine Code   | Languages like Python, JavaScript | Python Interpreter |

**Python uses both compiler and interpreter:**

1. The **Python compiler** first converts your code into **bytecode (.pyc)**.
2. The **Python interpreter** then executes that bytecode line by line.

To run Python programs, we must install the **Python Interpreter**.

**Example (running a Python file):**

```bash
python hello.py
```

Here, `python` is the interpreter that executes your code.

---

## 5. Programming is About Data and Data Manipulation

Programming is fundamentally about working with **data**:

- Storing data
- Processing data
- Producing meaningful output

**Example:**

```python
x = 5
y = 3
print(x + y)
```

This program manipulates data (numbers) to produce a new result (8).

---

## 6. To Manipulate Data, we temporarily Store it.

Data are stored in computer memory (RAM) temporarily, so that we can use them in our programs when we need them. But remembering memory addresses eg. `0x1234` is not easy. So this is where **variables** come into play. Variables do hardwork for us, so that we don't have to remember memory addresses. Also in other words, variable i.e. **vary** + **able**, means that it can be changed. We can change the value of a variable at any time.
For example.

```python
x = 5
#.... other code

x = 10

print(x)

```

- This program prints the value of `x` which is 10. Program runs from top to bottom. So first it stores 5 in `x` and then changes the value of `x` to 10. Finally it prints the value of `x` which is 10.

## 7. Built-in Data Types in Python

Python provides several **built-in data types** that we use to store and work with different kinds of data.

| Data Type    | Example                        | Description                         |
| :----------- | :----------------------------- | :---------------------------------- |
| **int**      | `10`, `-5`, `0`                | Integer numbers                     |
| **float**    | `3.14`, `-2.7`                 | Decimal numbers                     |
| **complex**  | `2 + 3j`                       | Complex numbers                     |
| **str**      | `"Hello"`, `'Python'`          | String or text data                 |
| **bool**     | `True`, `False`                | Logical values                      |
| **list**     | `[1, 2, 3]`                    | Ordered and changeable collection   |
| **tuple**    | `(1, 2, 3)`                    | Ordered and unchangeable collection |
| **set**      | `{1, 2, 3}`                    | Unordered and unique collection     |
| **dict**     | `{"name": "Alice", "age": 20}` | Key-value pairs                     |
| **NoneType** | `None`                         | Represents “no value” or “nothing”  |

**Example in Code:**

```python
a = 10          # int
b = 3.14        # float
c = "Python"    # str
d = [1, 2, 3]   # list
e = None        # NoneType
```

---

## 8. Importance of NoneType

`None` is a special value in Python that represents **“no value”** or **“nothing here yet.”**

It is not:

- `0` (zero)
- `False`
- or an empty string `""`

It is its own unique data type: **NoneType**

**Example:**

```python
x = None
print(x)
```

Output:

```
None
```

**Uses of None:**

- A function that doesn’t return anything automatically returns `None`.
- When you want to create a variable but don’t have a value for it yet.

**Example:**

```python
result = None
if condition_met:
    result = 10
```

In this way, `None` acts as a placeholder to indicate that a value is not yet assigned.

---

## Summary

| Concept                 | Key Idea                                                     |
| :---------------------- | :----------------------------------------------------------- |
| **Software**            | Collection of programs to perform specific tasks             |
| **Program**             | A set of instructions written in a programming language      |
| **Language Evolution**  | Machine → Assembly → High-Level (Python)                     |
| **Translators**         | Convert human code into machine code                         |
| **Python Interpreter**  | Executes Python programs using both compiler and interpreter |
| **Programming**         | Involves working with and manipulating data                  |
| **Built-in Data Types** | int, float, str, list, tuple, set, dict, bool, NoneType      |
| **NoneType**            | Represents the absence of a value                            |

---
