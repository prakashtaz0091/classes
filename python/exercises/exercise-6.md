# Python Set Exercises — 10 Main Questions

> **Instruction:** For every sub-question, first understand what is being asked, then decide which set operation or method is appropriate. Do not use loops unless necessary.

---

## Question 1 — Students and Sports

A school has two sports groups:

```python
cricket = {"Ram", "Sita", "Hari", "Gita", "Mina"}
football = {"Hari", "Gita", "Rita", "Kiran", "Suman"}
```

#### a. Find the students who play **both cricket and football**.

#### b. Find all students who play **at least one of the two sports**.

#### c. Find students who play cricket but **do not play football**.

#### d. Find students who play football but **do not play cricket**.

#### e. Find students who play **exactly one** of the two sports.

#### f. Check whether `"Hari"` plays at least one of the sports.

#### g. Check whether `"Mina"` plays football.

---

## Question 2 — Programming Courses

A training institute has three courses:

```python
python = {"Ram", "Sita", "Hari", "Gita", "Mina"}
javascript = {"Hari", "Gita", "Rita", "Kiran"}
java = {"Gita", "Mina", "Rita", "Suman"}
```

#### a. Find students studying both Python and JavaScript.

#### b. Find students studying all three courses.

#### c. Find all students studying at least one course.

#### d. Find students studying Python but not JavaScript.

#### e. Find students studying JavaScript but not Java.

#### f. Find students studying JavaScript and Java.

#### g. Find students studying Python but neither JavaScript nor Java.

#### h. Find students who study exactly one of the three courses.

---

## Question 3 — Company Employees and Skills

A company has employees with different technical skills:

```python
python = {"A", "B", "C", "D", "E"}
django = {"B", "C", "F", "G"}
react = {"C", "D", "G", "H"}
```

#### a. Find employees who know both Python and Django.

#### b. Find employees who know all three technologies.

#### c. Find employees who know Python but not Django.

#### d. Find employees who know Django but not React.

#### e. Find all employees who know at least one of these technologies.

#### f. Find employees who know Django and React.

#### g. Find employees who know Python but neither Django nor React.

#### h. Find employees who know exactly one of these technologies.

---

## Question 4 — Shopping

Two people have shopping lists:

```python
person_a = {"Rice", "Milk", "Bread", "Eggs", "Butter"}
person_b = {"Milk", "Bread", "Cheese", "Butter", "Tea"}
```

#### a. Find items that **both people need**.

#### b. Find all different items needed by either person.

#### c. Find items that only `person_a` needs.

#### d. Find items that only `person_b` needs.

#### e. Find items needed by exactly one person.

#### f. Check whether `"Milk"` is needed by both people.

#### g. Check whether `"Coffee"` is on either shopping list.

---

## Question 5 — School Attendance

A school records students who registered and students who attended an event:

```python
registered = {"Ram", "Sita", "Hari", "Gita", "Mina", "Rita"}
attended = {"Ram", "Hari", "Gita", "Rita"}
```

#### a. Find students who registered and attended.

#### b. Find students who registered but did not attend.

#### c. Find students who attended but were not registered.

#### d. Find everyone who appears in either list.

#### e. Check whether `"Mina"` attended.

#### f. Check whether `"Hari"` was registered.

#### g. Find students who appear in exactly one of the two groups.

---

## Question 6 — User Permissions

A web application requires certain permissions:

```python
required = {"read", "write", "login"}
user = {"read", "write", "login", "delete", "download"}
```

#### a. Check whether the user has all the required permissions.

#### b. Find permissions required by the system that the user does not have.

#### c. Find permissions the user has that are not required.

#### d. Check whether `"delete"` is available to the user.

#### e. Check whether `"admin"` is available to the user.

#### f. Create another user:

```python
user2 = {"login", "read"}
```

Check whether this user has everything required.

#### g. Find which permissions `user2` is missing.

---

## Question 7 — Library Books

Two libraries have different books:

```python
library_a = {"Python", "Django", "Java", "C++", "SQL"}
library_b = {"Python", "JavaScript", "Java", "React", "SQL"}
```

#### a. Find books available in both libraries.

#### b. Find all books available in at least one library.

#### c. Find books available only in Library A.

#### d. Find books available only in Library B.

#### e. Find books available in exactly one library.

#### f. Check whether `"Python"` is available in Library A.

#### g. Check whether `"Django"` is available in Library B.

#### h. Determine whether both libraries have exactly the same books.

---

## Question 8 — Examination Results

Three groups contain students who passed different subjects:

```python
math = {"Ram", "Sita", "Hari", "Gita", "Mina"}
science = {"Hari", "Gita", "Mina", "Rita"}
computer = {"Gita", "Mina", "Rita", "Kiran"}
```

#### a. Find students who passed both Math and Science.

#### b. Find students who passed all three subjects.

#### c. Find students who passed at least one subject.

#### d. Find students who passed Math but not Science.

#### e. Find students who passed Science but not Computer.

#### f. Find students who passed Science and Computer.

#### g. Find students who passed Math but neither Science nor Computer.

#### h. Find students who passed exactly one subject.

#### i. Find students who passed exactly two subjects.

---

## Question 9 — Social Media Followers

A person has followers on different platforms:

```python
facebook = {"Ram", "Sita", "Hari", "Gita", "Mina"}
instagram = {"Hari", "Gita", "Mina", "Rita", "Kiran"}
youtube = {"Gita", "Mina", "Rita", "Suman"}
```

#### a. Find people who follow both Facebook and Instagram.

#### b. Find people who follow all three platforms.

#### c. Find everyone who follows at least one platform.

#### d. Find people who follow Facebook but not Instagram.

#### e. Find people who follow Instagram and YouTube.

#### f. Find people who follow Instagram but not YouTube.

#### g. Find people who follow Facebook but neither Instagram nor YouTube.

#### h. Check whether `"Rita"` follows Facebook.

#### i. Check whether `"Suman"` follows at least one platform.

---

## Question 10 — Final Challenge: Employees and Departments

A company has employees working in different departments:

```python
development = {"Ram", "Sita", "Hari", "Gita", "Mina"}
design = {"Hari", "Gita", "Rita", "Kiran"}
marketing = {"Gita", "Mina", "Rita", "Suman"}
```

#### a. Find employees who work in both Development and Design.

#### b. Find employees who work in all three departments.

#### c. Find all employees who work in at least one department.

#### d. Find employees who work in Development but not Design.

#### e. Find employees who work in Design but not Marketing.

#### f. Find employees who work in Design and Marketing.

#### g. Find employees who work in Development but neither Design nor Marketing.

#### h. Find employees who work in exactly one department.

#### i. Find employees who work in exactly two departments.

#### j. Check whether `"Kiran"` works in Development.

#### k. Check whether `"Mina"` works in Marketing.

#### l. Add a new employee `"Nabin"` to the Design department.

#### m. Remove `"Suman"` from the Marketing department.

#### n. Determine whether Development and Design have any employee in common.

#### o. Determine whether everyone in Design is also in Development.
