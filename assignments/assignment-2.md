# Python Loops + List Practice Exercises

## Level 1 — Very Basic `for` Loop

### 1. Print "Hello" 10 times

Write a program that prints:

```text
Hello
Hello
Hello
...
```

exactly 10 times.

💡 **Hint:** Use `for` and `range()`.

---

### 2. Print numbers from 1 to 10

Expected output:

```text
1
2
3
4
5
6
7
8
9
10
```

💡 **Hint:** `range()` can generate a sequence of numbers.

---

### 3. Print numbers from 10 to 1

Expected output:

```text
10
9
8
...
1
```

💡 **Hint:** `range()` can have a **start, stop, and step**.

---

### 4. Print even numbers from 1 to 20

Expected:

```text
2
4
6
8
10
12
14
16
18
20
```

💡 **Hint:** Think about the third argument of `range()`.

---

### 5. Print odd numbers from 1 to 20

Expected:

```text
1
3
5
...
19
```

💡 **Hint:** Start `range()` at `1` and use an appropriate step.

---

### 6. Print "Good Morning" 5 times with the number

Expected:

```text
Good Morning 0
Good Morning 1
Good Morning 2
Good Morning 3
Good Morning 4
```

💡 **Hint:** Use `i` inside the loop.

---

## Level 2 — Multiplication Tables

### 7. Print the multiplication table of 5

Expected:

```text
5 x 1 = 5
5 x 2 = 10
...
5 x 10 = 50
```

💡 **Hint:** Use:

```python
for i in range(...):
```

and calculate `5 * i`.

---

### 8. Ask the user for a number and print its multiplication table

Example:

```text
Which multiplication table? 7

7 x 1 = 7
7 x 2 = 14
...
7 x 10 = 70
```

💡 **Hint:** Convert the user's input using `int()`.

---

### 9. Print tables from 1 to 5

Expected concept:

```text
1 x 1 = 1
...
1 x 10 = 10

2 x 1 = 2
...
5 x 10 = 50
```

💡 **Hint:** You will need **two loops**.

---

### 10. Print the multiplication table in reverse

For example, for `5`:

```text
5 x 10 = 50
5 x 9 = 45
...
5 x 1 = 5
```

💡 **Hint:** Use a negative step in `range()`.

---

# Level 3 — Looping Through Strings

### 11. Print every character of a string

Given:

```python
name = "Python"
```

Output:

```text
P
y
t
h
o
n
```

💡 **Hint:** A string can be directly used with a `for` loop.

---

### 12. Print every character with its position

Given:

```python
name = "Python"
```

Expected:

```text
0 P
1 y
2 t
3 h
4 o
5 n
```

💡 **Hint:** Use a counter variable along with the loop.

---

### 13. Count the number of characters

Given:

```python
text = "Hello Python"
```

Find how many characters it contains.

💡 **Hint:** Create a variable such as:

```python
count = 0
```

Then increase it inside the loop.

---

### 14. Count the letter `a`

Given:

```python
text = "banana"
```

Output:

```text
Number of a = 3
```

💡 **Hint:** Check each character using `if`.

---

### 15. Print only vowels

Given:

```python
text = "programming"
```

Expected:

```text
o
a
i
```

💡 **Hint:** Check whether each character is inside:

```python
"aeiou"
```

---

### 16. Count vowels in a word

Example:

```text
Enter a word: education
```

Output:

```text
Number of vowels = 5
```

💡 **Hint:** Loop through the string and check `a, e, i, o, u`.

---

# Level 4 — Basic `while` Loop

### 17. Print numbers from 1 to 10 using `while`

Expected:

```text
1
2
3
...
10
```

💡 **Hint:** You need:

```python
i = 1
while ...:
```

Remember to increase `i`.

---

### 18. Print numbers from 10 to 1 using `while`

💡 **Hint:** Start with `10` and decrease the variable every iteration.

---

### 19. Print even numbers from 2 to 20 using `while`

💡 **Hint:** Increase the number by `2` each time.

---

### 20. Print "Sorry" until the user says yes

Example:

```text
Sorry
Are you happy? no

Sorry
Are you happy? no

Sorry
Are you happy? yes

Thank you!
```

💡 **Hint:** Use a `while` loop and stop when the answer becomes `"yes"`.

---

### 21. Keep asking for a password until correct

Suppose the password is:

```python
"python123"
```

Example:

```text
Enter password: hello
Wrong password!

Enter password: abc
Wrong password!

Enter password: python123
Correct password!
```

💡 **Hint:** The loop should continue while the password is incorrect.

---

### 22. Keep asking for a number until the user enters 10

Example:

```text
Enter number: 4
Try again.

Enter number: 7
Try again.

Enter number: 10
Correct!
```

💡 **Hint:** Use `while` and compare the input with `10`.

---

# Level 5 — `break`

### 23. Stop when the number reaches 5

Print numbers from 1 onward, but stop when the number becomes 5.

