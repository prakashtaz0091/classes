# Python OOP Fundamentals

## 1. What is Object-Oriented Programming?

**Object-Oriented Programming (OOP)** is a programming style where we organize programs around **objects**.

An object can contain:

* **Data** → attributes/properties
* **Behavior** → methods/functions

For example, a `User` object might contain:

```text
User
 ├── name
 ├── email
 ├── password
 ├── show_info()
 └── save()
```

Python uses OOP extensively.

---

# 2. Everything in Python is an Object

One important concept:

> In Python, almost everything we work with is an object.

For example:

```python
print(type(5))
```

Output:

```text
<class 'int'>
```

`5` is an object of the `int` class.

Similarly:

```python
l = [1, 2, 3]

print(type(l))
```

Output:

```text
<class 'list'>
```

And:

```python
s = {1, 2}

print(type(s))
```

Output:

```text
<class 'set'>
```

A function is also an object:

```python
def add():
    pass

print(type(add))
```

Output:

```text
<class 'function'>
```

A module is an object too:

```python
import math

print(type(math))
```

Typically:

```text
<class 'module'>
```

---

# 3. Classes

A **class** is a blueprint/template for creating objects.

Example:

```python
class Player:
    pass
```

Here we have defined a class called `Player`.

However, we haven't created any player object yet.

---

# 4. Creating Objects

An object is created by calling the class:

```python
class Player:
    pass


player1 = Player()
player2 = Player()
```

Now:

```text
Player       → class
player1      → object
player2      → object
```

We can verify this:

```python
print(type(player1))
```

Output:

```text
<class '__main__.Player'>
```

The exact module name may vary depending on where the class is defined.

---

# 5. Class vs Object

Think of a class as a blueprint.

For example:

```text
Class: Car
```

describes what a car object can have/do.

Then:

```python
car1 = Car()
car2 = Car()
```

creates two separate objects.

Conceptually:

```text
Car class
    │
    ├── car1
    │
    └── car2
```

The class is the definition; the objects are individual instances created from that definition.

---

# 6. Instance Attributes

Python allows us to attach data to an object.

Example:

```python
class User:
    pass


user = User()

user.name = "Ram"
user.email = "ram@gmail.com"
user.password = "********"
```

Now `user` has three attributes:

```python
print(user.name)
print(user.email)
print(user.password)
```

Output:

```text
Ram
ram@gmail.com
********
```

Another object can have completely different values:

```python
user2 = User()

user2.name = "Hari"
user2.email = "hari@gmail.com"
user2.password = "ASDFQEWRQWER"
```

The two objects are independent:

```text
user
 ├── name = Ram
 ├── email = ram@gmail.com
 └── password = ********

user2
 ├── name = Hari
 ├── email = hari@gmail.com
 └── password = ASDFQEWRQWER
```

---

# 7. The Problem with Manually Creating Attributes

Although this works:

```python
user = User()

user.name = "Ram"
user.email = "ram@gmail.com"
user.password = "********"
```

it becomes inconvenient when objects require many attributes.

We would have to remember to set everything every time:

```python
user1 = User()
user1.name = "Ram"
user1.email = "ram@gmail.com"
user1.password = "..."

user2 = User()
user2.name = "Hari"
user2.email = "hari@gmail.com"
user2.password = "..."
```

Python provides a better approach.

That is where `__init__()` comes in.

---

# 8. The `__init__()` Method

`__init__()` is commonly called the **constructor** or initializer.

Example:

```python
class User:

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
```

Now we can create a user like this:

```python
user1 = User(
    "Ram",
    "ram@gmail.com",
    "User@123"
)
```

Python automatically calls:

```python
__init__()
```

when the object is created.

Conceptually:

```python
user1 = User("Ram", "ram@gmail.com", "User@123")
```

causes Python to initialize the object with:

```python
self.name = "Ram"
self.email = "ram@gmail.com"
self.password = "User@123"
```

---

# 9. What is `self`?

`self` refers to the **current object**.

Example:

