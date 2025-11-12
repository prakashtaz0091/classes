# Input and Ouput

## What is Input and Output in Python?

Input and output are the basic operations of a computer program. The input is data that is entered by the user, and the output is data that is displayed on the screen or saved to a file (we'll explore file handling later).

In Python, you can use the `input()` function to get input from the user, and the `print()` function to display output to the user.

```python
name = input("Enter your name: ")
print("Hello, " + name + "!")
```

- The `input()` function prompts the user for input, and the `print()` function displays the output to the user.

## Input statement

The `input()` function is used to get input from the user. It takes a prompt as an argument and returns the input as a string (always a string). If the user does not enter anything, the function returns an empty string. If we need input other than string then we can use `int(input())` or `float(input())` etc. to convert the input to the required data type.
Example:

```python
number = input("Enter a number: ")
print("Type of number:", type(number))

result = 5 + number  # This will raise a TypeError

```

- Here type printed will be `<class 'str'>` because by default input is string. If we need input other than string then we can use `int(input())` or `float(input())` etc. to convert the input to the required data type.

```python
number = int(input("Enter a number: "))
print("Type of number:", type(number))

result = 5 + number  # This will work

```

## Print Statement

The `print()` function is used to display output to the user. It takes one or more arguments, separated by commas, and prints them to the standard output (the screen).
Example:

```python
print("Hello, World!")
```

### Different ways to print

- `print("Hello, World!")`
- `print("Hello", "World!")`
- `print("Hello", "World!", sep=" ")`
- `print("Hello", "World!", end="\n")`
- `print("Hello", "World!", sep=" ", end="\n")`

Above are the different ways to print in Python. The `sep` argument is used to specify the separator between the printed values, and the `end` argument is used to specify the end character of the printed values.

# Python Operators

## What are Operators?

Operators are special symbols in Python that perform operations on variables and values.
Example:

```python
x = 10
y = 5
print(x + y)   # Output: 15
```

Here, `+` is an operator, and `x`, `y` are operands.

---

## Types of Operators in Python

| Type                                 | Description                     |
| ------------------------------------ | ------------------------------- |
| 1. Arithmetic Operators              | Perform mathematical operations |
| 2. Comparison (Relational) Operators | Compare values                  |
| 3. Logical Operators                 | Combine conditional statements  |
| 4. Assignment Operators              | Assign values to variables      |
| 5. Bitwise Operators                 | Perform bit-level operations    |
| 6. Membership Operators              | Test membership in sequences    |
| 7. Identity Operators                | Compare memory locations        |

---

## 1. Arithmetic Operators

Used for mathematical operations.

| Operator | Description         | Example  | Result |
| -------- | ------------------- | -------- | ------ |
| `+`      | Addition            | `5 + 2`  | 7      |
| `-`      | Subtraction         | `5 - 2`  | 3      |
| `*`      | Multiplication      | `5 * 2`  | 10     |
| `/`      | Division (float)    | `5 / 2`  | 2.5    |
| `//`     | Floor Division      | `5 // 2` | 2      |
| `%`      | Modulus (remainder) | `5 % 2`  | 1      |
| `**`     | Exponentiation      | `2 ** 3` | 8      |

---

## 2. Comparison (Relational) Operators

Used to compare two values.
They return `True` or `False`.

| Operator | Description              | Example  | Result |
| -------- | ------------------------ | -------- | ------ |
| `==`     | Equal to                 | `5 == 5` | True   |
| `!=`     | Not equal to             | `5 != 3` | True   |
| `>`      | Greater than             | `5 > 3`  | True   |
| `<`      | Less than                | `5 < 3`  | False  |
| `>=`     | Greater than or equal to | `5 >= 5` | True   |
| `<=`     | Less than or equal to    | `3 <= 5` | True   |

---

## 3. Logical Operators

Used to combine conditional statements.

| Operator | Description                  | Example               | Result |
| -------- | ---------------------------- | --------------------- | ------ |
| `and`    | True if both are true        | `(5 > 3) and (6 > 2)` | True   |
| `or`     | True if at least one is true | `(5 > 3) or (2 > 6)`  | True   |
| `not`    | Reverses the result          | `not(5 > 3)`          | False  |

---

## 4. Assignment Operators

Used to assign values to variables.

| Operator | Example     | Equivalent To  |
| -------- | ----------- | -------------- |
| `=`      | `x = 5`     | —              |
| `+=`     | `x += 3`    | `x = x + 3`    |
| `-=`     | `x -= 3`    | `x = x - 3`    |
| `*=`     | `x *= 3`    | `x = x * 3`    |
| `/=`     | `x /= 3`    | `x = x / 3`    |
| `%=`     | `x %= 3`    | `x = x % 3`    |
| `//=`    | `x //= 3`   | `x = x // 3`   |
| `**=`    | `x **= 3`   | `x = x ** 3`   |
| `&=`     | `x &= 3`    | `x = x & 3`    |
| &#124;=  | x &#124;= 3 | x = x &#124; 3 |
| `^=`     | `x ^= 3`    | `x = x ^ 3`    |
| `>>=`    | `x >>= 3`   | `x = x >> 3`   |
| `<<=`    | `x <<= 3`   | `x = x << 3`   |

---

## 5. Bitwise Operators

Used to perform bit-level operations on integers.

| Operator | Description | Example    | Binary Result            |
| -------- | ----------- | ---------- | ------------------------ |
| `&`      | Bitwise AND | `5 & 3`    | `101 & 011 = 001 (1)`    |
| &#124;   | Bitwise OR  | 5 &#124; 3 | 101 &#124; 011 = 111 (7) |
| `^`      | Bitwise XOR | `5 ^ 3`    | `101 ^ 011 = 110 (6)`    |
| `~`      | Bitwise NOT | `~5`       | `-(5+1) = -6`            |
| `<<`     | Left shift  | `5 << 1`   | `101 → 1010 (10)`        |
| `>>`     | Right shift | `5 >> 1`   | `101 → 10 (2)`           |

---

## 6. Membership Operators

Used to test if a sequence (like list, string, or tuple) contains a value.

| Operator | Description                          | Example              | Result |
| -------- | ------------------------------------ | -------------------- | ------ |
| `in`     | Returns True if value exists         | `'a' in 'apple'`     | True   |
| `not in` | Returns True if value does not exist | `'b' not in 'apple'` | True   |

---

## 7. Identity Operators

Used to compare memory locations (object identity).

| Operator | Description                       | Example      | Result       |
| -------- | --------------------------------- | ------------ | ------------ |
| `is`     | True if both refer to same object | `x is y`     | True / False |
| `is not` | True if they are not same object  | `x is not y` | True / False |

Example:

```python
x = [1, 2, 3]
y = x
z = [1, 2, 3]

print(x is y)     # True (same memory)
print(x is z)     # False (different memory)
print(x == z)     # True (same values)
```

---

## Summary

- Arithmetic Operators → Math operations
- Comparison Operators → Compare values
- Logical Operators → Combine conditions
- Assignment Operators → Assign and modify values
- Bitwise Operators → Work at binary level
- Membership Operators → Check element in sequence
- Identity Operators → Compare memory references

---