Expected:

```text
1
2
3
4
5
```

💡 **Hint:** Use an infinite loop or a large range with `break`.

---

### 24. Print numbers from 1 to 100, but stop at 20

💡 **Hint:** Use:

```python
if i == 20:
    break
```

---

### 25. Keep asking for numbers until the user enters 0

Example:

```text
Enter number: 5
Enter number: 8
Enter number: 3
Enter number: 0
Program stopped.
```

💡 **Hint:** Use `while True:` and `break`.

---

### 26. Simple guessing game

Set:

```python
secret = 7
```

Ask the user to guess the number until they get it correct.

Example:

```text
Guess: 4
Wrong!

Guess: 9
Wrong!

Guess: 7
Correct!
```

💡 **Hint:** `while True` + `if` + `break`.

---

# Level 6 — List Basics

Give students this list:

```python
participants = ["ram", "sita", "geeta", "hari", "saugat", "uttam"]
```

### 27. Print the entire list

💡 **Hint:**

```python
print(participants)
```

---

### 28. Print the first participant

Expected:

```text
ram
```

💡 **Hint:** Remember that list indexing starts from `0`.

---

### 29. Print the third participant

Expected:

```text
geeta
```

💡 **Hint:** What is the index of the third item?

---

### 30. Print the last participant

Expected:

```text
uttam
```

💡 **Hint:** You can use a negative index.

---

### 31. Print every participant using a loop

Expected:

```text
ram
sita
geeta
hari
saugat
uttam
```

💡 **Hint:** Use:

```python
for name in participants:
```

---

### 32. Print every participant with a capital first letter

Expected:

```text
Ram
Sita
Geeta
Hari
Saugat
Uttam
```

💡 **Hint:** You already used `.capitalize()` in today's class.

---

### 33. Print all participants on one line

Expected:

```text
Ram Sita Geeta Hari Saugat Uttam
```

💡 **Hint:** Use the `end` parameter of `print()`.

---

# Level 7 — Modifying Lists

### 34. Add `"Kushal"` to the end of the list

💡 **Hint:** Which list method adds one item at the end?

---

### 35. Add `"Priya"` at index 2

💡 **Hint:** Use `insert()`.

---

### 36. Add `"Ramesh"` and `"Roshan"` to the list

💡 **Hint:** You can use `extend()` when adding multiple items.

---

### 37. Remove `"saugat"`

💡 **Hint:** Use `remove()`.

---

### 38. Remove `"uttam"`

💡 **Hint:** Use `remove()`.

---

### 39. Add `"ram"` again

Then print the list.

💡 **Hint:** `append()` adds an item to the end.

---

### 40. Remove all `"uttam"` values

Given:

```python
participants = [
    "ram",
    "uttam",
    "sita",
    "uttam",
    "geeta",
    "uttam"
]
```

Remove every `"uttam"`.

Expected:

```python
["ram", "sita", "geeta"]
```

💡 **Hint:** Use:

```python
while "uttam" in participants:
```

Then remove one `"uttam"` each time.

---

# Level 8 — Lists + Loops Together

### 41. Print only names starting with `r`

Given:

```python
participants = ["ram", "sita", "ramesh", "geeta", "roshan"]
```

Expected:

```text
ram
ramesh
roshan
```

💡 **Hint:** Check the first character of each name.

---

### 42. Print names having more than 4 characters

Given:

```python
names = ["ram", "sita", "geeta", "hari", "saugat", "uttam"]
```

Expected:

```text
geeta
saugat
uttam
```

💡 **Hint:** Use `len()`.

---

### 43. Count how many names are in the list

```python
names = ["ram", "sita", "geeta", "hari"]
```

Expected:

```text
Total names = 4
```

💡 **Hint:** Create a counter and increase it inside the loop.

---

### 44. Count names longer than 4 characters

Given:

```python
names = ["ram", "sita", "geeta", "hari", "saugat", "uttam"]
```

Expected:

```text
3
```

💡 **Hint:** Combine `if` with `len()`.

---

### 45. Search for a participant

Ask:

```text
Enter participant name: sita
```

If the name exists:

```text
Participant found!
```

Otherwise:

```text
Participant not found!
```

💡 **Hint:** Use the `in` operator.

---

### 46. Keep asking until a valid participant is entered

Given:

```python
participants = ["ram", "sita", "geeta", "hari"]
```

Keep asking:

```text
Enter participant name:
```

until the user enters a name that exists in the list.

💡 **Hint:** `while` + `in`.

---

### 47. Print each name with a number

Expected:

```text
1. Ram
2. Sita
3. Geeta
4. Hari
```

💡 **Hint:** Maintain a separate counter variable.

---

### 48. Find the longest name

Given:

```python
names = ["ram", "sita", "geeta", "saugat", "uttam"]
```

Expected:

```text
Longest name: saugat
```

💡 **Hint:** Keep one variable containing the longest name found so far.

