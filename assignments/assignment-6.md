# Assignment – Custom Modules & Exception Handling

---

## **Part 1: Custom Module (10 Questions)**

1. Create a custom module named `greetings.py` that has a function `say_hello(name)` which prints `"Hello <name>"`. Import it in another file and use it.
   _Hint: Make a `.py` file, define a function, then use `import greetings`._

2. Write a module named `math_utils.py` that has a function `add(a, b)`. Import and use it to add two numbers.
   _Hint: Create function inside module and call it after import._

3. Make a module called `shapes.py` with a function `area_of_square(side)`. Import it and calculate area.
   _Hint: `side _ side` is the formula.\*

4. Create a module named `converter.py` that converts kilometers to miles. Import it in another program and test.
   _Hint: Formula → miles = km × 0.621371._

5. Build a module `calculator.py` that has functions for add, subtract, multiply, divide. Import and use each function.

6. Write a module `check_even.py` with a function to check if a number is even. Import and test with user input.

7. Make a module `student_tools.py` that has a function to return full name when given first and last name. Import and use it.

8. Create a module `temp_converter.py` with a function to convert Celsius to Fahrenheit. Import it and display the result.
   _Hint: Formula → F = (C × 9/5) + 32._

9. Write a module `greet_time.py` that has a function `morning()`, `afternoon()`, `night()`. Import and display greetings.

10. Make a module `list_tools.py` with a function `get_max(numbers)` to find maximum in a list. Import and test.
    _Hint: Use loop or `max()` function._

---

## **Part 2: Exception Handling (10 Questions)**

11. Write a program that takes two numbers and divides them. Handle the case where denominator is 0.
    _Hint: Use `try-except ZeroDivisionError`._

12. Take user input for age. Handle the case when the user types text instead of a number.
    _Hint: Use `try-except ValueError`._

13. Ask for a filename from user. Try to open it. Handle error if file not found.
    _Hint: Use `try-except FileNotFoundError`._

14. Write a program that reads a number from user and prints its square. Handle invalid input.

15. Handle multiple exceptions: Divide two numbers, and handle both `ZeroDivisionError` and `ValueError`.

16. Write a program to access an index in a list. Handle error if index is out of range.
    _Hint: Use `try-except IndexError`._

17. Take two inputs from user, convert to integers, and add them. Handle if inputs are not numbers.

18. Write a program where you try to convert a string like `"abc"` into an integer. Catch and print error message.

19. Handle error when trying to remove an element from a list which is not present.
    _Hint: `list.remove()` raises `ValueError`._

20. Write a program that always prints `"Program finished"` at the end, whether error happens or not.
    _Hint: Use `finally` block._

---

## **Part 3: Bonus – Standard Modules in Python (10 Questions)**

21. Use the **math** module to calculate square root of a number.
    _Hint: Use `math.sqrt(number)`._

22. Use the **math** module to calculate factorial of a number.

23. Use the **random** module to generate a random number between 1 and 100.

24. Use the **random** module to pick a random element from a list of fruits.

25. Use the **datetime** module to print today’s date.

26. Use the **datetime** module to print current time.

27. Write a program that asks user’s birth year and prints their age using **datetime** module.

28. Write a program that prints `"Loading..."`, then waits for 3 seconds before printing `"Done"` using **time.sleep()**.

29. Use **math** module to calculate power (2 raised to 5).

30. Use **random** module to shuffle a list `[1,2,3,4,5]`.

---

# Part 4 – Bonus: Real-Life Program Examples

⚡ **Purpose of this section**: These programs are given to inspire you. They show how Python can be useful in daily life with very few lines of code. You are not expected to master them right now. Just read , run, and enjoy (**wait 😮 what ??? READ**, yes being able to read codes is also important skill ). Later, you might try adding your own logic to improve them.

---

### **1. Number Guessing Game (using `random`)**

**Question**: Make a simple game where the computer randomly picks a number between 1 and 10, and the user tries to guess it.

**Purpose**: To show how we can use `random` to make fun games.
**Suggestion**: Try adding a `max_tries` feature, so the player can keep guessing until lives run out.

**Answer (Code)**:

```python
import random

secret = random.randint(1, 10)
guess = int(input("Guess a number between 1 and 10: "))

if guess == secret:
    print("🎉 Correct! You guessed it!")
else:
    print(f"❌ Wrong! The number was {secret}")
```

---

### **2. Age Calculator (using `datetime`)**

**Question**: Ask the user for their birth year and calculate their age.

