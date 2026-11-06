# Python Function Exercises for Beginners

## Level 1: Basic Functions

Practice defining and calling functions.

### Exercise 1: Greeting Function

Write a function called `greet()` that prints:

```
Hello, welcome to Python!
```

Call the function three times.

### Exercise 2: Greeting with Name

Write a function called `greet_user(name)` that accepts a user's name and prints:

```
Hello Ram, welcome to Python!
```

Call it with three different names.

### Exercise 3: Default Parameter

Write a function called `greet_user(name="Guest")`.

Requirements:

- If a name is provided, greet that person.
- If no name is provided, greet `"Guest"`.

Example:

```
greet_user("Ram")greet_user()
```

Expected output:

```
Hello Ram
Hello Guest
```

### Exercise 4: Addition Function

Write a function called `add_numbers(a, b)` that accepts two numbers and prints their sum.

Example:

```
add_numbers(10, 20)
```

Expected output:

```
30
```

### Exercise 5: Even or Odd

Write a function called `check_number(number)`.

Requirements:

- If the number is divisible by 2, print `"Even"`.
- Otherwise, print `"Odd"`.

Example:

```
check_number(7)
```

Expected output:

```
Odd
```

## Level 2: Functions with Return

Practice returning values from functions.

### Exercise 6: Square of a Number

Write a function called `square(number)` that returns the square of a number.

Example:

```
result = square(5)print(result)
```

Expected output:

```
25
```

### Exercise 7: Celsius to Fahrenheit

Write a function called `celsius_to_fahrenheit(celsius)`.

Formula:

```
F = (C * 9/5) + 32
```

Example:

```
temperature = celsius_to_fahrenheit(25)print(temperature)
```

Expected output:

```
77.0
```

### Exercise 8: Convert Meters to Kilometers

Write a function called `convert_to_km(meters)`.

Requirements:

- Convert meters into kilometers.
- Return the result.
- Store the returned value in a variable.
- Add 5 to the returned value and print it.

Example:

```
km = convert_to_km(7000)result = km + 5print(result)
```

Expected output:

```
12.0
```

### Exercise 9: Find the Maximum Number

Write a function called `find_max(a, b)`.

Requirements:

- Accept two numbers.
- Return the larger number.
- If both numbers are equal, return either number.

Example:

```
result = find_max(10, 20)print(result)
```

Expected output:

```
20
```

### Exercise 10: Calculate Total Price

Write a function called `calculate_total(price, quantity)`.

Requirements:

- Accept product price and quantity.
- Calculate the total price.
- Return the result.

Example:

```
total = calculate_total(100, 5)print(total)
```

Expected output:

```
500
```

## Level 3: Functions with Conditions and Input

Practice combining functions with conditional statements.

### Exercise 11: Greeting Based on Time

Write a function called `show_greeting(time, name="Guest")`.

Conditions:

| Time  | Greeting       |
| ----- | -------------- |
| 5–11  | Good morning   |
| 12–15 | Good afternoon |
| 16–18 | Good evening   |
| 19–23 | Good night     |

Example:

```
show_greeting(6, "Ram")show_greeting(14, "Hari")show_greeting(20)
```

### Exercise 12: Grade Calculator

Write a function called `calculate_grade(marks)`.

Conditions:

| Marks    | Grade |
| -------- | ----- |
| 90–100   | A     |
| 80–89    | B     |
| 70–79    | C     |
| 60–69    | D     |
| Below 60 | F     |

Requirements:

- Accept marks as an argument.
- Determine the grade using conditional statements.
- Return the grade.

Example:

```
grade = calculate_grade(85)print(grade)
```

Expected output:

```
B
```

### Exercise 13: Age Eligibility Checker

Write a function called `check_eligibility(age)`.

Requirements:

- If age is 18 or above, print `"You are eligible."`
- Otherwise, print `"You are not eligible."`

Call the function with different ages.

### Exercise 14: Simple Calculator

Write a function called `calculator(a, b, operator)`.

It should support:

- `+` Addition
- `-` Subtraction
- `*` Multiplication
- `/` Division

If the operator is invalid, print `"Invalid operator"`.

Example:

```
calculator(10, 5, "+")calculator(10, 5, "*")calculator(10, 5, "/")
```

### Exercise 15: User Input with Function

Write a function called `get_user_info()`.

Requirements:

1. Ask the user to enter their name.
2. Ask the user to enter their age.
3. Print their name and age.
4. Return their age.
5. Outside the function, use the returned age to calculate how many years remain until age 100.

Example output:

```
Enter your name: Ram
Enter your age: 20

Hello Ram
Your age is 20
Years until 100: 80
```

## Recommended Practice Order

| Level   | Exercises | Main Concepts                              |
| ------- | --------- | ------------------------------------------ |
| Level 1 | 1–5       | Function definition, parameters, arguments |
| Level 2 | 6–10      | Return values and variables                |
| Level 3 | 11–15     | Conditions, input, and practical problems  |

## Important Concepts to Remember

1. `def` is used to define a function.
2. Parameters are variables defined inside the function definition.
3. Arguments are actual values passed when calling a function.
4. Default parameters provide default values when arguments are omitted.
5. `return` sends a value back to the caller.
6. `print()` displays something on the screen.
7. Local variables are accessible only within their function (unless returned or otherwise exposed).

Practice tip: Try solving each exercise without looking at the examples. Focus especially on understanding the difference between `print()` and `return`.
