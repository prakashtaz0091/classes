# 🐍 Python Assignment – Operators & Variables (No Conditions, No Data Structures)

### 🎯 **Goal:**

To understand how different Python operators work

---

## **Part A: Relational Operators**

_(<, >, <=, >=, ==, !=)_

1. Take two numbers as input and print:

   ```python
   num1 = int(input("Enter first number: "))
   num2 = int(input("Enter second number: "))
   print(num1 < num2)
   print(num1 > num2)
   print(num1 == num2)
   print(num1 != num2)
   print(num1 <= num2)
   print(num1 >= num2)
   ```

   👉 Try entering different values and write what each result means.

---

2. Input your **age** and check:

   ```python
   age = int(input("Enter your age: "))
   print(age > 18)
   print(age == 18)
   print(age < 18)
   ```

---

3. Input your **marks** and test:

   ```python
   marks = int(input("Enter your marks: "))
   print(20 < marks < 40)
   ```

   👉 Try entering marks as 10, 30, and 50 — observe the results.

---

## **Part B: Logical Operators**

_(and, or, not)_

4. Input two numbers and test:

   ```python
   a = int(input("Enter first number: "))
   b = int(input("Enter second number: "))
   print(a > 0 and b > 0)
   print(a > 0 or b > 0)
   print(not (a > b))
   ```

---

5. Input marks and full marks (FM):

   ```python
   marks = int(input("Enter marks: "))
   FM = int(input("Enter full marks: "))
   print(marks < 0 or marks > FM)
   ```

   👉 Try values like 50 (out of 100) and 110 (out of 100).

---

6. Practice expressions:

   ```python
   print(5 > 3 and 2 < 4)
   print(5 < 2 or 10 > 3)
   print(not 7 == 7)
   ```

---

## **Part C: String Operators**

( + for joining, \* for repeating)

7. Input your first and last name and print:

   ```python
   first_name = input("Enter first name: ")
   last_name = input("Enter last name: ")
   print(first_name + last_name)
   print(first_name + " " + last_name)
   ```

---

8. Input a name and a number, and repeat the name:

   ```python
   name = input("Enter your name: ")
   n = int(input("Enter how many times to repeat: "))
   print(name * n)
   ```

---

## **Part D: Length Operator**

_(len)_

9. Input your name and print its length:

   ```python
   name = input("Enter your name: ")
   print(len(name))
   ```

10. Input any word and check if it’s longer than 5 characters:

```python
word = input("Enter a word: ")
print(len(word) > 5)
```

---

## **Part E: Membership Operator**

_(in)_

11. Input a short sentence and a word to search:

```python
text = input("Enter a sentence: ")
word = input("Enter a word to search: ")
print(word in text)
```

---

12. Try these and observe:

```python
print("a" in "apple")
print("x" in "apple")
print("ram" in "ramhari")
print("ram " in "ram hari")
```

---

## **Part F: Identity Operator**

_(is, is not)_

13. Try this:

```python
a = 5
b = 5
print(a is b)
print(a is not b)
```

---

14. Try this example:

```python
a = None
b = None
print(a is b)
print(a is not b)
```

---

15. Test identity on strings:

```python
name1 = "Ram"
name2 = "Ram"
print(name1 is name2)
print(name1 == name2)
```

---

## **Part G: Variable Naming Practice**

16. Write **5 valid** variable names and **5 invalid** ones.
    Example:
    ✅ `student_name = "Hari"`
    ❌ `1student = "Hari"`

---

17. Rename the following variables to meaningful names:

```python
a = 20
b = 30
c = a + b
print(c)
```

👉 Replace with clear names like `math_marks`, `science_marks`, `total_marks`.

---

18. Try writing variable names in **snake_case**:

- student_name
- total_marks
- number_of_students
- full_name
- english_marks

---

19. Try assigning reserved words as variable names (e.g., `or = 5`) and observe the syntax error.

---

20. Observe these results and write down what happens:

```python
print(10 > 5 and 5 < 10)
print(10 == 5 or 5 < 10)
print(not 3 > 2)
print("a" in "data")
print(len("python") >= 6)
```
