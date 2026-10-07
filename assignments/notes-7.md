# Python Notes: Decorators, Exception Handling, Iterators, Generators, and File Iteration

These notes explain the concepts from the class examples step by step, with an emphasis on **what happens internally**, **why we use each concept**, and **how these ideas are used in real applications such as Django**.

---

# 1. Decorators in Python

## 1.1 What is a decorator?

A **decorator** is a function that takes another function as input and **adds or changes its behavior without modifying the original function's code**.

In simple terms:

> A decorator wraps a function and adds some extra functionality around it.

For example, suppose we have:

```python
def home():
    print("Homepage")
```

We may want to check whether the user is logged in before allowing `home()` to execute.

Instead of putting this check inside every function:

```python
def home():
    if logged_in:
        print("Homepage")
```

we can create a decorator that handles the login check.

---

# 2. Understanding the `login_required` Example

Consider:

```python
logged_in = True

def login_required(func):
    def wrapper_func():
        if logged_in:
            func()
        else:
            print("Please login to access this page")
    
    return wrapper_func
```

Let's understand this carefully.

## Step 1: `login_required` receives a function

```python
def login_required(func):
```

Here, `func` is expected to be another function.

For example:

```python
def home():
    print("Homepage")
```

If we do:

```python
login_required(home)
```

then:

```text
func → home
```

So inside `login_required`, `func` refers to the `home` function.

---

## Step 2: Define a wrapper function

Inside the decorator:

```python
def wrapper_func():
```

This function will control whether the original function should execute.

```python
def wrapper_func():
    if logged_in:
        func()
    else:
        print("Please login to access this page")
```

The important part is:

```python
func()
```

This calls the **original function**.

---

## Step 3: Return the wrapper

```python
return wrapper_func
```

The decorator doesn't immediately execute the original function.

It returns a **new function**.

So conceptually:

```text
home()
   ↓
wrapper_func()
   ↓
check logged_in
   ↓
func()
   ↓
original home()
```

---

# 3. Using the Decorator Manually

We can use the decorator without the `@` syntax:

```python
def home():
    print("Homepage")

home = login_required(home)

home()
```

Initially:

```text
home → original home function
```

After:

```python
home = login_required(home)
```

the reference changes:

```text
home → wrapper_func
```

Therefore:

```python
home()
```

actually calls:

```python
wrapper_func()
```

which then checks:

```python
if logged_in:
```

and eventually calls the original `home()`.

---

# 4. The `@decorator` Syntax

Python provides a shorter syntax:

```python
@login_required
def home():
    print("Homepage")
```

This is equivalent to:

```python
def home():
    print("Homepage")

home = login_required(home)
```

So:

```python
@login_required
def home():
```

does **not** mean that `login_required` is called every time `home()` is called.

It means that **when the function is defined**, Python effectively does:

```python
home = login_required(home)
```

---

# 5. Complete Decorator Example

```python
logged_in = True

def login_required(func):

    def wrapper_func():
        if logged_in:
            func()
        else:
            print("Please login to access this page")

    return wrapper_func


@login_required
def home():
    print("Homepage")


home()
```

### Execution flow

```text
@login_required
       ↓
login_required(home)
       ↓
wrapper_func returned
       ↓
home now refers to wrapper_func
       ↓
home()
       ↓
wrapper_func()
       ↓
logged_in?
       ↓
Yes
       ↓
original home()
       ↓
Homepage
```

---

# 6. Why Are Decorators Useful?

Decorators are useful when the **same behavior needs to be applied to many functions**.

For example:

* Login checking
* Permission checking
* Logging
* Timing functions
* Caching
* Authentication
* Authorization
* Validation
* Transaction handling

For example:

```python
@login_required
def home():
    pass


@login_required
def profile():
    pass


@login_required
def dashboard():
    pass
```

We don't need to write:

```python
if logged_in:
```

inside every function.

The decorator handles the common behavior.

---

# 7. Decorators in Django

The idea is very important in Django.

For example:

```python
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    ...
```

The purpose is similar to our class example:

```python
@login_required
def home():
```

The decorator checks whether the user is authenticated before allowing the view to execute.

This is an example of **separation of concerns**.

The view focuses on:

```text
What should this page do?
```

while the decorator focuses on:

```text
Is the user allowed to access this page?
```

---

# 8. Important Problem: Decorators and Return Values

Consider:

```python
def login_required(func):
    def wrapper_func():
        if logged_in:
            func()
        else:
            print("Please login to access this page")

    return wrapper_func
```

Suppose:

```python
@login_required
def home():
    html = "This is homepage"
    return html
```

Now:

```python
print(home())
```

The original `home()` returns:

