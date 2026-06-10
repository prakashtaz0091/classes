# 🗄️ Database Concepts for Django ORM Beginners

> **Goal:** Understand the minimum database knowledge you need before learning Django ORM.
> No prior database experience needed!

---

## 1. What is a Database?

A **database** is an organized place to store and manage data so you can easily find, add, update, or remove it.

**Real-world analogy:** Think of a database like a digital filing cabinet. Instead of paper folders, data is stored in structured tables — similar to spreadsheets.

**Why do we need it?**
- Storing data in files (like `.txt` or `.csv`) gets messy fast.
- Databases keep data organized, searchable, and safe.

> 📌 Django uses a database (SQLite by default) to store all your app's data — users, posts, products, etc.

---

## 2. What Should (and Should NOT) Be Stored in a Database?

This confuses a lot of beginners, so let's clear it up early.

A database is designed to store **small, structured text and numbers** — things like names, emails, prices, and dates. It is **not** designed to store large files like images, videos, or PDFs.

---

### ✅ Store in the database

| Type of data | Examples |
|---|---|
| Text | Name, email, bio, post content |
| Numbers | Age, price, quantity, rating |
| Dates & times | Created at, date of birth, deadline |
| True/False values | Is active, is verified, is published |
| Short identifiers | Username, order number, status (`"pending"`) |

---

### ❌ Do NOT store in the database

| Type of data | Examples | Why not |
|---|---|---|
| Images | Profile photo, product image | Can be MBs or GBs in size — databases are slow at storing/serving binary files |
| Videos | Course videos, uploads | Extremely large — would make your database huge and sluggish |
| PDFs / Documents | Invoices, reports | Same reason — large binary files don't belong in a database |
| Audio files | Podcasts, voice notes | Binary and large |

---

### 🤔 Then where do files go?

Files are saved to the **file system** (a folder on your server) or a **cloud storage service** like AWS S3, Google Cloud Storage, or Cloudinary.

What you store in the database is just the **file's path or URL** — a short string that points to where the actual file lives.

```
Without Django (the idea):

  User uploads profile photo
          │
          ▼
  File saved to:  /media/avatars/alice.jpg   ← saved on disk / cloud
          │
          ▼
  Database stores:  "avatars/alice.jpg"      ← just the path (text)
```

**Real-world analogy:** Think of a library. The database is the **catalogue** — it holds the title, author, and shelf location of every book. The actual books sit on the **shelves** (file system / cloud). You look up the catalogue to find where to go, then fetch the book from the shelf.

---

### What this looks like in Django

Django's `ImageField` and `FileField` handle this automatically — they save the file to disk (or cloud) and store only the file path in the database.

```python
class UserProfile(models.Model):
    user  = models.OneToOneField(User, on_delete=models.CASCADE)
    bio   = models.TextField()                    # ✅ text → stored in DB
    photo = models.ImageField(upload_to='avatars/')  # ✅ file → saved to disk
                                                     #    path → stored in DB
```

So when you do `profile.photo`, Django gives you back the path/URL, not the raw image bytes.

> ⚠️ **Common beginner mistake:** Trying to store an image file directly in a `TextField` or `BinaryField`. Don't — use `ImageField` or `FileField` and let Django handle it the right way.

---

## 3. Tables, Rows, and Columns

A database stores data in **tables** — just like a spreadsheet.

| Concept | What it means | Spreadsheet equivalent |
|--------|---------------|------------------------|
| **Table** | A collection of related data | A sheet (tab) |
| **Column** | A category of data | A column header |
| **Row** | A single record | A single row of data |

**Example — a `users` table:**

| id | name    | email               | age |
|----|---------|---------------------|-----|
| 1  | Alice   | alice@email.com     | 25  |
| 2  | Bob     | bob@email.com       | 30  |
| 3  | Charlie | charlie@email.com   | 22  |

- Each **column** holds one type of info (`name`, `email`, `age`).
- Each **row** is one user's full record.

> 📌 In Django ORM, a **table** = a **Model class**, and each **row** = a **model instance**.

---

## 4. Common Data Types

Every column stores a specific **type** of data. Using the right type keeps data clean and efficient.

| Data Type   | What it stores           | Example value       |
|-------------|--------------------------|---------------------|
| `INTEGER`   | Whole numbers            | `1`, `42`, `2024`   |
| `VARCHAR`   | Short text (with limit)  | `"Alice"`, `"Hello"`|
| `TEXT`      | Long text                | A blog post body    |
| `BOOLEAN`   | True or False            | `True`, `False`     |
| `DATE`      | A calendar date          | `2024-01-15`        |
| `DATETIME`  | Date + time              | `2024-01-15 10:30`  |
| `FLOAT`     | Decimal numbers          | `9.99`, `3.14`      |

