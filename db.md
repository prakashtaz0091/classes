# **Introduction to Databases and Normalization**

This document provides the essential database concepts required before learning Django models. Understanding these fundamentals will help you understand how Django maps Python classes to tables, rows, and relationships in a relational database.

---

## **1. What is a Database?**

A database is a structured system for storing, organizing, and retrieving data efficiently.
Django uses relational databases by default, such as SQLite, PostgreSQL, or MySQL.

**Why databases instead of files:**

* Data is structured and organized.
* Faster lookup and filtering.
* Supports relationships between data.
* Supports concurrent access from multiple users.
* Provides reliability and consistency.

**Types of Databases:**

1. **SQL (Relational Databases):** Store data in tables with rows and columns. Examples: SQLite, PostgreSQL, MySQL.
2. **NoSQL (Non-relational Databases):** Store data in JSON-like documents, key-value pairs, graphs, etc. Example: MongoDB.

Django primarily works with SQL relational databases.

---

## **2. Tables, Rows, and Columns**

A table represents a collection of similar data. Each Django Model maps directly to one table.

* A **column** represents an attribute of the data.
* A **row** represents one record.

**Example: Student Table**

| id | name | email                                       | age |
| -- | ---- | ------------------------------------------- | --- |
| 1  | Ram  | [ram@example.com](mailto:ram@example.com)   | 18  |
| 2  | Sita | [sita@example.com](mailto:sita@example.com) | 20  |

**Mapping to Django:**

* Table → Model class
* Column → Model field
* Row → Model instance

---

## **3. Primary Keys**

A primary key is a unique identifier for each row in a table. Every table must have a primary key.

* Example: student_id, product_id
* Django automatically creates a primary key column named `id` unless specified otherwise.

**Why primary keys matter:**

* They uniquely identify a record.
* They are used to form relationships between tables.
* They make searching and indexing efficient.

---

## **4. Data Types**

Database columns have specific data types. Django maps these to model fields.

| SQL Type    | Django Field            |
| ----------- | ----------------------- |
| INTEGER     | IntegerField            |
| VARCHAR(n)  | CharField(max_length=n) |
| TEXT        | TextField               |
| DATE        | DateField               |
| DATETIME    | DateTimeField           |
| BOOLEAN     | BooleanField            |
| FOREIGN KEY | ForeignKey              |

Understanding data types helps you choose the correct Django field type.

---

## **5. Relationships Between Tables**

Real-life data is often connected. Databases represent these connections using relationships.

**Three main types:**

### One-to-One

One record in table A matches exactly one record in table B.
Example: One user has one profile.

### One-to-Many

One record in table A relates to many records in table B.
Example: One category has many products.
This is the most common relationship.

### Many-to-Many

Many records in table A are associated with many records in table B.
Example: Students and courses.
A student can join multiple courses, and each course can have many students.

Understanding these relationships is crucial because Django uses `ForeignKey`, `OneToOneField`, and `ManyToManyField` to implement them.

---

## **6. Foreign Keys**

A foreign key is a column in one table that references the primary key of another table.

**Example:**
Student table with a foreign key referencing Class table:

| student_id | name | class_id |
| ---------- | ---- | -------- |
| 1          | Ram  | 2        |
| 2          | Sita | 1        |

Here, `class_id` is a foreign key referencing `Class.id`.

**Why foreign keys matter:**

* Ensures data consistency (no invalid references)
* Establishes structured relationships
* Allows efficient querying across related tables

In Django:

```python
class Student(models.Model):
    name = models.CharField(max_length=100)
    class_ref = models.ForeignKey(Class, on_delete=models.CASCADE)
```

---

## **7. Basic SQL Commands (CRUD)**

CRUD refers to the four basic operations you perform in a database.

**Create (INSERT)**

```sql
INSERT INTO student (name, age) VALUES ('Ram', 18);
```

**Read (SELECT)**

```sql
SELECT * FROM student;
SELECT * FROM student WHERE age > 18;
```

**Update (UPDATE)**

```sql
UPDATE student SET age = 20 WHERE id = 1;
```

**Delete (DELETE)**

```sql
DELETE FROM student WHERE id = 1;
```

Django ORM provides Python methods that internally translate to these SQL commands.

---

## **8. Indexes**

An index is a data structure that makes data retrieval faster. Think of it like an index at the back of a book.

* Primary keys are automatically indexed.
* Indexes improve lookup performance.
* Overuse of indexes can slow down insert/update operations.

Django automatically creates indexes for primary keys and some unique fields.

---

## **9. Schema and Migrations**

A database schema refers to the structure of the database:

* Tables
* Columns
* Data types
* Relationships

When you define or update a Django model, the database schema must change accordingly.

A migration is a file that describes changes to the database schema:

* Adding a column
* Creating a table
* Removing a field

Django commands:

```bash
python manage.py makemigrations
python manage.py migrate
```

Migrations ensure the database stays in sync with your models.

---

## **10. Normalization**

Normalization organizes data to reduce redundancy and improve consistency. It splits data into multiple tables and defines relationships properly.

---