```python
"This is homepage"
```

but the wrapper does:

```python
func()
```

instead of:

```python
return func()
```

Therefore, the wrapper itself returns:

```python
None
```

So:

```python
print(home())
```

would print:

```text
This is homepage
None
```

if `func()` itself prints/produces output accordingly, because the returned value is not passed through.

A better decorator is:

```python
def login_required(func):
    def wrapper_func():
        if logged_in:
            return func()
        else:
            print("Please login to access this page")

    return wrapper_func
```

Now the return value is preserved.

---

# 9. Decorators with Arguments

Real functions often accept arguments.

For example:

```python
def home(request):
    return "Homepage"
```

A simple wrapper like:

```python
def wrapper_func():
```

cannot accept the `request` argument.

A general-purpose decorator therefore commonly uses:

```python
def login_required(func):

    def wrapper_func(*args, **kwargs):
        if logged_in:
            return func(*args, **kwargs)
        else:
            print("Please login")

    return wrapper_func
```

### `*args`

Collects positional arguments.

### `**kwargs`

Collects keyword arguments.

This allows the decorator to work with many different functions.

---

# 10. Exception Handling

Python programs can encounter errors while running.

For example:

```python
user_input = int(input("Enter a number: "))
```

If the user enters:

```text
abc
```

Python cannot convert `"abc"` into an integer.

It raises:

```python
ValueError
```

Without exception handling, the program may stop.

---

# 11. `try` and `except`

Basic syntax:

```python
try:
    # code that may cause an exception
except:
    # what to do if exception occurs
```

Example:

```python
try:
    user_input = int(input("Enter a number: "))
except ValueError:
    print("Something went wrong")
```

If the user enters:

```text
10
```

then:

```python
int("10")
```

works.

If the user enters:

```text
abc
```

then:

```python
int("abc")
```

raises:

```python
ValueError
```

and Python executes:

```python
print("Something went wrong")
```

---

# 12. Why Do We Handle Exceptions?

Exception handling allows us to deal with expected runtime problems **without crashing the entire program**.

Examples:

```text
Invalid user input
Database object doesn't exist
File doesn't exist
Network request fails
Permission denied
Invalid JSON
Division by zero
```

---

# 13. `try`, `except`, and `else`

Example:

```python
try:
    user_input = int(input("Enter a number: "))
except ValueError:
    print("Something went wrong")
else:
    print(user_input)
```

There are three parts:

### `try`

Code that might fail:

```python
try:
    user_input = int(input("Enter a number: "))
```

### `except`

Runs when the specified exception occurs:

```python
except ValueError:
    print("Something went wrong")
```

### `else`

Runs only if the `try` block succeeds:

```python
else:
    print(user_input)
```

So:

```text
try succeeds
    ↓
else executes

try fails
    ↓
except executes
```

---

# 14. `raise` — Manually Raising an Exception

Python also allows us to intentionally raise an exception.

Example:

```python
raise Exception("OTP verification failed")
```

This means:

> Stop normal execution here and raise an exception.

For example:

```python
try:
    print("Trying to verify otp")
    raise Exception("OTP verification failed")

except Exception:
    print("OTP verification failed, please request a new OTP")

else:
    print("OTP verified")
```

Output:

```text
Trying to verify otp
OTP verification failed, please request a new OTP
```

The `else` block doesn't execute because an exception occurred.

---

# 15. Why Use `raise`?

We use `raise` when **our program detects that something went wrong**.

For example:

```python
if otp != correct_otp:
    raise Exception("Invalid OTP")
```

The error doesn't necessarily have to come from Python itself.

Our application can deliberately raise an exception when a business rule fails.

---

# 16. `Exception` vs Specific Exceptions

This:

```python
except Exception:
```

catches many ordinary exceptions.

However, whenever possible, it is better to catch the **specific exception** we expect.

For example:

```python
try:
    number = int(input())
except ValueError:
    print("Please enter a valid number")
```

This is generally better than:

```python
try:
    number = int(input())
except Exception:
    print("Something went wrong")
```

Why?

Because broad exception handling can hide unexpected programming errors.

---

# 17. Django's `DoesNotExist`

The example:

```text
Student.DoesNotExist
```

is related to Django ORM.

Suppose:

```python
student = Student.objects.get(id=10)
```

If no student with `id=10` exists, Django raises:

```python
Student.DoesNotExist
```

We can handle it:

```python
try:
    student = Student.objects.get(id=10)
except Student.DoesNotExist:
    print("Student not found")
```

This is an example of using **specific exception handling**.

---

# 18. Iterator

An **iterator** is an object that allows us to retrieve elements **one at a time**.

For example:

```python
nums = [1, 2, 3, 4, 5]
```

