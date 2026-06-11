# Django ORM Study Notes
### For Students Who Already Know Basic Database & SQL Concepts

---

> **Who these notes are for:** You already understand tables, rows, columns, primary keys, foreign keys, relationships, and basic SQL (`SELECT`, `INSERT`, `UPDATE`, `DELETE`). These notes will show you how Django lets you do all of that — and more — using plain Python code.

---

## Table of Contents

1. [What is Django ORM?](#1-what-is-django-orm)
2. [Creating Models](#2-creating-models)
3. [Migrations](#3-migrations)
4. [Django Shell](#4-django-shell)
5. [CRUD Operations](#5-crud-operations)
6. [QuerySet Basics](#6-queryset-basics)
7. [Common Query Lookups](#7-common-query-lookups)
8. [Ordering and Limiting Results](#8-ordering-and-limiting-results)
9. [Useful QuerySet Methods](#9-useful-queryset-methods)
10. [Model Relationships](#10-model-relationships)
11. [Accessing Related Data](#11-accessing-related-data)
12. [Working with FileField and ImageField](#12-working-with-filefield-and-imagefield)
13. [Common ORM Mistakes](#13-common-orm-mistakes)
14. [ORM vs SQL Examples](#14-orm-vs-sql-examples)
15. [Cheat Sheet](#15-django-orm-cheat-sheet)
16. [Key Takeaways for Beginners](#16-key-takeaways-for-beginners)

---

## 1. What is Django ORM?

### ORM Meaning

**ORM** stands for **Object-Relational Mapper**. It is a tool that sits between your Python code and your database. Instead of writing raw SQL queries, you write Python code, and Django translates it into SQL for you automatically.

Think of ORM as a **translator**: you speak Python, the database speaks SQL, and Django handles the conversation in between.

```
Your Python Code  →  Django ORM  →  SQL Query  →  Database
```

### Benefits of ORM

| Benefit | Explanation |
|---|---|
| **No raw SQL needed** | Write Python instead of SQL strings |
| **Database independent** | Switch from SQLite to PostgreSQL with minimal changes |
| **Safer queries** | Django protects against SQL injection by default |
| **Less code** | Common operations require very few lines |
| **Readable** | Python code is easier to read and maintain than SQL strings |

### ORM vs SQL — Side by Side

| Task | SQL | Django ORM |
|---|---|---|
| Get all users | `SELECT * FROM users;` | `User.objects.all()` |
| Get user with id=1 | `SELECT * FROM users WHERE id=1;` | `User.objects.get(id=1)` |
| Insert a user | `INSERT INTO users ...` | `User.objects.create(...)` |
| Delete a user | `DELETE FROM users WHERE id=1;` | `user.delete()` |

---

## 2. Creating Models

### Defining Models

In Django, a **model** is a Python class that represents a database table. Each attribute of the class represents a column in that table.

Models go inside your app's `models.py` file.

```python
# models.py
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    enrolled = models.BooleanField(default=True)
    joined_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
```

> **Tip:** Always define `__str__` — it makes your model instances readable when printed or shown in the Django admin.

### Common Field Types

| Field | What It Stores | Example |
|---|---|---|
| `CharField` | Short text (requires `max_length`) | Name, title |
| `TextField` | Long text | Blog post body |
| `IntegerField` | Whole numbers | Age, quantity |
| `FloatField` | Decimal numbers | Price, rating |
| `BooleanField` | True / False | Is active? |
| `DateField` | Date only | Birthday |
| `DateTimeField` | Date + time | Created at |
| `EmailField` | Valid email address | user@example.com |
| `URLField` | Valid URL | Website link |
| `ImageField` | Image file path | Profile photo |
| `FileField` | Any file path | Uploaded document |
| `ForeignKey` | Link to another model | Author → Post |

**Common field options:**

```python
name = models.CharField(max_length=100, blank=True, null=True)
```

| Option | Meaning |
|---|---|
| `max_length` | Maximum number of characters (required for `CharField`) |
| `blank=True` | The field can be left empty in forms |
| `null=True` | The database column can store `NULL` |
| `default=value` | Default value if none is provided |
| `unique=True` | No two rows can have the same value |

### Understanding Django's Automatic `id` Field

You do **not** need to define a primary key manually. Django automatically adds an `id` field to every model:

```python
id = models.AutoField(primary_key=True)
```

This field:
- Starts at `1`
- Increments automatically for each new record
- Is the default way to look up individual objects

---

## 3. Migrations

### Why Migrations Are Needed

Your models are Python classes. The actual database tables do not exist yet. Migrations are Django's way of **creating and updating database tables** to match your models.

Think of it in two steps:
1. **Plan the changes** → `makemigrations`
2. **Apply the changes** → `migrate`

### `makemigrations`

This command reads your `models.py` and creates a migration file — a set of instructions that describes what to change in the database.

```bash
python manage.py makemigrations
```

**Output:**
```
Migrations for 'students':
  students/migrations/0001_initial.py
    - Create model Student
```

### `migrate`

This command takes those migration files and actually runs them against the database, creating or updating the tables.

```bash
python manage.py migrate
```

**Output:**
```
Applying students.0001_initial... OK
```

### Full Workflow

```
1. Edit models.py
        ↓
2. python manage.py makemigrations
        ↓
3. python manage.py migrate
        ↓
   Database table is created/updated
```

> ⚠️ **Common Mistake:** Many beginners add or change a field in `models.py` but forget to run `makemigrations` and `migrate`. If you skip this step, your database won't reflect your changes and you'll get errors.

---

## 4. Django Shell

### Opening the Shell

The Django shell is an interactive Python environment where you can test your ORM queries without writing a full view or script.

```bash
python manage.py shell
```

You'll see a Python `>>>` prompt. Now you can import your models and run queries.

### Testing ORM Queries

```python
>>> from students.models import Student

# Create a student
>>> s = Student.objects.create(name="Alice", email="alice@example.com", age=20)

# Retrieve all students
>>> Student.objects.all()
<QuerySet [<Student: Alice>]>

# Exit the shell
>>> exit()
```

> **Tip:** Use the shell constantly while learning. It gives you instant feedback and helps you understand exactly what each ORM method does.

---

## 5. CRUD Operations

CRUD stands for **Create, Read, Update, Delete** — the four basic operations you perform on any database.

### Create

**Method 1: `create()` — one step**

```python
student = Student.objects.create(name="Bob", email="bob@example.com", age=22)
```

**Method 2: Instantiate and `save()` — two steps**

```python
student = Student(name="Carol", email="carol@example.com", age=21)
student.save()  # Don't forget this!
```

> ⚠️ **Common Mistake:** With Method 2, if you forget to call `.save()`, the object exists in Python memory but is **never written to the database**.

### Read

```python
# Get all students
students = Student.objects.all()

# Get one specific student
student = Student.objects.get(id=1)

# Get students matching a condition
young_students = Student.objects.filter(age=20)
```

### Update

**Update a single object:**

```python
student = Student.objects.get(id=1)
student.name = "Bobby"
student.save()  # Must call save() to persist changes
```

**Update multiple objects at once:**

```python
Student.objects.filter(age=20).update(enrolled=False)
```

> ⚠️ **Common Mistake:** When updating a single object, you must call `.save()` at the end. Without it, your change only exists in Python — the database is untouched.

### Delete

**Delete a single object:**

```python
student = Student.objects.get(id=1)
student.delete()
```

**Delete multiple objects:**

```python
Student.objects.filter(enrolled=False).delete()
```

---

## 6. QuerySet Basics

A **QuerySet** is a list of database objects returned by Django ORM. It is lazy — meaning Django doesn't actually hit the database until you use the results (print them, loop over them, etc.).

### `all()`

Returns every row in the table.

```python
students = Student.objects.all()
# SQL equivalent: SELECT * FROM students;
```

### `get()`

Returns **exactly one** object. Raises an error if 0 or more than 1 result is found.

```python
student = Student.objects.get(id=3)
print(student.name)  # Output: Alice
```

> ⚠️ **Common Mistake:** Using `get()` when there might be 0 or multiple results will crash your app. Use `filter()` when you're unsure.

### `filter()`

Returns a QuerySet of **all matching objects** (could be 0, 1, or many).

```python
students = Student.objects.filter(age=20)
# Returns all students aged 20
```

### `first()`

Returns the first object in the QuerySet, or `None` if empty.

```python
student = Student.objects.filter(age=20).first()
```

### `last()`

Returns the last object in the QuerySet, or `None` if empty.

```python
student = Student.objects.filter(age=20).last()
```

### `get()` vs `filter()` — Quick Comparison

| | `get()` | `filter()` |
|---|---|---|
| Returns | Single object | QuerySet (list) |
| If 0 results | Raises `DoesNotExist` error | Returns empty QuerySet |
| If 2+ results | Raises `MultipleObjectsReturned` error | Returns all matches |
| When to use | When you're sure exactly 1 result exists | When you expect 0, 1, or many results |

---

## 7. Common Query Lookups

Django uses **double underscores (`__`)** to add conditions to queries. These are called **field lookups**.

Format: `field_name__lookup_type=value`

### `exact`

Exact match (default if no lookup is given).

```python
Student.objects.filter(name__exact="Alice")
# Same as:
Student.objects.filter(name="Alice")
```

### `contains`

Field contains the given value (case-sensitive).

```python
Student.objects.filter(name__contains="ali")
# Matches "alice", "Malia" — but NOT "Ali" (case-sensitive)
```

### `icontains`

Same as `contains` but case-insensitive. Most commonly used.

```python
Student.objects.filter(name__icontains="ali")
# Matches "alice", "Ali", "ALICE"
```

### `startswith` / `endswith`

```python
Student.objects.filter(name__startswith="A")   # Names starting with A
Student.objects.filter(email__endswith=".com")  # Emails ending with .com
```

### `gt`, `gte`, `lt`, `lte`

Numeric comparisons: greater than, greater than or equal, less than, less than or equal.

```python
Student.objects.filter(age__gt=20)   # age > 20
Student.objects.filter(age__gte=20)  # age >= 20
Student.objects.filter(age__lt=25)   # age < 25
Student.objects.filter(age__lte=25)  # age <= 25
```

### `in`

Match against a list of values.

```python
Student.objects.filter(age__in=[20, 21, 22])
# Returns students whose age is 20, 21, or 22
```

### Combining Multiple Filters

```python
# AND condition — chain filter() calls or use comma inside filter
Student.objects.filter(age__gte=20, enrolled=True)
```

---

## 8. Ordering and Limiting Results

### `order_by()`

Sort results by a field. Prefix with `-` for descending order.

```python
# Ascending (A → Z, lowest → highest)
Student.objects.all().order_by('name')

# Descending (Z → A, highest → lowest)
Student.objects.all().order_by('-age')

# Order by multiple fields
Student.objects.all().order_by('age', 'name')
```

### `reverse()`

Reverses the order of an already-ordered QuerySet.

```python
Student.objects.all().order_by('name').reverse()
```

### Slicing QuerySets

You can slice a QuerySet like a Python list to limit results.

```python
# Get the first 5 students
Student.objects.all()[:5]

# Get students 6–10 (offset 5, limit 5)
Student.objects.all()[5:10]
```

> ⚠️ **Note:** Negative indexing like `[-1]` does not work on QuerySets. Use `.last()` instead.

---

## 9. Useful QuerySet Methods

### `count()`

Returns the number of results as an integer.

```python
total = Student.objects.all().count()
print(total)  # Output: 42

enrolled = Student.objects.filter(enrolled=True).count()
print(enrolled)  # Output: 35
```

### `exists()`

Returns `True` if any results exist, `False` otherwise. Faster than `count()` for just checking existence.

```python
if Student.objects.filter(email="alice@example.com").exists():
    print("Email already registered!")
```

### `values()`

Returns QuerySet as a list of **dictionaries** instead of model objects. Useful when you only need specific fields.

```python
Student.objects.values('name', 'email')
# Output:
# <QuerySet [{'name': 'Alice', 'email': 'alice@example.com'}, ...]>
```

### `values_list()`

Like `values()`, but returns **tuples** instead of dictionaries.

```python
Student.objects.values_list('name', 'age')
# Output:
# <QuerySet [('Alice', 20), ('Bob', 22), ...]>

# With flat=True — returns a flat list (only works with one field)
Student.objects.values_list('name', flat=True)
# Output: <QuerySet ['Alice', 'Bob', 'Carol']>
```

---

## 10. Model Relationships

Django supports three types of relationships between models.

### `OneToOneField`

One record in table A is linked to **exactly one** record in table B.

**Real-world example:** A `User` has one `Profile`. Each profile belongs to one user.

```python
class User(models.Model):
    username = models.CharField(max_length=100)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True)
```

### `ForeignKey`

Many records in table A can link to **one** record in table B.

**Real-world example:** Many `Posts` are written by one `Author`. One author can write many posts.

```python
class Author(models.Model):
    name = models.CharField(max_length=100)

class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
```

**`on_delete` options:**

| Option | What happens when the referenced object is deleted |
|---|---|
| `CASCADE` | Delete all related objects too |
| `SET_NULL` | Set the field to `NULL` (requires `null=True`) |
| `PROTECT` | Prevent deletion if related objects exist |
| `SET_DEFAULT` | Set the field to its default value |

### `ManyToManyField`

Records in table A can link to **many** records in table B, and vice versa.

**Real-world example:** A `Student` can enroll in many `Courses`, and a `Course` can have many `Students`.

```python
class Course(models.Model):
    title = models.CharField(max_length=200)

class Student(models.Model):
    name = models.CharField(max_length=100)
    courses = models.ManyToManyField(Course, blank=True)
```

**Working with ManyToMany:**

```python
student = Student.objects.get(id=1)

# Enroll in a course
course = Course.objects.get(id=2)
student.courses.add(course)

# Remove from a course
student.courses.remove(course)

# View all courses for a student
student.courses.all()
```

---

## 11. Accessing Related Data

### Forward Relationships

Access data from the model that **holds the field**.

```python
# Post has a ForeignKey to Author
post = Post.objects.get(id=1)
print(post.author.name)  # Access the related Author directly
```

### Reverse Relationships

Access data from the **other side** of the relationship (the model that was referenced).

Django automatically creates a reverse accessor with the name `modelname_set`.

```python
# From an Author, get all their Posts
author = Author.objects.get(id=1)
posts = author.post_set.all()  # All posts by this author
```

### `related_name`

You can give the reverse accessor a custom name using `related_name`.

```python
class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=200)
```

Now instead of `author.post_set.all()`, you can write:

```python
author = Author.objects.get(id=1)
posts = author.posts.all()  # Much cleaner!
```

> **Tip:** Always set `related_name` — it makes your code much more readable.

---

## 12. Working with FileField and ImageField

### Basic Usage

`FileField` stores any uploaded file. `ImageField` is specifically for images (it validates the file is an image).

```python
class Document(models.Model):
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='documents/')

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
```

> `upload_to` specifies the subfolder inside your `MEDIA_ROOT` where files will be saved.

In `settings.py`, you need:

```python
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

> ⚠️ **Note:** To use `ImageField`, you need to install the `Pillow` library:
> ```bash
> pip install Pillow
> ```

### Accessing File URLs

```python
profile = UserProfile.objects.get(id=1)

# Get the file path (relative to MEDIA_ROOT)
print(profile.avatar.name)
# Output: avatars/alice_photo.jpg

# Get the URL to use in templates
print(profile.avatar.url)
# Output: /media/avatars/alice_photo.jpg
```

In a Django template:

```html
<img src="{{ profile.avatar.url }}" alt="Profile picture">
```

---

## 13. Common ORM Mistakes

### Mistake 1: Using `get()` When the Object Might Not Exist

```python
# BAD — crashes if no student with id=999 exists
student = Student.objects.get(id=999)

# GOOD — safe alternative
student = Student.objects.filter(id=999).first()
if student:
    print(student.name)
else:
    print("Not found")
```

Or use `get_or_404` in views:

```python
from django.shortcuts import get_object_or_404
student = get_object_or_404(Student, id=999)
```

### Mistake 2: Forgetting `save()`

```python
# BAD — change never reaches the database
student = Student.objects.get(id=1)
student.name = "Alice Updated"
# Forgot student.save() !

# GOOD
student = Student.objects.get(id=1)
student.name = "Alice Updated"
student.save()  ✓
```

### Mistake 3: Accessing Objects That Don't Exist

```python
# This raises Student.DoesNotExist error
Student.objects.get(name="Nobody Here")

# Safe approach with try/except
try:
    student = Student.objects.get(name="Alice")
except Student.DoesNotExist:
    student = None
```

### Mistake 4: The N+1 Query Problem (Brief Introduction)

Imagine you have 100 posts and you want to print the author name for each:

```python
# BAD — runs 1 query to get all posts, then 1 MORE query per post for the author
# That's 1 + 100 = 101 queries!
posts = Post.objects.all()
for post in posts:
    print(post.author.name)
```

```python
# GOOD — use select_related() to fetch everything in 1 query
posts = Post.objects.select_related('author').all()
for post in posts:
    print(post.author.name)  # No extra queries!
```

> **Rule of thumb:** Whenever you're looping over objects and accessing a related field inside the loop, use `select_related()` (for ForeignKey / OneToOne) or `prefetch_related()` (for ManyToMany).

---

## 14. ORM vs SQL Examples

| Task | SQL | Django ORM |
|---|---|---|
| Get all rows | `SELECT * FROM students;` | `Student.objects.all()` |
| Get specific columns | `SELECT name, email FROM students;` | `Student.objects.values('name', 'email')` |
| Filter rows | `SELECT * FROM students WHERE age = 20;` | `Student.objects.filter(age=20)` |
| Filter with condition | `SELECT * FROM students WHERE age > 18;` | `Student.objects.filter(age__gt=18)` |
| Get one row by ID | `SELECT * FROM students WHERE id = 1;` | `Student.objects.get(id=1)` |
| Insert a row | `INSERT INTO students (name, age) VALUES ('Alice', 20);` | `Student.objects.create(name='Alice', age=20)` |
| Update a row | `UPDATE students SET name='Bobby' WHERE id=1;` | `s = Student.objects.get(id=1); s.name='Bobby'; s.save()` |
| Update multiple rows | `UPDATE students SET enrolled=0 WHERE age < 18;` | `Student.objects.filter(age__lt=18).update(enrolled=False)` |
| Delete a row | `DELETE FROM students WHERE id=1;` | `Student.objects.get(id=1).delete()` |
| Count rows | `SELECT COUNT(*) FROM students;` | `Student.objects.count()` |
| Order results | `SELECT * FROM students ORDER BY name ASC;` | `Student.objects.order_by('name')` |
| Limit results | `SELECT * FROM students LIMIT 5;` | `Student.objects.all()[:5]` |
| Search with LIKE | `SELECT * FROM students WHERE name LIKE '%ali%';` | `Student.objects.filter(name__icontains='ali')` |

---

## 15. Django ORM Cheat Sheet

### Model Definition

```python
from django.db import models

class MyModel(models.Model):
    name    = models.CharField(max_length=100)
    text    = models.TextField()
    number  = models.IntegerField()
    decimal = models.FloatField()
    flag    = models.BooleanField(default=True)
    date    = models.DateField(auto_now_add=True)
    dt      = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
```

### Migrations

```bash
python manage.py makemigrations   # Detect model changes
python manage.py migrate          # Apply changes to database
python manage.py shell            # Open interactive shell
```

### CRUD

```python
# Create
obj = MyModel.objects.create(name="Hello")

# Read
MyModel.objects.all()                      # All objects
MyModel.objects.get(id=1)                  # One (exact match)
MyModel.objects.filter(name="Hello")       # Many (filtered)
MyModel.objects.filter(name="Hello").first()  # First match or None

# Update
obj = MyModel.objects.get(id=1)
obj.name = "Updated"
obj.save()
# or
MyModel.objects.filter(id=1).update(name="Updated")

# Delete
MyModel.objects.get(id=1).delete()
MyModel.objects.filter(flag=False).delete()
```

### QuerySet Methods

```python
.all()                    # All objects
.filter(field=value)      # Filter by condition
.exclude(field=value)     # Exclude matching objects
.get(field=value)         # Single object (raises error if 0 or 2+)
.first()                  # First result or None
.last()                   # Last result or None
.count()                  # Number of results (integer)
.exists()                 # True/False
.order_by('field')        # Ascending
.order_by('-field')       # Descending
[:5]                      # Limit to 5
[5:10]                    # Offset 5, limit 5
.values('f1', 'f2')       # List of dicts
.values_list('f1', flat=True)  # Flat list
.update(field=value)      # Bulk update
.delete()                 # Bulk delete
```

### Field Lookups

```python
__exact        # Exact match (default)
__iexact       # Exact match, case-insensitive
__contains     # LIKE %value% (case-sensitive)
__icontains    # LIKE %value% (case-insensitive)
__startswith   # LIKE value%
__endswith     # LIKE %value
__gt           # >
__gte          # >=
__lt           # <
__lte          # <=
__in           # IN (list)
__isnull       # IS NULL (True/False)
```

### Relationships

```python
# ForeignKey
class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='posts')

# Access forward
post.author.name

# Access reverse
author.posts.all()

# ManyToMany
student.courses.add(course)
student.courses.remove(course)
student.courses.all()

# Avoid N+1
Post.objects.select_related('author').all()       # FK / OneToOne
Post.objects.prefetch_related('tags').all()       # ManyToMany
```

---

## 16. Key Takeaways for Beginners

Here are the most important concepts to remember as you start using Django ORM:

1. **A model = a database table.** Each class is a table, each attribute is a column.

2. **Always run migrations after changing models.** `makemigrations` plans the change, `migrate` applies it.

3. **Django adds an `id` field automatically** — you don't need to define it yourself.

4. **`get()` is for exactly one result.** Use `filter()` when you're not sure how many results you'll get.

5. **Always call `.save()` after modifying an object.** Without it, your changes don't reach the database.

6. **QuerySets are lazy.** Django doesn't query the database until you actually use the data.

7. **`filter()` never crashes.** It returns an empty QuerySet if nothing matches. `get()` raises an error.

8. **Use `__` (double underscore) for lookups.** e.g., `age__gt=18`, `name__icontains="ali"`.

9. **`related_name` makes reverse lookups cleaner.** Always set it on your `ForeignKey` fields.

10. **Use `select_related()` in loops** to avoid the N+1 query problem when accessing related objects.

---

*Happy coding! The best way to learn Django ORM is to use the shell and experiment freely. Make models, query them, break things, and fix them — that's how it sticks.*