**Example:** In a `products` table:
- `name` → `VARCHAR`
- `price` → `FLOAT`
- `in_stock` → `BOOLEAN`
- `created_at` → `DATETIME`

> 📌 Django model fields map directly to these: `CharField`, `IntegerField`, `BooleanField`, `DateTimeField`, etc.

---

## 5. Primary Key

A **Primary Key (PK)** is a unique identifier for each row in a table. No two rows can have the same primary key.

**Real-world analogy:** Like a passport number — every person has a unique one.

```
users table
┌────┬─────────┬─────────────────────┐
│ id │  name   │        email        │
├────┼─────────┼─────────────────────┤
│  1 │  Alice  │  alice@email.com    │  ← PK = 1
│  2 │  Bob    │  bob@email.com      │  ← PK = 2
│  3 │ Charlie │  charlie@email.com  │  ← PK = 3
└────┴─────────┴─────────────────────┘
         ↑
    Primary Key (unique, never null)
```

**Rules for Primary Keys:**
- Must be **unique** (no duplicates)
- Must **never be empty** (never `NULL`)
- Usually auto-increments: 1, 2, 3, 4...

> 📌 Django automatically adds an `id` field as the primary key for every model unless you specify otherwise.

---

## 6. Foreign Key

A **Foreign Key (FK)** is a column in one table that **references the Primary Key** of another table. It's how tables are linked together.

**Real-world analogy:** An order receipt has a "customer ID" printed on it — that ID connects the receipt back to a specific customer.

```
users table                    posts table
┌────┬─────────┐               ┌────┬───────────────┬─────────────┐
│ id │  name   │               │ id │     title     │  user_id FK │
├────┼─────────┤               ├────┼───────────────┼─────────────┤
│  1 │  Alice  │◄──────────────│  1 │ "Hello World" │      1      │
│  2 │  Bob    │◄──────────────│  2 │ "My First App"│      1      │
└────┴─────────┘               │  3 │ "Django Tips" │      2      │
                               └────┴───────────────┴─────────────┘
```

Here, `user_id` in the `posts` table is a Foreign Key pointing to `users.id`.
- Posts 1 and 2 belong to Alice (user_id = 1)
- Post 3 belongs to Bob (user_id = 2)

> 📌 In Django: `user = models.ForeignKey(User, on_delete=models.CASCADE)`

---

## 7. Database Relationships

Relationships describe **how tables are connected** to each other.

---

### 6a. One-to-One (1:1)

One record in Table A is linked to **exactly one** record in Table B.

**Example:** One user has one profile.

```
users            profiles
┌────┬───────┐   ┌────┬──────────────┬─────────┐
│ id │ name  │   │ id │     bio      │ user_id │
├────┼───────┤   ├────┼──────────────┼─────────┤
│  1 │ Alice │──►│  1 │ "I love code"│    1    │
│  2 │ Bob   │──►│  2 │ "Django fan" │    2    │
└────┴───────┘   └────┴──────────────┴─────────┘
```

> 📌 Django: `user = models.OneToOneField(User, on_delete=models.CASCADE)`

---

### 6b. One-to-Many (1:N)

One record in Table A is linked to **many** records in Table B.

**Example:** One user can write many posts. But each post has only one author.

```
         ┌──────────────┐
Alice ───►│   Post 1     │
         │   Post 2     │
         │   Post 3     │
         └──────────────┘
         
         ┌──────────────┐
Bob   ───►│   Post 4     │
         └──────────────┘
```

> 📌 Django: `author = models.ForeignKey(User, on_delete=models.CASCADE)`
> This is the **most common** relationship type.

---

### 6c. Many-to-Many (M:N)

Many records in Table A can be linked to **many** records in Table B.

**Example:** A student can enroll in many courses. A course can have many students.

```
Students          Courses
┌───────────┐     ┌──────────────┐
│  Alice    │────►│  Python 101  │
│  Alice    │────►│  Django 201  │
│  Bob      │────►│  Python 101  │
│  Bob      │────►│  Web Design  │
│  Charlie  │────►│  Django 201  │
└───────────┘     └──────────────┘
```

A **junction table** is created behind the scenes to manage this:

| student_id | course_id |
|------------|-----------|
| 1 (Alice)  | 1 (Python)|
| 1 (Alice)  | 2 (Django)|
| 2 (Bob)    | 1 (Python)|

> 📌 Django: `courses = models.ManyToManyField(Course)` — Django handles the junction table automatically!

---

### ❓ Why split into multiple tables at all? Why not just one big table?

This is a great question. Let's look at what happens if you try to keep everything in one table.

**Attempt: One big `enrollments` table with everything:**

