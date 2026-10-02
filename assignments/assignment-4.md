# Python Functions — Practice

> **Level:** Beginner → Intermediate
> **Goal:** Practice Python functions until students are comfortable with defining functions, calling functions, parameters, arguments, default values, positional/keyword arguments, `return`, and multiple return values.
---

## 📚 Topics Covered

By the end of these 50 exercises, students should be able to:

* Define and call functions
* Understand why functions are useful
* Use parameters
* Pass positional arguments
* Pass keyword arguments
* Use default parameters
* Return values from functions
* Store returned values in variables
* Use returned values in calculations
* Return multiple values
* Unpack multiple returned values
* Combine functions with conditions and calculations
* Design small programs using functions

---

# Part 1 — Function Basics

### Question 1 — Welcome Message

Create a function named `welcome()` that prints:

```text
Welcome to Python Programming!
Let's learn functions.
```

Call the function.

---

### Question 2 — Reusable Line

Create a function named `line()` that prints:

```text
------------------------------
```

Call it three times to produce three lines.

**Think:** Why is using a function better than writing the `print()` statement three times?

---

### Question 3 — Student Introduction

Create a function named `student_intro()` that prints:

```text
Name: Prakash
Course: Python
Level: Beginner
```

Call the function once.

---

### Question 4 — Multiple Function Calls

Create a function named `show_menu()` that prints:

```text
1. Add
2. View
3. Exit
```

Call the function four times.

---

### Question 5 — Function for Repeated Calculation

Create a function named `calculate_square()` that prints the square of `8`.

Expected output:

```text
64
```

Call the function three times.

> **Note:** At this stage, don't worry about parameters. The purpose is to understand function definition and function calls.

---

# Part 2 — Parameters and Arguments

### Question 6 — Greeting a Person

Create a function:

```python
greet(name)
```

It should print:

```text
Hello, Ram!
```

when called with:

```python
greet("Ram")
```

Also call it with two other names.

---

### Question 7 — Display Age

Create a function `show_age(name, age)`.

Example:

```python
show_age("Sita", 21)
```

Output:

```text
Sita is 21 years old.
```

---

### Question 8 — Rectangle Information

Create a function:

```python
rectangle(length, width)
```

Print:

```text
Length: 10
Width: 5
Area: 50
```

Use the values passed to the function.

---

### Question 9 — Temperature Converter

Create a function:

```python
celsius_to_fahrenheit(celsius)
```

Use this formula:

```text
F = (C × 9/5) + 32
```

Example:

```python
celsius_to_fahrenheit(25)
```

Expected output:

```text
77.0
```

---

### Question 10 — Product Price

Create a function:

```python
show_price(product, price)
```

Example:

```python
show_price("Keyboard", 1500)
```

Output:

```text
Product: Keyboard
Price: Rs. 1500
```

---

# Part 3 — Positional Arguments

### Question 11 — Student Result

Create:

```python
show_result(name, marks)
```

Call:

```python
show_result("Anil", 78)
```

Output:

```text
Anil scored 78 marks.
```

Then call it with at least three different students.

---

### Question 12 — Simple Interest

Create:

```python
simple_interest(principal, rate, time)
```

Formula:

```text
SI = (P × R × T) / 100
```

Example:

```python
simple_interest(10000, 5, 2)
```

Expected output:

```text
1000
```

---

### Question 13 — Employee Salary

Create:

```python
employee_salary(name, salary)
```

Print:

```text
Employee: Ram
Salary: Rs. 30000
```

Call the function for three employees.

---

### Question 14 — Distance Converter

Create:

```python
km_to_meter(km)
```

Convert kilometers into meters.

Example:

```python
km_to_meter(5)
```

Output:

```text
5000
```

---

### Question 15 — Bill Calculator

Create:

```python
calculate_bill(item, price, quantity)
```

Calculate:

```text
total = price × quantity
```

Example:

```python
calculate_bill("Notebook", 80, 5)
```

Expected result:

```text
Item: Notebook
Price: 80
Quantity: 5
Total: 400
```

---

# Part 4 — Keyword Arguments

### Question 16 — Student Details

Create:

```python
student(name, age, course)
```

Call it using keyword arguments:

```python
student(
    name="Rita",
    age=20,
    course="Python"
)
```

Print all three values.

---

### Question 17 — Book Information

Create:

```python
book(title, author, price)
```

Call it using keyword arguments.

For example:

```python
book(
    title="Python Basics",
    author="ABC",
    price=500
)
```

---

### Question 18 — Mobile Information

Create:

```python
mobile(brand, model, price)
```

Call the function using keyword arguments in a **different order** from the parameter definition.

For example:

```python
mobile(
    price=25000,
    model="A15",
    brand="Samsung"
)
```