```python
class User:

    def __init__(self, name, email):
        self.name = name
        self.email = email
```

When we write:

```python
user1 = User("Ram", "ram@gmail.com")
```

we can think of:

```text
self     → user1
name     → "Ram"
email    → "ram@gmail.com"
```

Therefore:

```python
self.name = name
```

means:

> Store the value of `name` inside the current object's `name` attribute.

---

# 10. Why Do We Need `self`?

Consider:

```python
class User:

    def __init__(self, name):
        self.name = name
```

Here there are two different things:

```text
name
```

is a local parameter.

```text
self.name
```

is an attribute belonging to the object.

For:

```python
user1 = User("Ram")
```

we get:

```text
user1.name → "Ram"
```

For:

```python
user2 = User("Hari")
```

we get:

```text
user2.name → "Hari"
```

So each object stores its own data.

---

# 11. Instance Methods

A function defined inside a class is generally called a **method**.

Example:

```python
class User:

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def show_info(self):
        print("Name:", self.name)
        print("Email:", self.email)
```

Create an object:

```python
user1 = User("Ram", "ram@gmail.com")
```

Call the method:

```python
user1.show_info()
```

Output:

```text
Name: Ram
Email: ram@gmail.com
```

The method has access to the object's data through `self`.

---

# 12. How Does `user1.show_info()` Work?

When we write:

```python
user1.show_info()
```

Python effectively passes `user1` as the first argument.

It is conceptually similar to:

```python
User.show_info(user1)
```

Therefore this:

```python
user1.show_info()
```

and:

```python
User.show_info(user1)
```

refer to the same method call.

This is why:

```python
def show_info(self):
```

needs `self`.

---

# 13. Example: User Class

A complete example:

```python
class User:

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def show_info(self):
        print("Name:", self.name)
        print("Email:", self.email)
        print("Password:", self.password)

    def save(self):
        print("Saving to database")
        print("Saved to database")


user1 = User(
    "Ram",
    "ram@gmail.com",
    "User@123"
)

user1.show_info()
user1.save()
```

---

# 14. Instance Methods Can Modify Objects

Methods aren't limited to displaying information.

They can change object data.

Example:

```python
class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def show_balance(self):
        print("Balance:", self.balance)
```

Usage:

```python
account = BankAccount("Ram", 1000)

account.show_balance()

account.deposit(500)

account.show_balance()
```

Output:

```text
Balance: 1000
Balance: 1500
```

The method changes the object's state.

---

# 15. Static Methods

Sometimes a method belongs logically to a class but does **not need access to a particular object**.

For that, Python provides:

```python
@staticmethod
```

Example:

```python
class User:

    @staticmethod
    def check_password(password):
        if len(password) < 8:
            raise Exception("Password must be at least 8 chars long")

        return True
```

We can call it without creating a `User` object:

```python
User.check_password("Password@123")
```

---

# 16. Instance Method vs Static Method

### Instance method

```python
class User:

    def show_info(self):
        print(self.name)
```

It needs:

```python
self
```

because it works with a particular object.

Usage:

```python
user1.show_info()
```

---

### Static method

```python
class User:

    @staticmethod
    def check_password(password):
        ...
```

It does not need:

```python
self
```

Usage:

```python
User.check_password("Password@123")
```

---

# 17. Why Use a Static Method?

Suppose password validation is logically related to users.

We could write:

```python
def check_password(password):
    ...
```

outside the class.

But if the functionality is specifically related to the `User` concept, keeping it inside the class can make the code easier to organize:

```python
class User:

    @staticmethod
    def check_password(password):
        ...
```

The important point is:

> A static method does not automatically receive the current object.

---

# 18. Password Validation Example

This example uses:

```python
@staticmethod
def check_password(password, name):
    if len(password) < 8:
        raise Exception("Password must be at least 8 chars long")

    has_special_chars = any(
        not char.isalnum()
        for char in password
    )

    if password.isalpha() or password.isdigit() or not has_special_chars:
        raise Exception(
            "Password must be alphanumeric + special chars"
        )

    if name.lower() in password.lower():
        raise Exception(
            "Password must not contain personal info"
        )

    return True
```

