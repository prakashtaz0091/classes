# Python Practice Assignment

Work on the following projects step by step.

---

## **Project 1: Student Management System**

### Features to Implement

1. Add a new student with details: name, age, grade.
2. Remove a student by name.
3. Show all student records in a formatted way.
4. Search for a student by name.
5. Save all students into a CSV file (`students.csv`).
6. Load all students from the CSV file when the program starts.

### Hints / Steps

- Store all student records as a **list of dictionaries**:

  ```python
  {"name": "Ram", "age": 16, "grade": "10"}
  ```

- Create functions:

  - `add_student()`
  - `remove_student()`
  - `show_students()`
  - `search_student()`
  - `save_to_csv()`
  - `load_from_csv()`

- In the main loop, display a **menu** and call the required function.
- Use `try-except` to handle errors (e.g., removing a student that does not exist).

---

## **Project 2: Expense Tracker**

### Features to Implement

1. Add a new expense (amount, category, note).
2. Show all expenses.
3. Calculate and display the **total expense amount**.
4. Filter expenses by category (e.g., Food, Travel).
5. Save all expenses to a CSV file (`expenses.csv`).
6. Load existing expenses when the program starts.

### Hints / Steps

- Store each expense as a dictionary:

  ```python
  {"amount": 200, "category": "Food", "note": "Lunch"}
  ```

- Create functions:

  - `add_expense()`
  - `show_expenses()`
  - `total_expenses()`
  - `filter_by_category()`
  - `save_to_csv()`
  - `load_from_csv()`

- Use list comprehension to calculate totals.
- Use `filter()` to filter by category.
- Add exception handling for invalid inputs (e.g., entering a string instead of a number).

---

## **Project 3: Mini Games Collection 🎮**

### Game 1: Number Guessing Game

- The computer chooses a random number between 1–100.
- Keep asking the player to guess until correct.
- Show hints like **“Too high”** or **“Too low”**.
- Use a **decorator** to count and print the number of attempts.
- Suggestion: Add a **max tries** feature (example: player has 7 lives).

**Hints:**

- Use `random.randint(1, 100)` to generate the secret number.
- Use a loop to keep asking for guesses.
- Break the loop if guessed correctly or lives finish.

---

### Game 2: Simple Quiz Game

- Store questions in a dictionary like:

  ```python
  {"Capital of Nepal?": "Kathmandu", "2+2?": "4"}
  ```

- Ask each question one by one.
- Check if the answer is correct and keep score.
- At the end, show the **final score and percentage**.

**Hints:**

- Loop through the dictionary items.
- Compare user’s input with the correct answer.
- Use a counter to keep track of correct answers.

---

### Game 3 (Optional): Rock, Paper, Scissors

- Player chooses rock/paper/scissors.
- Computer randomly chooses one.
- Decide the winner.
- Loop until the player chooses Exit.

**Hints:**

- Use `random.choice(["rock", "paper", "scissors"])`.
- Use conditional statements to check the winner.

---

# 📌 Assignment Plan

- **Day 1–2:** Student Management System
- **Day 3–4:** Expense Tracker
- **Day 5–6:** Mini Games Collection
- **Day 7:** Review and improve — add extra features (example: save quiz results, track best scores, add more categories in expenses, etc.).