A list is an iterable.

We can do:

```python
for num in nums:
    print(num)
```

Python internally gets elements from the iterable one at a time.

---

# 19. Iterable vs Iterator

These two terms are related but different.

## Iterable

An object that can provide an iterator.

Examples:

```python
list
tuple
string
dictionary
set
file
range
```

For example:

```python
nums = [1, 2, 3]
```

The list is iterable.

---

## Iterator

An object that remembers its current position and provides the next value.

We can create an iterator using:

```python
iter(nums)
```

Example:

```python
nums_iter = iter(nums)
```

Now:

```text
nums
 ↓
[1, 2, 3, 4, 5]

nums_iter
 ↓
iterator object
```

---

# 20. `next()`

Once we have an iterator:

```python
nums_iter = iter(nums)
```

we can request the next value:

```python
print(next(nums_iter))
```

Output:

```text
1
```

Then:

```python
print(next(nums_iter))
```

Output:

```text
2
```

Then:

```text
3
4
5
```

The iterator remembers where it is.

---

# 21. What Happens After the Last Element?

Suppose:

```python
nums = [1, 2, 3]

nums_iter = iter(nums)

print(next(nums_iter))
print(next(nums_iter))
print(next(nums_iter))
print(next(nums_iter))
```

The first three calls return:

```text
1
2
3
```

The fourth call raises:

```python
StopIteration
```

This exception means:

> There are no more elements.

---

# 22. How Does `for` Work Internally?

When we write:

```python
for num in nums:
    print(num)
```

Python conceptually does something similar to:

```python
iterator = iter(nums)

while True:
    try:
        num = next(iterator)
    except StopIteration:
        break
    else:
        print(num)
```

This is why the class example:

```python
while True:
    try:
        num = next(nums_iter)
    except StopIteration:
        break
    else:
        print(num)
```

is effectively implementing a `for` loop manually.

---

# 23. Iterator Protocol

For an object to behave as an iterator, it generally implements:

```python
__iter__()
```

and:

```python
__next__()
```

For example:

```python
iterator = iter(nums)

next(iterator)
```

is roughly related to:

```python
iterator.__next__()
```

The iterator protocol is one of the important mechanisms behind Python's `for` loops.

---

# 24. Generator

A **generator** is a special type of iterator that makes it easy to produce values **lazily**, one at a time.

Generators use:

```python
yield
```

instead of returning all values at once.

Example:

```python
def crange(stop):
    start = 0

    while start < stop:
        yield start
        start += 1
```

---

# 25. Understanding `yield`

The key difference:

```python
return
```

usually means:

> Finish the function and give back a value.

While:

```python
yield
```

means:

> Give back this value temporarily and pause the function here.

For example:

```python
def numbers():
    yield 1
    yield 2
    yield 3
```

Calling:

```python
numbers()
```

doesn't immediately execute the whole function.

It creates a generator.

---

# 26. Generator Execution

Consider:

```python
def crange(stop):
    start = 0

    while start < stop:
        yield start
        start += 1
```

Now:

```python
crange_gen = crange(10)
```

At this point, Python hasn't generated all ten numbers.

Then:

```python
next(crange_gen)
```

produces:

```text
0
```

The function pauses at:

```python
yield start
```

Next:

```python
next(crange_gen)
```

continues from where it paused.

It produces:

```text
1
```

And so on:

```text
0
1
2
3
4
5
6
7
8
9
```

The next call raises:

```python
StopIteration
```

---

# 27. Generator vs List

Suppose we want numbers from `0` to `99999999`.

A list approach:

```python
numbers = list(range(100000000))
```

would require memory to store all those numbers.

A generator:

```python
def crange(stop):
    start = 0

    while start < stop:
        yield start
        start += 1
```

doesn't store all values.

It generates each value when requested.

Conceptually:

```text
List:

[0, 1, 2, 3, 4, 5, ... millions of values]
       ↓
large memory usage


Generator:

generate 0 → use it
generate 1 → use it
generate 2 → use it
...
       ↓
small memory usage
```

This is called **lazy evaluation**.

---

# 28. Why `range()` Is Important

The class mentioned:

```python
range(100000000)
```

This is a good example of lazy/compact iteration.

You don't generally need a list containing:

```text
0
1
2
3
...
99999999
```

in memory just to iterate over the numbers.

You can do:

```python
for i in range(100000000):
    ...
```

and Python can produce the numbers as needed.

---

# 29. File Objects Are Iterators

Consider:

```python
with open("passwords.txt", "r") as file:
    for line in file:
        print(line)
```

An important concept here is that a file can be iterated **line by line**.

Python doesn't need to load the entire file into memory.