The method is then called from `__init__()`:

```python
if User.check_password(password, name):
    self.password = password
```

So object creation becomes:

```python
user1 = User(
    "Ram",
    "ram@gmail.com",
    "User@123"
)
```

Before storing the password, the class validates it.

---

# 19. `raise Exception`

The `raise` keyword is used to generate an exception.

Example:

```python
if len(password) < 8:
    raise Exception("Password must be at least 8 chars long")
```

If someone does:

```python
User("Ram", "ram@gmail.com", "abc")
```

Python raises an exception instead of continuing normally.

Example output:

```text
Exception: Password must be at least 8 chars long
```

---

# 20. Better Exception Types

Instead of always using:

```python
raise Exception(...)
```

we can use a more specific exception:

```python
raise ValueError(
    "Password must be at least 8 characters long"
)
```

For example:

```python
class User:

    @staticmethod
    def check_password(password):

        if len(password) < 8:
            raise ValueError(
                "Password must be at least 8 characters long"
            )
```

`ValueError` is appropriate when a function receives a value of the correct general type but an invalid value.

---

# 21. Useful String Methods Used in the Example

The password validation also demonstrates several useful Python methods.

### `len()`

Returns the number of characters:

```python
password = "Hello123"

print(len(password))
```

Output:

```text
8
```

---

### `.isalnum()`

Checks whether all characters are letters or numbers.

```python
print("abc123".isalnum())
```

Output:

```text
True
```

But:

```python
print("abc@123".isalnum())
```

Output:

```text
False
```

because `@` is not alphanumeric.

---

### `.isalpha()`

Checks whether all characters are alphabetic:

```python
print("hello".isalpha())
```

Output:

```text
True
```

```python
print("hello123".isalpha())
```

Output:

```text
False
```

---

### `.isdigit()`

Checks whether all characters are digits:

```python
print("12345".isdigit())
```

Output:

```text
True
```

```python
print("123abc".isdigit())
```

Output:

```text
False
```

---

### `.lower()`

Converts a string to lowercase:

```python
name = "Ram"

print(name.lower())
```

Output:

```text
ram
```

This is useful for case-insensitive comparisons.

---

# 22. The `any()` Function

The code uses:

```python
has_special_chars = any(
    not char.isalnum()
    for char in password
)
```

This checks whether **at least one** character satisfies the condition.

For example:

```python
password = "Hello@123"

has_special_chars = any(
    not char.isalnum()
    for char in password
)
```

The `@` character is not alphanumeric, so:

```python
has_special_chars == True
```

A simpler way to understand `any()`:

```python
numbers = [False, False, True, False]

print(any(numbers))
```

Output:

```text
True
```

Because at least one value is `True`.

---

# 23. `dir()` — Inspecting an Object

Python provides:

```python
dir()
```

to inspect the names/attributes available on an object.

Example:

```python
class User:

    def show_info(self):
        pass


user = User()

print(dir(user))
```

You will see many names, including things inherited from Python's object system.

You can also write:

```python
print(user.__dir__())
```

However, `dir(user)` is the normal and preferred way to inspect available attributes/methods.

---

# 24. `type()` vs `dir()`

These two functions answer different questions.

### `type()`

> What type/class is this object?

```python
user = User()

print(type(user))
```

---

### `dir()`

> What attributes and methods are available on this object?

```python
print(dir(user))
```

Think:

```text
type() → What am I?

dir()  → What can I access?
```

---

# 25. Attribute Access

If an object has:

```python
user.name
```

we are accessing its `name` attribute.

For example:

```python
class User:

    def __init__(self, name):
        self.name = name


user = User("Ram")

print(user.name)
```

Output:

```text
Ram
```

Python uses the `.` operator to access attributes and methods:

```python
user.name
user.email
user.show_info()
user.save()
```

---

# 26. What Happens if an Attribute Doesn't Exist?

Example:

```python
class User:

    def __init__(self, name):
        self.name = name


user = User("Ram")

print(user.address)
```

If `address` hasn't been defined, Python raises:

```text
AttributeError
```

This is why the commented code:

```python
# print(user1.address)
```

would fail if `address` was never created.

---

# 27. Classes Can Have Many Objects

One class can create many objects.

```python
class User:

    def __init__(self, name, email):
        self.name = name
        self.email = email


user1 = User("Ram", "ram@gmail.com")
user2 = User("Hari", "hari@gmail.com")
user3 = User("Sita", "sita@gmail.com")
```

Conceptually:

```text
              User class
                  │
       ┌──────────┼──────────┐
       ↓          ↓          ↓
     user1      user2      user3
      Ram        Hari       Sita
```

Each object has its own instance attributes.

---

# 28. Methods vs Functions

A function:

```python
def add(a, b):
    return a + b
```

is defined independently.

A method:

```python
class Calculator:

    def add(self, a, b):
        return a + b
```

is defined inside a class.

Usage:

```python
calculator = Calculator()

calculator.add(5, 10)
```

So:

```text
Function → standalone behavior

Method   → behavior associated with a class/object
```

---

# 29. Modules Are Objects Too

Suppose we have a file:

```text
bill.py
```

containing:

```python
def show_bill_summary():
    print("Bill summary")
```

We can import it:

```python
import bill
```

Then:

```python
print(type(bill))
```

The result is a module type.

We can access things inside the module using `.`:

```python
bill.show_bill_summary()
```

This is the same general attribute-access mechanism:

```python
object.attribute
```

Examples:

```python
user.name
bill.show_bill_summary
math.pi
```

---

# 30. Dot Notation

A major pattern to understand is:

```python
something.something_else
```

Examples:

```python
user.name
user.show_info()

bill.show_bill_summary()

password.lower()

numbers.append(5)
```

The thing before `.` is an object, and the thing after `.` is an attribute/method available through that object.

---

# 31. `list.append()` and `set.add()`

Earlier examples:

```python
l = [1, 2, 3]

l.append(4)
```

`append()` is a method of the list object.

Similarly:

```python
s = {1, 2}

s.add(5)
```

`add()` is a method of the set object.

This is also OOP.

Python's built-in types are implemented as classes/objects.

---

# 32. A More Complete Example

Here is a small example combining the concepts:

```python
class Student:

    school = "ABC College"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("School:", Student.school)

    def have_birthday(self):
        self.age += 1

    @staticmethod
    def is_valid_age(age):
        return age >= 5


student1 = Student("Ram", 20)

student1.show_info()

student1.have_birthday()

student1.show_info()

print(Student.is_valid_age(20))
```

This example demonstrates:

* Class
* Object
* Instance attributes
* Instance methods
* Static methods
* Class attributes
* `self`
* Method calls

---

# 33. Instance Attribute vs Class Attribute

This is an important next concept.

### Instance attribute

Belongs to a particular object:

```python
class Student:

    def __init__(self, name):
        self.name = name
```

Each student can have a different name.

```python
student1.name
student2.name
```

---

### Class attribute

Belongs to the class:

```python
class Student:

    school = "ABC College"
```

All objects can access it:

```python
Student.school
student1.school
student2.school
```

Conceptually:

```text
Student class
 └── school = "ABC College"

student1
 └── name = "Ram"

student2
 └── name = "Hari"
```

---

# 34. A Note About Password Validation

The current condition is:

```python
if password.isalpha() or password.isdigit() or not has_special_chars:
    raise Exception(...)
```

This does reject passwords without special characters.

However, if the intended rule is:

> Password must contain at least one letter, one number, and one special character.

then it is clearer to explicitly check all three requirements.

For example:

```python
has_letter = any(char.isalpha() for char in password)
has_number = any(char.isdigit() for char in password)
has_special = any(not char.isalnum() for char in password)

if not has_letter:
    raise ValueError("Password must contain a letter")

if not has_number:
    raise ValueError("Password must contain a number")

if not has_special:
    raise ValueError("Password must contain a special character")
```

