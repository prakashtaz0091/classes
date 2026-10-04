# Python Modules

## 1. What is a Module in Python?

A **module** is simply a Python file (`.py`) that contains Python code.

A module can contain:

* Variables
* Constants
* Functions
* Classes
* Executable statements

For example:

```python
# calculator.py

PI = 3.14

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
```

Here, `calculator.py` is a **module**.

We can use its code from another Python file instead of writing the same code again.

```python
import calculator

result = calculator.add(10, 20)

print(result)
```

Output:

```text
30
```

---

# 2. Why Do We Need Modules?

Imagine writing a large application in a single file:

```text
app.py
```

The file might contain:

```text
1000+ lines
```

and include:

* User authentication
* Product management
* Payment calculation
* Database operations
* Reports
* Utility functions
* File operations

Maintaining such a file becomes difficult.

Instead, we can divide the application into smaller modules:

```text
project/
│
├── main.py
├── users.py
├── products.py
├── payments.py
├── reports.py
└── utilities.py
```

Each module has a particular responsibility.

This gives us:

> **Modularity + Reusability + Maintainability**

---

# 3. Types of Python Modules

There are three important categories of modules:

```text
Python Modules
│
├── 1. Built-in / Standard Library Modules
│
├── 2. User-defined Modules
│
└── 3. Third-party Modules
```

---

# 4. User-Defined Modules

A **user-defined module** is a Python module created by us.

For example:

```text
bill.py
day7.py
```

Here:

```text
bill.py
```

is our user-defined module.

It contains reusable billing-related functionality.

---

# 5. Our Class Example

We created:

```text
project/
│
├── bill.py
└── day7.py
```

The responsibility of each file is different.

### `bill.py`

Contains billing-related logic:

```python
DISCOUNT_PERCENTAGE = 5
TAX_PERCENTAGE = 13

def calculate_item_total(item_name, cart):
    ...

def calculate_subtotal(cart):
    ...

def calculate_discount(cart):
    ...

def calculate_tax(cart):
    ...

def calculate_final_amount(cart):
    ...

def show_bill_summary(cart):
    ...
```

### `day7.py`

Contains the user interaction:

```python
from bill import show_bill_summary
```

and:

```python
while True:
    ...
```

So we have separated:

```text
day7.py
    ↓
User interaction / program flow

bill.py
    ↓
Billing calculations
```

This is a good example of **separation of responsibilities**.

---

# 6. How Does `from bill import show_bill_summary` Work?

This is an important concept.

In `day7.py` we write:

```python
from bill import show_bill_summary
```

Python interprets this approximately as:

```text
Find bill.py
      ↓
Load/execute bill.py
      ↓
Find show_bill_summary
      ↓
Bring that name into day7.py
```

After importing, we can directly write:

```python
show_bill_summary(user_bag)
```

We don't need to write:

```python
bill.show_bill_summary(user_bag)
```

---

# 7. What Happens When We Run `day7.py`?

Suppose we execute:

```bash
python day7.py
```

Python starts executing `day7.py`.

The first important line is:

```python
from bill import show_bill_summary
```

Python needs to find the `bill` module.

It looks for:

```text
bill.py
```

Then Python loads the module.

Conceptually:

```text
day7.py
   │
   │ import
   ▼
bill.py
   │
   ├── DISCOUNT_PERCENTAGE
   ├── TAX_PERCENTAGE
   ├── calculate_item_total()
   ├── calculate_subtotal()
   ├── calculate_discount()
   ├── calculate_amount_after_discount()
   ├── calculate_tax()
   ├── calculate_final_amount()
   └── show_bill_summary()
```

Python then makes the requested function available in `day7.py`.

```python
show_bill_summary
```

can now be called from `day7.py`.

---

# 8. Important: Import Does Not Mean "Copy the Function"

When we write:

```python
from bill import show_bill_summary
```

Python does **not simply copy-paste** the function into `day7.py`.

Instead, Python loads the module and provides access to the imported object.

A useful mental model is:

```text
bill.py
   │
   │ contains
   ▼
show_bill_summary()
   │
   │ imported
   ▼
day7.py
   │
   │ can now use
   ▼
show_bill_summary()
```

---

# 9. `import module` vs `from module import`

There are two common styles.

## Style 1 — Import the module

```python
import bill
```

Then:

```python
bill.show_bill_summary(user_bag)
```

The module name remains part of the function call.

---

## Style 2 — Import a specific object

```python
from bill import show_bill_summary
```

Then:

```python
show_bill_summary(user_bag)
```

Both are valid.

---

# 10. Importing Multiple Functions

We can do:

```python
from bill import calculate_subtotal, calculate_tax
```

Then:

```python
subtotal = calculate_subtotal(cart)
tax = calculate_tax(cart)
```

---

# 11. Importing Everything

Python also allows:

```python
from bill import *
```

Then all names from `bill.py` become available.

However, this is generally **not recommended**.

Why?

Because it becomes difficult to know where a function came from.

For example:

```python
calculate_tax()
```

Where did this function come from?

```text
bill.py?
tax.py?
utils.py?
```

Better:

```python
from bill import calculate_tax
```

or:

```python
import bill

bill.calculate_tax()
```

---

# 12. Module Aliases

We can give a module another name.

```python
import datetime as dt
```

Now:

```python
dt.datetime.now()
```

instead of:

```python
datetime.datetime.now()
```

Another example:

```python
import random as rnd

number = rnd.randint(1, 100)
```

---

# 13. Built-in / Standard Library Modules

Python comes with a large collection of modules.

These modules are called the **Python Standard Library**.

We don't normally need to install them separately.

Examples:

```text
datetime
random
math
os
pathlib
json
csv
statistics
time
re
collections
```

For example:

```python
import math

print(math.sqrt(25))
```

Output:

```text
5.0
```

---

# 14. Third-Party Modules

Third-party modules are created by developers outside the Python standard library.

Usually, we install them using:

```bash
pip install package_name
```

Examples:

```text
requests
pandas
numpy
openpyxl
flask
django
beautifulsoup4
```

For example:

```bash
pip install requests
```

Then:

```python
import requests

response = requests.get("https://example.com")
```

---

# 15. Comparison

| Type             | Created by          | Installation | Example    |
| ---------------- | ------------------- | ------------ | ---------- |
| User-defined     | Us / our team       | No           | `bill.py`  |
| Standard library | Python developers   | Usually no   | `datetime` |
| Third-party      | External developers | Usually yes  | `requests` |

---

# 16. A Simple Mental Model

Think about modules like a toolbox.

```text
Python
│
├── Standard Library
│      ├── datetime
│      ├── random
│      ├── os
│      ├── pathlib
│      └── json
│
├── Third-party packages
│      ├── requests
│      ├── pandas
│      └── numpy
│
└── Your modules
       ├── bill.py
       ├── users.py
       └── products.py
```

Instead of creating everything ourselves, we reuse tools.

---

# 17. Practical Example — `datetime`

The `datetime` module is useful when working with:

* Current date
* Current time
* Dates
* Times
* Date differences
* Formatting dates
* Adding/subtracting days
* Calculating age
* Deadlines

---

## Get Current Date and Time

```python
from datetime import datetime

now = datetime.now()

print(now)
```

Example:

```text
2026-10-04 22:15:30.123456
```

---

## Get Current Date

```python
from datetime import date

today = date.today()

print(today)
```

---

## Format Date

```python
from datetime import datetime

now = datetime.now()

formatted = now.strftime("%Y-%m-%d")

print(formatted)
```

Output:

```text
2026-10-04
```

Common formatting codes:

| Code | Meaning         |
| ---- | --------------- |
| `%Y` | Four-digit year |
| `%m` | Month           |
| `%d` | Day             |
| `%H` | Hour            |
| `%M` | Minute          |
| `%S` | Second          |

Example:

```python
print(now.strftime("%d/%m/%Y"))
```

Output:

```text
04/10/2026
```

---

# 18. Practical Script — Age Calculator

```python
from datetime import date

birth_year = int(input("Enter your birth year: "))

current_year = date.today().year

age = current_year - birth_year

print(f"You are approximately {age} years old.")
```

