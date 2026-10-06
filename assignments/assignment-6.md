# Python Advanced Concepts

In this lesson, we will learn some powerful Python features that allow us to write code that is **shorter, cleaner, and more expressive**.

We will cover:

1. Comprehensions

   * List comprehension
   * Set comprehension
   * Dictionary comprehension
2. Higher-Order Functions

   * Functions as arguments
   * `filter()`
   * `map()`
   * `sorted()`
   * `lambda` functions
3. Iterators and `next()`

---

# 1. Comprehensions

A **comprehension** is a concise way to create a new collection from an existing iterable such as a list, tuple, set, or range.

Instead of writing multiple lines using a `for` loop, we can often write the same logic in a single line.

Python provides three commonly used comprehensions:

* List comprehension
* Set comprehension
* Dictionary comprehension

---

## 1.1 List Comprehension

Suppose we have a list of numbers and want to create a new list containing only the even numbers.

### Traditional approach

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 22]

even_numbers = []

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)

print(even_numbers)
```

Output:

```text
[2, 4, 6, 8, 10, 12, 22]
```

We can write the same logic using a list comprehension:

```python
even_numbers = [number for number in numbers if number % 2 == 0]

print(even_numbers)
```

Output:

```text
[2, 4, 6, 8, 10, 12, 22]
```

### General Syntax

```python
[expression for item in iterable if condition]
```

For example:

```python
[number for number in numbers if number % 2 == 0]
```

Here:

* `number` → expression
* `for number in numbers` → loop
* `if number % 2 == 0` → condition

The `if` condition is optional.

### Example without a condition

```python
numbers = [1, 2, 3, 4, 5]

squares = [number ** 2 for number in numbers]

print(squares)
```

Output:

```text
[1, 4, 9, 16, 25]
```

### Example with strings

```python
names = ["ram", "hari", "geeta"]

uppercase_names = [name.upper() for name in names]

print(uppercase_names)
```

Output:

```text
['RAM', 'HARI', 'GEETA']
```

---

# 1.2 Set Comprehension

A set comprehension works similarly to a list comprehension, but it creates a **set**.

For example:

```python
numbers = [1, 2, 2, 3, 3, 4, 5]

unique_numbers = {number for number in numbers}

print(unique_numbers)
```

Output:

```text
{1, 2, 3, 4, 5}
```

Because a set does not contain duplicate values, duplicate numbers are automatically removed.

### Example

Suppose we have users:

```python
users = [
    {
        "name": "Ram",
        "email": "ram@gmail.com"
    },
    {
        "name": "hari",
        "email": "hari@gmail.com"
    },
    {
        "name": "geeta",
        "email": "geeta@gmail.com"
    },
    {
        "name": "saugat",
        "email": "saugat@gmail.com"
    },
    {
        "name": "Roshan",
        "email": "ram@gmail.com"
    }
]
```

We can extract all emails into a list:

```python
emails = [user["email"] for user in users]

print(emails)
```

Output:

```text
['ram@gmail.com', 'hari@gmail.com', 'geeta@gmail.com',
 'saugat@gmail.com', 'ram@gmail.com']
```

Notice that `ram@gmail.com` appears twice.

If we want only unique emails, we can use a set comprehension:

```python
emails = {user["email"] for user in users}

print(emails)
```

Now the duplicate email is removed.

### Important

```python
[user["email"] for user in users]
```

creates a **list**.

```python
{user["email"] for user in users}
```

creates a **set**.

---

# 1.3 Dictionary Comprehension

A dictionary comprehension is used to create a new dictionary concisely.

### General Syntax

```python
{key: value for item in iterable}
```

Example:

```python
numbers = [1, 2, 3, 4, 5]

squares = {number: number ** 2 for number in numbers}

print(squares)
```

Output:

```text
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

We can also use a condition:

```python
numbers = [1, 2, 3, 4, 5, 6]

even_squares = {
    number: number ** 2
    for number in numbers
    if number % 2 == 0
}

print(even_squares)
```

Output:

```text
{2: 4, 4: 16, 6: 36}
```

---

# 2. Higher-Order Functions

Before understanding higher-order functions, remember:

> In Python, functions are objects.

This means we can:

* Store a function in a variable
* Pass a function as an argument
* Return a function from another function

A function that accepts another function as an argument or returns a function is called a **higher-order function**.

---

## Functions, Parameters, and Arguments

Consider:

```python
def greet(name):
    print("Hello", name)
```

Here:

```python
name
```

is a **parameter**.

When we call:

```python
greet("Ram")
```

`"Ram"` is an **argument**.

---

## Functions as Arguments

We can pass a function to another function.

Example:

```python
def square(x):
    return x ** 2

def calculate(function, number):
    return function(number)

result = calculate(square, 5)

print(result)
```

Output:

```text
25
```

Here:

```python
calculate(square, 5)
```

passes the `square` function as an argument.

Notice that we write:

```python
square
```

not:

```python
square()
```

because we are passing the function itself rather than calling it immediately.

---

# 3. `filter()`

The `filter()` function is used to select elements from an iterable based on a condition.

