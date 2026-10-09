# Python OOP Notes: Encapsulation, Properties, Inheritance, and Operator Overloading


## 1. Access Modifiers in Python

Access modifiers describe how class attributes and methods are intended to be accessed. Python uses naming conventions rather than strict access restrictions.

### 1.1 Public attributes

Public attributes can be accessed directly from outside the class.

```python
class User:
    def __init__(self, name):
        self.name = name


user = User("Ram")

print(user.name)
user.name = "Hari"

print(user.name)
```

Output:

```text
Ram
Hari
```

**Use public attributes** when direct access is appropriate.

### 1.2 Protected attributes

A single leading underscore (`_`) indicates that an attribute is intended for internal use or use by subclasses.

```python
class User:
    def __init__(self, name):
        self._name = name


user = User("Ram")

print(user._name)  # Works, but indicates internal use
```

Python does not prevent external access to `_name`. The underscore is a convention, not a security restriction.

### 1.3 Private attributes

A double leading underscore (`__`) triggers a mechanism called **name mangling**.

```python
class User:
    def __init__(self, name, password):
        self.name = name
        self.__password = password


user = User("Ram", "Secret@123")

print(user.name)

# print(user.__password)  # Raises AttributeError
print(user._User__password)  # Works
```

Python internally changes the attribute name approximately as follows:

```text
__password  →  _User__password
```

This is called **name mangling**.

It helps prevent accidental name conflicts, especially in inheritance. It does not make an attribute truly private or secure.

### Summary

| Syntax   | Meaning                 | External access                   |
| -------- | ----------------------- | --------------------------------- |
| `name`   | Public                  | Allowed                           |
| `_name`  | Protected by convention | Allowed                           |
| `__name` | Name-mangled            | Possible through the mangled name |

**Important:** Never store real user passwords as plain text in a production application. Passwords should be stored using an appropriate password-hashing mechanism.

---

## 2. Encapsulation

**Encapsulation** means grouping data and the methods that operate on that data inside a class, while controlling how the data is accessed or modified.

For example, a user should not be able to set an invalid password without validation.

```python
class User:
    def __init__(self, name, password):
        self.name = name
        self.__password = password

    def change_password(self, new_password):
        if len(new_password) < 8:
            raise ValueError("Password must be at least 8 characters")

        self.__password = new_password
```

In this example, the class controls password changes through a method.

### Benefits of encapsulation

1. Protects the integrity of an object's state.
2. Allows validation before changing data.
3. Hides implementation details.
4. Makes code easier to maintain.
5. Provides a clear interface for interacting with objects.

---

## 3. The `@property` Decorator

The `@property` decorator allows a method to be accessed like an attribute.

This is useful when we want to control what happens when someone reads or changes an attribute.

### Example: Password masking

```python
class User:
    def __init__(self, name, password):
        self.name = name
        self.__password = password

    @property
    def password(self):
        return "*" * len(self.__password)


user = User("Ram", "Secret@123")

print(user.password)
```

Output:

```text
***********
```

The expression `"*" * len(self.__password)` repeats the `*` character according to the password's length.

For example:

```python
print("ram" * 2)  # ramram
print("hari" * 3)  # hariharihari
print("*" * 8)  # ********
```

**Remember:** Masking a password only hides it in this particular display. It does not encrypt or securely store the original password.

### 3.1 The `@property` setter

A setter allows an attribute to be assigned through a method that performs validation.

```python
class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password

    @property
    def password(self):
        return "*" * len(self.__password)

    @password.setter
    def password(self, new_password):
        if len(new_password) < 8:
            raise ValueError(
                "Password must be at least 8 characters"
            )

        self.__password = new_password


user = User("Ram", "Secret@123")

print(user.password)

user.password = "Another@123"

print(user.password)
```

Here, `self.password = new_password` invokes the setter, whereas reading `user.password` invokes the getter.

### Why use a property instead of a normal method?

Without a property:

```python
user.get_password()
user.set_password("Another@123")
```

With a property:

```python
print(user.password)
user.password = "Another@123"
```

Properties provide a convenient attribute-like interface while allowing validation and other logic to run behind the scenes.

---

## 4. Magic Methods (Dunder Methods)

Magic methods are special methods with double underscores at the beginning and end of their names. They are also called **dunder methods**.

Examples include:

* `__init__()`
* `__str__()`
* `__repr__()`
* `__add__()`
* `__sub__()`
* `__len__()`
* `__eq__()`

Python invokes many of these methods automatically in response to operations.

### 4.1 The `__str__()` method

The `__str__()` method defines the human-readable string representation of an object.

```python
class User:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


user = User("Ram")

print(user)
```

Output:

```text
Ram
```

Without this override, printing an object usually displays a default representation containing its class and an identifier.

### Why does `print(90)` display `90`?

The `print()` function converts an object to a string for display, normally using its string representation.

```python
print(str(90))       # 90
print(str("Ram"))    # Ram
print(str([1, 2, 3]))  # [1, 2, 3]
```

For a custom class, `__str__()` lets you define that representation.

### 4.2 The `__repr__()` method

`__repr__()` defines the developer-oriented representation of an object.

```python
class User:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"User(name={self.name!r})"


user = User("Ram")

print(str(user))
print(repr(user))
```

Output:

```text
Ram
User(name='Ram')
```

A useful convention is that `__repr__()` should provide an informative, unambiguous representation.

---

## 5. Operator Overloading

Operator overloading allows a class to define what familiar operators do when used with its objects.

For example, `+` normally adds numbers or concatenates strings, but a custom class can define its own behavior for `+`.

### 5.1 Overloading the `+` operator

```python
class User:
    def __init__(self, name):
        self.name = name

    def __add__(self, other):
        return f"{self.name} + {other.name}"


user1 = User("Ram")
user2 = User("Hari")

print(user1 + user2)
```

Output:

```text
Ram + Hari
```

When Python evaluates:

```python
user1 + user2
```

it calls the left operand's `__add__()` method, approximately:

```python
user1.__add__(user2)
```

The `__add__()` method is responsible for defining the result.

### 5.2 Overloading the `-` operator

```python
class User:
    def __init__(self, name):
        self.name = name

    def __sub__(self, other):
        return f"{self.name} - {other.name}"


user1 = User("Ram")
user2 = User("Hari")

print(user1 - user2)
```

Output:

```text
Ram - Hari
```

Here, `-` does not perform mathematical subtraction. Its behavior is defined by the class.

### 5.3 Built-in examples of operator overloading

Python already defines operators for different data types.

```python
print(5 + 2)
print("Ram" + " Thapa")
print([1, 2, 3] + [4, 5])
print({1, 2, 3} - {3, 5})
```

Output:

```text
7
Ram Thapa
[1, 2, 3, 4, 5]
{1, 2}
```

The `+` operator performs addition for integers and concatenation for strings and lists. The `-` operator computes set difference for sets.

### Common operator-overloading methods

| Operator | Special method             |
| -------- | -------------------------- |
| `a + b`  | `__add__(self, other)`     |
| `a - b`  | `__sub__(self, other)`     |
| `a * b`  | `__mul__(self, other)`     |
| `a / b`  | `__truediv__(self, other)` |
| `a == b` | `__eq__(self, other)`      |
| `a < b`  | `__lt__(self, other)`      |
| `len(a)` | `__len__(self)`            |