---

# 19. Practical Script — Days Until Deadline

```python
from datetime import date

today = date.today()

deadline = date(2026, 12, 31)

remaining_days = deadline - today

print(f"{remaining_days.days} days remaining.")
```

This is useful for:

* Assignment deadlines
* Project deadlines
* Exam countdowns
* Subscription expiry
* Event countdowns

---

# 20. `timedelta`

`timedelta` is useful when we want to add or subtract time.

```python
from datetime import date, timedelta

today = date.today()

next_week = today + timedelta(days=7)

print(next_week)
```

We can also go backwards:

```python
previous_week = today - timedelta(days=7)

print(previous_week)
```

---

# 21. Practical Script — Generate Expiry Date

```python
from datetime import date, timedelta

purchase_date = date.today()

expiry_date = purchase_date + timedelta(days=30)

print("Purchase Date:", purchase_date)
print("Expiry Date:", expiry_date)
```

Useful for:

```text
Subscription
Membership
Trial period
Warranty
Temporary access
```

---

# 22. `random` Module

The `random` module is useful when we need random values.

Examples:

* Random number
* Random choice
* Random password generation
* Games
* OTP-like demos
* Quiz questions
* Randomized testing

---

## Random Integer

```python
import random

number = random.randint(1, 100)

print(number)
```

Possible output:

```text
57
```

Every execution can produce a different number.

---

# 23. Random Choice

```python
import random

colors = ["red", "green", "blue", "yellow"]

selected = random.choice(colors)

print(selected)
```

---

# 24. Simple Dice Program

```python
import random

dice = random.randint(1, 6)

print(f"You rolled: {dice}")
```

---

# 25. Simple Number Guessing Game

```python
import random

secret_number = random.randint(1, 10)

guess = int(input("Guess a number between 1 and 10: "))

if guess == secret_number:
    print("Correct!")
else:
    print(f"Wrong! The number was {secret_number}.")
```

---

# 26. Randomly Select a Student

```python
import random

students = [
    "Ram",
    "Sita",
    "Hari",
    "Gita",
    "John"
]

student = random.choice(students)

print("Today's selected student:", student)
```

This can be useful for classroom activities.

---

# 27. `random.shuffle()`

`shuffle()` randomly rearranges a list.

```python
import random

students = [
    "Ram",
    "Sita",
    "Hari",
    "Gita"
]

random.shuffle(students)

print(students)
```

This can be useful for:

```text
Random quiz order
Random presentation order
Random team selection
Random classroom activities
```

---

# 28. `os` Module

The `os` module allows Python to interact with the operating system.

It can be used for:

* Environment variables
* Current working directory
* Creating directories
* Listing files
* Removing files/directories
* Operating-system information
* File paths

---

# 29. Current Working Directory

```python
import os

current_directory = os.getcwd()

print(current_directory)
```

`getcwd()` means:

> Get Current Working Directory

---

# 30. List Files

```python
import os

files = os.listdir()

print(files)
```

This gives the files and folders in the current directory.

We can also specify a directory:

```python
files = os.listdir("data")

print(files)
```

---

# 31. Check Whether a File Exists

```python
import os

if os.path.exists("bill.py"):
    print("File exists")
else:
    print("File does not exist")
```

---

# 32. Create a Directory

```python
import os

os.mkdir("reports")
```

Now:

```text
project/
│
├── day7.py
├── bill.py
└── reports/
```

---

# 33. `os.makedirs()`

For nested directories:

```python
import os

os.makedirs("data/reports/2026")
```

This can create:

```text
data/
└── reports/
    └── 2026/
```

---

# 34. Environment Variables

The `os` module can also read environment variables.

```python
import os

username = os.getenv("USERNAME")

print(username)
```

Environment variables are commonly used for things such as:

```text
API keys
Database credentials
Configuration
Application settings
```

For example:

```python
import os

api_key = os.getenv("API_KEY")

print(api_key)
```

In real applications, sensitive credentials should generally **not be hard-coded** directly into Python files.

---