### General Syntax

```python
filter(function, iterable)
```

The function should return:

* `True` → keep the value
* `False` → remove the value

---

## Example

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def odd_filter(x):
    return x % 2 == 1
```

Test the function:

```python
print(odd_filter(1))
```

Output:

```text
True
```

```python
print(odd_filter(2))
```

Output:

```text
False
```

Now use `filter()`:

```python
odd_numbers = filter(odd_filter, numbers)

print(odd_numbers)
```

The output will look something like:

```text
<filter object at 0x...>
```

This is because `filter()` returns a **filter object**, which is an iterator.

To convert it to a list:

```python
odd_numbers_list = list(odd_numbers)

print(odd_numbers_list)
```

Output:

```text
[1, 3, 5, 7, 9]
```

---

# 4. Iterators and `next()`

The object returned by `filter()` is an **iterator**.

An iterator gives us values one at a time.

For example:

```python
numbers = [1, 2, 3, 4, 5]

odd_numbers = filter(lambda x: x % 2 == 1, numbers)

print(next(odd_numbers))
print(next(odd_numbers))
print(next(odd_numbers))
```

Output:

```text
1
3
5
```

Each call to `next()` asks the iterator for its next value.

Once there are no more values, calling `next()` raises:

```text
StopIteration
```

This is one reason iterators are useful: they can process values **one at a time** instead of necessarily creating another complete collection in memory.

---

# 5. `map()`

The `map()` function is used to apply a function to every item in an iterable.

### General Syntax

```python
map(function, iterable)
```

Suppose we have users:

```python
users = [
    {
        "name": "Ram",
        "email": "ram@gmail.com"
    },
    {
        "name": "hari",
        "email": "hari@gmail.com"
    },
    {
        "name": "geeta",
        "email": "geeta@gmail.com"
    }
]
```

We can create a function:

```python
def get_email(user):
    return user["email"]
```

Then:

```python
emails = map(get_email, users)
```

Convert the result to a list:

```python
print(list(emails))
```

Output:

```text
['ram@gmail.com', 'hari@gmail.com', 'geeta@gmail.com']
```

We can also convert it to a set:

```python
emails = map(get_email, users)

print(set(emails))
```

This gives us unique email addresses.

---

# 6. `filter()` vs `map()`

A common point of confusion is the difference between `filter()` and `map()`.

### `filter()`

Used when we want to **select some elements**.

```python
numbers = [1, 2, 3, 4, 5, 6]

even_numbers = filter(
    lambda x: x % 2 == 0,
    numbers
)

print(list(even_numbers))
```

Output:

```text
[2, 4, 6]
```

Think:

> **filter = keep/remove**

---

### `map()`

Used when we want to **transform every element**.

```python
numbers = [1, 2, 3, 4, 5]

squares = map(
    lambda x: x ** 2,
    numbers
)

print(list(squares))
```

Output:

```text
[1, 4, 9, 16, 25]
```

Think:

> **map = transform**

---

# 7. `sorted()`

Python provides the `sorted()` function to create a sorted version of an iterable.

Example:

```python
numbers = [3, 5, 1, 0, 10]

sorted_numbers = sorted(numbers)

print(sorted_numbers)
```

Output:

```text
[0, 1, 3, 5, 10]
```

---

## `sort()` vs `sorted()`

There is an important difference.

### `sort()`

`sort()` is a list method and modifies the original list.

```python
numbers = [3, 5, 1, 0, 10]

numbers.sort()

print(numbers)
```

The original list has been changed.

### `sorted()`

`sorted()` returns a new sorted list.

```python
numbers = [3, 5, 1, 0, 10]

sorted_numbers = sorted(numbers)

print(sorted_numbers)
print(numbers)
```

The original `numbers` list remains unchanged.

---

# 8. Sorting Using `key`

`sorted()` becomes especially powerful when working with objects such as dictionaries.

Consider:

```python
students = [
    {
        "name": "ram",
        "total_marks": 345
    },
    {
        "name": "roshan",
        "total_marks": 500
    },
    {
        "name": "harry",
        "total_marks": 150
    }
]
```

Suppose we want to sort students according to their marks.

First, create a function:

```python
def get_total_marks(student):
    return student["total_marks"]
```

Test it:

```python
print(get_total_marks({
    "name": "harry",
    "total_marks": 150
}))
```

Output:

```text
150
```

Now use it as the `key`:

```python
ranked_list = sorted(
    students,
    key=get_total_marks,
    reverse=True
)

print(ranked_list)
```

`key=get_total_marks` tells Python:

> "Use the value returned by `get_total_marks()` to decide the sorting order."

`reverse=True` means sort from highest to lowest.

Therefore, the student with the highest marks comes first.

---

# 9. Lambda Functions

A `lambda` function is a small anonymous function.

Instead of:

```python
def square(x):
    return x ** 2
```

we can write:

```python
lambda x: x ** 2
```

### General Syntax

```python
lambda parameters: expression
```

Example:

```python
lambda x: x * 2
```

This means:

> Take `x` and return `x * 2`.

Another example:

```python
lambda x: x % 2 == 1
```

This returns `True` if `x` is odd.

---

# 10. Lambda with `filter()`

Instead of creating a separate function:

```python
def odd_filter(x):
    return x % 2 == 1