This is easier to understand and maintain.

---

# 35. Improved User Example

Putting the concepts together:

```python
class User:

    def __init__(self, name, email, password):
        self.name = name
        self.email = email

        if User.check_password(password, name):
            self.password = password

    def show_info(self):
        print("Name:", self.name)
        print("Email:", self.email)

    def save(self):
        print("Saving to database...")
        print("Saved to database.")

    @staticmethod
    def check_password(password, name):

        if len(password) < 8:
            raise ValueError(
                "Password must be at least 8 characters long"
            )

        has_letter = any(
            char.isalpha()
            for char in password
        )

        has_number = any(
            char.isdigit()
            for char in password
        )

        has_special = any(
            not char.isalnum()
            for char in password
        )

        if not has_letter:
            raise ValueError(
                "Password must contain a letter"
            )

        if not has_number:
            raise ValueError(
                "Password must contain a number"
            )

        if not has_special:
            raise ValueError(
                "Password must contain a special character"
            )

        if name.lower() in password.lower():
            raise ValueError(
                "Password must not contain the user's name"
            )

        return True


user1 = User(
    "Ram",
    "ram@gmail.com",
    "Secure@123"
)

user1.show_info()
user1.save()
```

---

# 36. Important Mental Model

When learning OOP, remember this progression:

```text
Class
  ↓
Object
  ↓
Attributes + Methods
  ↓
Object State + Behavior
```

For example:

```python
class User:
    ...
```

defines the class.

Then:

```python
user1 = User(...)
```

creates an object.

The object has:

```python
user1.name
user1.email
```

which are its data/attributes.

And:

```python
user1.show_info()
user1.save()
```

which are its behaviors/methods.

---

# 37. Key Concepts to Remember

| Concept            | Meaning                                          |
| ------------------ | ------------------------------------------------ |
| `class`            | Defines a class/blueprint                        |
| Object             | Instance created from a class                    |
| `__init__()`       | Initializes a newly created object               |
| `self`             | Refers to the current object                     |
| Attribute          | Data associated with an object                   |
| Method             | Function defined inside a class                  |
| `@staticmethod`    | Method that doesn't receive `self` automatically |
| `type()`           | Tells us an object's type                        |
| `dir()`            | Shows available attributes/methods               |
| `raise`            | Raises an exception                              |
| `any()`            | Returns `True` if at least one item is truthy    |
| `.`                | Used to access attributes/methods                |
| Class attribute    | Data shared through the class                    |
| Instance attribute | Data belonging to a particular object            |

---

# 38. Practice Questions

### Beginner

1. Create a `Car` class.
2. Create two car objects.
3. Give each car a different `brand` and `model`.
4. Print their information.

### Intermediate

Create:

```python
class Employee:
    ...
```

with:

* `name`
* `email`
* `salary`

and methods:

```python
show_info()
increase_salary(amount)
```

### Static Method Practice

Add:

```python
@staticmethod
def is_valid_salary(salary):
    ...
```

The method should return `True` if salary is greater than `0`.

### Challenge

Create a `BankAccount` class with:

```text
owner
balance
deposit()
withdraw()
show_balance()
```

Add validation so that:

* Deposit amount cannot be negative.
* Withdrawal amount cannot be negative.
* Withdrawal cannot exceed the balance.

---

# 39. Final Takeaway

The most important idea from today's lesson is:

> **A class defines the structure and behavior, while an object is a concrete instance of that class.**

For example:

```python
class User:

    def __init__(self, name):
        self.name = name

    def show_info(self):
        print(self.name)
```

Then:

```python
user1 = User("Ram")
user2 = User("Hari")
```

creates two separate objects.

```text
User class
    │
    ├── user1
    │    └── name = "Ram"
    │
    └── user2
         └── name = "Hari"
```

And:

```python
user1.show_info()
```

is essentially a convenient way of calling:

```python
User.show_info(user1)
```

Understanding **class → object → `self` → attributes → methods** is the foundation for everything that comes next in Python OOP.