Observe why the values are still assigned correctly.

---

### Question 19 — Employee Information

Create:

```python
employee(name, department, salary)
```

Call it using only keyword arguments.

Try changing the order of the arguments.

---

### Question 20 — Identify the Argument Type

Consider:

```python
def display(name, age):
    print(name, age)
```

Identify whether each function call uses **positional arguments** or **keyword arguments**.

#### A

```python
display("Ram", 25)
```

#### B

```python
display(name="Ram", age=25)
```

#### C

```python
display(age=25, name="Ram")
```

#### D

```python
display("Ram", age=25)
```

**Challenge:** Explain why each one is valid or invalid.

---

# Part 5 — Default Parameters

### Question 21 — Default Greeting

Create:

```python
greet(name, message="Hello")
```

Calling:

```python
greet("Ram")
```

should produce:

```text
Hello, Ram
```

Calling:

```python
greet("Ram", "Good Morning")
```

should produce:

```text
Good Morning, Ram
```

---

### Question 22 — Default Country

Create:

```python
introduce(name, country="Nepal")
```

Examples:

```python
introduce("Ram")
introduce("John", "USA")
```

Expected idea:

```text
Ram is from Nepal.
John is from USA.
```

---

### Question 23 — Default Tax Rate

Create:

```python
calculate_tax(price, tax_rate=13)
```

Calculate the tax amount.

Example:

```python
calculate_tax(1000)
```

Use the default tax rate.

Then test:

```python
calculate_tax(1000, 10)
```

---

### Question 24 — Default Language

Create:

```python
course_info(course, language="English")
```

Example:

```python
course_info("Python")
```

and:

```python
course_info("Python", "Nepali")
```

Print the course and language.

---

### Question 25 — Default Quantity

Create:

```python
calculate_total(price, quantity=1)
```

Examples:

```python
calculate_total(500)
calculate_total(500, 4)
```

The first call should calculate the price of one item.

---

# Part 6 — Return Values

### Question 26 — Add Two Numbers

Create:

```python
add(a, b)
```

The function should **return** the sum instead of printing it.

Then:

```python
result = add(10, 20)
print(result)
```

Expected:

```text
30
```

---

### Question 27 — Use the Returned Value

Create:

```python
multiply(a, b)
```

Return the multiplication result.

Then use the returned value:

```python
result = multiply(5, 6)
answer = result + 10
print(answer)
```

What will be printed?

---

### Question 28 — Square Function

Create:

```python
square(number)
```

Return the square.

Then:

```python
x = square(7)
print(x)
```

---

### Question 29 — Calculate Area

Create:

```python
circle_area(radius)
```

Return the area of a circle.

Use:

```text
area = π × radius × radius
```

You may use:

```python
3.14
```

for π.

---

### Question 30 — Even or Odd

Create:

```python
is_even(number)
```

The function should return:

```python
True
```

if the number is even and:

```python
False
```

if it is odd.

Example:

```python
result = is_even(10)
print(result)
```

---

# Part 7 — Return + Conditions

### Question 31 — Pass or Fail

Create:

```python
check_result(marks)
```

Return:

```text
"Pass"
```

if marks are 40 or above.

Otherwise return:

```text
"Fail"
```

Example:

```python
result = check_result(75)
print(result)
```

---

### Question 32 — Positive, Negative, or Zero

Create:

```python
check_number(number)
```

Return:

* `"Positive"` if greater than 0
* `"Negative"` if less than 0
* `"Zero"` if equal to 0

Test all three cases.

---

### Question 33 — Find Larger Number

Create:

```python
larger(a, b)
```

Return the larger number.

Example:

```python
result = larger(50, 30)
print(result)
```

Output:

```text
50
```

---

### Question 34 — Discount Calculator

Create:

```python
calculate_discount(price, discount_percent)
```

Return the discount amount.

Example:

```python
discount = calculate_discount(2000, 10)
print(discount)
```

Expected:

```text
200
```

---

### Question 35 — Final Price

Create two functions:

```python
calculate_discount(price, discount_percent)
```

and:

```python
calculate_final_price(price, discount_percent)
```

The second function should use the first function's returned value.

**Goal:**

```text
Original price → Discount → Final price
```

### 💡 Hint

Inside `calculate_final_price()`, call:

```python
calculate_discount(...)
```

Then subtract the returned discount from the original price.

---

# Part 8 — Multiple Return Values

### Question 36 — Basic Calculations

Create:

```python
calculate(a, b)
```

Return:

* addition
* subtraction
* multiplication

Example:

```python
result = calculate(10, 5)
print(result)
```

Expected idea:

```text
(15, 5, 50)
```

---

### Question 37 — Unpacking Results

Using a function that returns three values:

```python
calculate(20, 4)
```

store the results separately:

```python
addition, subtraction, multiplication = calculate(20, 4)
```

Then print each result with a meaningful label.

---

### Question 38 — Rectangle Measurements

Create:

```python
rectangle_info(length, width)
```

Return:

1. Area
2. Perimeter

Then unpack the returned values.

Example:

```python
area, perimeter = rectangle_info(10, 5)
```

---

### Question 39 — Student Marks

Create:

```python
calculate_marks(m1, m2, m3)
```

Return:

1. Total marks
2. Average marks

Example:

```python
total, average = calculate_marks(70, 80, 90)
```

---

### Question 40 — Time Conversion

Create:

```python
convert_seconds(seconds)
```

Return:

1. Hours
2. Minutes
3. Remaining seconds

Example:

```python
h, m, s = convert_seconds(3670)
```

Expected:

```text
1 hour
1 minute
10 seconds
```

### 💡 Hint

Think about:

```text
hours = total_seconds // 3600
```

Then calculate the remaining seconds.

---

# Part 9 — Functions + Other Functions

### Question 41 — Shopping Bill

Create these functions:

```python
calculate_subtotal(price, quantity)
calculate_discount(subtotal, discount_percent)
calculate_final_amount(subtotal, discount)
```

Then use them together.

Example:

```text
Price = 500
Quantity = 4
Discount = 10%
```

Expected flow:

```text
Price × Quantity
        ↓
    Subtotal
        ↓
   Discount
        ↓
 Final Amount
```

### 💡 Steps

1. Calculate subtotal.
2. Pass subtotal to the discount function.
3. Get the discount amount.
4. Pass subtotal and discount to the final amount function.
5. Print the final amount.

---

### Question 42 — Student Grade System

Create:

```python
calculate_average(m1, m2, m3)
get_grade(average)
```

`calculate_average()` should return the average.

`get_grade()` should return:

| Average  | Grade |
| -------- | ----- |
| 80+      | A     |
| 70–79    | B     |
| 60–69    | C     |
| 50–59    | D     |
| Below 50 | F     |

Then connect both functions.

### 💡 Hint

The main program should conceptually work like:

```text
marks
  ↓
calculate_average()
  ↓
average
  ↓
get_grade()
  ↓
grade
```

---

### Question 43 — Login Validation

Create:

```python
check_username(username)
check_password(password)
```

The first function should return `True` if the username is not empty.

The second should return `True` if the password has at least 8 characters.

Then create:

```python
login(username, password)
```

which uses both functions.

Return:

```text
"Login successful"
```

or:

```text
"Invalid login"
```

### 💡 Steps

1. Check username.
2. Check password.
3. Store both returned values.
4. Use `and`.
5. Return the appropriate message.

---

### Question 44 — Electricity Bill

Create a function:

```python
calculate_bill(units)
```

Use these rules:

* First 50 units → Rs. 5 per unit
* Next 100 units → Rs. 7 per unit
* Above 150 units → Rs. 10 per unit

Return the bill amount.

### 💡 Hint

Break the problem into ranges.

For example:

```text
units <= 50
units between 51 and 150
units > 150
```

Be careful: for more than 150 units, don't charge every unit at Rs. 10.

---

### Question 45 — Salary Calculator

Create:

```python
calculate_bonus(salary, percentage)
calculate_total_salary(salary, bonus)
```

For example:

```text
Salary = 40,000
Bonus = 10%
```

Expected flow:

```text
Salary
  ↓
calculate_bonus()
  ↓
bonus
  ↓
calculate_total_salary()
  ↓
final salary
```

### Challenge

Make the bonus percentage have a default value of `10`.

---

# Part 10 — Real-World Function Problems

### Question 46 — Restaurant Order

Create:

```python
calculate_item_total(price, quantity)
calculate_tax(amount, tax_rate=13)
calculate_final_bill(amount, tax)
```

Use all three functions to calculate a restaurant bill.

Example:

```text
Food price: 250
Quantity: 3
Tax: 13%
```

Print:

```text
Subtotal: ...
Tax: ...
Final Bill: ...
```

### 💡 Challenge

The tax function should use `13` as the default tax rate but allow another rate to be passed.

---

### Question 47 — Exam Result System

Create the following functions:

```python
calculate_total(...)
calculate_percentage(...)
get_grade(...)
get_result(...)
```

Do **not** put everything inside one function.

For five subjects:

```text
English
Nepali
Math
Science
Computer
```

Calculate:

1. Total
2. Percentage
3. Grade
4. Pass/Fail status

### 💡 Important

Think about **which function should do which job**.

Don't make one giant function.

---

### Question 48 — ATM Withdrawal

Create:

```python
check_balance(balance)
can_withdraw(balance, amount)
withdraw(balance, amount)
```