| student_id | student_name | student_email       | course_id | course_name | course_duration |
|------------|--------------|---------------------|-----------|-------------|-----------------|
| 1          | Alice        | alice@email.com     | 1         | Python 101  | 8 weeks         |
| 1          | Alice        | alice@email.com     | 2         | Django 201  | 6 weeks         |
| 2          | Bob          | bob@email.com       | 1         | Python 101  | 8 weeks         |
| 2          | Bob          | bob@email.com       | 3         | Web Design  | 4 weeks         |

At first glance this looks fine. But notice the problems:

**Problem 1 — Repeated data (Redundancy)**
Alice's email `alice@email.com` appears twice. "Python 101 — 8 weeks" appears twice. If Alice changes her email, you have to update it in *every row* she appears in. Miss one row and your data is inconsistent.

**Problem 2 — Update anomalies**
If Python 101's duration changes from 8 weeks to 10 weeks, you must update every row that mentions Python 101. With thousands of students enrolled, that's thousands of updates — and one missed row silently corrupts your data.

**Problem 3 — Delete anomalies**
If Bob drops Web Design (deleting that row), you also lose the only record that Web Design exists, its duration, and any details about it. Deleting an enrollment accidentally destroys course information.

**Problem 4 — Hard to query**
"List all unique courses" or "find all students in Python 101" becomes awkward and slow when the same data is repeated everywhere.

**The fix — split into focused tables:**

```
students table        enrollments table             courses table
┌────┬───────┐        ┌────────────┬──────────┐    ┌────┬─────────────┬──────────┐
│ id │ name  │        │ student_id │ course_id│    │ id │    name     │ duration │
├────┼───────┤        ├────────────┼──────────┤    ├────┼─────────────┼──────────┤
│  1 │ Alice │        │     1      │    1     │    │  1 │ Python 101  │ 8 weeks  │
│  2 │ Bob   │        │     1      │    2     │    │  2 │ Django 201  │ 6 weeks  │
└────┴───────┘        │     2      │    1     │    │  3 │ Web Design  │ 4 weeks  │
                      │     2      │    3     │    └────┴─────────────┴──────────┘
                      └────────────┴──────────┘
```

Now each piece of information lives in exactly **one place**:
- Alice's email is stored once in `students`.
- Python 101's duration is stored once in `courses`.
- Enrollments only store the relationship (who joined what).

> This principle — store each fact in exactly one place — is called **normalization**. You don't need to master the formal rules yet, but the idea is simple: **no unnecessary repetition**.

---

### ❓ How do I decide when to split into a separate table?

Here's a practical checklist you can use when designing your models:

**Split into a separate table when...**

| Signal | Example |
|--------|---------|
| The same data repeats across multiple rows | Course name + duration appearing in every enrollment row |
| A group of columns describes a *different thing* | Student info mixed with Course info — these are clearly separate things |
| You'll need to update that data independently | Changing a course duration shouldn't require touching enrollment rows |
| The relationship is one-to-many or many-to-many | One student → many enrollments; one course → many enrollments |

**Keep in the same table when...**

| Signal | Example |
|--------|---------|
| The data only belongs to that one record | A user's own `date_of_birth` — only that user has it |
| It's a simple attribute with no repetition | A product's `price` or `weight` |
| It's a one-to-one detail that's always fetched together | A user's profile bio — always shown on the same page as the user |

**A simple rule of thumb:**

> Ask yourself: *"Is this column describing the same thing as the rest of the table, or is it describing something else?"*
>
> - `students.email` → describes the **student** ✅ keep it
> - `students.course_name` → describes the **course**, not the student ❌ move it out

**Real-world example — should `city` be its own table?**

Consider a `users` table with a `city` column:

- If city is just a text label (`"Kathmandu"`) and you never need extra info about the city → **keep it as a column**.
- If you need to store city population, timezone, country, etc., and many users share the same city → **split it into a `cities` table** to avoid repetition.

There is no single formula — it depends on your app's needs. But the question to always ask is: **"Will this data repeat, or will I need to change it independently?"** If yes to either, it's a candidate for its own table.

> 📌 In Django terms: if something deserves its own `Model` class, it deserves its own table.

---

## 8. CRUD Operations

**CRUD** describes the four basic things you can do with data:

| Letter | Operation | What it does          | Real-world example           |
|--------|-----------|-----------------------|------------------------------|
| **C**  | Create    | Add new data          | Register a new user          |
| **R**  | Read      | Fetch/view data       | Display all blog posts       |
| **U**  | Update    | Change existing data  | Edit your profile name       |
| **D**  | Delete    | Remove data           | Delete a comment             |

> 📌 Django ORM has direct methods for each: `.create()`, `.filter()` / `.get()`, `.update()`, `.delete()`

