# Django ORM Guide

Assume this model:

```python
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    published = models.DateField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
```

---

# 1. Creating Objects

### 1.1. Create and save

```python
book = Book(title="Django 101", author="John")
book.save()
```

Creates a Python object → then stores it in the database.

### 1.2. Create in one step

```python
Book.objects.create(title="Django 102", author="John")
```

Creates and saves the new row in one command.

---

# 2. Retrieving Objects

### 2.1. Get one object

```python
Book.objects.get(id=1)
```

Fetches exactly one row; errors if missing or duplicates.

### 2.2. Get all objects

```python
Book.objects.all()
```

Returns every row in the table.

### 2.3. Filter

```python
Book.objects.filter(author="John")
```

Returns only rows matching the condition.

### 2.4. Exclude

```python
Book.objects.exclude(author="John")
```

Returns all rows *except* those matching the condition.

### 2.5. First / Last

```python
Book.objects.first()
Book.objects.last()
```

Fetches the first or last entry based on default ordering.

### 2.6. exists

```python
Book.objects.filter(author="John").exists()
```

Checks **if data exists** without loading it.

### 2.7. Multiple conditions

```python
Book.objects.get(title="Django", author="John")
```

Finds a row that must match all given fields.

---

# 3. Updating

### 3.1. Update single object

```python
book = Book.objects.get(id=1)
book.price = 30
book.save()
```

Changes fields of a specific stored record.

### 3.2. Bulk update

```python
Book.objects.filter(author="John").update(price=10)
```

Updates multiple rows at once — efficient and fast.

---

# 4. Deleting

### 4.1. Delete one

```python
Book.objects.get(id=1).delete()
```

Deletes exactly one row.

### 4.2. Bulk delete

```python
Book.objects.filter(author="John").delete()
```

Deletes all matching rows.

---

# 5. Ordering

```python
Book.objects.order_by("price")     # ascending
Book.objects.order_by("-price")    # descending
```

Sorts results before returning them.

---

# 6. Field Lookups (Special Filters)

```python
Book.objects.filter(title__icontains="django")
```

Searches text inside a field (case-insensitive).

```python
Book.objects.filter(price__gte=20)
```

Finds values greater or equal to something.

```python
Book.objects.filter(published__year=2024)
```

Filters using part of a date.

```python
Book.objects.filter(price__range=(10, 30))
```

Finds values inside a numeric range.

```python
Book.objects.filter(author__in=["John", "Mike"])
```

Matches ANY value in a list.

These allow more advanced filtering than equality checks.

---

# 7. Selecting Specific Fields

### 7.1. Dictionaries

```python
Book.objects.values("title", "price")
```

Returns only selected fields in dictionary form.

### 7.2. Tuples

```python
Book.objects.values_list("title", "price")
```

Returns only chosen fields as tuples.

### 7.3. Flat values

```python
Book.objects.values_list("title", flat=True)
```

Returns a single column as a flat list.

Used when you want data without loading full model objects.

---

# 8. Counting and Summary

### 8.1. Count rows

```python
Book.objects.count()
```

Returns number of records.

### 8.2. Aggregations

```python
Book.objects.aggregate(Avg("price"))
```

Computes a numeric summary (max, min, avg, sum).

---

# 9. F Expressions (Field-to-field or math inside database)

### 9.1. Compare fields

```python
Book.objects.filter(price__gt=F("discounted_price"))
```

Compares two fields **without pulling data into Python**.

### 9.2. Increment/decrement

```python
Book.objects.update(price=F("price") + 5)
```

Increases a field value directly in the database.

### 9.3. Arithmetic operations

```python
Book.objects.update(price=F("price") * 1.1)
```

Performs math inside SQL — avoids race conditions.

### 9.4. Used inside annotate

```python
Book.objects.annotate(discounted=F("price") * 0.8)
```

Adds calculated fields to the result set.

### Why use F expressions?

They run **inside the database**, meaning:

* no Python-level iteration
* safe for concurrent updates
* faster for bulk operations

---

# 10. Q Objects (OR, NOT, complex conditions)

### 10.1. OR

```python
Book.objects.filter(Q(author="John") | Q(price__lt=20))
```

Allows logical OR in queries.

### 10.2. NOT

```python
Book.objects.filter(~Q(author="John"))
```

Negates a condition.

### 10.3. Combined logic

```python
Book.objects.filter(
    Q(author="John") & (Q(price__lt=30) | Q(title__startswith="D"))
)
```

Allows multiple logical layers — something `.filter()` alone can’t do.

---

# 11. Relationships

Given:

```python
class Author(models.Model):
    name = models.CharField(max_length=100)
```

### 11.1. Forward lookup

```python
Book.objects.filter(author__name="John")
```

Accesses fields on related models using double underscores.

### 11.2. Reverse lookup

```python
author.book_set.all()
```

Gets all books related to an author.

### 11.3. Count related items

```python
Author.objects.annotate(book_count=Count("book"))
```

Counts how many children exist per parent.

---

# 12. Query Optimizations

### 12.1. select_related

```python
Book.objects.select_related("author")
```

Performs a SQL JOIN to fetch the related object in a single query.
Use for **ForeignKey / OneToOne**.

### 12.2. prefetch_related

```python
Author.objects.prefetch_related("book_set")
```

Fetches related data efficiently using two queries.
Use for **ManyToMany / reverse FK**.

---

# 13. Limiting Retrieved Fields

### 13.1. only

```python
Book.objects.only("title")
```

Loads only selected fields initially.

### 13.2. defer

```python
Book.objects.defer("price")
```

Loads everything except certain fields.

Used for performance optimization.

---

# 14. Annotations (Add Calculated Fields)

### 14.1. Add static/calculated fields

```python
Book.objects.annotate(label=Value("New"))
```

Adds new fields to each result row.

### 14.2. Using math

```python
Book.objects.annotate(discounted=F("price") * 0.8)
```

Adds a calculated field.

### 14.3. Group-like operations

```python
Author.objects.annotate(total_books=Count("book"))
```

Adds counts or summaries **per item**.

### 14.4. Conditional annotation

```python
Book.objects.annotate(
    expensive=Case(
        When(price__gt=50, then=1),
        default=0,
        output_field=IntegerField()
    )
)
```

Creates fields based on conditions — like SQL’s CASE.

---

# 15. Bulk Operations

### 15.1. bulk_create

```python
Book.objects.bulk_create([...])
```

Inserts many rows in one query.

### 15.2. bulk_update

```python
Book.objects.bulk_update(books, ["price"])
```

Updates many rows efficiently.

---

# 16. get_or_create / update_or_create

### 16.1. get_or_create

```python
Book.objects.get_or_create(title="Django 101")
```

Fetches existing OR creates new — prevents duplicates.

### 16.2. update_or_create

```python
Book.objects.update_or_create(
    title="Django 101",
    defaults={"price": 30}
)
```

Finds and updates, or creates if missing.

---

# 17. Raw SQL

### 17.1. raw query

```python
Book.objects.raw("SELECT * FROM app_book")
```

Runs manual SQL while still returning model instances.

### 17.2. raw with parameters

```python
Book.objects.raw("SELECT * FROM app_book WHERE price > %s", [20])
```

Avoids SQL injection.

---

# 18. Transactions

### 18.1. atomic

```python
with transaction.atomic():
    ...
```

Ensures all database operations inside are treated as one —
if one fails, none are applied.

---