Conceptually:

```text
passwords.txt

line 1 → read
line 2 → read
line 3 → read
...
```

This is particularly useful for large files.

---

# 30. `readlines()` vs Iterating Over a File

Consider:

```python
with open("passwords.txt", "r") as file:
    content = file.readlines()
```

`readlines()` creates a collection containing the lines.

For a very large file, that can require significant memory.

Instead:

```python
with open("passwords.txt", "r") as file:
    for line in file:
        print(line)
```

processes the file incrementally.

This is more memory-efficient for large files.

---

# 31. Django QuerySets and Iteration

The class example:

```python
students = Student.objects.all()

for student in students:
    print(student)
```

is another important example.

A Django `QuerySet` is designed to support iteration.

You can write:

```python
students = Student.objects.all()

for student in students:
    ...
```

The important idea is that the database query and Python iteration are separate concepts.

The QuerySet represents the database query, and iteration causes Django to retrieve/process the results.

For very large datasets, Django also provides techniques such as:

```python
.iterator()
```

which can help avoid caching the entire result set in Django's normal QuerySet result cache.

---

# 32. Putting the Concepts Together

The topics from this class are actually connected.

## Decorators

Used to add behavior around functions:

```python
@login_required
def dashboard():
    ...
```

Think:

> **Before/around calling a function, perform some additional logic.**

---

## Exception Handling

Used to handle failures safely:

```python
try:
    student = Student.objects.get(id=10)
except Student.DoesNotExist:
    print("Student not found")
```

Think:

> **Something may go wrong, so handle the failure gracefully.**

---

## Iterators

Used to retrieve data one item at a time:

```python
iterator = iter(nums)

next(iterator)
```

Think:

> **Give me the next item.**

---

## Generators

A convenient way to create iterators:

```python
def numbers():
    yield 1
    yield 2
    yield 3
```

Think:

> **Generate values only when they are needed.**

---

## File Iteration

Allows large files to be processed incrementally:

```python
with open("file.txt") as file:
    for line in file:
        process(line)
```

Think:

> **Don't load everything; process one piece at a time.**

---

# 33. Quick Comparison

| Concept        | Main Purpose                       | Example                 |
| -------------- | ---------------------------------- | ----------------------- |
| Decorator      | Add behavior to a function         | `@login_required`       |
| `try/except`   | Handle errors                      | `except ValueError`     |
| `raise`        | Manually trigger an exception      | `raise Exception(...)`  |
| Iterable       | Something that can be iterated     | `list`, `tuple`, `file` |
| Iterator       | Produces next item                 | `iter(nums)`            |
| `next()`       | Gets next item                     | `next(iterator)`        |
| Generator      | Easily creates an iterator         | `yield`                 |
| File iteration | Process file incrementally         | `for line in file`      |
| QuerySet       | Represents a Django database query | `Student.objects.all()` |

---

# 34. Important Mental Models

### Decorator

```text
Original function
      ↓
    wrapper
      ↓
extra logic
      ↓
original function
```

### Exception Handling

```text
try something
     ↓
 ┌─── success ───→ else
 │
 └─── failure ───→ except
```

### Iterator

```text
Iterable
   ↓
iter()
   ↓
Iterator
   ↓
next()
   ↓
value
   ↓
next()
   ↓
value
```

### Generator

```text
generator function
       ↓
     yield
       ↓
   value produced
       ↓
   function pauses
       ↓
     next()
       ↓
   function resumes
```

---

# 35. Key Points Students Should Remember

1. **A decorator takes a function and returns another function.**

2. The syntax:

   ```python
   @login_required
   def home():
       ...
   ```

   is essentially:

   ```python
   home = login_required(home)
   ```

3. A wrapper should usually preserve the original function's return value:

   ```python
   return func()
   ```

4. Use `try/except` when an operation can raise an exception.

5. Prefer catching **specific exceptions**:

   ```python
   except ValueError:
   ```

   rather than unnecessarily catching everything:

   ```python
   except Exception:
   ```

6. `raise` allows our application to intentionally raise an exception.

7. An **iterable** can provide an iterator.

8. An **iterator** provides values one at a time using `next()`.

9. When an iterator has no more values, it raises:

   ```python
   StopIteration
   ```

10. A `for` loop internally relies on the iterator protocol.

11. A **generator** uses `yield` and produces values lazily.

12. Generators are especially useful when dealing with **large amounts of data**.

13. Files can be iterated line by line:

```python
for line in file:
```

14. Django QuerySets are iterable, which is why we can write:

```python
for student in Student.objects.all():
    ...
```

15. These concepts are not isolated Python features—they are heavily used in **Django, database processing, file processing, APIs, and backend development**.
