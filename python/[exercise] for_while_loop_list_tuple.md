# Python Assignment: `for` Loop, `while` Loop, Lists, and Tuples

## Instructions

* Solve each question using **Python**.
* Write clean and readable code.
* Test your program with different inputs.
* Read the **hint** before solving.
* Avoid using advanced built-in functions unless they have been covered in class.

---

# Section A: `for` Loop (9 Questions)

### 1. Print Each Character

**Task:** Ask the user to enter their name and print each character on a new line.

**Hint:** A string can be traversed using a `for` loop.

---

### 2. Count Uppercase and Lowercase Letters

**Task:** Count how many uppercase and lowercase letters are present in a sentence.

**Hint:** Use `isupper()` and `islower()`.

---

### 3. Replace Spaces with Hyphens

**Task:** Create a new string where every space is replaced with `-`.

**Hint:** Build a new string character by character.

---

### 4. Print Words Separately

**Task:** Print each word from a sentence on a new line.

**Hint:** Split the sentence into words first.

---

### 5. Display Characters at Even Positions

**Task:** Print only the characters that are at even index positions.

**Hint:** Use `range(len(text))`.

---

### 6. Mask a Password

**Task:** Print the password using only `*` symbols of the same length.

**Hint:** Loop through each character and print `*`.

---

### 7. Remove Vowels

**Task:** Create a new string after removing all vowels.

**Hint:** Skip vowels while building the new string.

---

### 8. Count Special Characters

**Task:** Count how many special characters (such as `@`, `#`, `$`, `%`, etc.) are present in a string.

**Hint:** Check whether a character is neither a letter nor a digit.

---

### 9. Print a Rectangle Pattern

**Task:** Print a rectangle made of stars based on user input for rows and columns.

**Hint:** Use nested `for` loops.

---

# Section B: `while` Loop (8 Questions)

### 10. Login System

**Task:** Keep asking the user for a password until the correct password is entered.

**Hint:** Repeat until the password matches.

---

### 11. Menu-Driven Calculator

**Task:** Display a menu repeatedly until the user chooses Exit.

**Hint:** Use a `while True` loop.

---

### 12. ATM PIN Verification

**Task:** Give the user only three attempts to enter the correct PIN.

**Hint:** Count the number of attempts.

---

### 13. Read Until "stop"

**Task:** Keep accepting words until the user types `"stop"`.

**Hint:** Compare the input with `"stop"`.

---

### 14. Number Validation

**Task:** Keep asking the user for a positive number until they enter one.

**Hint:** Check if the number is greater than zero.

---

### 15. Password Length Checker

**Task:** Keep asking for a password until it contains at least 8 characters.

**Hint:** Use `len(password)`.

---

### 16. Shopping Cart

**Task:** Let the user enter item names until they type `"done"`.

**Hint:** Store each item in a list.

---

### 17. Continue or Quit

**Task:** Keep displaying a welcome message until the user enters `"q"`.

**Hint:** Ask the user after every iteration.

---

# Section C: Lists (10 Questions)

### 18. Grocery List

**Task:** Create a grocery list and print all the items.

**Hint:** Use a loop.

---

### 19. Find Longest Word

**Task:** Find the longest word in a list of words.

**Hint:** Compare the lengths of the words.

---

### 20. Student Attendance

**Task:** Store the attendance status (`Present`/`Absent`) of students and count how many students are present.

**Hint:** Compare each element with `"Present"`.

---

### 21. Remove Empty Strings

**Task:** Remove all empty strings (`""`) from a list.

**Hint:** Create a new list.

---

### 22. Search for a Student

**Task:** Ask the user for a student's name and check whether it exists in the class list.

**Hint:** Compare each name.

---

### 23. Convert Names to Uppercase

**Task:** Convert every name in a list to uppercase.

**Hint:** Use `upper()`.

---

### 24. Count Fruits

**Task:** Count how many times each fruit appears in a list.

**Hint:** Use nested loops or maintain another list.

---

### 25. Filter Short Words

**Task:** Create a new list containing only words with more than five letters.

**Hint:** Check the length of each word.

---

### 26. Movie Collection

**Task:** Display all movie names with numbering starting from 1.

**Hint:** Maintain a counter variable.

---

### 27. To-Do List

**Task:** Remove a completed task from a to-do list and display the updated list.

**Hint:** Use the `remove()` method.

---

# Section D: Tuples (8 Questions)

### 28. Days of the Week

**Task:** Store the days of the week in a tuple and print each day.

**Hint:** Use a loop.

---

### 29. Student Information

**Task:** Store a student's name, age, grade, and city in a tuple and display each value.

**Hint:** Access elements using indexing or a loop.

---

### 30. Count a Subject

**Task:** Store subjects in a tuple and count how many times `"Math"` appears.

**Hint:** Compare each element.

---

### 31. Display Subjects Alphabetically

**Task:** Convert a tuple of subjects into a list and sort it alphabetically.

**Hint:** Convert the tuple first.

---

### 32. Check Favorite Color

**Task:** Check whether the user's favorite color exists in a tuple of colors.

**Hint:** Compare each element.

---

### 33. Tuple to Sentence

**Task:** Store words in a tuple and print them as a complete sentence.

**Hint:** Print each word with a space.

---

### 34. Print Every Alternate Element

**Task:** Print every second element of a tuple.

**Hint:** Use a step value in `range()`.

---

### 35. Compare Two Tuples

**Task:** Check whether two tuples contain exactly the same elements in the same order.

**Hint:** Compare them directly using `==`.

---

# Bonus Challenge

### 36. Library Management Mini Program

Create a simple library system where the user can:

* View available books
* Search for a book
* Borrow a book (remove it from the list)
* Return a book (add it back to the list)
* Exit the program

**Hint:** Combine **lists**, **loops**, and **conditions** to build a menu-driven program.
