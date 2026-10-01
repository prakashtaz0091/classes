# Python Practice: Tuple, Set & Dictionary

## Part 1 — Tuples

### 1. Create a Tuple

Create a tuple containing the following values:

```python
10, 20, 30, 40, 50
```

---

### 2. Access Tuple Elements

Given:

```python
numbers = (10, 20, 30, 40, 50)
```

Print the **first element** and the **last element**.

---

### 3. Tuple Length

Given:

```python
colors = ("red", "green", "blue", "yellow")
```

Find the number of elements in the tuple.

---

### 4. Tuple Indexing

Given:

```python
fruits = ("apple", "banana", "mango", "orange")
```

Print `"mango"` using its index.

---

### 5. Negative Indexing

Given:

```python
numbers = (5, 10, 15, 20, 25)
```

Print the last two elements using negative indexing.

---

### 6. Tuple Slicing

Given:

```python
numbers = (10, 20, 30, 40, 50, 60)
```

Print:

```text
(20, 30, 40)
```

using slicing.

---

### 7. Check an Item

Given:

```python
fruits = ("apple", "banana", "mango")
```

Check whether `"banana"` exists in the tuple.

---

### 8. Count an Element

Given:

```python
numbers = (1, 2, 2, 3, 2, 4)
```

Count how many times `2` appears.

---

### 9. Find the Index

Given:

```python
animals = ("cat", "dog", "lion", "tiger")
```

Find the index of `"lion"`.

---

### 10. Concatenate Tuples

Given:

```python
a = (1, 2, 3)
b = (4, 5, 6)
```

Create a new tuple containing all six numbers.

---

### 11. Repeat a Tuple

Given:

```python
x = ("Python",)
```

Create a tuple containing `"Python"` five times.

**Hint:** Think about the `*` operator.

---

### 12. Convert List to Tuple

Given:

```python
numbers = [10, 20, 30, 40]
```

Convert the list into a tuple.

---

### 13. Convert Tuple to List

Given:

```python
numbers = (10, 20, 30, 40)
```

Convert it into a list.

---

### 14. Find Maximum and Minimum

Given:

```python
numbers = (15, 5, 25, 10, 30)
```

Find the largest and smallest values.

**Hint:** Python has built-in functions for both operations.

---

### 15. Tuple Unpacking

Given:

```python
person = ("Prakash", 25, "Nepal")
```

Unpack the tuple into three variables:

```text
name
age
country
```

---

### 16. Swap Two Variables

Use tuple unpacking to swap:

```python
a = 10
b = 20
```

without using a third variable.

**Hint:** Python allows multiple assignment in one statement.

---

### 17. Nested Tuple

Given:

```python
students = (
    ("Ram", 80),
    ("Sita", 90),
    ("Hari", 75)
)
```

Print Sita's marks.

**Hint:** You need to use two indexes.

---

## Part 2 — Sets

### 18. Create a Set

Create a set containing:

```text
10, 20, 30, 40, 50
```

---

### 19. Duplicate Values

What will be the output?

```python
numbers = {1, 2, 2, 3, 3, 3, 4}
print(numbers)
```

Explain why the output contains fewer elements than the original values.

---

### 20. Add an Element

Given:

```python
numbers = {10, 20, 30}
```

Add `40` to the set.

---

### 21. Add Multiple Elements

Given:

```python
numbers = {10, 20}
```

Add:

```text
30, 40, 50
```

to the set.

**Hint:** There is a set method designed for adding multiple elements.

---

### 22. Remove an Element

Given:

```python
fruits = {"apple", "banana", "mango"}
```

Remove `"banana"`.

---

### 23. Check Membership

Given:

```python
colors = {"red", "green", "blue"}
```

Check whether `"green"` exists in the set.

---

### 24. Find Set Length

Given:

```python
numbers = {5, 10, 15, 20, 25}
```

Find the number of elements.

---

### 25. Union of Sets

Given:

```python
a = {1, 2, 3}
b = {3, 4, 5}
```

Find the union of `a` and `b`.

**Hint:** Union combines elements from both sets and removes duplicates.

---

### 26. Intersection of Sets

Given:

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
```

Find the common elements.

---

### 27. Difference of Sets

Given:

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
```

Find the elements that are in `a` but not in `b`.

---

### 28. Symmetric Difference

Given:

```python
a = {1, 2, 3}
b = {3, 4, 5}
```

Find the elements that exist in either set but **not in both**.

**Hint:** Look at the set operation that removes the common elements.

---

### 29. Remove Duplicates from a List

Given:

```python
numbers = [1, 2, 2, 3, 4, 4, 5, 5]
```

Create a new collection containing only unique values.

**Hint:** Think about what makes a set different from a list.