---

# Level 9 — Numbers + Lists

### 49. Print every number in a list

```python
numbers = [10, 20, 30, 40, 50]
```

Expected:

```text
10
20
30
40
50
```

💡 **Hint:** Loop directly through the list.

---

### 50. Find the sum of all numbers

```python
numbers = [10, 20, 30, 40, 50]
```

Expected:

```text
Sum = 150
```

💡 **Hint:** Start with:

```python
total = 0
```

Then add each number to `total`.

---

### 51. Find the largest number

```python
numbers = [10, 45, 23, 89, 12, 56]
```

Expected:

```text
Largest = 89
```

💡 **Hint:** Assume the first number is the largest initially.

---

### 52. Find the smallest number

```python
numbers = [10, 45, 23, 89, 12, 56]
```

Expected:

```text
Smallest = 10
```

💡 **Hint:** Similar to the previous question, but compare for a smaller value.

---

### 53. Count even numbers

```python
numbers = [10, 15, 22, 31, 44, 57, 60]
```

Expected:

```text
Even numbers = 4
```

💡 **Hint:** Use the `%` operator.

---

### 54. Count odd numbers

Using the same list, count the odd numbers.

💡 **Hint:** A number is odd when its remainder after division by `2` is not `0`.

---

### 55. Print only numbers greater than 50

```python
numbers = [20, 75, 34, 90, 45, 61, 10]
```

Expected:

```text
75
90
61
```

💡 **Hint:** Loop through the list and use `if`.

---

# Level 10 — Challenge Exercises

These are good for stronger students.

### 56. Reverse a list manually

Given:

```python
numbers = [1, 2, 3, 4, 5]
```

Output:

```text
5
4
3
2
1
```

💡 **Hint:** Try using a `for` loop with `range()` and list indexes.

---

### 57. Create a new list containing only even numbers

Given:

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
```

Expected:

```python
[2, 4, 6, 8]
```

💡 **Hint:** Create an empty list first:

```python
even_numbers = []
```

Then use `append()`.

---

### 58. Create a new list containing only names longer than 4 characters

Given:

```python
names = ["ram", "sita", "geeta", "hari", "saugat", "uttam"]
```

Expected:

```python
["geeta", "saugat", "uttam"]
```

💡 **Hint:** Empty list + `for` + `if` + `append()`.

---

### 59. Remove all numbers greater than 50

Given:

```python
numbers = [20, 75, 34, 90, 45, 61, 10]
```

Expected:

```python
[20, 34, 45, 10]
```

💡 **Hint:** Be careful when modifying a list while looping through it. A simple approach at this stage is to build a new list.

---

### 60. Simple student attendance system

Start with:

```python
students = ["Ram", "Sita", "Hari", "Geeta", "Saugat"]
```

Ask the user for a student's name.

If the student exists:

```text
Ram is present.
```

Otherwise:

```text
Student not found.
```

💡 **Hint:** Use `input()` and the `in` operator.

---

# 🏆 Mini Projects

After students finish the exercises above, give them these without much guidance.

## Mini Project 1 — Number Guessing Game

The computer has a secret number:

```python
secret = 7
```

The user repeatedly guesses until they get the correct answer.

Example:

```text
Guess the number: 3
Wrong! Try again.

Guess the number: 9
Wrong! Try again.

Guess the number: 7
Correct! 🎉
```

**Hint:** `while True` → `input()` → `if` → `break`.

---

## Mini Project 2 — Simple Shopping List

Start with:

```python
shopping = []
```

Keep asking the user to enter items.

Example:

```text
Enter item: rice
Enter item: milk
Enter item: apple
Enter item: done

Your shopping list:
rice
milk
apple
```

**Hint:** Use `while True`, `append()`, and `break`.

---

## Mini Project 3 — Student List

Start with:

```python
students = []
```

Repeatedly ask for student names.

When the user enters `"done"`, stop taking names and display all students.

Example:

```text
Enter student: Ram
Enter student: Sita
Enter student: Hari
Enter student: done

Students:
Ram
Sita
Hari
```

**Hint:** `while True` + `append()` + `break` + `for`.

---

## Mini Project 4 — Number Analyzer

Given:

```python
numbers = [10, 23, 45, 12, 67, 88, 31, 90]
```

Your program should display:

```text
Total numbers: 8
Even numbers: ...
Odd numbers: ...
Largest number: ...
Smallest number: ...
Sum: ...
```

**Hint:** Solve each part separately using loops and variables.

---

## Mini Project 5 — Participant Management

Start with:

```python
participants = ["ram", "sita", "geeta", "hari"]
```

Create a program that repeatedly asks:

```text
1. Add participant
2. Remove participant
3. Show participants
4. Search participant
5. Exit
```

**Hint:** Use `while True`, `if/elif`, `append()`, `remove()`, `in`, and a `for` loop.

# 🎉 Congratulations!