Rules:

* Amount must be greater than 0.
* Amount cannot be greater than balance.
* If withdrawal is valid, return the new balance.
* Otherwise return the original balance.

Example:

```python
balance = 10000

if can_withdraw(balance, 3000):
    balance = withdraw(balance, 3000)

print(balance)
```

Expected:

```text
7000
```

### 💡 Steps

1. Check whether amount is positive.
2. Check whether amount is within balance.
3. Return `True`/`False` from the validation function.
4. Perform withdrawal only when valid.
5. Store the returned balance.

---

### Question 49 — Student Report Generator

Create these functions:

```python
calculate_total(...)
calculate_average(...)
get_grade(...)
get_status(...)
```

The program should generate something like:

```text
------ Student Report ------

Name: Sita
Total: 410
Average: 82.0
Grade: A
Status: Pass
```

### Requirements

* Use functions for each separate task.
* Functions should return values where appropriate.
* Avoid repeating calculations.
* Don't put the entire program inside one function.

### 💡 Suggested flow

```text
marks
  ↓
calculate_total()
  ↓
total
  ↓
calculate_average()
  ↓
average
  ↓
get_grade()
  ↓
grade

average/marks
  ↓
get_status()
  ↓
status
```

---

# Part 11 — Final Challenge

### Question 50 — Mini Billing System 🏆

Build a small billing system using functions.

The system should accept information about **three products**.

For each product, you should have:

```text
Product name
Price
Quantity
```

Create functions that perform separate tasks.

Your program should calculate:

```text
Subtotal
Discount
Tax
Final Amount
```

Use:

* A default discount percentage of `5`
* A default tax percentage of `13`

The output should look similar to:

```text
==============================
       BILL SUMMARY
==============================

Product 1: Keyboard
Price: Rs. 1500
Quantity: 2
Total: Rs. 3000

Product 2: Mouse
Price: Rs. 800
Quantity: 1
Total: Rs. 800

Product 3: USB Cable
Price: Rs. 300
Quantity: 3
Total: Rs. 900

------------------------------
Subtotal: Rs. 4700
Discount: Rs. 235
Tax: Rs. 580.45
------------------------------
Final Amount: Rs. 5045.45
==============================
```

### Requirements

Your solution must use functions.

At minimum, create functions for:

```python
calculate_item_total(...)
calculate_subtotal(...)
calculate_discount(...)
calculate_tax(...)
calculate_final_amount(...)
```

### 💡 Step-by-step hint

**Step 1:** Calculate each product's total:

```text
price × quantity
```

**Step 2:** Add all product totals:

```text
item1 + item2 + item3
```

**Step 3:** Calculate discount from subtotal.

**Step 4:** Calculate the amount after discount.

**Step 5:** Calculate tax.

**Step 6:** Calculate final amount.

### 🧠 Final Challenge

Try to make your program follow this structure:

```text
                  ┌────────────────────┐
Product 1 ───────→│                    │
Product 2 ───────→│   Subtotal         │
Product 3 ───────→│                    │
                  └─────────┬──────────┘
                            ↓
                       Discount
                            ↓
                    Amount After Discount
                            ↓
                           Tax
                            ↓
                     Final Amount
```

---

# 🎯 Function Mastery Checklist

After completing all 50 questions, students should be able to explain and use all of these:

### Basic

* [ ] What is a function?
* [ ] Why do we use functions?
* [ ] What does DRY mean?
* [ ] Function definition
* [ ] Function call

### Parameters & Arguments

* [ ] What is a parameter?
* [ ] What is an argument?
* [ ] Positional arguments
* [ ] Keyword arguments
* [ ] Default parameters

### Return

* [ ] Difference between `print()` and `return`
* [ ] Store a returned value in a variable
* [ ] Use a returned value in another calculation
* [ ] Return values from conditional logic
* [ ] Return multiple values
* [ ] Unpack multiple returned values

### Problem Solving

* [ ] Break a large problem into functions
* [ ] Make one function responsible for one task
* [ ] Call one function from another function
* [ ] Pass returned values between functions
* [ ] Use default parameters in practical programs
* [ ] Combine functions to build a complete program

---

## 🏁 Final Rule

For **Questions 41–50**, don't immediately try to write the whole program.

Use this approach:

```text
1. Understand the problem
        ↓
2. Identify the separate tasks
        ↓
3. Create a function for each task
        ↓
4. Decide the parameters
        ↓
5. Decide what each function should return
        ↓
6. Test each function separately
        ↓
7. Connect the functions
        ↓
8. Test the complete program
```

> **Golden rule:** A function should ideally have **one clear responsibility**. Don't create one huge function when the problem can naturally be divided into smaller reusable functions.
