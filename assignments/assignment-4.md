# Assignment: Practice Problems on `return` Statement & Menu-Driven Programs

---

## Part 1: Functions with `return` Statement (10 Questions)

**1. Function to return the square of a number.**

- Steps:

  1. Define a function with one parameter.
  2. Multiply the number by itself.
  3. Return the result.
  4. Call the function and print the returned value.

---

**2. Function to return the cube of a number.**

- Steps:

  1. Define a function with one parameter.
  2. Multiply the number three times.
  3. Return the result.

---

**3. Function to return the sum of two numbers.**

- Steps:

  1. Define a function with two parameters.
  2. Add the two numbers.
  3. Return the sum.
  4. Print the result outside the function.

---

**4. Function to return factorial of a number.**

- Steps:

  1. Define a function with one parameter.
  2. Initialize result = 1.
  3. Loop from 1 to n.
  4. Multiply result by each number.
  5. Return the final result.

---

**5. Function to return the maximum of three numbers.**

- Steps:

  1. Define a function with three parameters.
  2. Compare the numbers using `if-elif-else`.
  3. Return the largest number.

---

**6. Function to return average of numbers in a list.**

- Steps:

  1. Define a function with a list as parameter.
  2. Find the total sum of numbers.
  3. Divide total by the length of the list.
  4. Return the average.

---

**7. Function to check if a number is even or odd and return a message.**

- Steps:

  1. Define a function with one parameter.
  2. Check if number % 2 == 0.
  3. If yes, return `"Even"`. Otherwise, return `"Odd"`.

---

**8. Function to return largest element from a list.**

- Steps:

  1. Define a function with a list as parameter.
  2. Assume first element as largest.
  3. Loop through the list and compare values.
  4. Return the largest value.

---

**9. Function to return total marks and percentage of a student.**

- Steps:

  1. Define a function with a list of marks as parameter.
  2. Find the total marks.
  3. Calculate percentage = (total ÷ (number of subjects × 100)) × 100.
  4. Return both total and percentage.

---

**10. Function to return the reverse of a string.**

- Steps:

  1. Define a function with one string parameter.
  2. Reverse the string using loop or slicing.
  3. Return the reversed string.

---

# Part 2: Menu-Driven Program Simulation (6 Problems)

---

**1. Student Marks Manager**

- Menu Options:

  1. Add Marks
  2. Remove Marks
  3. Show All Marks
  4. Show Average Marks
  5. Exit

- Functions to create:

  - `add_marks()`
  - `remove_marks()`
  - `show_marks()`
  - `average_marks()`

- Steps:

  1. Create an empty list to store marks.
  2. In `add_marks()`, take input and append to the list.
  3. In `remove_marks()`, take input and remove from list.
  4. In `show_marks()`, print all marks.
  5. In `average_marks()`, calculate average and return result.
  6. Create a while loop to show the menu and take user choice.

---

**2. To-Do List Manager**

- Menu Options:

  1. Add Task
  2. Remove Task
  3. View All Tasks
  4. Exit

- Functions to create:

  - `add_task()`
  - `remove_task()`
  - `show_tasks()`

- Steps:

  1. Use a list to store tasks.
  2. In `add_task()`, take input and append to the list.
  3. In `remove_task()`, take input and remove from the list.
  4. In `show_tasks()`, display all tasks.
  5. Use a while loop for continuous menu until exit.

---

**3. Movie Collection Manager**

- Menu Options:

  1. Add Movie
  2. Remove Movie
  3. Show All Movies
  4. Search Movie
  5. Exit

- Functions to create:

  - `add_movie()`
  - `remove_movie()`
  - `show_movies()`
  - `search_movie()`

- Steps:

  1. Use a list to store movie names.
  2. In `add_movie()`, input movie name and append to list.
  3. In `remove_movie()`, remove by name.
  4. In `show_movies()`, display all movies with numbering.
  5. In `search_movie()`, check if movie exists and show a message.

---

**4. Library Book Manager**

- Menu Options:

  1. Add Book
  2. Remove Book
  3. Show All Books
  4. Search Book by Name
  5. Exit

- Functions to create:

  - `add_book()`
  - `remove_book()`
  - `show_books()`
  - `search_book()`

- Steps:

  1. Use a list to store book names.
  2. In `add_book()`, input book name and append to list.
  3. In `remove_book()`, input book name and remove it.
  4. In `show_books()`, display all books with numbering.
  5. In `search_book()`, check if book exists and show message.

---

**5. Contact Manager**

- Menu Options:

  1. Add Contact (name + phone)
  2. Delete Contact
  3. Show All Contacts
  4. Search Contact by Name
  5. Exit

- Functions to create:

  - `add_contact()`
  - `delete_contact()`
  - `show_contacts()`
  - `search_contact()`

- Steps:

  1. Use a dictionary with name as key and phone as value.
  2. In `add_contact()`, take name and phone as input and store in dictionary.
  3. In `delete_contact()`, remove by key.
  4. In `show_contacts()`, print all contacts neatly.
  5. In `search_contact()`, check if name exists in dictionary.

---

**6. Expense Tracker**

- Menu Options:

  1. Add Expense
  2. Remove Expense
  3. Show All Expenses
  4. Show Total Expenses
  5. Exit

- Functions to create:

  - `add_expense()`
  - `remove_expense()`
  - `show_expenses()`
  - `total_expenses()`

- Steps:

  1. Use a list to store expenses as numbers.
  2. In `add_expense()`, input expense and append to list.
  3. In `remove_expense()`, delete by value or index.
  4. In `show_expenses()`, print all expenses.
  5. In `total_expenses()`, calculate sum of expenses and return it.

---
