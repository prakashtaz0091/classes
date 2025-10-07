# 🧩 **Python Special Methods Practice (Beginner Level)**

---

## 🔹 **1. `__init__` + `__str__` — Create a Readable Object**

### 🎯 Goal:

Learn how to initialize an object and make it print nicely.

### 📝 Assignment:

```python
# Step 1: Create a class Rectangle.
# Step 2: Add attributes: length and width.
# Step 3: Initialize them using __init__.
# Step 4: Define __str__ to return text like:
#         "Rectangle: length=5, width=3"

class Rectangle:
    def __init__(self, length, width):
        pass  # TODO: store the values

    def __str__(self):
        pass  # TODO: return descriptive string

# Try:
r1 = Rectangle(5, 3)
print(r1)  # should print: Rectangle: length=5, width=3
```

🧠 **Learning Point:**

- `__init__` sets object data.
- `__str__` defines how your object appears when printed.

---

## 🔹 **2. `__add__` — Add Two Objects**

### 🎯 Goal:

Learn to define how `+` behaves between two objects.

### 📝 Assignment:

```python
# Step 1: Use the same Rectangle class.
# Step 2: Add a method __add__ that:
#         - Combines two rectangles by adding their lengths and widths.
#         - Returns a new Rectangle object.

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def __add__(self, other):
        pass  # TODO: return a new Rectangle with summed length & width

    def __str__(self):
        return f"Rectangle: length={self.length}, width={self.width}"

# Try:
r1 = Rectangle(4, 2)
r2 = Rectangle(3, 5)
r3 = r1 + r2
print(r3)  # Rectangle: length=7, width=7
```

🧠 **Learning Point:**

- `__add__` lets you define what `object1 + object2` means.

---

## 🔹 **3. `__sub__` — Subtract Objects**

### 🎯 Goal:

Use `-` operator with custom behavior.

### 📝 Assignment:

```python
# Step 1: Add __sub__ method to Rectangle.
# Step 2: It should subtract the length and width separately.
# Step 3: If result becomes negative, set it to 0.

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def __sub__(self, other):
        new_length = self.length - other.length
        new_width = self.width - other.width
        if new_length < 0: new_length = 0
        if new_width < 0: new_width = 0
        return Rectangle(new_length, new_width)

    def __str__(self):
        return f"Rectangle: length={self.length}, width={self.width}"

# Try:
r1 = Rectangle(10, 6)
r2 = Rectangle(3, 8)
r3 = r1 - r2
print(r3)  # Rectangle: length=7, width=0
```

🧠 **Learning Point:**

- `__sub__` defines how objects interact using `-`.

---

## 🔹 **4. `__mul__` — Multiply Object by a Number**

### 🎯 Goal:

Define how an object behaves when multiplied by an integer.

### 📝 Assignment:

```python
# Step 1: Add __mul__ to Rectangle.
# Step 2: It should multiply both length and width by the given number.
# Step 3: Return a new Rectangle object.

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def __mul__(self, number):
        pass  # TODO: multiply both length and width by number

    def __str__(self):
        return f"Rectangle: length={self.length}, width={self.width}"

# Try:
r1 = Rectangle(4, 3)
r2 = r1 * 2
print(r2)  # Rectangle: length=8, width=6
```

🧠 **Learning Point:**

- `__mul__` lets you define custom behavior for `object * number`.

---

## 🔹 **5. Combined Practice — “Box” Class**

### 🎯 Goal:

Apply all learned dunder methods in one small project.

### 📝 Assignment:

```python
# Step 1: Create a class Box with height, width, and depth.
# Step 2: Define:
#     - __init__ → sets the values
#     - __str__ → returns "Box(h=?, w=?, d=?)"
#     - __add__ → adds sizes of two boxes
#     - __sub__ → subtracts sizes (no negatives)
#     - __mul__ → scales box size by a number

class Box:
    pass  # TODO: implement step by step

# Try:
b1 = Box(4, 5, 6)
b2 = Box(2, 3, 1)
print(b1 + b2)
print(b1 - b2)
print(b1 * 2)
```
