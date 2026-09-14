### 1. 🛒 Shopping List Manager

Create a menu-driven Python program to manage a shopping list.

**Menu:**

```text
===================================
       SHOPPING LIST MANAGER
===================================
1. Add item
2. Show all items
3. Remove item
4. Search item
Q. Quit
===================================
```

**Requirements:**

* Store items in a list.
* Option `1`: Ask for an item and add it.
* Option `2`: Display all items.
* Option `3`: Ask for an item and remove it if it exists.
* Option `4`: Ask for an item and tell whether it exists.
* Option `Q`: Exit the program.
* Display an appropriate message for invalid choices.

---

### 2. 📚 Book Collection Manager

Create a program to manage a collection of books.

**Menu:**

```text
===================================
        BOOK COLLECTION
===================================
1. Add book
2. Show all books
3. Remove book
4. Count books
Q. Quit
===================================
```

**Requirements:**

* Use a list called `books`.
* Add book names using `append()`.
* Display all books using a `for` loop.
* Remove a book only if it exists.
* Option `4` should display the total number of books.
* Make book names look clean using `.capitalize()` or `.title()`.

**Example:**

```text
Enter book name: python basics

Book added successfully!

Total books: 3
```

---

### 3. 👨‍🎓 Student Name Manager

Create a menu-driven program for managing student names.

**Menu:**

```text
===================================
       STUDENT NAME MANAGER
===================================
1. Add student
2. Show students
3. Remove student
4. Find student
Q. Quit
===================================
```

**Requirements:**

* Store student names in a list.
* Add new students.
* Show all students with numbering.

Example:

```text
1. Ram
2. Sita
3. Hari
```

* Remove a student if they exist.
* Search for a student and display:

```text
Student found!
```

or

```text
Student not found!
```

* Handle invalid menu choices.

**Challenge:** Make the search work even if the user enters different capitalization, such as `ram`, `Ram`, or `RAM`.

---

### 4. 🎬 Movie Watchlist Manager

Create a program to manage a movie watchlist.

**Menu:**

```text
===================================
        MOVIE WATCHLIST
===================================
1. Add movie
2. Show movies
3. Remove movie
4. Mark as watched
Q. Quit
===================================
```

**Requirements:**

* Store movie names in a list.
* Option `1`: Add a movie.
* Option `2`: Display all movies.
* Option `3`: Remove a movie.
* Option `4`: Ask for a movie and display:

```text
You watched: Inception
```

* If the movie doesn't exist, display:

```text
Movie not found in your watchlist.
```

**Extra challenge:** Prevent the same movie from being added twice.

---

### Difficulty progression

| Exercise              | Difficulty | Main concepts                             |
| --------------------- | ---------- | ----------------------------------------- |
| 🛒 Shopping List      | ⭐⭐         | List, `append`, `remove`, `in`            |
| 📚 Book Collection    | ⭐⭐         | List, loop, `len()`, string methods       |
| 👨‍🎓 Student Manager | ⭐⭐⭐        | Search, case handling, loops              |
| 🎬 Movie Watchlist    | ⭐⭐⭐        | Multiple operations, duplicate prevention |