---

## 9. Basic SQL Queries

**SQL** (Structured Query Language) is the language used to talk to a database. Django ORM generates SQL for you, but knowing the basics helps you understand what's happening under the hood.

---

### INSERT — Add new data (Create)
```sql
INSERT INTO users (name, email, age)
VALUES ('Alice', 'alice@email.com', 25);
```

---

### SELECT — Fetch data (Read)
```sql
-- Get all users
SELECT * FROM users;

-- Get only name and email
SELECT name, email FROM users;

-- Get users older than 18
SELECT * FROM users WHERE age > 18;
```

---

### UPDATE — Change existing data (Update)
```sql
UPDATE users
SET age = 26
WHERE name = 'Alice';
```

---

### DELETE — Remove data (Delete)
```sql
DELETE FROM users
WHERE name = 'Charlie';
```

> ⚠️ Always use `WHERE` with `UPDATE` and `DELETE` — without it, you'll modify **every row** in the table!

---

## 10. Introduction to JOINs

A **JOIN** combines rows from two or more tables based on a related column (usually a Foreign Key).

**Example:** You want to see each post title along with its author's name.

**Tables:**

`users`
| id | name  |
|----|-------|
| 1  | Alice |
| 2  | Bob   |

`posts`
| id | title         | user_id |
|----|---------------|---------|
| 1  | Hello World   | 1       |
| 2  | Django Tips   | 2       |

**JOIN Query:**
```sql
SELECT posts.title, users.name
FROM posts
JOIN users ON posts.user_id = users.id;
```

**Result:**
| title       | name  |
|-------------|-------|
| Hello World | Alice |
| Django Tips | Bob   |

```
posts table         users table
┌──────────────┐    ┌────────────┐
│ user_id = 1  │───►│  id = 1    │
│ "Hello World"│    │  "Alice"   │
└──────────────┘    └────────────┘
```

> 📌 Django ORM handles JOINs automatically when you access related models:
> `post.author.name` — no SQL needed!

---

## 11. How These Concepts Relate to Django ORM

Django ORM (Object-Relational Mapper) lets you work with your database using **Python code** instead of writing SQL.

Here's how everything maps:

| Database Concept        | Django Equivalent                                  |
|-------------------------|----------------------------------------------------|
| Table                   | `Model` class (e.g., `class Post(models.Model)`)   |
| Column                  | Model field (e.g., `title = models.CharField(...)`) |
| Row                     | Model instance (e.g., `post = Post(title="Hello")`) |
| Primary Key             | Auto-added `id` field                              |
| Foreign Key             | `models.ForeignKey(...)`                           |
| One-to-One              | `models.OneToOneField(...)`                        |
| Many-to-Many            | `models.ManyToManyField(...)`                      |
| `INSERT INTO`           | `Post.objects.create(...)`                         |
| `SELECT * FROM`         | `Post.objects.all()`                               |
| `SELECT WHERE`          | `Post.objects.filter(title="Hello")`               |
| `UPDATE SET WHERE`      | `post.title = "New Title"; post.save()`            |
| `DELETE WHERE`          | `post.delete()`                                    |
| `JOIN`                  | Accessing related fields: `post.author.name`       |

**Quick Django ORM Example:**
```python
from myapp.models import Post, User

# CREATE — INSERT INTO posts...
post = Post.objects.create(title="Hello World", author=alice)

# READ — SELECT * FROM posts WHERE title = 'Hello World'
post = Post.objects.get(title="Hello World")

# READ all — SELECT * FROM posts
all_posts = Post.objects.all()

# UPDATE — UPDATE posts SET title = ... WHERE id = 1
post.title = "Updated Title"
post.save()

# DELETE — DELETE FROM posts WHERE id = 1
post.delete()

# JOIN (automatic!) — access related table
print(post.author.name)  # No SQL needed
```

---

## ✅ Summary

```
Database Concept          →   Django ORM
─────────────────────────────────────────────────────
Database                  →   Your Django project's db
Table                     →   models.py Model class
Column / Data Type        →   Field (CharField, IntField…)
Row / Record              →   Model instance
Primary Key               →   Auto id field
Foreign Key               →   ForeignKey()
One-to-One                →   OneToOneField()
One-to-Many               →   ForeignKey()
Many-to-Many              →   ManyToManyField()
INSERT                    →   .create() or .save()
SELECT                    →   .all() / .filter() / .get()
UPDATE                    →   modify field + .save()
DELETE                    →   .delete()
JOIN                      →   dot notation (obj.related.field)
```

> 🎉 **You're ready for Django ORM!** With these fundamentals, you'll understand *why* Django models and queries work the way they do — not just *how* to use them.
