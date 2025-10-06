## **"Learn by Doing"** style set of assignments.

---

## 🧩 **1. Instance and Class Attributes**

### 🎯 Goal:

Understand the difference between data that belongs to the **class** vs data that belongs to each **object (instance)**.

### 📝 Assignment:

```python
# Step 1: Create a class named Dog.
# Step 2: Add a CLASS attribute 'species' = "Canine".
# Step 3: Add INSTANCE attributes 'name' and 'age' in the constructor.
# Step 4: Create two Dog objects with different names and ages.
# Step 5: Print each dog's name, age, and species.
# Step 6: Try changing species for one dog only — what happens?

class Dog:
    species = "Canine"  # class attribute

    def __init__(self, name, age):
        self.name = name      # instance attribute
        self.age = age

# create two dogs
dog1 = Dog("Buddy", 3)
dog2 = Dog("Charlie", 5)

# print details
print(dog1.name, dog1.age, dog1.species)
print(dog2.name, dog2.age, dog2.species)

# now try this:
dog1.species = "Wolf"
print(dog1.species)
print(dog2.species)
```

🧠 **Learning Point:**

- Class attributes are shared by all instances.
- Instance attributes are unique per object.

---

## 🧩 **2. Instance and Class Methods**

### 🎯 Goal:

Learn when to use `@classmethod` and `@staticmethod` vs regular instance methods.

### 📝 Assignment:

```python
# Step 1: Create a class Student.
# Step 2: Add a class attribute 'school_name' = "ABC International School".
# Step 3: Add an instance constructor with name and grade.
# Step 4: Add:
#    - An instance method 'show_info' → prints name and grade.
#    - A class method 'change_school' → changes the school_name.
#    - A static method 'is_passed' → takes marks and returns True if marks >= 40.

class Student:
    school_name = "ABC International School"

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def show_info(self):
        print(f"Name: {self.name}, Grade: {self.grade}, School: {Student.school_name}")

    @classmethod
    def change_school(cls, new_name):
        cls.school_name = new_name

    @staticmethod
    def is_passed(marks):
        return marks >= 40

# Create students
s1 = Student("Aarav", "10")
s2 = Student("Sita", "9")

s1.show_info()
s2.show_info()

# Change school
Student.change_school("Sunrise Public School")
s1.show_info()
s2.show_info()

# Test static method
print(Student.is_passed(55))
print(Student.is_passed(35))
```

🧠 **Learning Point:**

- `@classmethod` changes data for the class (affects all objects).
- `@staticmethod` is a helper function — doesn’t touch instance/class data.

---

## 🧩 **3. Public and Private Attributes + @property and setter**

### 🎯 Goal:

Learn encapsulation — hiding sensitive data and controlling access via getters/setters.

### 📝 Assignment:

```python
# Step 1: Create a class BankAccount.
# Step 2: Add a private attribute __balance (default 0).
# Step 3: Add:
#    - A property 'balance' → getter that returns __balance.
#    - A setter for 'balance' that ensures new balance is not negative.
#    - A method 'deposit' to add money.
#    - A method 'withdraw' to deduct money (check enough balance first).

class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self.__balance = 0

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            print("Balance cannot be negative!")
        else:
            self.__balance = value

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited {amount}. New balance: {self.__balance}")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient funds!")
        else:
            self.__balance -= amount
            print(f"Withdrew {amount}. Remaining balance: {self.__balance}")

# Try:
acc = BankAccount("Prakash")
acc.deposit(500)
acc.withdraw(200)
print(acc.balance)
acc.balance = -100  # should show warning
```

🧠 **Learning Point:**

- `__private` attributes can’t be accessed directly from outside.
- Use `@property` and `@<name>.setter` for safe, controlled access.

---

## 🧩 **4. Simple Inheritance**

### 🎯 Goal:

Understand how child classes reuse and extend parent class behavior.

### 📝 Assignment:

```python
# Step 1: Create a base class Vehicle with attributes: brand and speed.
# Step 2: Add a method 'move' that prints "<brand> is moving at <speed> km/h".
# Step 3: Create a subclass Car that inherits Vehicle.
# Step 4: Add an extra attribute 'fuel_type' and a new method 'show_info'.
# Step 5: Create an object of Car and call methods.

class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def move(self):
        print(f"{self.brand} is moving at {self.speed} km/h")

class Car(Vehicle):
    def __init__(self, brand, speed, fuel_type):
        super().__init__(brand, speed)
        self.fuel_type = fuel_type

    def show_info(self):
        print(f"Car Brand: {self.brand}, Speed: {self.speed}, Fuel: {self.fuel_type}")

# Try:
car1 = Car("Toyota", 120, "Petrol")
car1.move()
car1.show_info()
```

🧠 **Learning Point:**

- `super().__init__()` calls the parent constructor.
- Child class inherits all public methods of parent class.

---

## ✅ Optional Challenge (Combining All Concepts)

Create a `StudentAccount` class that:

- Inherits from `BankAccount`.
- Has a class attribute `bank_name = "Student Savings Bank"`.
- Adds an instance attribute `student_id`.
- Uses a private balance.
- Has a `show_details()` method showing owner name, student ID, and current balance.
- Use `@property` for balance.

---