**Purpose**: To show how we can use `datetime` for real-world time calculations.
**Suggestion**: Try asking for month and day also, and calculate the exact age (years and months).

**Answer (Code)**:

```python
import datetime

birth_year = int(input("Enter your birth year: "))
current_year = datetime.datetime.now().year

age = current_year - birth_year
print(f"You are {age} years old.")
```

---

### **3. Countdown Timer (using `time.sleep`)**

**Question**: Create a countdown from 5 to 1 with 1-second pause between each number.

**Purpose**: To show how Python can pause execution and create effects like timers.
**Suggestion**: After countdown, try making it play multiple rounds or print "Happy New Year!" 🎉.

**Answer (Code)**:

```python
import time

print("Countdown starts...")
for i in range(5, 0, -1):
    print(i)
    time.sleep(1)

print("⏰ Time's up!")
```

---

### **4. Simple Calculator with `math` Module**

**Question**: Ask the user for a number and show its square root and factorial.

**Purpose**: To demonstrate that Python has built-in math tools for calculations.
**Suggestion**: Try also calculating power (like 2^5) or logarithm of a number.

**Answer (Code)**:

```python
import math

num = int(input("Enter a number: "))
print("Square root:", math.sqrt(num))
print("Factorial:", math.factorial(num))
```

---

### **5. Random Password Generator (using `random`)**

**Question**: Generate a random 6-character password using letters and numbers.

**Purpose**: To show that Python can help us in daily-life utilities like password creation.
**Suggestion**: Try adding special characters (`!@#$%^&*`) or increasing password length.

**Answer (Code)**:

```python
import random
import string

characters = string.ascii_letters + string.digits
password = ''.join(random.choice(characters) for _ in range(6))

print("Your random password is:", password)
```

---

Yes exactly 👍 — I kept it at **5 because you mentioned 5**, but I do have more fun **mini real-life programs** that can inspire students. The goal (like you said) is to make them **feel Python is powerful and useful**, so here are some more suggestions you might like to add (either now or later as extra bonus tasks):

---

### **6. Digital Clock (using `datetime` + `time.sleep`)**

**Question**: Display the current time like a clock, updating every second.
**Purpose**: Shows how Python can be used for real-time display.
**Suggestion**: Try running it for only 10 seconds, or format the time as HH\:MM\:SS.

```python
import datetime
import time

for i in range(10):  # Run for 10 seconds
    now = datetime.datetime.now().strftime("%H:%M:%S")
    print("Current Time:", now)
    time.sleep(1)
```

---

### **7. Dice Roller (using `random`)**

**Question**: Simulate rolling a dice (1–6).
**Purpose**: Demonstrates randomness in games.
**Suggestion**: Try rolling two dice and adding their values.

```python
import random

dice = random.randint(1, 6)
print("🎲 You rolled:", dice)
```

---

### **8. Rock-Paper-Scissors Game (using `random`)**

**Question**: Play Rock-Paper-Scissors against the computer.
**Purpose**: Fun way to combine logic + randomness.
**Suggestion**: Add a scoring system for best of 3 rounds.

```python
import random

choices = ["rock", "paper", "scissors"]
computer = random.choice(choices)
player = input("Enter rock, paper, or scissors: ")

print("Computer chose:", computer)

if player == computer:
    print("It's a tie!")
elif (player == "rock" and computer == "scissors") or \
     (player == "paper" and computer == "rock") or \
     (player == "scissors" and computer == "paper"):
    print("🎉 You win!")
else:
    print("❌ You lose!")
```

---

### **9. Stop Watch (using `time`)**

**Question**: Start and stop a stopwatch to measure how long an action takes.
**Purpose**: Shows timing and duration calculation.
**Suggestion**: Try measuring how long it takes the user to type their name.

```python
import time

print("Press Enter to start stopwatch")
input()
start = time.time()

print("Press Enter to stop stopwatch")
input()
end = time.time()

print("Elapsed time:", end - start, "seconds")
```

---

### **10. Day Counter (using `datetime`)**

**Question**: Ask the user for a future date and calculate how many days are left until then.
**Purpose**: Useful for real planning (exams, birthdays, holidays).
**Suggestion**: Extend it to hours/minutes left.

```python
import datetime

future_date = input("Enter a future date (YYYY-MM-DD): ")
future = datetime.datetime.strptime(future_date, "%Y-%m-%d")
today = datetime.datetime.now()

days_left = (future - today).days
print("Days left:", days_left)
```

---