---

### 30. Set from a String

Convert:

```python
word = "programming"
```

into a set and observe which characters remain.

---

### 31. Subset

Given:

```python
a = {1, 2}
b = {1, 2, 3, 4}
```

Check whether `a` is a subset of `b`.

---

### 32. Superset

Using:

```python
a = {1, 2, 3, 4}
b = {1, 2}
```

Check whether `a` is a superset of `b`.

---

### 33. Empty Set

Create an empty set.

**Hint:** Be careful: `{}` creates a different Python data type.

---

### 34. Common Students

Two classes have these students:

```python
class_a = {"Ram", "Sita", "Hari", "Gita"}
class_b = {"Sita", "Gita", "Mina", "Ravi"}
```

Find the students who are in **both classes**.

---

## Part 3 — Dictionaries

### 35. Create a Dictionary

Create a dictionary containing:

```text
name → Prakash
age → 25
country → Nepal
```

---

### 36. Access a Dictionary Value

Given:

```python
student = {
    "name": "Ram",
    "age": 20,
    "marks": 85
}
```

Print Ram's marks.

---

### 37. Add a New Key

Given:

```python
student = {
    "name": "Ram",
    "age": 20
}
```

Add:

```text
"city": "Biratnagar"
```

---

### 38. Update a Value

Given:

```python
student = {
    "name": "Ram",
    "age": 20,
    "marks": 75
}
```

Change the marks from `75` to `90`.

---

### 39. Delete a Key

Given:

```python
student = {
    "name": "Ram",
    "age": 20,
    "marks": 75
}
```

Remove the `"age"` key.

---

### 40. Check a Key

Given:

```python
student = {
    "name": "Ram",
    "age": 20,
    "marks": 75
}
```

Check whether `"marks"` exists as a key.

---

### 41. Dictionary Length

Given:

```python
person = {
    "name": "Sita",
    "age": 22,
    "city": "Kathmandu"
}
```

Find the number of key-value pairs.

---

### 42. Print All Keys

Given:

```python
student = {
    "name": "Ram",
    "age": 20,
    "marks": 80
}
```

Print all the keys.

**Hint:** Use a dictionary method specifically designed to return keys.

---

### 43. Print All Values

Using the same dictionary, print all the values.

**Hint:** There is a dictionary method corresponding to the previous question.

---

### 44. Print Key-Value Pairs

Given:

```python
student = {
    "name": "Ram",
    "age": 20,
    "marks": 80
}
```

Print every key and value like:

```text
name : Ram
age : 20
marks : 80
```

**Hint:** Think about looping through key-value pairs together.

---

### 45. Dictionary from Two Lists

Given:

```python
keys = ["name", "age", "city"]
values = ["Ram", 20, "Pokhara"]
```

Create:

```python
{
    "name": "Ram",
    "age": 20,
    "city": "Pokhara"
}
```

**Hint:** Think about pairing corresponding elements from the two lists.

---

### 46. Count Characters

Given:

```python
word = "apple"
```

Create a dictionary that counts how many times each character appears.

Expected result:

```python
{
    "a": 1,
    "p": 2,
    "l": 1,
    "e": 1
}
```

**Hint:** Loop through each character and check whether it already exists in the dictionary.

---

### 47. Find the Student with Highest Marks

Given:

```python
students = {
    "Ram": 75,
    "Sita": 92,
    "Hari": 81,
    "Gita": 88
}
```

Find the student who has the highest marks.

**Hint:** You can compare the dictionary's values while keeping track of the corresponding key.

---

### 48. Nested Dictionary

Given:

```python
students = {
    "student1": {
        "name": "Ram",
        "age": 20,
        "marks": 85
    },
    "student2": {
        "name": "Sita",
        "age": 21,
        "marks": 90
    }
}
```

Print Sita's marks.

**Hint:** First access `"student2"`, then access its `"marks"` key.

---

### 49. Word Frequency Counter

Given:

```python
sentence = "python is easy and python is powerful"
```

Create a dictionary that counts how many times each word occurs.

Expected idea:

```text
python → 2
is → 2
easy → 1
and → 1
powerful → 1
```

**Hint:** Use `split()` to separate the sentence into words, then update a dictionary for each word.

---

### 50. Mini Student Record System

Create a dictionary containing information about **three students**.

For example:

```python
students = {
    "Ram": 80,
    "Sita": 95,
    "Hari": 75
}
```

Your program should:

1. Print all students.
2. Print each student's marks.
3. Calculate the average marks.
4. Find the student with the highest marks.
5. Find the student with the lowest marks.
6. Add a new student.
7. Update an existing student's marks.

**Hint:** Break the problem into small steps. First practice looping through the dictionary, then use the values for calculations.

---