# 35. `pathlib` Module

For modern Python programs, `pathlib` is often easier and cleaner for working with paths.

Instead of:

```python
import os

os.path.exists("data/report.txt")
```

we can use:

```python
from pathlib import Path

path = Path("data/report.txt")

print(path.exists())
```

---

# 36. Why `pathlib`?

It provides an object-oriented way of working with paths.

```python
from pathlib import Path

path = Path("data/report.txt")
```

Now we can ask:

```python
path.exists()
path.name
path.parent
path.suffix
path.stem
```

---

# 37. Path Properties

Suppose:

```python
from pathlib import Path

path = Path("reports/annual_report.pdf")
```

Then:

```python
print(path.name)
```

Output:

```text
annual_report.pdf
```

```python
print(path.suffix)
```

Output:

```text
.pdf
```

```python
print(path.stem)
```

Output:

```text
annual_report
```

```python
print(path.parent)
```

Output:

```text
reports
```

---

# 38. Creating Paths

One of the useful features of `pathlib` is `/`.

```python
from pathlib import Path

base_directory = Path("data")

file_path = base_directory / "students.txt"

print(file_path)
```

Output:

```text
data/students.txt
```

This is much cleaner than manually joining strings.

---

# 39. Create a Directory with `pathlib`

```python
from pathlib import Path

reports_directory = Path("reports")

reports_directory.mkdir(exist_ok=True)
```

`exist_ok=True` means:

> If the directory already exists, don't raise an error.

---

# 40. Find Python Files

```python
from pathlib import Path

current_directory = Path(".")

python_files = current_directory.glob("*.py")

for file in python_files:
    print(file)
```

Example:

```text
bill.py
day7.py
calculator.py
```

---

# 41. Recursively Find Files

Suppose we have:

```text
project/
│
├── app.py
├── utils.py
│
└── modules/
    ├── bill.py
    └── user.py
```

We can search recursively:

```python
from pathlib import Path

project = Path(".")

for file in project.rglob("*.py"):
    print(file)
```

Output:

```text
app.py
utils.py
modules/bill.py
modules/user.py
```

---

# 42. Practical Script — File Explorer

We can combine `pathlib` and `os` concepts.

```python
from pathlib import Path

directory = Path(".")

for item in directory.iterdir():

    if item.is_file():
        print("FILE :", item)

    elif item.is_dir():
        print("DIR  :", item)
```

This creates a simple directory explorer.

---

# 43. Practical Script — Count Python Files

```python
from pathlib import Path

directory = Path(".")

python_files = list(directory.rglob("*.py"))

print("Python files:", len(python_files))
```

---

# 44. Practical Script — Find Large Files

```python
from pathlib import Path

directory = Path(".")

for file in directory.rglob("*"):

    if file.is_file():

        size = file.stat().st_size

        if size > 1024 * 1024:
            print(file, size, "bytes")
```

This can be extended into a useful disk-analysis tool.

---

# 45. Another Useful Standard Module — `math`

```python
import math

print(math.sqrt(25))
print(math.ceil(4.2))
print(math.floor(4.8))
print(math.pi)
```

Output:

```text
5.0
5
4
3.141592653589793
```

Useful for:

```text
Mathematical calculations
Geometry
Scientific programs
Financial calculations
```

---

# 46. Another Useful Module — `json`

JSON is extremely common when working with APIs and configuration data.

```python
import json

student = {
    "name": "Ram",
    "age": 20,
    "course": "Python"
}

json_data = json.dumps(student)

print(json_data)
```

Output:

```text
{"name": "Ram", "age": 20, "course": "Python"}
```

---

# 47. Convert JSON Back to Python

```python
import json

data = '{"name": "Ram", "age": 20}'

student = json.loads(data)

print(student["name"])
```

Output:

```text
Ram
```

The basic relationship is:

```text
Python dictionary
       ↓
    json.dumps()
       ↓
    JSON string
```

and:

```text
JSON string
       ↓
    json.loads()
       ↓
Python dictionary
```

---

# 48. Another Useful Module — `statistics`