odd_numbers = filter(odd_filter, numbers)
```

we can use a lambda:

```python
odd_numbers = filter(
    lambda x: x % 2 == 1,
    numbers
)

print(list(odd_numbers))
```

Output:

```text
[1, 3, 5, 7, 9, 11, ...]
```

This is useful when the function is very small and will only be used once.

---

# 11. Lambda with `map()`

Example:

```python
numbers = [1, 2, 3, 4, 5]

squares = map(
    lambda x: x ** 2,
    numbers
)

print(list(squares))
```

Output:

```text
[1, 4, 9, 16, 25]
```

---

# 12. Lambda with `sorted()`

We can also use a lambda as the sorting key.

Using the previous `students` example:

```python
students = [
    {"name": "ram", "total_marks": 345},
    {"name": "roshan", "total_marks": 500},
    {"name": "harry", "total_marks": 150}
]
```

Instead of writing:

```python
def get_total_marks(student):
    return student["total_marks"]
```

we can directly write:

```python
ranked_list = sorted(
    students,
    key=lambda student: student["total_marks"],
    reverse=True
)
```

This is shorter and is often convenient when the sorting logic is simple.

---

# 13. Comprehension vs `map()` / `filter()`

Many operations can be written in multiple ways.

For example, using `filter()`:

```python
numbers = [1, 2, 3, 4, 5, 6]

even_numbers = filter(
    lambda x: x % 2 == 0,
    numbers
)

print(list(even_numbers))
```

The same operation can be written using list comprehension:

```python
even_numbers = [
    x for x in numbers
    if x % 2 == 0
]

print(even_numbers)
```

Both are valid.

For simple transformations and filtering, **comprehensions are often easier to read**.

However, understanding `map()`, `filter()`, iterators, and higher-order functions is important because they appear frequently in Python code and other programming languages.

---

# 14. Important Concepts to Remember

### Comprehensions

```python
[expression for item in iterable]
```

Creates a list.

```python
{expression for item in iterable}
```

Creates a set.

```python
{key: value for item in iterable}
```

Creates a dictionary.

---

### `filter()`

Selects elements based on a condition.

```python
filter(function, iterable)
```

Think:

> **Which elements should I keep?**

---

### `map()`

Transforms every element.

```python
map(function, iterable)
```

Think:

> **What should each element become?**

---

### `sorted()`

Returns a sorted list.

```python
sorted(iterable)
```

Can use:

```python
sorted(iterable, key=function)
```

and:

```python
sorted(iterable, reverse=True)
```

---

### `lambda`

Creates a small anonymous function.

```python
lambda x: x ** 2
```

---

### Iterator

An iterator produces values one at a time.

```python
next(iterator)
```

gets the next value.

---

# Quick Comparison

| Feature            | Purpose                  | Example                            |
| ------------------ | ------------------------ | ---------------------------------- |
| List comprehension | Create a list            | `[x * 2 for x in numbers]`         |
| Set comprehension  | Create a set             | `{x for x in numbers}`             |
| Dict comprehension | Create a dictionary      | `{x: x**2 for x in numbers}`       |
| `filter()`         | Select values            | `filter(lambda x: x > 5, numbers)` |
| `map()`            | Transform values         | `map(lambda x: x * 2, numbers)`    |
| `sorted()`         | Sort values              | `sorted(numbers)`                  |
| `lambda`           | Small anonymous function | `lambda x: x * 2`                  |
| `next()`           | Get next iterator value  | `next(iterator)`                   |

# Practice Questions

## Question 1

Given:

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

Create a list containing only the numbers greater than 5 using list comprehension.

---

## Question 2

Create a list containing the squares of all numbers from 1 to 10 using list comprehension.

Expected result:

```text
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

---

## Question 3

Given:

```python
numbers = [1, 2, 2, 3, 3, 3, 4, 5]
```

Create a set containing only the unique numbers using set comprehension.

---

## Question 4

Given:

```python
students = [
    {"name": "Ram", "marks": 80},
    {"name": "Hari", "marks": 65},
    {"name": "Sita", "marks": 95},
]
```

Sort the students by marks from highest to lowest using `sorted()` and `key`.

---

## Question 5

Use `filter()` and `lambda` to find all numbers divisible by 3.

```python
numbers = [1, 3, 4, 6, 8, 9, 10, 12]
```

Expected result:

```text
[3, 6, 9, 12]
```

---

## Question 6

Use `map()` and `lambda` to convert:

```python
numbers = [1, 2, 3, 4, 5]
```

into:

```text
[10, 20, 30, 40, 50]
```

---

## Question 7

Given:

```python
users = [
    {"name": "Ram", "email": "ram@gmail.com"},
    {"name": "Hari", "email": "hari@gmail.com"},
    {"name": "Sita", "email": "sita@gmail.com"},
]
```

Extract all email addresses using:

1. List comprehension
2. `map()`
3. Set comprehension