```python
import statistics

marks = [70, 80, 90, 60, 75]

print(statistics.mean(marks))
```

Output:

```text
75
```

Other useful functions:

```python
statistics.mean()
statistics.median()
statistics.mode()
```

---

# 49. Combining Multiple Modules

Modules become especially powerful when we combine them.

For example:

```python
from datetime import datetime
from pathlib import Path
import random
```

We could create a simple log generator:

```python
from datetime import datetime
from pathlib import Path
import random

log_file = Path("activity.log")

actions = [
    "LOGIN",
    "LOGOUT",
    "VIEW_PRODUCT",
    "ADD_TO_CART"
]

action = random.choice(actions)

timestamp = datetime.now()

log_entry = f"{timestamp} - {action}\n"

with log_file.open("a") as file:
    file.write(log_entry)

print("Activity recorded.")
```

Here we are using:

```text
datetime → timestamp
random   → random activity
pathlib  → file path
```

This is where modules become very useful in real programs.

---

# 50. Connecting This Back to Your `bill.py`

Your project demonstrates a very important programming principle.

Instead of putting everything inside:

```text
day7.py
```

we moved billing logic into:

```text
bill.py
```

So:

```text
day7.py
│
├── Input
├── Menu
├── Cart management
└── Program flow
        │
        │ calls
        ▼
     bill.py
        │
        ├── calculate_item_total()
        ├── calculate_subtotal()
        ├── calculate_discount()
        ├── calculate_tax()
        └── calculate_final_amount()
```

This makes the code easier to understand and maintain.

---

# 51. Key Concept to Remember

A module helps us organize code.

A function helps us organize logic.

So we can have:

```text
Application
    │
    ├── Modules
    │      │
    │      ├── Functions
    │      │
    │      └── Classes
    │
    └── Program flow
```

For your application:

```text
day7.py
    │
    └── User interaction

bill.py
    │
    ├── calculate_item_total()
    ├── calculate_subtotal()
    ├── calculate_discount()
    ├── calculate_tax()
    └── calculate_final_amount()
```

---

# 54. Recommended Modules to Learn

As a beginner, these are particularly useful:

| Module        | Main Purpose                 |
| ------------- | ---------------------------- |
| `math`        | Mathematical operations      |
| `random`      | Random values and selections |
| `datetime`    | Dates and times              |
| `time`        | Time-related operations      |
| `os`          | Operating system interaction |
| `pathlib`     | File and directory paths     |
| `json`        | JSON data                    |
| `csv`         | CSV files                    |
| `statistics`  | Statistical calculations     |
| `re`          | Regular expressions          |
| `collections` | Specialized data structures  |
| `sqlite3`     | SQLite databases             |

Later, third-party libraries can be introduced:

| Package          | Common Use          |
| ---------------- | ------------------- |
| `requests`       | HTTP/API requests   |
| `numpy`          | Numerical computing |
| `pandas`         | Data analysis       |
| `openpyxl`       | Excel files         |
| `flask`          | Web applications    |
| `django`         | Web applications    |
| `beautifulsoup4` | HTML parsing        |

---

# 55. Final Summary

### Module

A `.py` file containing reusable Python code.

```python
bill.py
```

### User-defined module

A module created by us.

```python
from bill import show_bill_summary
```

### Standard library module

Comes with Python.

```python
import datetime
import random
import os
from pathlib import Path
```

### Third-party module

Created outside Python's standard library and usually installed separately.

```bash
pip install requests
```

Then:

```python
import requests
```

---

## The Big Picture

```text
                    PYTHON MODULES
                         │
          ┌──────────────┼──────────────┐
          │              │              │
          ▼              ▼              ▼
     User-defined    Standard       Third-party
       modules        library         modules
          │              │              │
          ▼              ▼              ▼
       bill.py        datetime       requests
       users.py       random         pandas
       products.py    pathlib        numpy
                      os             flask
```

The main idea is:

> **Don't put everything into one Python file. Break your program into logical, reusable modules and import what you need.**

And your `bill.py` example demonstrates exactly that: **`day7.py` handles the application flow, while `bill.py` handles billing logic.**
